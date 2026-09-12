# Bronson Technologies

Bronson Technologies is the public architecture root for inspectable AI systems, workflow design, knowledge provenance, bounded automation, and early platform experiments. The developer portfolio remains available as evidence, but it is no longer the repository's organizing identity.

## Architecture-first website

GitHub Pages is built as a disposable projection of repository authority:

- `catalog/site.json` defines site identity, routes, and navigation;
- `catalog/ontology.json` defines the architecture planes and provenance spine;
- `catalog/artifacts.json` is the publication registry, requiring maturity, availability, and evidence metadata for every public artifact;
- `scripts/validate_catalog.py` blocks incomplete or invalid publication records;
- `scripts/build_site.py` generates `site/`; and
- `.github/workflows/pages.yml` validates, tests, builds, and deploys the Pages artifact from `main`.

The public entry points are `/architecture/`, `/free/`, `/licensed/`, and `/developer/`. Existing profile, credential, portfolio, and proof files remain canonical in their current repository locations. The prior portfolio is projected under `/legacy/`; credentials are projected under `/developer/credentials/` with a compatibility redirect from the earlier public path.

Build and verify locally with Python 3.11+:

```text
python scripts/validate_catalog.py
python scripts/build_site.py
python -m unittest discover -s tests -v
```

## Searchable proof portfolio

Start with the generated architecture registry for the architecture-first interface. The preserved [`portfolio/index.html`](portfolio/index.html) remains the human-readable proof walkthrough connecting identity, credentials, projects, methodologies, third-party credibility, and public implementation evidence.

Machine-readable proof entry points are available as [`portfolio/proof-map.yaml`](portfolio/proof-map.yaml), [`portfolio/proof-map.json`](portfolio/proof-map.json), [`portfolio/data/search-index.json`](portfolio/data/search-index.json), and [`portfolio/llms.txt`](portfolio/llms.txt).

## Current status

This repository is a **public-release candidate**. The current tree contains portfolio and research documentation, credential indexes, and an early ABCI research-preview package. It does not contain credential secrets, certificate originals, private source corpora, or client data.

The `main` branch now includes the ABCI platform specification and a dependency-free simulated state emitter promoted from the implementation candidate branch.

The repository is intentionally clear about maturity:

- portfolio categories may be scaffolds or release candidates;
- claims should point to inspectable evidence;
- the ABCI package is research architecture, not a medical or security product; and
- placeholders remain placeholders until evidence and publication approval exist.

## Verification

The ABCI simulated emitter can be checked with Python 3.11+:

```text
python platforms/abci/examples/python/simulated_abci_emit.py
```

The check should produce a typed, time-bounded state claim marked as simulated, with raw export and identity binding disabled. This command is the canonical manual verification path for the current research preview.

## Repository map

- `profile/` — professional biography, capability map, and career timeline.
- [`credentials.html`](credentials.html) — public-facing living index of current credentials, project evidence, proficiency, and planned study.
- `credentials/` — credential indexes organized by provider. Current entries are safe templates; do not add private IDs, QR codes, account credentials, or unredacted certificate originals.
- [`portfolio/`](portfolio/) — selected work organized by capability area plus the searchable human/machine-readable proof map.
- `platforms/abci/` — early ABCI architecture extraction, specification drafts, safety boundary, and simulated adapter.
- `papers/` — public papers, abstracts, and publication metadata.
- `demos/` — runnable or inspectable demonstrations using synthetic or approved data.
- `evidence-index.md` — central map connecting claims to reviewable evidence.

## Evidence standard

Each public claim should identify its evidence, maturity level, limitations, and verification method. Appropriate maturity labels include `concept`, `prototype`, `implemented toolkit`, `tested demo`, `deployed pilot`, and `production system`.

The proof portfolio additionally separates historical third-party credibility, institutional credentials, active-development architecture, and inspectable implementation evidence rather than treating them as interchangeable forms of proof.

## Authorship and publication boundary

ABCI and the original Bronson Technologies content and repository structures are created and owned by Robert Bronson, also published under the author name Robin A Bronson. See [`AUTHORS.md`](AUTHORS.md) for the public attribution statement and the distinction between the author-name alias and the `nanogarden-org` GitHub hosting identity.

The repository currently does not publish a license file for the original Bronson Technologies material, so public visibility confirms authorship and publication—not a general permission to reuse it. Add an explicit license only when you want to define reuse terms. Third-party names, logos, certificate records, course materials, and linked resources remain attributed to their respective owners.

Keep secrets, private client data, unpublished commercial material, private credential identifiers, and third-party content without permission out of this repository. Public release does not turn an unsupported claim into evidence: retain the distinction between draft, research preview, tested demonstration, and production system.
