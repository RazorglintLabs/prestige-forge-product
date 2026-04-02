# Free Tier Examples

## What this category covers

The free tier gives you proof visibility — the ability to see the current verification state of a project at a glance.

This folder contains real output from a Prestige Forge verification run:

- **`manifest.json`** — bundle manifest listing proof files, evidence files, commit hash, and run metadata
- **`evidence/`** — raw stdout captured from each check (lint, unit tests)
- **`proofs/`** — one proof file per check, containing the verdict, evidence hash, and claim linkage

These are the artifacts Prestige Forge produces on every run at no cost.

## What you should learn from these examples

- What a bundle manifest looks like and what metadata it carries
- How evidence is captured verbatim from your check commands
- How proof files tie a check verdict to its evidence via SHA-256 hashes
- What information is included in a proof bundle without any paid features enabled

## File listing

```
manifest.json                              — Bundle manifest
evidence/check__3a__lint.stdout.log        — Lint check stdout
evidence/check__3a__unit-tests.stdout.log  — Unit test stdout
proofs/check__3a__lint.proof               — Proof artifact for lint check
proofs/check__3a__unit-tests.proof         — Proof artifact for unit tests
```

## What is deliberately omitted

- **No source code.** These are output artifacts only. The engine that produces them is not included.
- **No internal file paths.** Paths in proof files are relative to the bundle, not your machine.
- **No implementation detail.** You will not find module names, class structures, or internal wiring here.
- **No private proof data.** These examples are drawn from Prestige Forge's own demo verification run. No customer data appears.
