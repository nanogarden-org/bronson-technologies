# Public Provenance and Challenge Protocol

## Purpose

Bronson Technologies publishes some architecture work before it is polished because early public inspection is part of the engineering method.

The goal is not to declare a finished standard. The goal is to leave a dated, inspectable record of a formulation; provide enough implementation or structure for another person to test it; and make corrections visible rather than rewriting history after the fact.

## Minimum publication packet

For architecture claims that matter, prefer to publish as many of these as the maturity level supports:

1. **Problem statement** — what seam, failure mode, or unresolved system behavior is being addressed.
2. **Invariant set** — what must remain true if the architecture is working as intended.
3. **Reference artifact** — schema, code, fixture, diagram, or runnable toy model that makes the claim inspectable.
4. **Verification path** — tests, commands, fixtures, expected outputs, or review steps.
5. **Maturity label** — concept, prototype, implemented toolkit, tested demo, deployed pilot, or production system.
6. **Known limits** — what is intentionally absent or unproven.
7. **Related work** — established terminology, standards, projects, or prior approaches known at the time.
8. **Delta statement** — what is specifically different about this treatment without claiming ownership of the whole problem space.
9. **Chronology anchor** — version SHA plus a separately recorded publication or archival anchor for any public-availability claim.
10. **Challenge invitation** — how another person can report a broken invariant, counterexample, missing edge case, or better mapping.

## Challenge rule

A useful public architecture should be possible to disagree with.

Open an issue or provide a counterexample when:

- an invariant does not hold;
- a boundary is missing or incorrectly drawn;
- the terminology conflicts with established practice;
- a simpler architecture produces the same guarantees;
- a claimed distinction collapses under a real edge case;
- the reference implementation and written contract disagree; or
- related work materially predates or supersedes the framing.

Corrections should be additive and traceable where practical. Do not silently rewrite the origin story to make earlier versions appear more complete than they were.

## Chronology is evidence, not exclusivity

Git history identifies artifact versions and recorded dates. Commit dates and retained snapshots alone do not establish when an artifact became publicly accessible. Public-availability claims require a separately recorded publication or archival anchor. This packet does not establish a verified first-publication date. Neither repository chronology nor publication evidence establishes universal novelty, exclusive ownership of abstract ideas, or derivation by later work.

They do not, by themselves, prove:

- that no earlier related work existed;
- that an abstract idea is exclusively owned;
- patentability or patent priority in every jurisdiction;
- that another party later encountered or copied the work; or
- that a prototype was production-ready.

When those distinctions matter, say exactly what the evidence supports: **this version is identified by this commit; public availability is supported only by the separately linked publication record**.

## Provenance rule

Preserve the path:

```text
source / observation
  -> interpretation
  -> architecture claim
  -> reference implementation
  -> verification
  -> external challenge
  -> correction / next version
```

Do not collapse those stages into one retrospective story.

## Why publish early?

The work is intended to be useful, testable, and transferable. Early publication creates a surface where other engineers, researchers, users, and institutions can break the model before it hardens into an assumption.

The desired reaction is not only “interesting project.”

It is:

> What happens if this assumption is false?
>
> What edge case did this miss?
>
> Can this invariant survive another implementation?
>
> What else can this architecture be used to solve?

## Challenge submission packet

Include repository/version or commit SHA, invariant challenged, minimal synthetic input, commands or reasoning steps, expected versus observed behavior, and a related-work link where applicable. Identify implemented behavior versus proposed architecture. Open an issue in the affected repository and exclude private or unlicensed source material.
