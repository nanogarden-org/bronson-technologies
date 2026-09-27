#!/usr/bin/env python3
"""Build the GitHub Pages projection from canonical publication metadata."""

from __future__ import annotations

import html
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog"
OUTPUT = ROOT / "site"


def load(name: str) -> dict:
    return json.loads((CATALOG / name).read_text(encoding="utf-8"))


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def path_url(value: str, base_path: str) -> str:
    if value.startswith(("https://", "http://", "mailto:")):
        return value
    return f"{base_path}/{value.lstrip('/')}"


def badge(label: str, value: str, tone: str = "") -> str:
    return f'<span class="badge {esc(tone)}"><b>{esc(label)}</b>{esc(value)}</span>'


def write(route: str, content: str) -> None:
    target = OUTPUT / route.strip("/") / "index.html" if route.strip("/") else OUTPUT / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")


def render_page(config: dict, title: str, eyebrow: str, body: str, description: str) -> str:
    base = config["base_path"]
    nav = "".join(
        f'<a href="{esc(path_url(item["path"], base))}">{esc(item["label"])}</a>'
        for item in sorted(config["navigation"], key=lambda item: item["order"])
    )
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{esc(description)}"><meta name="theme-color" content="#081210">
<title>{esc(title)} | Bronson Technologies</title><link rel="stylesheet" href="{esc(base)}/assets/site.css">
</head><body><a class="skip" href="#content">Skip to content</a>
<header class="site-header"><div class="shell nav"><a class="brand" href="{esc(base)}/"><span class="brand-mark" aria-hidden="true">BT</span><span>Bronson Technologies<small>Architecture Registry</small></span></a><nav aria-label="Primary">{nav}</nav></div></header>
<main id="content">{body}</main>
<footer><div class="shell footer-grid"><div><strong>Bronson Technologies</strong><p>Public representation derived from repository metadata. The repository remains authoritative.</p></div><div><a href="{esc(config['repository_url'])}">Source repository</a><a href="{esc(base)}/artifacts.json">Artifact registry</a><a href="{esc(base)}/llms.txt">llms.txt</a></div></div></footer>
</body></html>"""


def evidence_link(entry: dict, config: dict) -> str:
    href = entry.get("url") or f'{config["repository_url"]}/blob/main/{entry["path"]}'
    if entry.get("path", "").endswith("/"):
        href = f'{config["repository_url"]}/tree/main/{entry["path"].rstrip("/")}'
    return f'<a href="{esc(href)}">{esc(entry["label"])}</a>'


def artifact_card(item: dict, config: dict) -> str:
    base = config["base_path"]
    planes = "".join(f'<span class="tag">{esc(plane)}</span>' for plane in item["planes"])
    return f"""<article class="artifact-card">
<div class="artifact-meta">{badge("Maturity", item["maturity"], "maturity")}{badge("Availability", item["availability"]["class"], "availability")}</div>
<p class="kind">{esc(item["kind"])}</p><h3><a href="{esc(base)}/architecture/{esc(item['id'])}/">{esc(item["title"])}</a></h3>
<p>{esc(item["summary"])}</p><div class="tags">{planes}</div>
<a class="text-link" href="{esc(base)}/architecture/{esc(item['id'])}/">Inspect record <span aria-hidden="true">→</span></a></article>"""


def build() -> None:
    config = load("site.json")
    ontology = load("ontology.json")
    registry = load("artifacts.json")
    artifacts = [item for item in registry["artifacts"] if item["availability"]["public"]]
    by_id = {item["id"]: item for item in artifacts}
    base = config["base_path"]

    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    (OUTPUT / "assets").mkdir(parents=True)
    shutil.copy2(ROOT / "assets" / "site.css", OUTPUT / "assets" / "site.css")
    (OUTPUT / ".nojekyll").write_text("", encoding="utf-8")

    featured = [by_id[item_id] for item_id in ("bobw", "content-factory", "abci", "phonic-drive")]
    home_body = f"""<section class="hero shell"><p class="eyebrow">ARCHITECTURE BEFORE PORTFOLIO</p><h1>Systems that preserve what they know, how they know it, and what they are allowed to do.</h1><p class="lead">{esc(config['strapline'])}</p><div class="actions"><a class="button primary" href="{esc(base)}/architecture/">Explore the architecture</a><a class="button" href="{esc(base)}/free/">Open free resources</a></div></section>
