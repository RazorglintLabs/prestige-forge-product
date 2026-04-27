"""
Prestige Forge — Internal Use Proof Images (UI Report Style)

Generates 7 JPG proof images styled as Prestige Forge product reports.
Clean dashboard aesthetic, large readable fonts, timestamped, card-based layout.

All data sourced from real artifacts. No invented claims.
Output: assets/proof/*.jpg
"""

import datetime
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# ─── Config ──────────────────────────────────────────────────────────────────

OUT_DIR = Path(r"c:\prestige-forge-product\assets\proof")
OUT_DIR.mkdir(parents=True, exist_ok=True)

NOW_UTC = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
NOW_FULL = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

W = 1400
MARGIN = 48
INNER = MARGIN + 16
TEXT_W = W - 2 * MARGIN

# ─── Fonts ───────────────────────────────────────────────────────────────────

FD = "C:/Windows/Fonts"

def f_light(sz):    return ImageFont.truetype(f"{FD}/segoeuil.ttf", sz)
def f_reg(sz):      return ImageFont.truetype(f"{FD}/segoeui.ttf", sz)
def f_semi(sz):     return ImageFont.truetype(f"{FD}/seguisb.ttf", sz)
def f_bold(sz):     return ImageFont.truetype(f"{FD}/segoeuib.ttf", sz)
def f_mono(sz):     return ImageFont.truetype(f"{FD}/consola.ttf", sz)
def f_monobold(sz): return ImageFont.truetype(f"{FD}/consolab.ttf", sz)

# ─── Color System ────────────────────────────────────────────────────────────

BG_PAGE    = "#f8f9fa"
BG_HEADER  = "#1a1f36"
BG_CARD    = "#ffffff"
BG_SUBTLE  = "#f0f2f5"

PF_BLUE    = "#2563eb"
PF_NAVY    = "#1e293b"

GREEN_BG   = "#dcfce7"
GREEN_TX   = "#166534"
GREEN_BD   = "#86efac"

AMBER_BG   = "#fef3c7"
AMBER_TX   = "#92400e"
AMBER_BD   = "#fcd34d"

RED_BG     = "#fee2e2"
RED_TX     = "#991b1b"
RED_BD     = "#fca5a5"

BLUE_BG    = "#dbeafe"
BLUE_TX    = "#1e40af"

TX_PRIMARY   = "#1e293b"
TX_SECONDARY = "#64748b"
TX_MUTED     = "#94a3b8"
TX_WHITE     = "#ffffff"

BD_LIGHT   = "#e2e8f0"

# ─── Drawing Helpers ─────────────────────────────────────────────────────────

def new_image(height):
    img = Image.new("RGB", (W, height), BG_PAGE)
    draw = ImageDraw.Draw(img)
    return img, draw


def draw_header_bar(draw, project_label=None):
    bar_h = 64
    draw.rectangle([0, 0, W, bar_h], fill=BG_HEADER)
    draw.text((MARGIN, 14), "Prestige Forge", font=f_bold(24), fill=TX_WHITE)
    draw.rectangle([MARGIN, 48, MARGIN + 170, 50], fill=PF_BLUE)
    if project_label:
        draw.text((W - MARGIN - 10, 22), project_label,
                  font=f_reg(14), fill=TX_MUTED, anchor="ra")
    return bar_h + 20


def draw_report_title(draw, y, title, subtitle=None, timestamp=True):
    draw.text((MARGIN, y), title, font=f_bold(28), fill=TX_PRIMARY)
    y += 40
    if subtitle:
        draw.text((MARGIN, y), subtitle, font=f_reg(15), fill=TX_SECONDARY)
        y += 26
    if timestamp:
        draw.text((MARGIN, y), f"Report rendered: {NOW_UTC}", font=f_mono(12), fill=TX_MUTED)
        y += 22
    y += 6
    draw.line([(MARGIN, y), (W - MARGIN, y)], fill=BD_LIGHT, width=2)
    y += 18
    return y


def draw_card(draw, x, y, w, h, fill=BG_CARD, border=BD_LIGHT):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=8, fill=fill, outline=border, width=1)


