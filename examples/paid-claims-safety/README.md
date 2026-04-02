# Paid Tier 2 (Beta) — Claims Safety Examples

## What this category covers

The claims safety engine checks whether the things you say publicly are actually backed by current proof. You declare your claims. The engine compares each one against your proof state and returns a verdict.

This folder contains a real claims safety report and example claim registries:

- **`claims_safety_report.txt`** — full claims safety analysis with per-claim verdicts
- **`example_claim_registry.json`** — a two-claim registry matching the report output
- **`example_claim_registry_minimal.json`** — the simplest possible one-claim registry

This example shows two claims, both fully backed by current proof (SAFE TO SAY). The report includes:

- **Verdict summary** — total claims and breakdown by safety category
- **Per-claim verdicts** — each claim with its reason, supporting artifacts, and temporal drift status
- **Fix First section** — a prioritized list of claims that need attention (empty when all claims are safe)
- **Temporal drift section** — comparison against historical baseline (when available)

## What you should learn from these examples

- What a per-claim verdict looks like in practice — not just the label, but the reasoning behind it
- How Fix First ordering works and why the ranking matters more than a flat list of failures
- What information you need to prepare (a claim registry) before the engine can run
- Whether this level of claims discipline is relevant to how you ship and communicate today

## What is deliberately omitted

- **No source code.** The claims safety engine is not included. You see its output, not its internals.
- **No internal scoring formulas.** Fix First ranking is shown as a result. The weighting logic is not exposed.
- **No customer data.** This example is drawn from Prestige Forge's own demo verification run.

## How to create your own claim registry

A claim registry is a JSON file with three top-level keys:

- **`schema_version`** — always `"1.0"`
- **`as_of_utc`** — UTC timestamp for freshness comparison (e.g. `"2026-04-01T00:00:00Z"`)
- **`claims`** — array of claim objects

Each claim needs:

| Field | Values | Purpose |
|-------|--------|---------|
| `claim_id` | Any unique string (e.g. `CLM-001`) | Identifies the claim |
| `claim_text` | Free text | The statement you want to verify |
| `required_proof_claims` | Array of strings | Must match the `claim` field in your gate check definitions exactly |
| `audience` | `client` or `internal` | Who sees this claim |
| `surface` | `public` or `private` | Where the claim appears |
| `breadth` | `broad` or `narrow` | How widely the claim is used |
| `trust_impact` | `high`, `medium`, or `low` | How much damage if the claim is wrong |
| `max_age_days` | Integer >= 1 | Proof older than this is treated as stale |

Save the file as `claim_registry.json` in your project root and it will be detected automatically.
