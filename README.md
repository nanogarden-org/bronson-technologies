# Bronson Technologies

Bronson Technologies is a public-facing portfolio and research index for applied AI systems, workflow design, knowledge provenance, and early platform experiments.

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
- `portfolio/` — selected work organized by capability area.
- `platforms/abci/` — early ABCI architecture extraction, specification drafts, safety boundary, and simulated adapter.
- `papers/` — public papers, abstracts, and publication metadata.
- `demos/` — runnable or inspectable demonstrations using synthetic or approved data.
- `evidence-index.md` — central map connecting claims to reviewable evidence.

## Evidence standard

Each public claim should identify its evidence, maturity level, limitations, and verification method. Appropriate maturity labels include `concept`, `prototype`, `implemented toolkit`, `tested demo`, `deployed pilot`, and `production system`.

## Publication boundary

ABCI is an original creation of Bronson Technologies / NanoGarden. The repository currently does not publish a license file, so public visibility confirms authorship and publication—not a general permission to reuse the ABCI material. Add an explicit license only when you want to define reuse terms.

Keep secrets, private client data, unpublished commercial material, private credential identifiers, and third-party content without permission out of this repository. Public release does not turn an unsupported claim into evidence: retain the distinction between draft, research preview, tested demonstration, and production system.
