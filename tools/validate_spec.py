"""Offline structural validation. Does not validate financial or operational behavior."""

import argparse
import json
import re
from datetime import UTC, datetime
from graphlib import CycleError, TopologicalSorter
from pathlib import Path
from urllib.parse import unquote, urlsplit

from jsonschema import Draft202012Validator, FormatChecker
from openapi_spec_validator import validate as validate_openapi

try:
    from tools.sync_docs import sync
    from tools.validate_design import validate_design
    from tools.validate_r2 import validate_r2
except ModuleNotFoundError:
    from sync_docs import sync
    from validate_design import validate_design
    from validate_r2 import validate_r2

ROOT = Path(__file__).resolve().parents[1]


def validate_dag(tasks: list[dict]) -> list[str]:
    errors = []
    ids = [t["id"] for t in tasks]
    if len(ids) != len(set(ids)):
        errors.append("duplicate task id")
    for task in tasks:
        for dependency in task["dependencies"]:
            if dependency not in ids:
                errors.append(f"{task['id']}: unknown dependency {dependency}")
    try:
        tuple(TopologicalSorter({t["id"]: t["dependencies"] for t in tasks}).static_order())
    except CycleError:
        errors.append("task dependency cycle")
    return errors


def local_ref_errors(document: dict) -> list[str]:
    """Reject external references, resolve JSON pointers without network access."""
    errors = []

    def walk(value: object) -> None:
        if isinstance(value, dict):
            ref = value.get("$ref")
            if ref:
                if not ref.startswith("#/"):
                    errors.append(f"non-local reference: {ref}")
                else:
                    target = document
                    try:
                        for token in ref[2:].split("/"):
                            target = target[token.replace("~1", "/").replace("~0", "~")]
                    except (KeyError, TypeError):
                        errors.append(f"unresolved reference: {ref}")
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)

    walk(document)
    return errors


