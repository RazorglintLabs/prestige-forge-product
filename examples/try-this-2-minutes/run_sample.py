#!/usr/bin/env python3
"""
Prestige Forge — Sample Claim-Safety Tester

Checks sample claims against sample evidence and produces a timestamped
mini truthpack with verdicts, qualifiers, safer rewrites, a manifest,
and SHA-256 checksums.

Python 3.11+ stdlib only. No external dependencies.

Usage:
    python run_sample.py
    python run_sample.py --claims sample_claims.json --evidence sample_evidence.json
"""

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

SAMPLE_VERSION = "0.1.0"
TOOL_NAME = "Prestige Forge Sample Tester"

# ---------------------------------------------------------------------------
# Forbidden / overclaim phrase tables
# ---------------------------------------------------------------------------

FORBIDDEN_PHRASES = [
    "legally compliant",
    "certified compliant",
    "tamper-proof",
    "impossible to bypass",
    "proven in the wild",
    "guarantees safety",
]

UNSAFE_PATTERNS = [
    ("proves real-world", "Extends simulation evidence to real-world deployment claim."),
    ("real-world fleet safety", "Converts simulation evidence into deployment safety claim."),
    ("all bypasses closed", "Overstates scope — should say 'tested bypass classes closed'."),
]

QUALIFIER_KEYWORDS = {
    "simulation-grade": "Simulation only — not a deployment or hardware claim.",
    "internally": "Internal use only — not customer deployment or third-party validation.",
    "proving ground": "Proving ground for testing — not a production deployment claim.",
    "public-facing claim language": "Internal claim-checking use — not customer deployment.",
}

# ---------------------------------------------------------------------------
# Safer rewrites for known unsafe claims
# ---------------------------------------------------------------------------

SAFER_REWRITES = {
    "production-ready": {
        "rewrite": None,  # filled per-project below
        "note": "'Production-ready' requires deployment evidence not present in sample.",
    },
    "proves real-world fleet safety": {
        "rewrite": "FleetSim is a simulation-grade proving ground for SAR governance testing.",
        "note": "Simulation evidence cannot support real-world safety claims.",
    },
    "makes projects legally compliant": {
        "rewrite": None,
        "note": "'Legally compliant' requires legal/compliance authority. Prestige Forge maps claims to evidence — it does not confer legal status.",
    },
    "tamper-proof": {
        "rewrite": "Tamper-evident (where supported by hash-chain evidence).",
        "note": "'Tamper-proof' is an absolute claim. 'Tamper-evident' is the defensible term.",
    },
}

