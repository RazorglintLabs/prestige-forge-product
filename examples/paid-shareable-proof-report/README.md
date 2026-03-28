# Paid Tier 1 — Shareable Proof Report Examples

## What this category covers

The shareable proof report is the artifact that lets you prove your verification state to someone else — a buyer, an auditor, a stakeholder — without giving them your source code.

This folder will contain examples of what a recipient actually receives:

- **Proof state overview** — overall pass/fail, total proof count
- **Workflow summary** — ordered list of checks and their verdicts
- **Artifact references** — SHA-256 hashes for every proof file, so the receiver can verify integrity independently
- **Verification instructions** — step-by-step guidance for the receiver to check what they received

The report is generated from a sealed proof bundle. The receiver never needs access to your codebase.

## What you should learn from these examples

- What the receiver actually sees when you hand them a proof report
- How artifact integrity is referenced (hash-based, not path-based)
- How verification instructions are written so a non-technical stakeholder can follow them
- Whether this format meets the trust-transfer needs you have today

## What is deliberately omitted

- **No source code.** The report generation engine is not included. You see the output, not the tooling.
- **No internal paths or module names.** The report is designed to be clean of implementation detail by design — that property carries through to these examples.
- **No customer data.** When populated, examples will be drawn from Prestige Forge's own Client Zero self-verification run.
- **No report-generation configuration.** How the report is built internally is not shown. What matters here is what the receiver gets.