def draw_badge(draw, x, y, label, bg, tx, border=None):
    fnt = f_semi(13)
    bbox = fnt.getbbox(label)
    tw = bbox[2] - bbox[0]
    pw = tw + 20
    ph = 28
    outline = border if border else bg
    draw.rounded_rectangle([x, y, x + pw, y + ph], radius=14, fill=bg, outline=outline, width=1)
    draw.text((x + 10, y + 5), label, font=fnt, fill=tx)
    return x + pw + 10


def draw_section_title(draw, y, title):
    draw.text((MARGIN, y), title, font=f_semi(16), fill=TX_PRIMARY)
    return y + 28


def draw_footer(draw, img_h, text):
    foot_h = 40
    foot_y = img_h - foot_h - 8
    draw.rounded_rectangle([MARGIN, foot_y, W - MARGIN, foot_y + foot_h],
                           radius=6, fill=AMBER_BG, outline=AMBER_BD, width=1)
    draw.text((MARGIN + 14, foot_y + 10), text, font=f_reg(13), fill=AMBER_TX)


def draw_source_footer(draw, y, source):
    draw.text((MARGIN, y), f"Source: {source}", font=f_mono(11), fill=TX_MUTED)
    return y + 18


def save_jpg(img, filename):
    path = OUT_DIR / filename
    img.save(path, "JPEG", quality=95)
    size_kb = path.stat().st_size / 1024
    print(f"  {filename}: {img.width}x{img.height}px, {size_kb:.1f}KB")
    return path


# ═════════════════════════════════════════════════════════════════════════════
# IMAGE 1 — Client Zero Self-Verification
# ═════════════════════════════════════════════════════════════════════════════

def img1_client_zero():
    H = 700
    img, draw = new_image(H)

    y = draw_header_bar(draw, "Self-Verification Report")
    y = draw_report_title(draw, y, "Client Zero — Self-Verification",
                          "Prestige Forge verified its own claims using its own engine",
                          timestamp=False)
    draw.text((MARGIN, y), "Self-verification run: 2026-03-27", font=f_mono(12), fill=TX_MUTED)
    draw.text((MARGIN + 280, y), f"Report rendered: {NOW_UTC}", font=f_mono(12), fill=TX_MUTED)
    y += 28

    # Big result card
    card_h = 100
    draw_card(draw, MARGIN, y, TEXT_W, card_h, fill="#f0fdf4", border=GREEN_BD)
    draw_badge(draw, INNER, y + 12, "ALL CHECKS PASSED", GREEN_BG, GREEN_TX, GREEN_BD)
    draw_badge(draw, INNER + 220, y + 12, "ALL CLAIMS SAFE", GREEN_BG, GREEN_TX, GREEN_BD)
    draw.text((INNER, y + 54), "25/25", font=f_bold(30), fill=GREEN_TX)
    draw.text((INNER + 130, y + 62), "proof checks passed", font=f_reg(16), fill=TX_SECONDARY)
    draw.text((INNER + 440, y + 54), "15/15", font=f_bold(30), fill=GREEN_TX)
    draw.text((INNER + 570, y + 62), "SAFE TO SAY", font=f_reg(16), fill=TX_SECONDARY)
    y += card_h + 24

    # Stats grid
    y = draw_section_title(draw, y, "Verification Details")
    stats = [
        ("Proof checks executed", "25", GREEN_TX),
        ("Checks passed", "25", GREEN_TX),
        ("Checks failed", "0", GREEN_TX),
        ("Claims evaluated", "15", TX_PRIMARY),
        ("SAFE TO SAY", "15", GREEN_TX),
        ("UNSAFE TO SAY", "0", GREEN_TX),
        ("PARTIALLY SUPPORTED", "0", TX_SECONDARY),
        ("Fix First items", "0", GREEN_TX),
        ("Temporal drift", "NO BASELINE", TX_SECONDARY),
    ]
    draw_card(draw, MARGIN, y, TEXT_W, len(stats) * 30 + 16)
    row_y = y + 12
    for label, value, color in stats:
        draw.text((INNER + 8, row_y), label, font=f_reg(14), fill=TX_SECONDARY)
        draw.text((INNER + 380, row_y), value, font=f_semi(14), fill=color)
        row_y += 30
    y = row_y + 16

    y = draw_source_footer(draw, y, "docs/client-zero.md  ·  Self-verification run  ·  2026-03-27")
    draw_footer(draw, H, "Self-verification run — not third-party validation")
    save_jpg(img, "prestige_forge_client_zero_15_safe.jpg")


