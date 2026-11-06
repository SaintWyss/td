"""Mutation checks for documentary accounting evidence, not product tests."""

import copy
import json
from pathlib import Path

from tools.validate_r2 import financial_errors

ROOT = Path(__file__).resolve().parents[2]


def fixtures():
    path = ROOT / "docs/contracts"
    return (
        json.loads((path / "scenarios/financial.json").read_text()),
        json.loads((path / "domain.schema.json").read_text()),
    )


def test_financial_oracles_are_internally_consistent():
    document, schema = fixtures()
    assert financial_errors(document, schema) == []


def test_unbalanced_asset_is_rejected_even_if_final_balance_matches():
    document, schema = fixtures()
    case = document["cases"][0]
    case["expected_output"]["journal_lines"][0]["signed_atoms"] = "-24999999"
    case["expected_state"]["balances"]["USDC:EXTERNAL"] = "-124999999"
    assert any("unbalanced per asset" in e for e in financial_errors(document, schema))


def test_balanced_journal_cannot_mask_wrong_final_balance():
    document, schema = fixtures()
    document["cases"][0]["expected_state"]["balances"]["USDC:AVAILABLE"] = "124999999"
    assert any("final balance" in e for e in financial_errors(document, schema))


def test_unknown_reservation_cannot_use_valid_release_oracle():
    document, schema = fixtures()
    case = copy.deepcopy(document["cases"][7])
    case["initial_state"]["context"]["finality"] = "UNKNOWN"
    document["cases"] = [case]
    assert any("UNKNOWN reservation released" in e for e in financial_errors(document, schema))


def test_reversal_cannot_choose_different_accounts():
    document, schema = fixtures()
    case = document["cases"][11]
    case["expected_output"]["journal_lines"][0]["account_id"] = "USDC:COLLATERAL"
    assert any("exact inverse" in e for e in financial_errors(document, schema))
