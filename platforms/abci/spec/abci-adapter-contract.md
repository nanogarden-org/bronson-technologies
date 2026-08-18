# ABCI Adapter Contract Draft

An ABCI adapter converts a hardware, file, simulator, or service stream into typed ABCI observations.

## Required responsibilities

1. Declare capabilities.
2. Emit timestamped observations.
3. Report signal quality where available.
4. Preserve source metadata.
5. Refuse unsupported permission scopes.
6. Avoid leaking raw data unless explicitly configured.

## Minimal Python interface

```python
class ABCIAdapter:
    def capabilities(self) -> dict: ...
    def read(self) -> list[dict]: ...
    def close(self) -> None: ...
```

Adapters are unstable implementation edges. Applications should depend on ABCI state/query interfaces, not adapter internals.