# ═════════════════════════════════════════════════════════════════════════════
# IMAGE 2 — Systems Architecture Claim Safety Pack
# ═════════════════════════════════════════════════════════════════════════════

def img2_systems_architecture():
    H = 760
    img, draw = new_image(H)

    y = draw_header_bar(draw, "Claim Safety Report")
    y = draw_report_title(draw, y, "Systems Architecture — Claim Safety Pack",
                          "Public-language claim audit across the Razorglint portfolio")

    # Total card
    card_h = 70
    draw_card(draw, MARGIN, y, TEXT_W, card_h, fill=BLUE_BG, border="#93c5fd")
    draw.text((INNER, y + 10), "78", font=f_bold(36), fill=BLUE_TX)
    draw.text((INNER + 70, y + 22), "claims reviewed", font=f_semi(18), fill=BLUE_TX)
    y += card_h + 20

    # Verdict breakdown
    y = draw_section_title(draw, y, "Verdict Breakdown")
    verdicts = [
        ("SAFE_TO_SAY",          28, GREEN_BG, GREEN_TX, GREEN_BD, 0.36),
        ("SAFE_WITH_QUALIFIER",  18, AMBER_BG, AMBER_TX, AMBER_BD, 0.23),
        ("UNSAFE_OVERCLAIM",     14, RED_BG,   RED_TX,   RED_BD,   0.18),
        ("FORBIDDEN",            12, RED_BG,   RED_TX,   RED_BD,   0.15),
        ("NEEDS_MORE_EVIDENCE",   6, AMBER_BG, AMBER_TX, AMBER_BD, 0.08),
    ]
    card_h = len(verdicts) * 50 + 20
    draw_card(draw, MARGIN, y, TEXT_W, card_h)
    vy = y + 14
    bar_max = 500
    for label, count, bg, tx, bd, pct in verdicts:
        draw_badge(draw, INNER + 4, vy, label, bg, tx, bd)
        draw.text((INNER + 310, vy + 3), str(count), font=f_bold(18), fill=tx)
        bar_x = INNER + 360
        bar_w = int(pct * bar_max)
        draw.rounded_rectangle([bar_x, vy + 4, bar_x + bar_w, vy + 22],
                               radius=4, fill=bg, outline=bd)
        draw.text((bar_x + bar_w + 10, vy + 4), f"{pct:.0%}",
                  font=f_reg(13), fill=TX_MUTED)
        vy += 50
    y = vy + 18

    # Audit inputs
    y = draw_section_title(draw, y, "Audit Inputs")
    inputs = [
        "systems-architecture/README.md",
        "PROOF_AUDIT_2026-04-26.md",
        "Command Guardian ENTERPRISE_AUDIT_REPORT.md",
        "audit_pass2/PROOF_MANIFEST.md",
    ]
    draw_card(draw, MARGIN, y, TEXT_W, len(inputs) * 26 + 16)
    iy = y + 10
    for inp in inputs:
        draw.text((INNER + 8, iy), f"·  {inp}", font=f_mono(12), fill=TX_SECONDARY)
        iy += 26
    y = iy + 20

    y = draw_source_footer(draw, y, "systems-architecture/PUBLIC_CLAIMS_SAFETY_PACK.md")
    draw_footer(draw, H, "Internal Razorglint public-language audit — not external certification")
    save_jpg(img, "prestige_forge_systems_architecture_claim_pack.jpg")


# ═════════════════════════════════════════════════════════════════════════════
# IMAGE 3 — Unsafe Claim Firewall
# ═════════════════════════════════════════════════════════════════════════════

