from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class GeneratedSiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        subprocess.run([sys.executable, "scripts/validate_catalog.py"], cwd=ROOT, check=True)
        subprocess.run([sys.executable, "scripts/build_site.py"], cwd=ROOT, check=True)
        cls.config = json.loads((ROOT / "catalog/site.json").read_text(encoding="utf-8"))
        cls.registry = json.loads((ROOT / "catalog/artifacts.json").read_text(encoding="utf-8"))

    def test_required_entry_points_exist(self) -> None:
        for route in ("architecture", "free", "licensed", "developer"):
            self.assertTrue((ROOT / "site" / route / "index.html").is_file(), route)

    def test_interest_test_offer_pages_are_projected(self) -> None:
        for filename in (
            "ai-workflow-boundary-checklist.html",
            "simplified-evidence-interpretation-action-model.html",
            "best-workflow-tips-for-non-standard-situations.html",
            "verify-ai-outputs-before-you-send.html",
        ):
            self.assertTrue((ROOT / "site" / "offers" / filename).is_file(), filename)

    def test_free_field_note_is_projected_and_downloadable(self) -> None:
        self.assertTrue((ROOT / "site" / "free" / "protocol-independent-human-ai-operating-layer.html").is_file())
        self.assertTrue((ROOT / "site" / "free" / "protocol-independent-human-ai-operating-layer.md").is_file())
        page = (ROOT / "site" / "free" / "index.html").read_text(encoding="utf-8")
        self.assertIn("protocol-independent-human-ai-operating-layer.html", page)

    def test_every_artifact_has_a_detail_page(self) -> None:
        for item in self.registry["artifacts"]:
            page = ROOT / "site" / "architecture" / item["id"] / "index.html"
            self.assertTrue(page.is_file(), item["id"])

    def test_navigation_is_rendered_from_metadata(self) -> None:
        page = (ROOT / "site/index.html").read_text(encoding="utf-8")
        for item in self.config["navigation"]:
            self.assertIn(item["label"], page)
            self.assertIn(item["path"], page)

    def test_legacy_portfolio_is_preserved_in_projection(self) -> None:
        for filename in ("index.html", "profile.html", "credentials.html", "proof-map.yaml"):
            self.assertTrue((ROOT / "site" / "legacy" / filename).is_file(), filename)

    def test_credentials_are_projected_behind_developer(self) -> None:
        self.assertEqual(
            (ROOT / "credentials.html").read_bytes(),
            (ROOT / "site/developer/credentials/index.html").read_bytes(),
        )
        redirect = (ROOT / "site/credentials.html").read_text(encoding="utf-8")
        self.assertIn("/developer/credentials/", redirect)

    def test_pages_use_architecture_first_branding(self) -> None:
        home = (ROOT / "site/index.html").read_text(encoding="utf-8")
        self.assertIn("ARCHITECTURE BEFORE PORTFOLIO", home)
        self.assertNotIn("Robert Bronson / Robin A. Bronson's applied technology work", home)


if __name__ == "__main__":
    unittest.main()
