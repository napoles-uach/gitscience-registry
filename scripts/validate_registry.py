"""Validate structural publication invariants for a compiled registry."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: validate_registry.py REGISTRY.json")
    path = Path(sys.argv[1])
    registry = json.loads(path.read_text())
    if registry.get("schema_version") != "gitscience-observatory-v1":
        raise SystemExit("unexpected registry schema")
    studies = registry.get("studies", [])
    claims = registry.get("claims", [])
    if not studies or not claims:
        raise SystemExit("registry must contain studies and claims")
    claim_ids = [state.get("claim", {}).get("id") for state in claims]
    if None in claim_ids or len(claim_ids) != len(set(claim_ids)):
        raise SystemExit("claim IDs must be present and unique")
    for state in claims:
        dimensions = state.get("status", {}).get("dimensions", {})
        if "formalization" not in dimensions or "scientific_grounding" not in dimensions:
            raise SystemExit(
                f"claim lacks formalization dimensions: {state.get('claim', {}).get('id')}"
            )
        for formalization in state.get("formalizations", []):
            statement = formalization.get("formal_statement", {})
            approval = formalization.get("semantic_approval", {})
            if formalization.get("status") == "human_approved" and (
                approval.get("status") != "accepted"
                or approval.get("formal_statement_sha256") != statement.get("sha256")
            ):
                raise SystemExit(
                    f"formal statement is not locked: {formalization.get('id')}"
                )
    for study in studies:
        coverage = study.get("coverage", {})
        if coverage.get("shown") != coverage.get("total"):
            raise SystemExit(f"public study has partial coverage: {study.get('id')}")
        if not study.get("article") or not study.get("equations"):
            raise SystemExit(f"study lacks article or equations: {study.get('id')}")
        if study["article"].get("source", {}).get("state") != "committed":
            raise SystemExit(f"article is not committed: {study.get('id')}")
        for equation in study["equations"]:
            if equation.get("source", {}).get("state") != "committed":
                raise SystemExit(f"equation is not committed: {equation.get('id')}")
    print(
        f"Registry valid: {len(studies)} studies, {len(claims)} complete claim states"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
