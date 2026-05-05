"""CLI entrypoint for the AI Legal Team agent."""

import argparse
import sys
from pathlib import Path

from orchestrator import LegalTeamOrchestrator


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="ai-legal-team",
        description="Run the AI Legal Team agents on a document.",
    )
    parser.add_argument("path", type=Path, help="Path to a .txt or .md legal doc")
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if not args.path.exists():
        print(f"file not found: {args.path}", file=sys.stderr)
        return 2

    document = args.path.read_text(encoding="utf-8", errors="ignore")
    report = LegalTeamOrchestrator().run(document)

    if args.json:
        import json
        from dataclasses import asdict

        print(json.dumps(asdict(report), indent=2, default=str))
    else:
        print(report.summary)
        print()
        print("STRATEGY:", report.strategy.posture)
        for p in report.strategy.priorities:
            print("  -", p)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
