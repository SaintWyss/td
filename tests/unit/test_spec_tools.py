"""Adversarial checks for the validation gate, not financial behavior."""

import json
import shutil
from pathlib import Path

import pytest

from tools.sync_docs import sync
from tools.validate_spec import ROOT, local_ref_errors, validate, validate_dag


@pytest.fixture
def spec_copy(tmp_path: Path) -> Path:
    shutil.copytree(ROOT / "docs", tmp_path / "docs")
    shutil.copy(ROOT / "README.md", tmp_path / "README.md")
    return tmp_path


def test_dag_accepts_dependency_order_independent_of_ids() -> None:
    assert (
        validate_dag(
            [
                {"id": "T-001", "dependencies": ["T-002"]},
                {"id": "T-002", "dependencies": []},
            ]
        )
        == []
    )


def test_dag_rejects_cycle_and_missing_dependency() -> None:
    failures = validate_dag(
        [
            {"id": "T-001", "dependencies": ["T-002", "T-999"]},
            {"id": "T-002", "dependencies": ["T-001"]},
        ]
    )
    assert "task dependency cycle" in failures
    assert "T-001: unknown dependency T-999" in failures


def test_references_fail_closed_without_network() -> None:
    assert local_ref_errors({"$ref": "https://example.invalid/schema"})
    assert local_ref_errors({"$ref": "#/$defs/Missing"})
    assert not local_ref_errors({"$defs": {"A": {}}, "$ref": "#/$defs/A"})


def test_table_check_is_read_only_and_sync_repairs_drift(spec_copy: Path) -> None:
    path = spec_copy / "docs/33-implementation-backlog.md"
    path.write_text(path.read_text().replace("V0 / P0", "V99 / P0", 1))
    before = path.read_bytes()
    assert "docs/33-implementation-backlog.md" in sync(spec_copy, check=True)
    assert path.read_bytes() == before
    sync(spec_copy, check=False)
    assert not sync(spec_copy, check=True)


def test_gate_rejects_invalid_positive_example(spec_copy: Path) -> None:
    path = spec_copy / "docs/contracts/examples/valid.json"
    examples = json.loads(path.read_text())
    examples["Money"]["atoms"] = 1.5
    path.write_text(json.dumps(examples))
    result = validate(spec_copy)
    assert result["status"] == "FAIL"
    assert any("example Money" in e for e in result["errors"])


def test_gate_rejects_valid_negative_example(spec_copy: Path) -> None:
    positive = json.loads((spec_copy / "docs/contracts/examples/valid.json").read_text())
    path = spec_copy / "docs/contracts/examples/invalid.json"
    examples = json.loads(path.read_text())
    examples[0]["value"] = positive[examples[0]["schema"]]
    path.write_text(json.dumps(examples))
    result = validate(spec_copy)
    assert any("unexpectedly accepted" in e for e in result["errors"])
