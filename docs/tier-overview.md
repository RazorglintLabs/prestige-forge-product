# Tier Overview

## Why the ladder exists

Proof means different things at different stages of trust.

When you are building alone, you want to see whether your checks pass. When you hand work to someone else, you need proof they can read without your help. When you make public claims about your project, you need to know whether those claims are actually supported right now — not last month, not in theory.

Prestige Forge is structured around these three real needs, in order.

---

## Free — Proof Visibility

The free tier answers: **what is the current proof state of my project?**

You run checks. Prestige Forge captures evidence, mints cryptographic proofs, and assembles everything into a portable bundle tied to a specific git commit.

What you get:

- **Badge and proof summary** — instant pass/fail with proof counts
- **Verification history** — an ordered timeline showing every check, its verdict, and when it ran
- **Self-check** — structural pre-flight validation before any run
- **Vault audit** — independent integrity check of your proof artifacts after the fact

Everything runs offline. No cloud. No accounts. The proof engine is stdlib-only Python 3.11+. The local UI requires Flask.

This tier is genuinely useful on its own. You can see your proof state, track it over time, and know whether your project's verification is clean — without paying anything.

---

## Paid Tier 1 — Shareable Proof Report

The free tier proves things to you. Paid Tier 1 lets you prove things to someone else.

A shareable proof report is a structured document generated from a sealed proof bundle. It is designed to be handed to a buyer, auditor, stakeholder, or reviewer so they can inspect your proof state without needing your source code.

What the report includes:

- **Proof state overview** — overall pass/fail, proof counts
- **Workflow summary** — ordered list of checks and verdicts
- **Artifact references** — SHA-256 hashes for every proof file so the receiver can verify integrity
- **Verification instructions** — step-by-step guidance for the receiver to independently check what they received

No source code appears in the report. No internal paths. The receiver gets a clean, self-contained verification record.

**Why this is paid:** Producing proof for yourself is table stakes. Producing proof that someone else can trust without a walkthrough is the harder problem. The shareable proof report is the artifact that makes trust transfer possible.

---

## Paid Tier 2 (Beta) — Claims Safety

**Beta price: €89** — [Get Tier 2 Beta Access](STRIPE_TIER2_LINK_HERE)  
Planned post-beta price: €129–€149. All rights reserved.

Most teams can produce proof. Far fewer can answer the question: **are the things we say publicly actually backed by current proof?**

The claims safety engine compares a set of declared claims against the current proof state and returns a verdict for each one:

- **SAFE TO SAY** — every required proof exists and is current
- **UNSAFE TO SAY** — proof is missing, failing, or too stale to support the claim
- **PARTIALLY SUPPORTED** — some proof exists but gaps remain

On top of that:

- **Fix First** — a ranked list showing which claims to fix first, scored by how much trust damage they carry (trust impact, audience reach, proof gap severity)
- **Temporal drift** — comparison against a prior report to catch claims that were safe last month but are not safe now

You write a claim registry declaring exactly what you claim. The engine tells you what the proof actually supports. No guessing. No "it should be fine."

**Why this is paid:** This is the layer that changes behavior. It catches overstatement before a client, buyer, or auditor catches it for you. It turns "we think we can say this" into a concrete, evidence-checked answer.

---

## Comparison

| | Free | Paid Tier 1 | Paid Tier 2 (Beta) |
|---|---|---|---|
| See proof state | Yes | Yes | Yes |
| Verification history | Yes | Yes | Yes |
| Share proof with others | — | Yes | Yes |
| Per-claim safety verdicts | — | — | Yes |
| Fix First ranking | — | — | Yes |
| Temporal drift detection | — | — | Yes |

All tiers share the same properties: deterministic output, offline operation, read-only (never mutates your artifacts), and stdlib-only proof engine (the local UI requires Flask).

---

## See it in action

- [Client Zero](client-zero.md) — Prestige Forge's own self-verification run, 15/15 claims SAFE TO SAY
- [Free tier examples](../examples/free/) — badge, proof summary, verification history
- [Shareable proof report examples](../examples/paid-shareable-proof-report/) — what the receiver sees
- [Claims safety examples](../examples/paid-claims-safety/) — SAFE, UNSAFE, PARTIAL verdicts and Fix First ordering
