"""Check independent documentary oracles; this is not a ledger implementation."""

import json
from collections import defaultdict
from graphlib import CycleError, TopologicalSorter
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker


def financial_errors(document: dict, schema: dict) -> list[str]:
    errors = []
    accounts = document["account_registry"]
    for case in document["cases"]:
        prefix = case["id"]

        def fail(message: str, prefix: str = prefix) -> None:
            errors.append(f"{prefix}: {message}")

        validator = Draft202012Validator(
            {**schema, "$ref": f"#/$defs/{case['input_schema']}"},
            format_checker=FormatChecker(),
        )
        for error in validator.iter_errors(case["input"]):
            fail(f"command {list(error.absolute_path)}: {error.message}")
        initial, final = case["initial_state"], case["expected_state"]
        output = case["expected_output"]
        lines = output["journal_lines"]
        balances = {k: int(v) for k, v in initial["balances"].items()}
        sums: dict[str, int] = defaultdict(int)
        for line in lines:
            account = accounts.get(line["account_id"])
            if account is None or account["asset_id"] != line["asset_id"]:
                fail("journal account/asset mismatch")
                continue
            amount = int(line["signed_atoms"])
            sums[line["asset_id"]] += amount
            balances[line["account_id"]] = balances.get(line["account_id"], 0) + amount
        if any(sums.values()):
            fail("unbalanced per asset")
        expected = {k: int(v) for k, v in final["balances"].items()}
        if balances != expected:
            fail("final balance differs from independent journal deltas")
        for account_id, amount in expected.items():
            if (
                accounts[account_id]["role"]
                in {"AVAILABLE", "RESERVED", "RENT_LOCKED", "COLLATERAL"}
                and amount < 0
            ):
                fail("negative owned balance")
        posted = output["outcome"] == "POSTED"
        if final["portfolio_revision"] != initial["portfolio_revision"] + int(posted):
            fail("wrong revision effect")
        if not posted and (
            lines or balances != {k: int(v) for k, v in initial["balances"].items()}
        ):
            fail("rejection/duplicate changes balances")
        if posted and (not lines or case["expected_error"] is not None):
            fail("posted oracle lacks effects or declares error")
        if (
            case["expected_error"]
            and case["expected_error"]
            not in schema["$defs"]["FinancialError"]["properties"]["code"]["enum"]
        ):
            fail("unknown typed error")
        context = initial["context"]
        operation = case["input"]["operation"]
        if operation == "RELEASE" and context.get("reservation_state") == "ATTEMPTED":
            if context.get("finality") != "VERIFIED" and posted:
                fail("UNKNOWN reservation released")
        payload = case["input"]["payload"]
        if posted and operation == "TRADE":
            fill = payload["fill"]
            for side in ("input", "output"):
                move = payload[side + "_move"]
                if move["amount"]["asset_id"] != fill[side + "_asset_id"] or int(
                    move["amount"]["atoms"]
                ) != int(fill[side + "_atoms"]):
                    fail("fill/move mismatch")
        if posted and operation == "REVERSAL":
            original = initial["original_journal_lines"]
            inverse = [
                {**line, "signed_atoms": str(-int(line["signed_atoms"]))} for line in original
            ]
            if sorted(lines, key=lambda x: x["account_id"]) != sorted(
                inverse, key=lambda x: x["account_id"]
            ):
                fail("reversal is not exact inverse")
    return errors


def validate_r2(root: Path, schema: dict) -> list[str]:
    path = root / "docs/contracts/scenarios/financial.json"
    document = json.loads(path.read_text())
    errors = financial_errors(document, schema)
    task_ids = {x["id"] for x in json.loads((root / "docs/tasks/index.json").read_text())}
    req_ids = {x["id"] for x in json.loads((root / "docs/requirements.json").read_text())}
    seen = set()
    for case in document["cases"]:
        if case["id"] in seen:
            errors.append(f"duplicate scenario {case['id']}")
        seen.add(case["id"])
        if not set(case["tasks"]) <= task_ids or not set(case["requirement_ids"]) <= req_ids:
            errors.append(f"{case['id']}: unknown task/requirement")
        for field in ("units", "independent_calculation", "invariant", "validation_method"):
            if not case.get(field):
                errors.append(f"{case['id']}: missing {field}")
    required = set(schema["$defs"]["LedgerPostRequest"]["properties"]["operation"]["enum"])
    covered = {c["input"]["operation"] for c in document["cases"]}
    if required != covered:
        errors.append(f"financial scenarios: operation coverage {required - covered}")
    if (root / "docs/contracts/feature-catalog.json").exists():
        errors.extend(feature_catalog_errors(root, schema))
    ports = json.loads((root / "docs/contracts/ports.json").read_text())
    if (root / "docs/contracts/auxiliary-ports.md").exists():
        errors.extend(port_contract_errors(ports, schema))
    return errors


