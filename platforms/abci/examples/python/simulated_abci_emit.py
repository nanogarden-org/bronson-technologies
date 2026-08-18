from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timedelta, timezone
from random import random
from uuid import uuid4


@dataclass
class ABCIState:
    id: str
    type: str
    value: float
    confidence: float
    timestamp_utc: str
    expires_at_utc: str
    provenance: dict
    permissions: dict


def emit_simulated_focus() -> ABCIState:
    now = datetime.now(timezone.utc)
    return ABCIState(
        id=str(uuid4()),
        type="cognitive.focus.simulated",
        value=round(0.45 + random() * 0.35, 3),
        confidence=0.50,
        timestamp_utc=now.isoformat(),
        expires_at_utc=(now + timedelta(seconds=2)).isoformat(),
        provenance={
            "source_modality": "simulated",
            "adapter": "simulated.v0",
            "device": "none",
            "transform_chain": ["random_demo_generator"],
            "calibration_id": None,
            "artifact_flags": ["not_real_physiology"],
        },
        permissions={
            "scope": "demo",
            "raw_export_allowed": False,
            "retention": "ephemeral",
            "identity_binding_allowed": False,
        },
    )


if __name__ == "__main__":
    print(asdict(emit_simulated_focus()))