def validate(root: Path) -> dict:
    errors: list[str] = []
    counts: dict[str, int] = {}
    docs: dict[str, object] = {}
    for path in sorted((root / "docs").rglob("*.json")):
        try:
            docs[str(path.relative_to(root))] = json.loads(path.read_text(encoding="utf-8"))
        except (ValueError, OSError) as exc:
            errors.append(f"{path.relative_to(root)}: {exc}")
    counts["json_files"] = len(docs)

    def load(name: str):
        return docs["docs/" + name]

    schema = load("contracts/domain.schema.json")
    defs = schema["$defs"]
    counts["domain_definitions"] = len(defs)
    for name, document in docs.items():
        if name.endswith(".schema.json") or name.endswith("/openapi.json"):
            errors.extend(f"{name}: {e}" for e in local_ref_errors(document))
        if name.endswith(".schema.json"):
            try:
                Draft202012Validator.check_schema(document)
            except Exception as exc:
                errors.append(f"{name}: {exc}")

    def check_example(name: str, value: object, *, valid: bool = True) -> None:
        if name not in defs:
            errors.append(f"unknown example schema {name}")
            return
        wrapped = {**schema, "$ref": f"#/$defs/{name}"}
        validator = Draft202012Validator(wrapped, format_checker=FormatChecker())
        failures = list(validator.iter_errors(value))
        if valid and failures:
            errors.append(f"example {name}: {failures[0].message}")
        if not valid and not failures:
            errors.append(f"negative example {name} unexpectedly accepted")

    # Ref errors must fail before any validator could attempt retrieval.
    if any("reference:" in e for e in errors):
        return report(counts, errors)
    positives = load("contracts/examples/valid.json")
    negatives = load("contracts/examples/invalid.json")
    if set(positives) != set(defs):
        errors.append("positive examples do not cover exactly all domain definitions")
    if {e["schema"] for e in negatives} != set(defs):
        errors.append("negative examples do not cover exactly all domain definitions")
    for name, value in positives.items():
        check_example(name, value)
    for example in negatives:
        check_example(example["schema"], example["value"], valid=False)
    counts.update(positive_examples=len(positives), negative_examples=len(negatives))
    errors.extend(validate_design(root, schema, positives, negatives))
    errors.extend(validate_r2(root, schema))
    counts["financial_oracles"] = len(load("contracts/scenarios/financial.json")["cases"])

    policy_validator = Draft202012Validator(
        load("contracts/policy.schema.json"), format_checker=FormatChecker()
    )
    errors.extend(
        f"policy: {e.message}"
        for e in policy_validator.iter_errors(load("contracts/policy-defaults.json"))
    )
    api = load("contracts/openapi.json")
    try:
        validate_openapi(api)
    except Exception as exc:
        errors.append(f"OpenAPI: {exc}")
    counts["api_paths"] = len(api["paths"])
    if api["components"]["schemas"] != json.loads(
        json.dumps(defs).replace("#/$defs/", "#/components/schemas/")
    ):
        errors.append("OpenAPI schemas differ from canonical domain definitions")

    tasks = load("tasks/index.json")
    requirements = load("requirements.json")
    components = {c["id"] for c in load("components.json")}
    errors.extend(validate_dag(tasks))
    task_map = {t["id"]: t for t in tasks}
    counts.update(tasks=len(tasks), requirements=len(requirements), components=len(components))
    for requirement in requirements:
        task = task_map.get(requirement["task"])
        if not task:
            errors.append(f"{requirement['id']}: missing task")
            continue
        for field, task_field in [
            ("id", "requirement_id"),
            ("contract", "contract"),
            ("component", "component"),
            ("test", "test_id"),
            ("acceptance", "acceptance_id"),
            ("phase", "phase"),
        ]:
            if requirement[field] != task[task_field]:
                errors.append(f"{requirement['id']}: mismatch {field}")
    for key in ("id", "task", "test", "acceptance"):
        values = [r[key] for r in requirements]
        if len(values) != len(set(values)):
            errors.append(f"duplicate requirement {key}")
    if {r["task"] for r in requirements} != set(task_map):
        errors.append("requirements/task coverage mismatch")
    for task in tasks:
        if task["component"] not in components or task["contract"] not in defs:
            errors.append(f"{task['id']}: unknown component or contract")
        fiche = root / f"docs/tasks/{task['id']}.md"
        if not fiche.is_file():
            errors.append(f"missing {task['id']} fiche")
        else:
            text = fiche.read_text()
            if f"Fase: **{task['phase']}**" not in text:
                errors.append(f"{task['id']}: fiche phase mismatch")
            match = re.search(r"Dependencias: (.*?)\. Verificar", text)
            if not match or set(re.findall(r"T-\d{3}", match[1])) != set(task["dependencies"]):
                errors.append(f"{task['id']}: fiche dependency mismatch")
        for doc in task["docs"]:
            if not (root / "docs" / doc).is_file():
                errors.append(f"{task['id']}: missing doc {doc}")
        for adr in task["adrs"]:
            if not list((root / "docs/adr").glob(adr + "*.md")):
                errors.append(f"{task['id']}: missing ADR {adr}")
    errors.extend(f"outdated generated table: {name}" for name in sync(root, check=True))

    events = {e["type"]: e for e in load("contracts/events.json")}
    for event in events.values():
        if event["payload_schema"] not in defs:
            errors.append(f"unknown payload schema: {event['type']}")
        if any(c not in components for c in [event["producer"], *event["consumers"]]):
            errors.append(f"unknown event component: {event['type']}")
    for example in load("contracts/examples/events.json"):
        check_example("EventEnvelope", example)
        if example["event_type"] not in events:
            errors.append(f"unknown example event: {example['event_type']}")
        else:
            check_example(events[example["event_type"]]["payload_schema"], example["payload"])
    counts["event_types"] = len(events)
    for example in load("contracts/examples/strategies.json"):
        check_example("StrategyConfig", example)
    for port in load("contracts/ports.json"):
        if port["owner"] not in components:
            errors.append(f"unknown owner in port {port['name']}")
        for field in ("input_schema", "output_schema"):
            if port[field] not in defs:
                errors.append(f"unknown {field} in port {port['name']}")
    for kind, name in load("contracts/observation-kinds.json").items():
        if name not in defs:
            errors.append(f"unknown observation schema {kind}: {name}")
    for filename in ("order-machine.json", "cex-order-machine.json"):
        machine = load("contracts/" + filename)
        states = set(machine["states"])
        for transition in machine["transitions"]:
            endpoints = (
                [transition["source"], transition["target"]]
                if isinstance(transition, dict)
                else transition
            )
            if any(state not in states for state in endpoints):
                errors.append(f"{filename}: unknown transition state")
        if "initial" in machine and machine["initial"] not in states:
            errors.append(f"{filename}: unknown initial state")
        if not set(machine.get("terminal", [])).issubset(states):
            errors.append(f"{filename}: unknown terminal state")

    # File targets only: anchor validity and external URL freshness are separate reviews.
    checked_links = 0
    for path in [root / "README.md", *(root / "docs").rglob("*.md")]:
        if path.name == "input-research.md" or "status/history" in path.as_posix():
            continue
        for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", path.read_text()):
            parsed = urlsplit(target)
            if parsed.scheme or not parsed.path:
                continue
            checked_links += 1
            if not (path.parent / unquote(parsed.path)).exists():
                errors.append(f"{path.relative_to(root)}: missing link target {target}")
    counts["local_link_targets"] = checked_links
    return report(counts, errors)


def report(counts: dict, errors: list[str]) -> dict:
    return {
        "generated_at": datetime.now(UTC).isoformat(),
        "scope": "offline structural specification validation",
        "status": "PASS" if not errors else "FAIL",
        "counts": counts,
        "errors": errors,
        "not_verified": [
            "runtime enforcement of semantic rules; cross-record financial and temporal invariants",
            "runtime product, providers, permissions, data quality or profitability",
            "Mermaid rendering and Markdown anchors",
            "external URL freshness, licenses and legal requirements",
            "full editorial consistency of prose and task implementation paths",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    try:
        result = validate(ROOT)
    except Exception as exc:
        result = report({}, [f"validator aborted: {type(exc).__name__}: {exc}"])
    output = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    print(output, end="")
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(output, encoding="utf-8")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
