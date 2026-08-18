# Falsifiable Claims Register

This register separates architectural claims, engineering claims, and biological claims. Early ABCI should prefer claims that can be tested cheaply and safely.

## Claim classes

- **A — Architectural:** about interfaces, modularity, provenance, permissions.
- **E — Engineering:** about runtime behavior, latency, cost, adapter replacement, reliability.
- **B — Biological:** about physiology, neurological state, EEG/GSR/HRV correlations. Highest caution.
- **S — Security:** about spoofing resistance, authentication, replay resistance. Requires adversarial testing.

## Initial claims

| ID | Claim | Class | Test | Passing condition | Failure condition | Status |
|---|---|---:|---|---|---|---|
| ABCI-FAL-001 | ABCI apps can run against simulated data without physical NeuroCrown hardware. | A/E | Build simulated adapter and run demo. | Demo produces valid typed state claims. | Demo requires hardware-specific code. | proposed |
| ABCI-FAL-002 | A new sensor can be integrated by adding an adapter without changing downstream demo app logic. | A/E | Add CSV adapter after simulated adapter. | Demo app unchanged except config. | Demo app requires sensor-specific branches. | proposed |
| ABCI-FAL-003 | Every emitted state claim can include source, transform, timestamp, confidence, and expiry. | A/E | Unit tests over message schema. | Missing fields rejected. | Untyped/missing-provenance output accepted. | proposed |
| ABCI-FAL-004 | Permission policy can prevent raw-signal access while allowing derived-state access. | A/S | Mock app requests raw EEG and focus state under limited scope. | Raw denied, focus allowed. | Raw available without scope. | proposed |
| ABCI-FAL-005 | State claims expire and are rejected after max age. | A/E | Replay stale event. | Runtime rejects stale event for current-state query. | Runtime accepts stale event as fresh. | proposed |
| ABCI-FAL-006 | Personal calibration improves repeatability over generic thresholds for a chosen biofeedback task. | B/E | Within-subject sessions; compare generic vs calibrated thresholds. | Predefined metric improves out-of-sample. | No improvement or overfit. | future |
| ABCI-FAL-007 | Adding peripheral GSR/HRV/EMG features improves classification of a target state over EEG-only baseline. | B/E | Controlled protocol with train/test split. | Multimodal model beats EEG-only by predefined margin. | No significant improvement. | future |
| ABCI-FAL-008 | ABCI authentication tokens reduce replay risk compared with static biometric template matching. | S | Threat-model replay simulation. | Replayed stale token rejected. | Replay succeeds within protected scope. | future |

## Non-falsifiable or deferred claims

Do not treat the following as active scientific claims without stricter definitions:

- consciousness expansion,
- spiritual resonance,
- full sensory input,
- reliable emotion reading,
- identity continuity,
- direct mental-state proof.

These may remain as speculative research language or experience design motifs, but they should not be presented as validated ABCI capabilities.
