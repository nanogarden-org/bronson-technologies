# GitHub Pages publication contract

## Authority layers

1. Repository source, Git history, tests, and canonical evidence records are authoritative.
2. `portfolio/proof-map.yaml` remains the canonical structured proof record.
3. `catalog/artifacts.json` is the canonical public-site publication registry.
4. `site/` is generated output and is never edited as an authority source.
5. GitHub Pages is a presentation and routing surface, not a second datastore.

## Publication gate

Every artifact appearing on the public site must declare:

- a stable artifact ID;
- title, summary, and kind;
- at least one ontology plane;
- maturity from the controlled vocabulary;
- availability class, public flag, license posture, and acquisition route;
- at least one evidence record with a verification instruction; and
- relations only to registered public artifacts.

`scripts/validate_catalog.py` enforces these fields and verifies local evidence paths. A visible repository file is not automatically an offering. Availability is explicit metadata and public visibility does not grant reuse rights.

## Compatibility boundary

The migration does not delete or relocate `portfolio/`, `profile/`, `credentials/`, `credentials.html`, `evidence-index.md`, or the proof-map mirrors. The generator copies the previous portfolio into `/legacy/`, projects the canonical credential HTML at `/developer/credentials/`, and preserves the former credential URL as a redirect.

## Navigation

Primary navigation is generated exclusively from `catalog/site.json`. Add, remove, reorder, or rename a public entry point there; do not hand-edit generated HTML.

## Deployment

The Pages workflow runs catalog validation, generates the static projection, runs the test suite, uploads `site/` as the Pages artifact, and deploys it through the protected `github-pages` environment. Pull requests run validation and generation without deploying.
