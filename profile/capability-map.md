# Capability Map

This page is the fast translation layer between the broader architecture portfolio and concrete public evidence. Maturity describes the artifact named here, not every related idea or private implementation.

| Capability | What it means in practice | Supporting evidence | Maturity |
|---|---|---|---|
| AI systems design | Model stages, controls, approval gates, provenance, authority boundaries, and reviewable outputs | [TurtleML](https://github.com/nanogarden-org/TurtleML), [LCA-MVP](https://github.com/nanogarden-org/LCA-MVP), [ABCI research preview](../platforms/abci/) | Executable alpha / research architecture |
| Workflow automation | Convert repeatable handoffs into explicit contracts, checks, routing, and reusable tooling | [B.o.B.W.](https://github.com/nanogarden-org/BOBW), [Portfolio methodology](../portfolio/methodology.html) | Tested local reference implementation + documented methodology |
| Knowledge provenance | Keep source identity, transformations, claims, interpretations, and authorization boundaries distinguishable | [B.o.B.W.](https://github.com/nanogarden-org/BOBW), [LCA-MVP](https://github.com/nanogarden-org/LCA-MVP), [Evidence index](../evidence-index.md) | Implemented/tested components plus active architecture |
| Offline / local-first AI | Design systems that can preserve useful operation and authority boundaries without making cloud access the architectural dependency | [TurtleML](https://github.com/nanogarden-org/TurtleML), [LCA-MVP](https://github.com/nanogarden-org/LCA-MVP) | Executable alpha / local reference foundation |
| Creative and knowledge production | Coordinate source intake, provenance, structured transformation, review, and release across a reusable production workflow | [B.o.B.W.](https://github.com/nanogarden-org/BOBW), [Projects](../portfolio/projects.html), [Methodology](../portfolio/methodology.html) | Mixed: tested ingestion component + active-development workflow |
| Cross-language conformance | Express architectural semantics so different implementations can be checked against the same decision and integrity behavior | [LCA-MVP](https://github.com/nanogarden-org/LCA-MVP) | Runnable foundation with Python/Rust conformance evidence |
| Capability extraction | Turn solved problems and recurring reasoning into explicit, reusable methods rather than one-off answers | [Methodology](../portfolio/methodology.html), [Proof map](../portfolio/proof-map.yaml) | Documented methodology / active refinement |

## Reading rule

Use the linked repository or artifact as the authority for its current status. This map intentionally avoids upgrading a prototype into a production claim simply because the underlying architecture is broader.

## Direct verification paths

- [BOBW validation and limitations](https://github.com/nanogarden-org/BOBW/blob/main/docs/validation.md).
- [TurtleML authority tests](https://github.com/nanogarden-org/TurtleML/blob/main/tests/test_authority.py) and [demo](https://github.com/nanogarden-org/TurtleML/blob/main/examples/pump_demo.py).
- [LCA 001a conformance scope and commands](https://github.com/nanogarden-org/LCA-MVP/blob/main/conformance/README.md); MVP 002 remains proposed architecture.

See the [documentation process](../docs/hiring-review-process.md) for contribution, scope, and evidence requirements.
