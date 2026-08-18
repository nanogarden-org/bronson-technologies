# ABCI Architecture Extraction

## One-line definition

ABCI is a hardware-agnostic physiological information runtime that converts noisy biological signals into typed, time-bounded, permission-aware, provenance-carrying state claims.

## Layer model

```text
Biological source
  ↓
Sensor / acquisition adapter
  ↓
Signal normalization
  ↓
Feature extraction
  ↓
Multimodal fusion
  ↓
Typed state claim
  ↓
Trust / permission / provenance layer
  ↓
Application
```

## Design invariants

| ID | Invariant | Meaning | Falsification pressure |
|---|---|---|---|
| ABCI-INV-001 | Sensor independence | No single device defines ABCI. Sensors are adapters. | A downstream app requires vendor-specific raw channels. |
| ABCI-INV-002 | Local-first processing | Raw physiology should remain local unless explicitly exported. | Normal operation requires cloud raw-signal upload. |
| ABCI-INV-003 | Typed physiological claims | `focus`, `theta`, `GSR`, `identity-token`, and `arousal` are distinct types, not interchangeable floats. | The SDK allows untyped arbitrary numeric routing. |
| ABCI-INV-004 | Temporal validity | Physiological state claims expire. | Old claims are reused as current user state. |
| ABCI-INV-005 | Provenance-carrying outputs | Every derived claim should point to source modality, device/adapter, time, transform, and confidence. | A state output cannot explain how it was derived. |
| ABCI-INV-006 | Replaceable hardware | New sensors should require adapters, not architecture rewrites. | Adding a sensor forces changes across application logic. |
| ABCI-INV-007 | Consent-bounded routing | Applications receive only the classes of signals they are authorized to use. | An app can request raw or identity-binding data without permission boundary. |
| ABCI-INV-008 | Calibration accountability | Personal models and thresholds must track calibration context. | Claims lack calibration version or population/user basis. |
| ABCI-INV-009 | Confidence propagation | Derived state should carry uncertainty. | Outputs present categorical states without confidence or quality indicators. |
| ABCI-INV-010 | Simulation before embodiment | The runtime and app contracts must run with simulated streams before physical hardware is mandatory. | Hardware is required before SDK/application development can begin. |

## ABCI vs NeuroCrown

ABCI is the protocol/runtime layer. NeuroCrown is a reference embodiment and research corpus that explores hardware, user experience, multimodal monitoring, guided neurofeedback, and future bio-hybrid interfaces.

## Near-term MVP

The first credible MVP should not claim neurological interpretation. It should demonstrate:

1. Simulated and CSV sensor adapters.
2. Typed signal/state messages.
3. Provenance attached to every output.
4. Permission scopes for raw, feature, and derived-state access.
5. Expiring state claims.
6. A simple neurofeedback demo using simulated data.
7. A test harness that proves invalid permission/type/lifetime requests fail.