PROJECT_PROD_REWRITES = {
    "Command Guardian": "Command Guardian is a hardened prototype with 131 passing tests. It is not production-ready.",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def load_json(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# Evidence matching
# ---------------------------------------------------------------------------

def find_evidence(claim_text: str, evidence_records: list, project: str) -> list:
    """Return evidence records whose keywords overlap with the claim text."""
    claim_lower = claim_text.lower()
    matches = []
    for ev in evidence_records:
        if ev["project"].lower() != project.lower():
            continue
        for kw in ev.get("supported_claim_keywords", []):
            if kw.lower() in claim_lower:
                matches.append(ev)
                break
    return matches


# ---------------------------------------------------------------------------
# Verdict engine
# ---------------------------------------------------------------------------

def evaluate_claim(claim: dict, evidence_records: list) -> dict:
    text = claim["text"]
    text_lower = text.lower()
    project = claim["project"]

    result = {
        "claim_id": claim["claim_id"],
        "original_claim": text,
        "project": project,
        "intended_context": claim.get("intended_context", ""),
        "verdict": None,
        "reason": None,
        "evidence_refs": [],
        "required_qualifier": None,
        "safer_rewrite": None,
        "limitation_notes": [],
    }

    # --- FORBIDDEN check ---
    for phrase in FORBIDDEN_PHRASES:
        if phrase in text_lower:
            result["verdict"] = "FORBIDDEN"
            result["reason"] = f"Contains forbidden phrase: '{phrase}'."
            rw = SAFER_REWRITES.get(phrase, {})
            result["safer_rewrite"] = rw.get("rewrite")
            result["limitation_notes"] = [rw.get("note", "No safe rewrite available.")]
            return result

    # "production-ready" — forbidden unless evidence explicitly says so (sample evidence does NOT)
    if "production-ready" in text_lower:
        result["verdict"] = "FORBIDDEN"
        result["reason"] = "'Production-ready' requires deployment evidence. Sample evidence explicitly states this is not available."
        result["safer_rewrite"] = PROJECT_PROD_REWRITES.get(project)
        result["limitation_notes"] = ["Production-ready requires deployment evidence not present in sample evidence."]
        return result

    # --- UNSAFE / OVERCLAIM check ---
    for pattern, reason in UNSAFE_PATTERNS:
        if pattern in text_lower:
            result["verdict"] = "UNSAFE_OVERCLAIM"
            result["reason"] = reason
            rw_key = next((k for k in SAFER_REWRITES if k in text_lower), None)
            if rw_key:
                result["safer_rewrite"] = SAFER_REWRITES[rw_key].get("rewrite")
                result["limitation_notes"] = [SAFER_REWRITES[rw_key].get("note", "")]
            return result

    # Check for "makes projects legally compliant" style
    if "legally compliant" in text_lower or "makes" in text_lower and "compliant" in text_lower:
        result["verdict"] = "FORBIDDEN"
        result["reason"] = "Claims legal compliance status, which requires legal/compliance authority."
        rw = SAFER_REWRITES.get("makes projects legally compliant", {})
        result["safer_rewrite"] = rw.get("rewrite")
        result["limitation_notes"] = [rw.get("note", "")]
        return result

    # --- Evidence lookup ---
    matched_evidence = find_evidence(text, evidence_records, project)
    if not matched_evidence:
        # Try cross-project evidence (e.g. governance rules)
        matched_evidence = find_evidence(text, evidence_records, "Razorglint Architecture")

    result["evidence_refs"] = [e["evidence_id"] for e in matched_evidence]

    # Collect limitations from matched evidence
    all_limitations = []
    for ev in matched_evidence:
        all_limitations.extend(ev.get("limitations", []))
    result["limitation_notes"] = sorted(set(all_limitations))

    if not matched_evidence:
        result["verdict"] = "NEEDS_MORE_EVIDENCE"
        result["reason"] = "No evidence record found supporting this claim for the stated project."
        return result

    # --- SAFE_WITH_QUALIFIER check ---
    for kw, qualifier in QUALIFIER_KEYWORDS.items():
        if kw in text_lower:
            result["verdict"] = "SAFE_WITH_QUALIFIER"
            result["reason"] = f"Claim is supported but requires scope qualifier: {qualifier}"
            result["required_qualifier"] = qualifier
            return result

    # --- SAFE_TO_SAY ---
    result["verdict"] = "SAFE_TO_SAY"
    result["reason"] = "Claim directly matches evidence and does not exceed stated limitations."
    return result


# ---------------------------------------------------------------------------
# Output generation
# ---------------------------------------------------------------------------

def generate_output_readme(run_id: str, timestamp: str, verdicts: list, verdict_counts: dict) -> str:
    safe = verdict_counts.get("SAFE_TO_SAY", 0)
    qual = verdict_counts.get("SAFE_WITH_QUALIFIER", 0)
    unsafe = verdict_counts.get("UNSAFE_OVERCLAIM", 0)
    forbidden = verdict_counts.get("FORBIDDEN", 0)
    needs = verdict_counts.get("NEEDS_MORE_EVIDENCE", 0)
    total = sum(verdict_counts.values())

    lines = [
        f"# Mini Truthpack — {run_id}",
        "",
        f"**Generated:** {timestamp}",
        f"**Tool:** {TOOL_NAME}",
        f"**Sample version:** {SAMPLE_VERSION}",
        "",
        "---",
        "",
        "## What was checked",
        "",
        f"{total} sample claims were evaluated against {len(set(v['evidence_refs'][0] for v in verdicts if v['evidence_refs']))} evidence records.",
        "",
        "## Verdict Summary",
        "",
        f"| Verdict | Count |",
        f"|---------|-------|",
        f"| SAFE_TO_SAY | {safe} |",
        f"| SAFE_WITH_QUALIFIER | {qual} |",
        f"| UNSAFE_OVERCLAIM | {unsafe} |",
        f"| FORBIDDEN | {forbidden} |",
        f"| NEEDS_MORE_EVIDENCE | {needs} |",
        f"| **Total** | **{total}** |",
        "",
        "## What this proves",
        "",
        "- Sample claims were checked against sample evidence using deterministic rules.",
        "- Unsafe and forbidden claims were blocked.",
        "- Safe claims were tied to specific evidence records.",
        "- Limitations remained visible in every verdict.",
        "- The output is timestamped and hashed for inspectability.",
        "",
        "## What this sample does NOT prove",
        "",
        "- It does not prove legal compliance.",
        "- It does not certify any system.",
        "- It does not prove production readiness.",
        "- It does not replace legal, audit, or regulatory review.",
        "- It does not create evidence that does not exist.",
        "- It only demonstrates a small local claim-safety workflow using sample inputs.",
        "",
        "## How to re-run",
        "",
        "```bash",
        "cd examples/try-this-2-minutes",
        "python run_sample.py",
        "```",
        "",
        "Each run produces a fresh timestamped output folder.",
        "",
        f"---",
        "",
        f"*Run ID: {run_id} — {timestamp}*",
        "",
    ]
    return "\n".join(lines)


def build_mini_truthpack(run_id, timestamp, claims, evidence, verdicts, verdict_counts,
                         input_hashes, report_files):
    return {
        "run_id": run_id,
        "generated_at_utc": timestamp,
        "tool_name": TOOL_NAME,
        "sample_version": SAMPLE_VERSION,
        "input_files": ["sample_claims.json", "sample_evidence.json"],
        "input_hashes": input_hashes,
        "verdict_counts": verdict_counts,
        "claims_checked": len(claims),
        "evidence_records_used": len(evidence),
        "verdicts": verdicts,
        "limitations": [
            "This is a sample tester with deterministic rules, not a production engine.",
            "Evidence records are sample summaries, not live proof artifacts.",
            "Verdicts are based on keyword matching, not semantic analysis.",
        ],
        "non_claims": [
            "This output does not prove legal compliance.",
            "This output does not certify any system.",
            "This output does not prove production readiness.",
            "This output does not replace legal, audit, or regulatory review.",
        ],
        "report_files": report_files,
    }


def build_manifest(run_id, timestamp, output_dir: Path, input_hashes: dict, engine_hash: str):
    file_hashes = {}
    for f in sorted(output_dir.iterdir()):
        if f.name == "checksums.sha256":
            continue
        if f.is_file():
            file_hashes[f.name] = sha256_file(f)

    return {
        "run_id": run_id,
        "generated_at_utc": timestamp,
        "sample_version": SAMPLE_VERSION,
        "files_written": sorted(file_hashes.keys()),
        "file_sha256": file_hashes,
        "input_claims_sha256": input_hashes.get("sample_claims.json", ""),
        "input_evidence_sha256": input_hashes.get("sample_evidence.json", ""),
        "engine_file_sha256": engine_hash,
    }


def write_checksums(output_dir: Path, engine_path: Path, claims_path: Path, evidence_path: Path):
    lines = []
    for f in sorted(output_dir.iterdir()):
        if f.name == "checksums.sha256":
            continue
        if f.is_file():
            lines.append(f"{sha256_file(f)}  {f.name}")
    # Include input and engine files
    lines.append(f"{sha256_file(engine_path)}  run_sample.py")
    lines.append(f"{sha256_file(claims_path)}  sample_claims.json")
    lines.append(f"{sha256_file(evidence_path)}  sample_evidence.json")
    checksum_path = output_dir / "checksums.sha256"
    checksum_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return checksum_path


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=TOOL_NAME)
    parser.add_argument("--claims", default="sample_claims.json", help="Path to claims JSON file")
    parser.add_argument("--evidence", default="sample_evidence.json", help="Path to evidence JSON file")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    claims_path = script_dir / args.claims
    evidence_path = script_dir / args.evidence
    engine_path = script_dir / "run_sample.py"

    if not claims_path.exists():
        print(f"ERROR: Claims file not found: {claims_path}", file=sys.stderr)
        sys.exit(1)
    if not evidence_path.exists():
        print(f"ERROR: Evidence file not found: {evidence_path}", file=sys.stderr)
        sys.exit(1)

    claims = load_json(claims_path)
    evidence = load_json(evidence_path)

    # Generate timestamp and run_id
    now = datetime.now(timezone.utc)
    timestamp = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    ts_slug = now.strftime("%Y%m%d-%H%M%S")
    short_hash = sha256_bytes(timestamp.encode())[:8]
    run_id = f"pf-sample-{ts_slug}-{short_hash}"

    print(f"Prestige Forge Sample Tester v{SAMPLE_VERSION}")
    print(f"Run ID:    {run_id}")
    print(f"Timestamp: {timestamp}")
    print(f"Claims:    {len(claims)}")
    print(f"Evidence:  {len(evidence)}")
    print()

    # Evaluate
    verdicts = []
    for claim in claims:
        v = evaluate_claim(claim, evidence)
        verdicts.append(v)

    # Verdict counts
    verdict_counts = {}
    for v in verdicts:
        vtype = v["verdict"]
        verdict_counts[vtype] = verdict_counts.get(vtype, 0) + 1

    # Print verdicts
    print("=" * 60)
    print("VERDICT REPORT")
    print("=" * 60)
    for v in verdicts:
        icon = {
            "SAFE_TO_SAY": "SAFE",
            "SAFE_WITH_QUALIFIER": "QUAL",
            "UNSAFE_OVERCLAIM": "UNSAFE",
            "FORBIDDEN": "FORBIDDEN",
            "NEEDS_MORE_EVIDENCE": "NEEDS_EV",
        }.get(v["verdict"], "???")
        print(f"  [{icon:>9}]  {v['claim_id']}: {v['original_claim']}")
        if v.get("required_qualifier"):
            print(f"             Qualifier: {v['required_qualifier']}")
        if v.get("safer_rewrite"):
            print(f"             Safer: {v['safer_rewrite']}")
    print()
    print("Verdict counts:")
    for vtype, count in sorted(verdict_counts.items()):
        print(f"  {vtype}: {count}")
    print()

    # Create output directory
    output_dir = script_dir / "output" / run_id
    output_dir.mkdir(parents=True, exist_ok=True)

    # Input hashes
    input_hashes = {
        "sample_claims.json": sha256_file(claims_path),
        "sample_evidence.json": sha256_file(evidence_path),
    }

    report_files = ["verdict_report.json", "mini_truthpack.json", "manifest.json", "checksums.sha256", "README.md"]

    # Write verdict_report.json
    verdict_report = {
        "run_id": run_id,
        "generated_at_utc": timestamp,
        "tool_name": TOOL_NAME,
        "sample_version": SAMPLE_VERSION,
        "verdict_counts": verdict_counts,
        "verdicts": verdicts,
    }
    vr_path = output_dir / "verdict_report.json"
    vr_path.write_text(json.dumps(verdict_report, indent=2) + "\n", encoding="utf-8")

    # Write mini_truthpack.json
    truthpack = build_mini_truthpack(run_id, timestamp, claims, evidence, verdicts,
                                     verdict_counts, input_hashes, report_files)
    tp_path = output_dir / "mini_truthpack.json"
    tp_path.write_text(json.dumps(truthpack, indent=2) + "\n", encoding="utf-8")

    # Write README.md
    readme_text = generate_output_readme(run_id, timestamp, verdicts, verdict_counts)
    readme_path = output_dir / "README.md"
    readme_path.write_text(readme_text, encoding="utf-8")

    # Write manifest.json (after other files exist)
    engine_hash = sha256_file(engine_path)
    manifest = build_manifest(run_id, timestamp, output_dir, input_hashes, engine_hash)
    manifest_path = output_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    # Write checksums.sha256 (last — after manifest is written)
    write_checksums(output_dir, engine_path, claims_path, evidence_path)

    print(f"Output written to: {output_dir.relative_to(script_dir)}")
    print()
    print("Files:")
    for f in sorted(output_dir.iterdir()):
        print(f"  {f.name}")
    print()
    print("Done. No proof, no claim.")


if __name__ == "__main__":
    main()
