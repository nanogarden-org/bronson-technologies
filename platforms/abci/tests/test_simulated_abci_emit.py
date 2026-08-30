from datetime import datetime
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "examples" / "python"))

from simulated_abci_emit import emit_simulated_focus


class SimulatedABCIStateTests(unittest.TestCase):
    def test_emission_is_typed_time_bounded_and_non_authorizing(self):
        state = emit_simulated_focus()

        self.assertTrue(state.id)
        self.assertEqual(state.type, "cognitive.focus.simulated")
        self.assertGreaterEqual(state.value, 0.45)
        self.assertLessEqual(state.value, 0.80)
        self.assertGreaterEqual(state.confidence, 0.0)
        self.assertLessEqual(state.confidence, 1.0)
        self.assertGreater(
            datetime.fromisoformat(state.expires_at_utc),
            datetime.fromisoformat(state.timestamp_utc),
        )
        self.assertEqual(state.provenance["source_modality"], "simulated")
        self.assertIn("not_real_physiology", state.provenance["artifact_flags"])
        self.assertFalse(state.permissions["raw_export_allowed"])
        self.assertFalse(state.permissions["identity_binding_allowed"])


if __name__ == "__main__":
    unittest.main()
