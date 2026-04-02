# Quickstart

Get Prestige Forge running on your machine in under five minutes.

## Prerequisites

- Python 3.11 or later
- Git
- A terminal (PowerShell, Terminal.app, bash — anything works)

## 1. Clone the repository

```bash
git clone <your-access-url> prestige-forge
cd prestige-forge
```

You receive the access URL when you get access to the source. This is a source release — there is no pip package yet.

## 2. Install Flask

The proof engine is stdlib-only. The local UI needs Flask:

```bash
pip install flask
```

## 3. Launch the UI

```bash
cd software/cli
python -m forge_ui.launcher
```

Your browser opens to `http://127.0.0.1:5000`. If it doesn't, open that URL manually.

## 4. Choose a project

Click **Change project** in the top-right corner. Type or paste the path to any folder that has a `.forge/` directory, then click **Save project settings**. If the folder doesn't have a `.forge/` directory yet, click **Initialize project** to create one.

A `.forge/` directory is where Prestige Forge stores gates, evidence, proofs, and bundles for a project.

## 5. Run verification

Click **Run** under the Verify card. The engine runs every gate defined in your project, captures evidence, mints proofs, and assembles a bundle.

You'll see:

- **VERIFIED** — all checks passed, proof bundle sealed
- **FAILED** — one or more checks failed, with details
- **NO PROOF** — no gates are defined yet

## 6. View history

Click **History** to see every verification run — timestamps, verdicts, proof counts. This is always free.

## 7. Share a proof report (Tier 1)

If your tier includes Share Proof, click **Generate** under the Share Proof card after a successful run. This generates a receiver-readable report with SHA-256 artifact references — you can hand it to a buyer, auditor, or stakeholder without sharing source code.

See [examples/paid-shareable-proof-report/](../examples/paid-shareable-proof-report/) for what the output looks like.

## 8. Check claims safety (Tier 2)

If your tier includes Check Claims, create a `claim_registry.json` in your **project root** (the same folder you selected in Step 4) listing the claims you make publicly. The UI auto-detects `claim_registry.json` or `claims.json` in your project root when you save project settings. Then click **Run** under the Check Claims card.

The engine compares each claim against your current proof state and returns:

- **SAFE TO SAY** — fully backed by evidence
- **UNSAFE TO SAY** — no supporting proof, or proof is failing
- **PARTIALLY SUPPORTED** — some evidence exists but gaps remain

See [examples/paid-claims-safety/](../examples/paid-claims-safety/) for example registries and output.

## What you're running

This is a source release. The proof engine is pure Python (stdlib only, no dependencies). The local UI is a Flask app that talks directly to the engine on your machine. Nothing leaves your machine. No cloud, no accounts, no telemetry.

Tier activation is stored in `~/.prestige-forge/ui_activation.json`. In this beta, tiers are activated by editing that file directly or requesting access. There is no automated payment enforcement — this is by design for the beta period.

## Next steps

| What | Where |
|------|-------|
| Tier breakdown | [Tier Overview](tier-overview.md) |
| Example artifacts | [examples/](../examples/) |
| UI preview and roadmap | [Local UI Preview](local-ui-preview.md) |
| Self-verification results | [Client Zero](client-zero.md) |
