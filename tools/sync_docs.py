"""Render tables from canonical catalogs; --check fails instead of writing."""

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def rendered_tables(root: Path) -> dict[str, list[str]]:
    tasks = json.loads((root / "docs/tasks/index.json").read_text())
    requirements = json.loads((root / "docs/requirements.json").read_text())
    return {
        "docs/33-implementation-backlog.md": [
            "| Tarea | Fase / prioridad | Feature y objetivo | Dependencias |",
            "|---|---|---|---|",
            *[
                f"| [{t['id']}](tasks/{t['id']}.md) | {t['phase']} / {t['priority']} | "
                f"{t['title']} | {', '.join(t['dependencies']) or '—'} |"
                for t in tasks
            ],
        ],
        "docs/03-functional-requirements.md": [
            "| ID | Fase | Requisito verificable | Componente |",
            "|---|---|---|---|",
            *[
                f"| {r['id']} | {r['phase']} | {r['statement']} | {r['component']} |"
                for r in requirements
            ],
        ],
        "docs/35-traceability-matrix.md": [
            "| Requisito / origen | Componente | Contrato | Tarea | Prueba | Criterio |",
            "|---|---|---|---|---|---|",
            *[
                f"| {r['id']} {r['source_section']} | {r['component']} | {r['contract']} | "
                f"{r['task']} | {r['test']} | {r['acceptance']} |"
                for r in requirements
            ],
        ],
    }


def sync(root: Path, *, check: bool) -> list[str]:
    changed = []
    for name, rows in rendered_tables(root).items():
        path = root / name
        original = path.read_text(encoding="utf-8")
        lines = original.splitlines()
        start = next(i for i, line in enumerate(lines) if line.startswith("|"))
        end = start
        while end < len(lines) and lines[end].startswith("|"):
            end += 1
        expected = "\n".join(lines[:start] + rows + lines[end:]) + "\n"
        if original != expected:
            changed.append(name)
            if not check:
                path.write_text(expected, encoding="utf-8")
    return changed


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    differences = sync(ROOT, check=args.check)
    print(json.dumps({"changed": differences, "check_only": args.check}, ensure_ascii=False))
    raise SystemExit(1 if args.check and differences else 0)
