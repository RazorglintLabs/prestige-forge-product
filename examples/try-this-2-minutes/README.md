# Try Prestige Forge in 2 Minutes

This local sample checks a small set of public claims against a small evidence file and produces a timestamped mini truthpack.

It demonstrates the core Prestige Forge pattern:

**claim → evidence → verdict → qualifier/rewrite → mini truthpack**

No external dependencies. Python 3.11+ stdlib only. Runs offline.

---

## Run

```bash
cd examples/try-this-2-minutes
python run_sample.py
```

Or with explicit paths:

```bash
python run_sample.py --claims sample_claims.json --evidence sample_evidence.json
```

---

## What you get

A new folder under:

```
output/<run_id>/
```

Containing:

| File | Purpose |
|------|---------|
| `verdict_report.json` | Per-claim verdicts with reasons, qualifiers, and safer rewrites |
| `mini_truthpack.json` | Full run record — inputs, hashes, verdicts, limitations, non-claims |
| `manifest.json` | File inventory with SHA-256 hashes for every output and input file |
| `checksums.sha256` | Standalone checksum file for independent verification |
| `README.md` | Buyer-readable summary of the run |

Each run produces a fresh timestamped folder. Nothing is overwritten.

---

## What this demonstrates

- Unsupported claims are **blocked** (FORBIDDEN)
- Risky claims are **softened** with safer rewrites (UNSAFE_OVERCLAIM)
- Qualified claims get **explicit scope** (SAFE_WITH_QUALIFIER)
- Safe claims are **tied to evidence** (SAFE_TO_SAY)
- Limitations remain visible in every verdict
- Every run has a timestamp, run ID, and SHA-256 hashes

---

## Sample claims and expected verdicts

| Claim | Expected Verdict |
|-------|-----------------|
| Command Guardian has 131 passing tests after remediation. | SAFE_TO_SAY |
| FleetSim currently has 103 passing simulation governance tests. | SAFE_TO_SAY |
| FleetSim is a simulation-grade proving ground for SAR. | SAFE_WITH_QUALIFIER |
| Prestige Forge has been used internally to check public-facing claim language. | SAFE_WITH_QUALIFIER |
| Command Guardian is production-ready. | FORBIDDEN |
| FleetSim proves real-world fleet safety. | UNSAFE_OVERCLAIM |
| Prestige Forge makes projects legally compliant. | FORBIDDEN |
| The system is tamper-proof. | FORBIDDEN |

See `expected_output_report.json` for the full expected verdict set.

---

## What this does NOT demonstrate

- No legal compliance
- No certification
- No production readiness
- No customer deployment
- No third-party validation
- No replacement for counsel or auditors

This is a **sample tester** with deterministic keyword rules and sample evidence summaries. It is not the production Prestige Forge engine.

---

## Why this matters

Public claims can create risk when they outrun evidence. Prestige Forge helps slow the claim down until the evidence catches up.

**No proof, no claim.**

---

## Files in this folder

| File | Purpose |
|------|---------|
| `run_sample.py` | Sample tester script (stdlib-only Python) |
| `sample_claims.json` | 8 sample claims across 4 projects |
| `sample_evidence.json` | 4 sample evidence records |
| `expected_output_report.json` | Expected verdicts for validation |
| `expected_mini_truthpack_manifest.json` | Expected manifest shape (with placeholders) |
| `output/` | Generated output folders (one per run, gitignored) |
| `example_output_snapshot/` | One committed example output for reference |
