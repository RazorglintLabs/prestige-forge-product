<div align="center">

# PRESTIGE FORGE
**Evidence-to-Claim Review | Original Razorglint Demonstration**

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-local%20UI-000000?style=for-the-badge&logo=flask&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-proof%20records-334155?style=for-the-badge&logo=json&logoColor=white)
![License](https://img.shields.io/badge/Source-Proprietary-5D406F?style=for-the-badge)

**Check the claim against its evidence before publishing it.**

</div>

Prestige Forge is Razorglint's earlier local claim-safety tool and demonstration surface. It evaluates **declared claims against supplied proof records**, reports unsupported or qualified language and produces review artifacts for human inspection.

> **Product distinction · 20 November 2026:** This repository documents **Prestige Forge**, not a completed release of its successor **Prestige-Reforged**. The successor is under separate private development and Windows acceptance gates. Historical test counts and screenshots from this repository do not qualify the successor.

## What the earlier implementation demonstrates

- Classifying supplied claims into supported, qualified, unsupported or prohibited language according to available proof and rules.
- Producing per-claim findings, suggested qualifiers and review artifacts.
- Providing a Python standard-library sample path; the optional browser-based local UI uses Flask.

**Run the bundled sample (Python 3.11+):**

```sh
cd examples/try-this-2-minutes
python run_sample.py
```

Inspect the source and output under [examples/try-this-2-minutes](examples/try-this-2-minutes). The [quickstart](docs/quickstart.md) describes the optional local interface and prerequisites.

## Evidence, with correct limits

The repository retains [internal use examples](assets/proof/PRESTIGE_FORGE_INTERNAL_USE_PROOF_MANIFEST.md), [self-review records](docs/client-zero.md), screenshots and earlier tier documentation. Those are **historical demonstrations**, not independent validation, current customer adoption or a fresh November 2026 full-suite qualification.

In particular, **a product marking its own claims SAFE is not independent assurance**. A positive verdict means the supplied claims met the tool's declared checks against the supplied artifacts; it does not prove authentic source data, legal compliance, unrestricted production safety or real-world performance.

The older README cited **798 passing tests**, but this refresh does not promote that historical count into a current exact-source CI claim. For current independently verifiable public testing, see [Compliance Drift Detector's dated release receipt](https://github.com/RazorglintLabs/ComplianceDriftDetector/blob/main/docs/RELEASE_STATUS.md).

## Related engineering cases

The broader Razorglint portfolio also includes [BRE's source-aware regression and candidate review](https://github.com/RazorglintLabs/damian-ketting-ai-systems-portfolio/blob/main/CASE_BRE_2026-11-20.md), [Elite Pantry's method and evidence qualification](https://github.com/RazorglintLabs/damian-ketting-ai-systems-portfolio/blob/main/CASE_ELITE_PANTRY_2026-11-20.md), and a [scope-limited Proton-related public-source research methodology](https://github.com/RazorglintLabs/damian-ketting-ai-systems-portfolio/blob/main/CASE_PROTON_RESEARCH_2026-11-20.md).

These are **independent workstreams**, not a unified shipped product, proof of a vendor vulnerability or a transfer of private source rights.

## Today’s Razorglint portfolio

For active work in evidence lineage, governed systems, customer/IR presentation and the separate Prestige-Reforged development track, see:

- [Razorglint Systems Architecture](https://github.com/RazorglintLabs/systems-architecture)
- [Damian G. L. Ketting | Engineering portfolio](https://github.com/RazorglintLabs/damian-ketting-ai-systems-portfolio)

**Licensing and technical enquiries:** [razorglint.ops@protonmail.com](mailto:razorglint.ops@protonmail.com)

*Proprietary · © 2026 TCOG Collective LLC / Razorglint Labs. Public visibility does not grant open-source, redistribution or commercial reuse rights; see [LICENSE](LICENSE).*
