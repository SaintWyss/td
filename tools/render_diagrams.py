"""Render every Mermaid source; explicit local renderer/browser required, no downloads."""

import argparse
import hashlib
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mmdc", required=True)
    parser.add_argument("--chromium", required=True)
    parser.add_argument("--output", type=Path, default=ROOT / "audit/g-design/diagrams")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    config = args.output / "puppeteer.json"
    config.write_text(json.dumps({"executablePath": args.chromium, "args": ["--no-sandbox"]}))

    def render(source: Path) -> dict:
        dest = args.output / (source.stem + ".svg")
        cmd = [
            args.mmdc,
            "-p",
            str(config),
            "-i",
            str(source),
            "-o",
            str(dest),
            "--size",
            "1800",
        ]
        run = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        (args.output / (source.stem + ".log")).write_text(run.stdout + run.stderr)
        return {
            "source": str(source.relative_to(ROOT)),
            "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            "command": cmd,
            "exit_code": run.returncode,
            "svg_sha256": hashlib.sha256(dest.read_bytes()).hexdigest()
            if run.returncode == 0 and dest.exists()
            else None,
        }

    with ThreadPoolExecutor(max_workers=3) as pool:
        records = list(pool.map(render, sorted((ROOT / "docs/diagrams").glob("*.mmd"))))
    version = subprocess.run([args.mmdc, "--version"], capture_output=True, text=True, timeout=10)
    (args.output / "render.json").write_text(
        json.dumps(
            {
                "renderer_version": version.stdout.strip(),
                "records": records,
                "scope": "syntax/render only; visual review recorded separately",
            },
            indent=2,
        )
        + "\n"
    )
    print(
        json.dumps(
            {"rendered": len(records), "failures": sum(r["exit_code"] != 0 for r in records)}
        )
    )
    return int(any(r["exit_code"] != 0 for r in records))


if __name__ == "__main__":
    raise SystemExit(main())
