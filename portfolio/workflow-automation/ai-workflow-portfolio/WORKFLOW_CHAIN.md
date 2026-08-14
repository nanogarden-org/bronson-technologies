# Workflow Chain Specification

## Purpose

Define the public portfolio process for demonstrating a complete AI-assisted workflow from evidence intake through finished output.

This specification intentionally keeps stages separate. The workflow must not collapse acquisition, reasoning, planning, production, review, and external action into a monolithic prompt.

---

## Stage 1 — PIRATE: Evidence Intake

### Job

Capture the source material and preserve enough provenance to reconstruct what entered the workflow.

### Inputs

- source files, URLs, notes, transcripts, images, or other bounded evidence
- source ownership / license / public-use status
- task context

### Outputs

- evidence manifest
- source inventory
- provenance notes
- exclusions / unresolved source questions

### Gate

Before continuing, confirm:

- source identity is clear enough for the demonstration
- source use is permitted
- private or sensitive material is excluded
- no unsupported interpretation has been introduced during capture

---

## Stage 2 — THREAD: Structured Reasoning

### Job

Convert captured evidence into an inspectable map of relationships, mechanisms, tensions, dependencies, or hypotheses.

### Inputs

- approved PIRATE evidence package

### Outputs

- reasoning map
- claims / observations separation
- unresolved questions
- assumptions
- candidate mechanisms or relationships

### Gate

Before continuing, confirm:

- observations are distinguishable from inference
- unsupported claims are marked
- important ambiguity is preserved
- the reasoning map can be challenged or revised

---

## Stage 3 — AI Workflow Plan

### Job

Turn the bounded job into an operating workflow.

### Required elements

- one concrete goal
- audience / user
- trigger
- inputs
- final output
- constraints and privacy boundaries
- four to six phases
- capability map
- review gate at every phase
- human-judgment boundaries
- responsible-use review
- bounded test
- improvement log

### Gate

Before continuing, confirm:

- the task is not several unrelated jobs disguised as one
- capabilities are used only where needed
- review occurs near the work
- external actions remain human-authorized
- failure recovery is defined

---

## Stage 4 — Book-Vault Skill: Persistent Project State

### Job

Instantiate a durable project container so the workflow can pause, resume, hand off, and preserve decisions.

### Minimum project state

- PROJECT_MANIFEST.md
- STATUS.md
- SOURCE_INTAKE.md
- DECISIONS.md
- WORK_LOG.md
- OUTPUTS/
- REVIEW/
- ARCHIVE/

### Gate

Before execution, confirm:

- current authoritative inputs are identified
- open decisions are explicit
- previous work is not silently overwritten
- the next executable step is visible
- the project can resume without relying on chat memory

---

## Stage 5 — Reusable / Automated Process

### Job

Execute the workflow and identify the parts stable enough to reuse or automate.

### Rules

- automate only an understood and repeatable step
- keep the written procedure as the specification
- preserve stage boundaries
- log failures and interventions
- make retries safe where practical
- do not hide human approvals inside automation

### Outputs

- reusable procedure
- scripts / templates / schemas where useful
- run log
- failure / retry record
- improvement notes

### Gate

Confirm:

- automation reproduced the intended procedure
- failures are visible rather than silently swallowed
- reruns do not corrupt project state
- human decisions remain attributable

---

## Stage 6 — Finished Output

### Job

Produce the bounded deliverable the workflow was designed to create.

### Examples

- research analysis
- technical report
- project specification
- publication package
- documented dataset
- structured knowledge artifact
- other reviewable deliverable

### Required release evidence

- final artifact
- output manifest
- provenance statement
- limitations
- review result
- run summary
- version / date

---

# Portfolio Demonstration Rule

The workflow is not demonstrated merely because the tools exist.

The portfolio proof is:

```text
INPUT
  ↓
CAPTURED EVIDENCE
  ↓
STRUCTURED REASONING
  ↓
OPERATING PLAN
  ↓
PERSISTENT PROJECT STATE
  ↓
EXECUTION / AUTOMATION
  ↓
REVIEW
  ↓
FINISHED OUTPUT
```

All major transitions must leave an inspectable artifact.

---

# Two-Run Requirement

## Run 001

A research or analytical workflow ending in a finished analysis.

## Run 002

A production workflow ending in a different class of finished artifact.

The same workflow grammar must be recognizable in both runs.

This is the main evidence that the project is a reusable workflow architecture rather than a one-off prompt sequence.

---

# Portfolio-Ready Definition of Done

The project is ready to present publicly when:

- [ ] the workflow chain is documented
- [ ] Run 001 is complete
- [ ] Run 002 is complete
- [ ] both runs contain public-safe inputs
- [ ] stage handoffs are inspectable
- [ ] review gates are visible
- [ ] human decisions are attributable
- [ ] failure / recovery behavior is documented
- [ ] at least one stable step is reusable or automated
- [ ] finished outputs are included
- [ ] limitations are explicit
- [ ] repository setup instructions are sufficient for an outsider to inspect or reproduce a bounded example
