"""Check independent documentary oracles; this is not a ledger implementation."""

import json
from collections import defaultdict
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
    return errors
