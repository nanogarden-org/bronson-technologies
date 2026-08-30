# Bronson Technologies

Bronson Technologies is a public-facing portfolio and research index for applied AI systems, workflow design, knowledge provenance, and early platform experiments.

## Current status

This repository is a **public-release candidate**. The current tree contains portfolio and research documentation, credential-index templates, and an early ABCI research-preview package. It does not contain credential secrets, certificate originals, private source corpora, or client data.

The latest implementation work is on the `abci-formalization` branch. It adds the ABCI platform specification and a dependency-free simulated state emitter. That branch is the validated implementation candidate for `main`.

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

The check should produce a typed, time-bounded state claim marked as simulated, with raw export and identity binding disabled. GitHub Actions also compiles and exercises the emitter on pushes and pull requests to `main`.

## Repository map

- `profile/` — professional biography, capability map, and career timeline.
- `credentials/` — credential indexes organized by provider. Current entries are safe templates; do not add private IDs, QR codes, account credentials, or unredacted certificate originals.
- `portfolio/` — selected work organized by capability area.
- `platforms/abci/` — early ABCI architecture extraction, specification drafts, safety boundary, and simulated adapter.
- `papers/` — public papers, abstracts, and publication metadata.
- `demos/` — runnable or inspectable demonstrations using synthetic or approved data.
- `evidence-index.md` — central map connecting claims to reviewable evidence.

## Evidence standard

Each public claim should identify its evidence, maturity level, limitations, and verification method. Appropriate maturity labels include `concept`, `prototype`, `implemented toolkit`, `tested demo`, `deployed pilot`, and `production system`.

## Publication boundary

Keep secrets, private client data, unpublished commercial material, private credential identifiers, and third-party content without permission out of this repository. Public release does not turn an unsupported claim into evidence: retain the distinction between draft, research preview, tested demonstration, and production system.

The repository does not currently assert a separate open-source license for the ABCI extraction. Check the applicable file-level notices before reusing research or portfolio material.
