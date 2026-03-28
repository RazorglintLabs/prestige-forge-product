# Paid Tier 2 — Claims Safety Examples

## What this category covers

The claims safety engine checks whether the things you say publicly are actually backed by current proof. You declare your claims. The engine compares each one against your proof state and returns a verdict.

This example category is meant to show:

- **One SAFE claim** — fully backed by current proof, safe to publish
- **One PARTIAL claim** — some proof exists but gaps remain, needs attention before publishing
- **One UNSAFE claim** — proof is missing or failing, should not be published in its current form
- **A Fix First ordering view** — a ranked list showing which claims to fix first, scored by trust impact, audience reach, and proof gap severity

These four cases cover the full range of what the claims safety engine can return. Together they show what it looks like when claims are supported, when they are not, and how the engine helps you prioritize repairs.

## What you should learn from these examples

- What a per-claim verdict looks like in practice — not just the label, but the reasoning behind it
- How Fix First ordering works and why the ranking matters more than a flat list of failures
- What information you need to prepare (a claim registry) before the engine can run
- Whether this level of claims discipline is relevant to how you ship and communicate today

## What is deliberately omitted

- **No source code.** The claims safety engine is not included. You see its output, not its internals.
- **No internal scoring formulas.** Fix First ranking is shown as a result. The weighting logic is not exposed.
- **No customer data.** When populated, examples will be drawn from Prestige Forge's own Client Zero run — 15 claims, all evaluated against a real proof bundle.
- **No claim registry templates.** These examples show output, not input configuration.
