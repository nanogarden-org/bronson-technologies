# AI Workflow Portfolio

A portfolio demonstration of a bounded, provenance-aware AI workflow chain that converts raw evidence into structured reasoning, an explicit workflow plan, persistent project state, a reusable process, and a finished deliverable.

## Portfolio Claim

This project demonstrates the ability to design and operate an AI-assisted workflow as a system rather than as a single prompt.

The public demonstration chain is:

```text
PIRATE
  ↓
THREAD
  ↓
AI Workflow Plan
  ↓
Book-Vault Skill
  ↓
Reusable / Automated Process
  ↓
Finished Output
```

Each stage has a distinct responsibility and produces an inspectable handoff artifact.

## What This Demonstrates

- evidence capture and provenance
- structured reasoning and mechanism mapping
- workflow decomposition
- deliberate capability selection
- review gates and human-judgment boundaries
- persistent project state
- resumability and handoffs
- reusable process extraction
- bounded automation
- finished, reviewable outputs

## Public Demonstration Strategy

The project uses one workflow grammar with two demonstration runs.

### Run 001 — Research / Analysis

```text
source material
→ PIRATE evidence capture
→ THREAD reasoning map
→ AI workflow plan
→ project vault
→ execution + review
→ finished analysis
```

### Run 002 — Production / Delivery

```text
brief + source material
→ PIRATE evidence capture
→ THREAD reasoning map
→ AI workflow plan
→ project vault
→ execution + review
→ finished production artifact
```

The two runs should differ in domain and output while preserving the same process grammar.

## Repository Boundary

This repository is a public demonstration layer.

It should include only:

- public-safe workflow specifications
- synthetic, licensed, public-domain, or user-owned demonstration inputs
- selected public-safe skills and schemas
- intermediate artifacts necessary to inspect the chain
- finished outputs
- tests, run logs, and limitations

Private source corpora, private conversation identifiers, credentials, unpublished commercial material, and unrelated internal tooling remain outside the public repository.

## Success Criteria

A technically literate reviewer should be able to answer:

1. What problem does the workflow solve?
2. What does each stage contribute?
3. What enters and leaves each stage?
4. Where does human judgment occur?
5. How is provenance preserved?
6. How does the workflow recover or resume after interruption?
7. What was automated and what was deliberately not automated?
8. What finished artifact did the workflow produce?
9. Can the same workflow grammar operate in a second domain?
10. What limitations remain?

If those questions can be answered from the repository without reconstructing private context, the demonstration is portfolio-ready.

## Status

**Current state:** architecture bounded; demonstration runs not yet completed.

**Next gate:** complete Run 001 end-to-end with public-safe inputs and preserve every stage handoff.
