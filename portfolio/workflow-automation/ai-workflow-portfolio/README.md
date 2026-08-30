# AI Workflow Portfolio

A portfolio demonstration of a bounded, provenance-aware AI workflow chain that converts raw evidence into structured reasoning, an explicit workflow plan, persistent project state, a reusable process, and a finished deliverable.

## Current status

**Architecture bounded; demonstration runs not yet completed.**

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

The repository currently contains the workflow specification and run templates. It does not yet contain completed public-safe Run 001 or Run 002 outputs, so it should not be presented as a completed case study.

## Public demonstration boundary

Include only:

- public-safe workflow specifications;
- synthetic, licensed, public-domain, or user-owned demonstration inputs;
- selected public-safe skills and schemas;
- intermediate artifacts necessary to inspect the chain;
- finished outputs; and
- tests, run logs, and limitations.

Keep private source corpora, private conversation identifiers, credentials, unpublished commercial material, and unrelated internal tooling outside the public release.

## Success criteria

A technically literate reviewer should be able to determine what each stage contributes, what enters and leaves each stage, where human judgment occurs, how provenance is preserved, how the workflow resumes after interruption, what was automated, what was not automated, and what finished artifact was produced.

**Next gate:** complete Run 001 end-to-end with public-safe inputs and preserve every stage handoff.
