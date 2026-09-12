# Maintenance

1. Update `proof-map.yaml` first for proof or evidence changes.
2. Mirror the proof change to `proof-map.json` and `data/search-index.json`.
3. Update `catalog/artifacts.json` when the public site's maturity, availability, evidence, or ontology relationship changes.
4. Run `python scripts/validate_catalog.py`, `python scripts/build_site.py`, and the tests from the repository root.
5. Update preserved portfolio HTML only when the legacy proof walkthrough itself changes.
6. Prefer links to public implementation evidence over duplicated claims.
7. Preserve historical evidence wording and interpretation boundaries.
8. Verify external validators and public links.
9. Commit with an evidence-specific message rather than a generic portfolio update.
