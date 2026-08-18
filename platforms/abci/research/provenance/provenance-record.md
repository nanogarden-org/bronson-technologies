# Provenance and Accountability Record

## Supplied corpus

Two archives were supplied for this formalization pass:

- NeuroCrown archive: 73 files, earliest visible archive timestamps in July/August 2025, with later files through October 2025 and September 2025 in the supplied folder inventory.
- ABCI archive: 25 files, including the 2025 ABCI whitepaper copy and a June/July 2026 formalization stack.

This record does not prove invention, ownership, novelty, or patentability. It documents what was present in the supplied archives and provides a reproducible hash inventory for accountability.

## Evidence rule

ABCI research should preserve three layers separately:

1. **Provenance:** what existed when.
2. **Experiment:** what was tested and observed.
3. **Evaluation:** what model survives after testing.

Later evaluation must not silently rewrite prior claims.

## Recommended commit practice

Each future repo change should use commit messages that indicate the evidence layer, for example:

```text
provenance: add NeuroCrown corpus inventory
spec: define typed state claim schema
experiment: add simulated adapter demo run
evaluation: revise claim ABCI-FAL-003 after schema test
```
