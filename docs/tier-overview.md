# Tier Overview

Prestige Forge has three tiers. The free tier covers proof visibility. The two paid tiers add trust transfer and claims safety.

---

## Free — Proof Visibility

What you get without paying anything.

| Capability | Description |
|------------|-------------|
| Proof bundle production | Every verification run produces per-check evidence, cryptographic proofs, and a run manifest bound to a git commit |
| Badge + proof summary | Instant pass/fail status with proof counts |
| Verification history | Ordered timeline of every check, verdict, and timestamp |
| Structural self-check | Pre-flight validation of vault integrity before runs |
| Vault audit | Independent integrity auditing of vault and run artifacts |
| Offline operation | Runs locally with stdlib-only Python 3.11+. No cloud, no accounts. The local UI requires Flask |

---

## Paid Tier 1 — Trust Transfer

Share proof without sharing code.

| Capability | Description |
|------------|-------------|
| Shareable proof report | Generate a complete verification record for external recipients from any sealed bundle |
| Artifact references | Report includes SHA-256 hashes and paths for every proof artifact |
| Workflow summary | Report shows the ordered sequence of checks and verdicts |
| Verification instructions | Report includes step-by-step instructions for the receiver to verify independently |
| Source-safe | No source code or internal paths appear in the report |

---

## Paid Tier 2 — Claims Safety

Know what you can safely say.

| Capability | Description |
|------------|-------------|
| Per-claim verdicts | Compare declared claims against current proof state — SAFE TO SAY, UNSAFE TO SAY, or PARTIALLY SUPPORTED |
| Fix First ranking | Prioritized list of which claims to fix first, scored by trust impact, audience breadth, and proof state |
| Temporal drift detection | Compare current proof state against a prior baseline to detect worsened, improved, or unchanged claims |
| Explicit claim registry | You declare exactly what you claim. The engine tells you what the proof actually supports |

---

## What Every Tier Has in Common

- Deterministic: same inputs produce the same outputs
- Offline: no cloud, no API calls, no accounts
- Read-only: the engine never mutates your source artifacts
- stdlib-only: proof engine has zero external Python dependencies (the local UI requires Flask)

---

## Comparison

| | Free | Paid Tier 1 | Paid Tier 2 |
|---|---|---|---|
| See proof state | Yes | Yes | Yes |
| Verification history | Yes | Yes | Yes |
| Share proof with others | — | Yes | Yes |
| Per-claim safety verdicts | — | — | Yes |
| Fix First ranking | — | — | Yes |
| Temporal drift detection | — | — | Yes |

---

## See It in Action

- [Client Zero](client-zero.md) — Prestige Forge's own self-verification run, 15/15 claims SAFE TO SAY
- [Free tier examples](../examples/free/) — badge, proof summary, verification history
- [Shareable proof report examples](../examples/paid-shareable-proof-report/) — what the receiver sees
- [Claims safety examples](../examples/paid-claims-safety/) — SAFE, UNSAFE, PARTIAL verdicts and Fix First ordering

---

[Back to README](../README.md) | [Client Zero](client-zero.md)