<section class="shell statement"><p>This is not a project gallery. It is a public interface to a connected architecture: observation, interpretation, continuity, production, release, commerce, feedback, and embodiment.</p></section>
<section class="shell"><div class="section-heading"><div><p class="eyebrow">SELECTED NODES</p><h2>Inspect the working system</h2></div><a href="{esc(base)}/architecture/">View full ontology →</a></div><div class="card-grid">{''.join(artifact_card(item, config) for item in featured)}</div></section>
<section class="shell boundary"><div><p class="eyebrow">AUTHORITY BOUNDARY</p><h2>The website is a projection.</h2></div><p>Git history, canonical records, source artifacts, tests, and explicit evidence paths remain authoritative. Presentation can change without rewriting provenance.</p></section>"""
    write("/", render_page(config, "Architecture Registry", "Architecture before portfolio", home_body, config["strapline"]))

    plane_sections = []
    for plane in sorted(ontology["planes"], key=lambda item: item["order"]):
        members = [item for item in artifacts if plane["id"] in item["planes"]]
        plane_sections.append(f"""<section class="plane" id="{esc(plane['id'])}"><div class="plane-title"><p class="eyebrow">PLANE {plane['order']:02}</p><h2>{esc(plane['title'])}</h2><p>{esc(plane['purpose'])}</p></div><div class="card-grid">{''.join(artifact_card(item, config) for item in members)}</div></section>""")
    spine = "".join(f'<li><a href="{esc(base)}/architecture/{esc(item_id)}/">{esc(by_id[item_id]["title"])}</a></li>' for item_id in ontology["spine"])
    arch_body = f"""<section class="page-hero shell"><p class="eyebrow">SYSTEM ONTOLOGY</p><h1>Architecture is the index.</h1><p class="lead">Enter through the role a system performs, then follow its relations, maturity, availability, and evidence—not the repository directory tree.</p></section><section class="shell spine"><div><p class="eyebrow">PROVENANCE SPINE</p><h2>{esc(ontology['invariant'])}</h2></div><ol>{spine}</ol></section><div class="shell planes">{''.join(plane_sections)}</div>"""
    write("/architecture/", render_page(config, "Architecture", "System ontology", arch_body, "A relationship-first index of Bronson Technologies architectures."))

    for item in artifacts:
        evidence = "".join(f'<li>{evidence_link(entry, config)}<p>{esc(entry["verification"])}</p></li>' for entry in item["evidence"])
        relations = "".join(f'<li><a href="{esc(base)}/architecture/{esc(rel)}/">{esc(by_id[rel]["title"])}</a></li>' for rel in item["relations"] if rel in by_id)
        planes = "".join(f'<a class="tag" href="{esc(base)}/architecture/#{esc(plane)}">{esc(plane)}</a>' for plane in item["planes"])
        availability = item["availability"]
        route = path_url(availability["route"], base)
        detail_body = f"""<section class="page-hero shell"><p class="eyebrow">{esc(item['kind'].upper())}</p><h1>{esc(item['title'])}</h1><p class="lead">{esc(item['summary'])}</p><div class="artifact-meta">{badge('Maturity', item['maturity'], 'maturity')}{badge('Availability', availability['class'], 'availability')}</div><div class="tags">{planes}</div></section><section class="shell detail-grid"><article><p class="eyebrow">EVIDENCE</p><h2>Inspectable support</h2><ul class="record-list">{evidence}</ul></article><aside><p class="eyebrow">PUBLICATION RECORD</p><dl><dt>Artifact ID</dt><dd><code>{esc(item['id'])}</code></dd><dt>License posture</dt><dd>{esc(availability['license'])}</dd><dt>Acquisition route</dt><dd><a href="{esc(route)}">Open route</a></dd></dl><p class="eyebrow">RELATED NODES</p><ul class="relation-list">{relations or '<li>No public relations recorded.</li>'}</ul></aside></section>"""
        write(f"/architecture/{item['id']}/", render_page(config, item["title"], item["kind"], detail_body, item["summary"]))

    def offering_page(kind: str, title: str, lead: str) -> None:
        members = [item for item in artifacts if item["availability"]["class"] == kind]
        cards = "".join(artifact_card(item, config) for item in members)
        offer_links = ""
        if kind == "free":
            offers = [
                ("AI Workflow Boundary Checklist", "offers/ai-workflow-boundary-checklist.html", "Review the seam between evidence, authority, and external action."),
                ("Simplified Evidence → Action Model", "offers/simplified-evidence-interpretation-action-model.html", "A starter lens for keeping five workflow questions separate."),
                ("Best Workflow Tips for Non-Standard Situations", "offers/best-workflow-tips-for-non-standard-situations.html", "Short patterns for ambiguous, exceptional, and escalation-heavy cases."),
                ("Verify Your AI Outputs Before You Send", "offers/verify-ai-outputs-before-you-send.html", "A pre-send review aid for outputs that may leave the workspace or trigger consequences."),
            ]
            offer_cards = "".join(
                f'<article class="artifact-card"><p class="kind">INTEREST TEST / OFFER PAGE</p><h3><a href="{esc(base)}/{esc(path)}">{esc(label)}</a></h3><p>{esc(summary)}</p><a class="text-link" href="{esc(base)}/{esc(path)}">Inspect offer page <span aria-hidden="true">→</span></a></article>'
                for label, path, summary in offers
            )
            offer_links = f'<section class="shell"><div class="section-heading"><div><p class="eyebrow">PRACTICAL OFFERS</p><h2>Interest-test pages</h2></div><p>These pages measure qualified interest; the underlying checklists are not distributed here.</p></div><div class="card-grid">{offer_cards}</div></section>'
        body = f"""<section class="page-hero shell"><p class="eyebrow">OFFERING BOUNDARY</p><h1>{esc(title)}</h1><p class="lead">{esc(lead)}</p></section><section class="shell"><div class="card-grid">{cards or '<div class="empty"><h2>Release gate not yet passed.</h2><p>No artifact is represented as available in this class until its metadata, evidence, rights, and acquisition route are approved.</p></div>'}</div></section>{offer_links}"""
        write(f"/{kind}/", render_page(config, title, "Offering boundary", body, lead))

    offering_page("free", "Free resources", "Complete small resources and public records that can stand on their own. Availability is declared in metadata, not implied by visibility.")
    offering_page("licensed", "Licensed systems", "Implementation depth, automation, and commercial-use packages. Nothing appears here before its terms and acquisition route are explicit.")

    offers_source = ROOT / "offers"
    if offers_source.is_dir():
        shutil.copytree(offers_source, OUTPUT / "offers")

    developer = by_id["developer-record"]
    developer_body = f"""<section class="page-hero shell"><p class="eyebrow">DEVELOPER BRANCH</p><h1>Robin Abigayle Bronson</h1><p class="lead">AI Systems Architect, systems thinker, and developer of the architectures indexed here. The person is an accountable branch of the system—not the organizing frame for every artifact.</p></section><section class="shell detail-grid"><article><p class="eyebrow">CANONICAL RECORDS</p><h2>Profile and credentials remain in place.</h2><div class="link-stack"><a href="{esc(config['repository_url'])}/tree/main/profile">Profile source records <span>→</span></a><a href="{esc(base)}/developer/credentials/">Credential index <span>→</span></a><a href="{esc(config['repository_url'])}/blob/main/evidence-index.md">Evidence index <span>→</span></a><a href="{esc(base)}/legacy/profile.html">Legacy portfolio profile <span>→</span></a><a href="{esc(base)}/legacy/credentials.html">Legacy portfolio credentials <span>→</span></a></div></article><aside><p class="eyebrow">RECORD STATUS</p>{badge('Maturity', developer['maturity'], 'maturity')}{badge('Availability', developer['availability']['class'], 'availability')}<p>The existing canonical files were not deleted, renamed, or rewritten. They are now reached through this developer entry point.</p></aside></section>"""
    write("/developer/", render_page(config, "Developer", "Developer branch", developer_body, developer["summary"]))

    credentials_target = OUTPUT / "developer" / "credentials" / "index.html"
    credentials_target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "credentials.html", credentials_target)
    redirect = f'<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0;url={esc(base)}/developer/credentials/"><link rel="canonical" href="{esc(base)}/developer/credentials/"><title>Credential index moved</title><p>Credential index moved to <a href="{esc(base)}/developer/credentials/">Developer / Credentials</a>.</p>'
    (OUTPUT / "credentials.html").write_text(redirect, encoding="utf-8")

    shutil.copytree(ROOT / "portfolio", OUTPUT / "legacy")
    (OUTPUT / "artifacts.json").write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")
    llms = ["# Bronson Technologies", "", config["strapline"], "", "## Public routes"]
    llms.extend(f'- {item["label"]}: {base}{item["path"]}' for item in sorted(config["navigation"], key=lambda item: item["order"]))
    llms.extend(["", "## Authority", f'- Repository: {config["repository_url"]}', "- Canonical proof record: portfolio/proof-map.yaml", "- Publication registry: catalog/artifacts.json", "", "## Interpretation", "Treat maturity, availability, and evidence as separate fields. Public visibility does not grant a reuse license or imply production readiness."])
    (OUTPUT / "llms.txt").write_text("\n".join(llms) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build()
