# ABCI — Adaptive Bio-Cryptic Interface

**Status:** early research architecture / validated simulated-emitter slice.

ABCI is a hardware-agnostic framework for routing neurological and physiological information with provenance, consent boundaries, temporal validity, confidence, and replaceable sensor adapters. It is intended to sit between sensing devices and applications, much like a runtime/protocol layer rather than a single headset or biometric product.

NeuroCrown is referenced here as a proposed/reference embodiment of ABCI: a wearable and peripheral sensing ecosystem that can supply EEG, autonomic, muscular, temperature, and interaction-state signals to an ABCI runtime. ABCI itself is not defined by NeuroCrown hardware.

## What this repo formalizes

- the known ABCI/NeuroCrown corpus inventory and provenance posture;
- a public-safe architectural extraction from the corpus;
- legal, safety, privacy, and non-medical boundaries;
- falsifiable claims that can be tested without pretending early prototypes are validated science; and
- a repo skeleton for SDK/runtime development.

## Current verification

The simulated emitter at [`examples/python/simulated_abci_emit.py`](./examples/python/simulated_abci_emit.py) produces a typed, time-bounded claim with simulated provenance, an explicit artifact flag, and permissions that disable raw export and identity binding.

Run it from the repository root:

```text
python platforms/abci/examples/python/simulated_abci_emit.py
```

This is an executable contract demonstration, not physiological validation.

## Core distinction

```text
ABCI = protocol / runtime / trust layer
NeuroCrown = reference sensing platform and experience ecosystem
```

## Maturity warning

ABCI is not a medical device, diagnostic system, treatment, or validated biometric identity product. Any physiological or neurological claims in this repo are hypotheses until tested under documented protocols.

## Public-release posture

This package is a research preview inside `bronson-technologies` and is an original creation of Bronson Technologies / NanoGarden. No separate license notice has yet been selected for the ABCI material; that concerns reuse permissions, not authorship. Publication does not imply clinical, security, or commercial readiness.

## Next implementation gate

Add a simulator/CSV adapter test harness, permission and lifetime checks, and a documented protocol before connecting physical hardware or making physiological claims.
