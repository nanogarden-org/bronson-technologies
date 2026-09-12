#!/usr/bin/env python3
"""Validate publication metadata and local evidence paths."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog"


def read(name: str) -> dict:
    return json.loads((CATALOG / name).read_text(encoding="utf-8"))


def main() -> int:
    config = read("site.json")
    ontology = read("ontology.json")
    registry = read("artifacts.json")
    maturity = set(config["maturity_vocabulary"])
    availability = set(config["availability_vocabulary"])
    planes = {plane["id"] for plane in ontology["planes"]}
    artifacts = registry.get("artifacts", [])
    ids = [item.get("id") for item in artifacts]
    errors: list[str] = []

    if len(ids) != len(set(ids)):
        errors.append("artifact ids must be unique")
    required = {"id", "title", "summary", "kind", "planes", "maturity", "availability", "evidence", "relations"}
    for item in artifacts:
        name = item.get("id", "<missing-id>")
        missing = sorted(required - item.keys())
        if missing:
            errors.append(f"{name}: missing fields: {', '.join(missing)}")
            continue
        if item["maturity"] not in maturity:
            errors.append(f"{name}: unknown maturity {item['maturity']!r}")
        if not item["planes"] or not set(item["planes"]) <= planes:
            errors.append(f"{name}: planes must be non-empty and defined in ontology")
        state = item["availability"]
        for field in ("class", "public", "license", "route"):
            if field not in state:
                errors.append(f"{name}: availability.{field} is required")
        if state.get("class") not in availability:
            errors.append(f"{name}: unknown availability class {state.get('class')!r}")
        if state.get("public") is not True:
            errors.append(f"{name}: site registry may contain only explicitly public artifacts")
        if not item["evidence"]:
            errors.append(f"{name}: at least one evidence record is required")
        for evidence in item["evidence"]:
            for field in ("type", "label", "verification"):
                if not evidence.get(field):
                    errors.append(f"{name}: evidence.{field} is required")
            if not evidence.get("url") and not evidence.get("path"):
                errors.append(f"{name}: evidence requires url or path")
            path = evidence.get("path")
            if path and not (ROOT / path.rstrip("/")).exists():
                errors.append(f"{name}: local evidence path does not exist: {path}")
        for relation in item["relations"]:
            if relation not in ids:
                errors.append(f"{name}: unknown relation {relation!r}")

    for item_id in ontology["spine"]:
        if item_id not in ids:
            errors.append(f"ontology spine references unknown artifact {item_id!r}")
    for nav in config["navigation"]:
        if not {"label", "path", "order"} <= nav.keys():
            errors.append("every navigation item requires label, path, and order")

    if errors:
        print("Catalog validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Validated {len(artifacts)} public artifacts across {len(planes)} ontology planes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
