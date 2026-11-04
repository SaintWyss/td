.PHONY: setup verify-spec lint typecheck test-unit check docs-sync

setup:
	uv sync --locked
	pnpm --dir web install --frozen-lockfile

verify-spec:
	uv run --frozen python tools/validate_spec.py --report audit/latest.json

lint:
	uv run --frozen ruff check backend tools tests
	uv run --frozen ruff format --check backend tools tests

typecheck:
	uv run --frozen mypy
	pnpm --dir web typecheck

test-unit:
	uv run --frozen pytest

check: verify-spec lint typecheck test-unit

docs-sync:
	uv run --frozen python tools/sync_docs.py