def port_contract_errors(ports: list[dict], schema: dict) -> list[str]:
    errors = []
    seen = set()
    for port in ports:
        key = (port["name"], port["method"])
        if key in seen:
            errors.append(f"duplicate port method {key}")
        seen.add(key)
        for field in ("context_schema", "error_schema", "input_schema", "output_schema"):
            if port.get(field) not in schema["$defs"]:
                errors.append(f"{key}: undefined {field}")
        for field in (
            "idempotence",
            "transaction",
            "cancellation",
            "retry_policy",
            "unknown",
            "consumer",
            "adapter",
            "contract_tests",
        ):
            if not port.get(field):
                errors.append(f"{key}: missing {field}")
        if port.get("timeout_ms", 0) <= 0:
            errors.append(f"{key}: unbounded timeout")
        if port["effect"] in {"EXTERNAL_EFFECT", "SECRET_BOUNDARY"}:
            if port.get("retry_policy", {}).get("max_attempts") != 1:
                errors.append(f"{key}: blind external effect retry")
    return errors


def feature_catalog_errors(root: Path, schema: dict) -> list[str]:
    """Validate traceability, not the behavior of unimplemented strategies."""
    contracts = root / "docs/contracts"
    features = json.loads((contracts / "feature-catalog.json").read_text())["features"]
    strategies = json.loads((contracts / "strategy-specs.json").read_text())["strategies"]
    errors = []
    ids = {f["id"] for f in features}
    if len(ids) != len(features):
        errors.append("duplicate feature id")
    for feature in features:
        name = feature["id"]
        properties = schema["$defs"].get(feature["source_schema"], {}).get("properties", {})
        if not set(feature["original_fields"]) <= set(properties):
            errors.append(f"{name}: unknown original source fields")
        if not set(feature["dependencies"]) <= ids:
            errors.append(f"{name}: undefined feature dependency")
        for field in (
            "formula",
            "unit",
            "entity",
            "event_time",
            "available_at",
            "missing_policy",
            "late_policy",
            "validations",
            "quality_constraints",
            "permission",
            "definition_version",
            "classification",
            "consumers",
        ):
            if not feature.get(field):
                errors.append(f"{name}: missing {field}")
        if feature["window_s"] < 0 or feature["validity_s"] <= 0:
            errors.append(f"{name}: invalid temporal bounds")
    try:
        tuple(TopologicalSorter({f["id"]: f["dependencies"] for f in features}).static_order())
    except CycleError:
        errors.append("feature dependency cycle")
    expected_ids = {f"S{n:02}" for n in range(1, 21)}
    if {x["strategy_id"] for x in strategies} != expected_ids or len(strategies) != 20:
        errors.append("strategy coverage must be exactly S01..S20")
    fields = set(schema["$defs"]["StrategyInput"]["properties"])
    for strategy in strategies:
        name = strategy["strategy_id"]
        if not set(strategy["required_feature_ids"] + strategy["optional_feature_ids"]) <= ids:
            errors.append(f"{name}: undefined feature")
        if not set(strategy["required_context"]) <= fields:
            errors.append(f"{name}: undefined typed context")
        for field in ("minimum_data", "algorithm_and_exit", "experiment", "acceptance", "oracle"):
            if not strategy.get(field):
                errors.append(f"{name}: missing {field}")
        for task_field in ("evaluator_task", "experiment_task"):
            if not (root / "docs/tasks" / (strategy[task_field] + ".md")).exists():
                errors.append(f"{name}: missing task")
    return errors