def img3_forbidden_claims():
    H = 820
    img, draw = new_image(H)

    y = draw_header_bar(draw, "Claims Safety Engine")
    y = draw_report_title(draw, y, "Unsafe Claim Firewall",
                          "Language blocked or rewritten before public use")

    blocked = [
        ('"production-ready"',              '"hardened prototype"'),
        ('"certified compliant"',           '"evidence-mapped"'),
        ('"tamper-proof"',                  '"tamper-evident"'),
        ('"impossible to bypass"',          '"tested bypass classes closed"'),
        ('"all bypasses closed"',           '"critical bypass classes closed in tested set"'),
        ('"CG is SAR-integrated"',          '"SAR integration deferred"'),
        ('"unhackable"',                    '"deny-by-default enforcement"'),
        ('"military-grade security"',       '"hash-chained, Ed25519 where implemented"'),
    ]

    card_h = len(blocked) * 48 + 60
    draw_card(draw, MARGIN, y, TEXT_W, card_h)
    hy = y + 14
    draw.rectangle([MARGIN + 1, hy, W - MARGIN - 1, hy + 32], fill=BG_SUBTLE)
    draw.text((INNER + 8, hy + 6), "BLOCKED PHRASE", font=f_semi(13), fill=RED_TX)
    draw.text((INNER + 520, hy + 6), "SAFER REPLACEMENT", font=f_semi(13), fill=GREEN_TX)
    hy += 42
    for unsafe, safer in blocked:
        draw_badge(draw, INNER, hy, "BLOCKED", RED_BG, RED_TX, RED_BD)
        draw.text((INNER + 110, hy + 4), unsafe, font=f_reg(14), fill=RED_TX)
        draw.text((INNER + 490, hy + 4), "\u2192", font=f_bold(16), fill=TX_MUTED)
        draw.text((INNER + 520, hy + 4), safer, font=f_reg(14), fill=GREEN_TX)
        hy += 48
    y = hy + 24

    draw_card(draw, MARGIN, y, TEXT_W, 44, fill=BG_SUBTLE)
    draw.text((INNER + 8, y + 12),
              "12 absolute prohibitions  \u00b7  14 unsafe overclaims rewritten",
              font=f_semi(14), fill=TX_SECONDARY)
    y += 60

    y = draw_source_footer(draw, y, "systems-architecture/FORBIDDEN_PUBLIC_CLAIMS.md")
    draw_footer(draw, H, "Claim safety prevents overstatement before publication")
    save_jpg(img, "prestige_forge_forbidden_claims_blocked.jpg")


# ═════════════════════════════════════════════════════════════════════════════
# IMAGE 4 — Command Guardian Claim Safety
# ═════════════════════════════════════════════════════════════════════════════

def img4_command_guardian():
    H = 820
    img, draw = new_image(H)

    y = draw_header_bar(draw, "Claim Safety Report")
    y = draw_report_title(draw, y, "Command Guardian — Claim Safety",
                          "Post-remediation language checked before public release")

    safe_claims = [
        "131/131 tests passing after emergency security remediation",
        "Critical bypass classes closed in tested set",
        "DENY receipts store command hashes, not raw strings",
        "Token issuance is now audit-receipted",
        "Version corrected to 0.2.0; status hardened prototype",
        "Earlier v1.0.0 release marked superseded",
    ]

    y = draw_section_title(draw, y, "Safe Claims \u2014 Backed by Evidence")
    card_h = len(safe_claims) * 40 + 16
    draw_card(draw, MARGIN, y, TEXT_W, card_h, fill="#f0fdf4", border=GREEN_BD)
    sy = y + 12
    for claim in safe_claims:
        draw_badge(draw, INNER, sy, "SAFE", GREEN_BG, GREEN_TX, GREEN_BD)
        draw.text((INNER + 76, sy + 4), claim, font=f_reg(14), fill=TX_PRIMARY)
        sy += 40
    y = sy + 20

    limits = [
        "Not production-ready",
        "Not certified",
        "Not SAR-integrated \u2014 integration deferred",
        "Receipt signing deferred \u2014 hash-chained only",
        "Token storage and revocation architecture open",
        "AV retest log confirmation not available",
    ]

    y = draw_section_title(draw, y, "Required Limitations \u2014 Must Accompany Any Public Claim")
    card_h = len(limits) * 40 + 16
    draw_card(draw, MARGIN, y, TEXT_W, card_h, fill="#fffbeb", border=AMBER_BD)
    ly = y + 12
    for lim in limits:
        draw_badge(draw, INNER, ly, "LIMIT", AMBER_BG, AMBER_TX, AMBER_BD)
        draw.text((INNER + 86, ly + 4), lim, font=f_reg(14), fill=TX_PRIMARY)
        ly += 40
    y = ly + 20

    y = draw_source_footer(draw, y, "Command Guardian/ENTERPRISE_AUDIT_REPORT.md  \u00b7  audit_pass2/PROOF_MANIFEST.md")
    draw_footer(draw, H, "Proof-backed remediation language \u2014 limitations preserved")
    save_jpg(img, "prestige_forge_command_guardian_claim_safety.jpg")


