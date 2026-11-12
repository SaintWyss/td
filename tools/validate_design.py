"""Checks of documentary contracts. Never executes trading or declares G-DESIGN ready."""

import copy
import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker


def negative_reason_errors(schema: dict, positives: dict, examples: list[dict]) -> list[str]:
    """Require the single declared omission, not an unrelated invalid field."""
    errors = []
    for ex in examples:
        expected = ex.get("expected", {})
        missing = expected.get("missing_field")
        if expected.get("validator") != "required" or expected.get("instance_path") != []:
            errors.append(f"negative reason {ex['schema']}: missing precise required-field oracle")
            continue
        original = copy.deepcopy(positives[ex["schema"]])
        if missing not in original:
            errors.append(f"negative reason {ex['schema']}: missing field is not in positive")
            continue
        del original[missing]
        if ex["value"] != original:
            errors.append(
                f"negative reason {ex['schema']}: incidental mutation differs from oracle"
            )
        validator = Draft202012Validator({**schema, "$ref": f"#/$defs/{ex['schema']}"})
        if not list(validator.iter_errors(ex["value"])):
            errors.append(f"negative reason {ex['schema']}: omission accepted")
    return errors


def machine_errors(name: str, machine: dict) -> list[str]:
    errors = []
    states = set(machine["states"])
    terminals = set(machine.get("terminal", []))
    edges = machine["transitions"]
    reached = {machine["initial"]}
    for _ in states:
        for edge in edges:
            if not edge.get("guard", "").strip():
                errors.append(f"{name}: empty guard")
            if edge["source"] in terminals:
                errors.append(f"{name}: transition from terminal")
            if edge["source"] not in states or edge["target"] not in states:
                errors.append(f"{name}: unknown endpoint")
            if edge["source"] in reached:
                reached.add(edge["target"])
    if reached != states:
        errors.append(f"{name}: unreachable states {sorted(states - reached)}")
    return sorted(set(errors))


def validate_design(root: Path, schema: dict, positives: dict, negatives: list) -> list[str]:
    errors = negative_reason_errors(schema, positives, negatives)
    contracts = root / "docs/contracts"
    machines = json.loads((contracts / "lifecycle-machines.json").read_text())
    machines["order"] = json.loads((contracts / "order-machine.json").read_text())
    machines["cex"] = json.loads((contracts / "cex-order-machine.json").read_text())
    for name, machine in machines.items():
        errors.extend(machine_errors(name, machine))
    for edge in machines["reservation"]["transitions"]:
        if edge["source"] == "ATTEMPTED" and edge["target"] == "RELEASED":
            if "reconciliation" not in edge["guard"]:
                errors.append("reservation: release without reconciliation guard")
    forbidden = {"CANCELLED", "REJECTED", "CREATED"}
    for edge in machines["order"]["transitions"]:
        if edge["source"] == "UNKNOWN" and edge["target"] in forbidden:
            errors.append("order: UNKNOWN has unsafe terminal/retry edge")
    binding = {
        "intent_hash",
        "instrument_id",
        "instrument_revision",
        "rent_asset_id",
        "max_rent_atoms",
        "wallet_id",
        "chain_id",
        "mode",
        "input_asset_id",
        "output_asset_id",
        "fee_asset_id",
        "min_output_atoms",
        "max_fee_atoms",
        "quote_hash",
        "policy_hash",
        "control_epoch",
        "fencing_token",
        "expires_at",
        "reduce_only",
        "allowed_program_ids",
    }
    for name in ("Reservation", "ExecutionIntent"):
        if not binding.issubset(schema["$defs"][name]["required"]):
            errors.append(f"{name}: incomplete required authorization binding")
    if "signed_transaction_b64" not in schema["$defs"]["SignatureResult"]["required"]:
        errors.append("SignatureResult: missing durable signed bytes")
    cases = json.loads((contracts / "examples/adversarial.json").read_text())
    for case in cases:
        validator = Draft202012Validator(
            {**schema, "$ref": f"#/$defs/{case['schema']}"}, format_checker=FormatChecker()
        )
        failures = list(validator.iter_errors(case["value"]))
        if case["valid"] and failures:
            errors.append(f"adversarial {case['id']}: valid boundary rejected")
        elif not case["valid"]:
            if not failures:
                errors.append(f"adversarial {case['id']}: invalid boundary accepted")
            elif not any(
                e.validator == case["keyword"] and list(e.absolute_path) == case["path"]
                for e in failures
            ):
                errors.append(f"adversarial {case['id']}: wrong validation reason")
    tasks = json.loads((root / "docs/tasks/index.json").read_text())
    for task in tasks:
        for path in task["files"]:
            if "/t_" in path and path.startswith(("backend/", "web/src/", "infra/")):
                errors.append(f"{task['id']}: provisional production path {path}")
    return errors
