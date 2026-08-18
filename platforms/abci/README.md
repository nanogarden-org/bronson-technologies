# ABCI — Adaptive Bio-Cryptic Interface

**Status:** early research architecture / pre-validation MVP specification.

ABCI is a hardware-agnostic framework for routing neurological and physiological information with provenance, consent boundaries, temporal validity, confidence, and replaceable sensor adapters. It is intended to sit between sensing devices and applications, much like a runtime/protocol layer rather than a single headset or biometric product.

NeuroCrown is referenced here as a proposed/reference embodiment of ABCI: a wearable and peripheral sensing ecosystem that can supply EEG, autonomic, muscular, temperature, and interaction-state signals to an ABCI runtime. ABCI itself is not defined by NeuroCrown hardware.

## What this repo formalizes

- The known ABCI/NeuroCrown corpus inventory and provenance posture.
- A public-safe architectural extraction from the corpus.
- Legal, safety, privacy, and non-medical boundaries.
- Falsifiable claims that can be tested without pretending early prototypes are validated science.
- A repo skeleton for SDK/runtime development.

## Core distinction

```text
ABCI = protocol / runtime / trust layer
NeuroCrown = reference sensing platform and experience ecosystem
```

## Maturity warning

ABCI is not a medical device, diagnostic system, treatment, or validated biometric identity product. Any physiological or neurological claims in this repo are hypotheses until tested under documented protocols.

## Suggested repo path

This package can live inside `nanogarden-org/bronson-technologies` under:

```text
platforms/abci/
```

It can later be promoted to its own repo, for example:

```text
nanogarden-org/abci
```

## License posture

No final open-source license is asserted by this extraction. Keep the initial repo private or research-preview until Bronson Technologies / NanoGarden chooses a license.