# ═════════════════════════════════════════════════════════════════════════════
# IMAGE 5 — FleetSim Claim Safety
# ═════════════════════════════════════════════════════════════════════════════

def img5_fleetsim():
    H = 880
    img, draw = new_image(H)

    y = draw_header_bar(draw, "Claim Safety Report")
    y = draw_report_title(draw, y, "FleetSim \u2014 Claim Safety",
                          "Claims scoped before public posting and LinkedIn evidence PDF")

    safe_claims = [
        "103 tests passing \u2014 full suite, no skips, no xfails",
        "Simulation-grade trust-plane proving ground for SAR",
        "SHA-256-hashed transition receipts on every state change",
        "5-tier severity ladder enforced (GREEN through BLACK)",
        "7-state identity lifecycle enforced",
        "Token rotation under partition tested",
        "Illegal identity \u00d7 severity transitions rejected",
        "S1\u2013S4 scenario families exercised in simulation",
    ]

    y = draw_section_title(draw, y, "Safe Claims \u2014 Backed by 103 Tests")
    card_h = len(safe_claims) * 38 + 16
    draw_card(draw, MARGIN, y, TEXT_W, card_h, fill="#f0fdf4", border=GREEN_BD)
    sy = y + 12
    for claim in safe_claims:
        draw_badge(draw, INNER, sy, "SAFE", GREEN_BG, GREEN_TX, GREEN_BD)
        draw.text((INNER + 76, sy + 3), claim, font=f_reg(14), fill=TX_PRIMARY)
        sy += 38
    y = sy + 20

    limits = [
        "Not hardware-certified",
        "Not a field deployment claim",
        "No live customer fleet exists",
        "Not production certification",
        "Not real-time guaranteed \u2014 simulated time only",
        "Simulation-derived proof surface only",
    ]

    y = draw_section_title(draw, y, "Required Limitations \u2014 Present on FleetSim Public Artifacts")
    card_h = len(limits) * 38 + 16
    draw_card(draw, MARGIN, y, TEXT_W, card_h, fill="#fffbeb", border=AMBER_BD)
    ly = y + 12
    for lim in limits:
        draw_badge(draw, INNER, ly, "LIMIT", AMBER_BG, AMBER_TX, AMBER_BD)
        draw.text((INNER + 86, ly + 3), lim, font=f_reg(14), fill=TX_PRIMARY)
        ly += 38
    y = ly + 20

    y = draw_source_footer(draw, y, "FleetSim/FLEETSIM_EVIDENCE_CAROUSEL_NOTES.md  \u00b7  FLEETSIM_EVIDENCE_CAROUSEL_MANIFEST.md")
    draw_footer(draw, H, "FleetSim claims scoped before public posting")
    save_jpg(img, "prestige_forge_fleetsim_claim_safety.jpg")


# ═════════════════════════════════════════════════════════════════════════════
# IMAGE 6 — Public Language Law
# ═════════════════════════════════════════════════════════════════════════════

