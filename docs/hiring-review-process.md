# Project documentation standard

## Purpose

Make a project understandable to a hiring reviewer within one minute, then provide an inspectable evidence path without flattening the underlying architecture.

## Execute for each project

1. Inventory the current README, code, tests, validation records, roadmap, attribution, and open reviews at a recorded commit. Separate implemented, historically tested, proposed, and externally validated claims.
2. Write the business problem in plain language: what fails, who handles the failure, and what decision or handoff is affected. Avoid unmeasured savings and unsupported deployment claims.
3. State the author's concrete contribution using attribution and repository evidence. Distinguish design from implemented code and external validation.
4. Add the README summary: business problem, contribution, working scope, direct evidence, limits, relevant assignments.
5. Add a short case study: problem, contribution, constraints, decision, working result, limits, business application. Include commands or direct verification links and label historical test results with their recorded version/date when available.
6. Add challenge instructions: version/SHA, invariant, synthetic reproduction, expected/observed result, related work, and issue link. Separate implementation failures from design challenges.
7. Update the portfolio's authoritative YAML, synchronized JSON, search index, HTML project cards, and capability map. Every implemented project needs a direct project URL and a verification path. Resolve links relative to the containing file.
8. Check syntax, YAML/JSON parity, link targets, maturity consistency, and documentation-only scope. Run the existing site checks where available. Do not report old tests as newly executed.
9. Update the documentation PR description with final scope and actual validation. Review and merge through the existing repository process.

## Reusable README packet

| Question | Required content |
| --- | --- |
| Business problem | Concrete operational failure and affected workflow |
| What I built | Specific design and implementation work |
| Working today | Version and implemented slice |
| Evidence | Demo, tests, commands, validation record |
| Limits | Unimplemented scope and unproven guarantees |
| Applications | Work this evidence equips the author to perform |

## Chronology and provenance

Git dates identify versions and recorded history. First public availability requires separate publication or archival evidence. Hashes prove integrity of the captured bytes within their verification scope, not source truth, authorship, or signer identity. Preserve known related work and describe the specific treatment being claimed.

## Completion criteria

A reviewer can explain the business problem and contribution without learning project-specific terminology; reach verification in one click from the summary; distinguish working code from plans; and submit a precise challenge. Portfolio records agree on project identity, links, maturity, and review date.


## Editorial standard

Describe the project, explain the engineering decisions, and link the evidence. Use plain project headings such as Overview, What I built, Verification, Limits, and Applications. Keep task logs, conversation history, and descriptions of the documentation exercise out of project pages. Record validation by version, date when available, environment, and result. Preserve uncertainty without repeating disclaimers. Write PR descriptions around the final change and actual checks.