def img6_language_law():
    H = 780
    img, draw = new_image(H)

    y = draw_header_bar(draw, "Language Governance")
    y = draw_report_title(draw, y, "Public Language Law",
                          "Rules applied across Razorglint public-facing language")

    laws = [
        "If proof does not support it, do not say it.",
        "Prefer executed passing tests over verified tests.",
        "Prefer tamper-evident over tamper-proof.",
        "Prefer evidence-ready over compliant.",
        "Prefer hardened prototype over production-ready.",
        "Never turn a proof artifact into a certification claim.",
        "Name limitations before readers find them.",
        "Promise evidence of process, not outcomes.",
        "Say we know gaps \u2014 not there are no gaps.",
    ]

    card_h = len(laws) * 46 + 20
    draw_card(draw, MARGIN, y, TEXT_W, card_h)
    ly = y + 14
    for i, law in enumerate(laws, 1):
        cx = INNER + 18
        cy = ly + 14
        draw.ellipse([cx - 16, cy - 16, cx + 16, cy + 16], fill=PF_BLUE)
        num_str = str(i)
        num_bbox = f_bold(14).getbbox(num_str)
        num_w = num_bbox[2] - num_bbox[0]
        draw.text((cx - num_w // 2, cy - 10), num_str, font=f_bold(14), fill=TX_WHITE)
        draw.text((INNER + 50, ly + 2), law, font=f_reg(16), fill=TX_PRIMARY)
        ly += 46
    y = ly + 24

    # Principle callout
    draw_card(draw, MARGIN, y, TEXT_W, 56, fill=BG_HEADER)
    draw.text((INNER + 8, y + 14), "No proof, no claim.", font=f_bold(22), fill=TX_WHITE)
    y += 72

    y = draw_source_footer(draw, y, "systems-architecture/OUTREACH_LANGUAGE_GUARDRAILS.md")
    draw_footer(draw, H, "Applied across Razorglint public communication")
    save_jpg(img, "prestige_forge_public_language_law.jpg")


# ═════════════════════════════════════════════════════════════════════════════
# IMAGE 7 — Internal Razorglint Use Summary
# ═════════════════════════════════════════════════════════════════════════════

def img7_internal_use_summary():
    H = 800
    img, draw = new_image(H)

    y = draw_header_bar(draw, "Internal Use Summary")
    y = draw_report_title(draw, y, "Internal Razorglint Use",
                          "Prestige Forge claim safety applied across the portfolio")

    uses = [
        ("Client Zero", "Self-verification: 15 claims, 25 checks, 15/15 SAFE TO SAY",
         "2026-03-27", GREEN_BG, GREEN_TX, GREEN_BD),
        ("Systems Architecture", "Public claim audit: 78 claims, 28 SAFE, 18 qualified, 26 blocked/forbidden",
         "2026-04-27", GREEN_BG, GREEN_TX, GREEN_BD),
        ("Command Guardian", "Post-remediation wording: 131/131 tests, limitations enforced",
         "2026-04-26", GREEN_BG, GREEN_TX, GREEN_BD),
        ("FleetSim", "Evidence post/PDF claim scoping: 103 tests, 6 explicit non-claims",
         "2026-04-27", GREEN_BG, GREEN_TX, GREEN_BD),
        ("LinkedIn / Outreach", "10 claim-checked safe-to-post drafts, 7 guardrail rules applied",
         "2026-04-27", BLUE_BG, BLUE_TX, "#93c5fd"),
        ("Forbidden Claims", "12 absolute prohibitions, 14 overclaims rewritten with safer alternatives",
         "2026-04-27", RED_BG, RED_TX, RED_BD),
    ]

    for name, desc, date, bg, tx, bd in uses:
        card_h = 80
        draw_card(draw, MARGIN, y, TEXT_W, card_h)
        draw_badge(draw, INNER, y + 12, name.upper(), bg, tx, bd)
        draw.text((W - MARGIN - 120, y + 16), date, font=f_mono(12), fill=TX_MUTED)
        draw.text((INNER + 8, y + 48), desc, font=f_reg(14), fill=TX_PRIMARY)
        y += card_h + 10
    y += 10

    # Summary stats
    draw_card(draw, MARGIN, y, TEXT_W, 50, fill=BG_SUBTLE)
    draw.text((INNER + 8, y + 14),
              "6 internal proof runs  \u00b7  78 claims audited  \u00b7  26 blocked or rewritten  \u00b7  28 approved",
              font=f_semi(13), fill=TX_SECONDARY)
    y += 64

    y = draw_source_footer(draw, y,
        "PUBLIC_CLAIMS_SAFETY_PACK.md  \u00b7  docs/client-zero.md  \u00b7  ENTERPRISE_AUDIT_REPORT.md  \u00b7  + 3 more")
    draw_footer(draw, H, "Internal use only shown here \u2014 no customer deployment claim")
    save_jpg(img, "prestige_forge_internal_use_summary.jpg")


# ─── Main ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print(f"Generating Prestige Forge Internal Use Proof Images (UI Style) \u2014 {NOW_FULL}\n")

    img1_client_zero()
    img2_systems_architecture()
    img3_forbidden_claims()
    img4_command_guardian()
    img5_fleetsim()
    img6_language_law()
    img7_internal_use_summary()

    print(f"\nAll images saved to: {OUT_DIR}")
    print(f"Timestamp: {NOW_FULL}")
