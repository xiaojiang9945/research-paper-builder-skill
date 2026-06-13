from __future__ import annotations

import csv
import math
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT_DIR = ROOT / "input"
OUTPUT_DIR = ROOT / "output"
FIGURE_DIR = OUTPUT_DIR / "figures"
QC_DIR = OUTPUT_DIR / "qc"

DAYS = [f"day{i}_count" for i in range(1, 8)]

PALETTE = {
    "gray_bg": "#F4F5F7",
    "gray_panel": "#ECEFF3",
    "gray_grid": "#D9DDE3",
    "gray_text": "#2F3437",
    "gray_muted": "#6F7782",
    "control": "#C9CDD4",
    "Mock-Wheat-WT": "#FFD59E",
    "Mock-Wheat-A": "#FFB3BA",
    "Mock-Wheat-B": "#BAE1FF",
    "Mock-Wheat-C": "#BAFFC9",
    "accent_lilac": "#D7C7FF",
}

RAW_ROWS = [
    ("Mock-Wheat-WT", "Control", "R1", 50, [10, 32, 43, 47, 48, 48, 49], 6.2, 5.0),
    ("Mock-Wheat-WT", "Control", "R2", 50, [8, 30, 42, 46, 48, 49, 49], 6.0, 5.1),
    ("Mock-Wheat-WT", "Control", "R3", 50, [9, 31, 41, 45, 47, 48, 48], 5.9, 4.9),
    ("Mock-Wheat-WT", "Control", "R4", 50, [11, 33, 44, 47, 49, 49, 49], 6.1, 5.0),
    ("Mock-Wheat-WT", "NaCl-150mM", "R1", 50, [1, 6, 12, 16, 18, 19, 19], 2.2, 1.6),
    ("Mock-Wheat-WT", "NaCl-150mM", "R2", 50, [0, 5, 11, 15, 17, 18, 18], 2.0, 1.5),
    ("Mock-Wheat-WT", "NaCl-150mM", "R3", 50, [1, 4, 10, 14, 16, 17, 17], 1.9, 1.4),
    ("Mock-Wheat-WT", "NaCl-150mM", "R4", 50, [0, 5, 10, 15, 17, 18, 18], 2.1, 1.5),
    ("Mock-Wheat-A", "Control", "R1", 50, [12, 34, 45, 48, 49, 49, 50], 6.4, 5.3),
    ("Mock-Wheat-A", "Control", "R2", 50, [11, 33, 44, 48, 49, 50, 50], 6.5, 5.2),
    ("Mock-Wheat-A", "Control", "R3", 50, [13, 35, 46, 49, 49, 50, 50], 6.3, 5.4),
    ("Mock-Wheat-A", "Control", "R4", 50, [12, 34, 45, 48, 49, 49, 50], 6.4, 5.3),
    ("Mock-Wheat-A", "NaCl-150mM", "R1", 50, [2, 12, 24, 32, 36, 38, 39], 3.9, 3.1),
    ("Mock-Wheat-A", "NaCl-150mM", "R2", 50, [3, 13, 25, 33, 37, 39, 40], 4.0, 3.0),
    ("Mock-Wheat-A", "NaCl-150mM", "R3", 50, [2, 11, 23, 31, 35, 37, 38], 3.8, 2.9),
    ("Mock-Wheat-A", "NaCl-150mM", "R4", 50, [3, 12, 24, 32, 36, 38, 39], 3.9, 3.0),
    ("Mock-Wheat-B", "Control", "R1", 50, [10, 31, 42, 46, 48, 48, 49], 6.1, 5.0),
    ("Mock-Wheat-B", "Control", "R2", 50, [9, 30, 41, 45, 47, 48, 48], 6.0, 4.8),
    ("Mock-Wheat-B", "Control", "R3", 50, [10, 32, 43, 46, 48, 49, 49], 6.2, 5.0),
    ("Mock-Wheat-B", "Control", "R4", 50, [9, 31, 42, 46, 48, 48, 48], 6.0, 4.9),
    ("Mock-Wheat-B", "NaCl-150mM", "R1", 50, [1, 9, 19, 25, 29, 30, 31], 3.2, 2.5),
    ("Mock-Wheat-B", "NaCl-150mM", "R2", 50, [1, 8, 18, 24, 28, 30, 30], 3.1, 2.4),
    ("Mock-Wheat-B", "NaCl-150mM", "R3", 50, [2, 9, 19, 26, 29, 31, 31], 3.3, 2.5),
    ("Mock-Wheat-B", "NaCl-150mM", "R4", 50, [1, 8, 17, 24, 28, 29, 30], 3.0, 2.3),
    ("Mock-Wheat-C", "Control", "R1", 50, [8, 29, 40, 44, 46, 47, 48], 5.8, 4.7),
    ("Mock-Wheat-C", "Control", "R2", 50, [8, 28, 39, 43, 46, 47, 47], 5.7, 4.6),
    ("Mock-Wheat-C", "Control", "R3", 50, [9, 30, 40, 44, 47, 47, 48], 5.9, 4.8),
    ("Mock-Wheat-C", "Control", "R4", 50, [8, 29, 39, 43, 46, 47, 47], 5.8, 4.7),
    ("Mock-Wheat-C", "NaCl-150mM", "R1", 50, [0, 7, 15, 20, 23, 24, 25], 2.7, 2.1),
    ("Mock-Wheat-C", "NaCl-150mM", "R2", 50, [1, 7, 14, 19, 22, 23, 24], 2.6, 2.0),
    ("Mock-Wheat-C", "NaCl-150mM", "R3", 50, [1, 8, 15, 21, 24, 25, 25], 2.8, 2.1),
    ("Mock-Wheat-C", "NaCl-150mM", "R4", 50, [0, 6, 14, 19, 22, 23, 24], 2.5, 1.9),
]

REFERENCES = {
    "R01": "Demo Reference 1. Wheat seed germination and early seedling establishment under abiotic stress. Synthetic Wheat Review Series. 2026.",
    "R02": "Demo Reference 2. Osmotic and ionic components of salinity response during cereal germination. Synthetic Crop Physiology. 2026.",
    "R03": "Demo Reference 3. Hormonal regulation of wheat germination under water-limited conditions. Synthetic Plant Signaling. 2026.",
    "R04": "Demo Reference 4. Genetic variation in wheat seedling vigor and stress emergence. Synthetic Wheat Genetics. 2026.",
    "R05": "Demo Reference 5. Experimental design for replicated cereal germination assays. Synthetic Methods in Agronomy. 2026.",
    "R06": "Demo Reference 6. Reporting time-course germination data in crop science. Synthetic Biometry. 2026.",
    "R07": "Demo Reference 7. Seedling vigor indices and their limitations in wheat screening. Synthetic Phenotyping Notes. 2026.",
    "R08": "Demo Reference 8. Claim calibration in salt-tolerance screening experiments. Synthetic Editorial Practice. 2026.",
    "R09": "Demo Reference 9. Multi-panel figure design for crop-science manuscripts. Synthetic Figure Methods. 2026.",
    "R10": "Demo Reference 10. Source-data traceability for biological figures. Synthetic Research Integrity. 2026.",
    "R11": "Demo Reference 11. Literature-intake matrices for field-aware manuscript writing. Synthetic Scientific Writing. 2026.",
    "R12": "Demo Reference 12. Citation-reference consistency checks before manuscript submission. Synthetic Open Research. 2026.",
    "R13": "Demo Reference 13. Terminology control in genotype-by-treatment studies. Synthetic Nomenclature Notes. 2026.",
    "R14": "Demo Reference 14. Reviewer expectations for wheat stress-tolerance papers. Synthetic Peer Review. 2026.",
    "R15": "Demo Reference 15. Distinguishing seedling assay rankings from field tolerance. Synthetic Interpretation Letters. 2026.",
    "R16": "Demo Reference 16. Integrating physiology, genetics and phenotyping in wheat stress studies. Synthetic Crop Systems. 2026.",
    "R17": "Demo Reference 17. Data availability and reproducibility in crop biology. Synthetic FAIR Data. 2026.",
    "R18": "Demo Reference 18. From preliminary screens to mechanistic validation in cereals. Synthetic Translational Botany. 2026.",
}


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def sd(values: list[float]) -> float:
    if len(values) < 2:
        return 0.0
    m = mean(values)
    return math.sqrt(sum((v - m) ** 2 for v in values) / (len(values) - 1))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def raw_records() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for genotype, treatment, replicate, total, counts, root_len, shoot_len in RAW_ROWS:
        record: dict[str, object] = {
            "genotype": genotype,
            "treatment": treatment,
            "replicate": replicate,
            "total_seeds": total,
            "day7_root_length_cm": root_len,
            "day7_shoot_length_cm": shoot_len,
        }
        for day, count in enumerate(counts, start=1):
            record[f"day{day}_count"] = count
        rows.append(record)
    return rows


def summarize(records: list[dict[str, object]]) -> tuple[list[dict[str, object]], list[dict[str, object]], dict[str, dict[str, float]]]:
    genotypes = sorted({str(r["genotype"]) for r in records})
    treatments = ["Control", "NaCl-150mM"]
    source_rows: list[dict[str, object]] = []
    endpoint_rows: list[dict[str, object]] = []
    endpoints: dict[str, dict[str, float]] = {}

    for genotype in genotypes:
        endpoints[genotype] = {}
        for treatment in treatments:
            group = [r for r in records if r["genotype"] == genotype and r["treatment"] == treatment]
            day7 = [float(r["day7_count"]) / float(r["total_seeds"]) * 100 for r in group]
            root = [float(r["day7_root_length_cm"]) for r in group]
            shoot = [float(r["day7_shoot_length_cm"]) for r in group]
            vigor = [g * (ro + sh) for g, ro, sh in zip(day7, root, shoot)]
            endpoints[genotype][treatment] = mean(day7)
            endpoints[genotype][f"{treatment}_vigor"] = mean(vigor)
            endpoint_rows.append(
                {
                    "genotype": genotype,
                    "treatment": treatment,
                    "day7_germination_mean_pct": f"{mean(day7):.1f}",
                    "day7_germination_sd_pct": f"{sd(day7):.1f}",
                    "root_length_mean_cm": f"{mean(root):.2f}",
                    "root_length_sd_cm": f"{sd(root):.2f}",
                    "shoot_length_mean_cm": f"{mean(shoot):.2f}",
                    "shoot_length_sd_cm": f"{sd(shoot):.2f}",
                    "vigor_index_mean": f"{mean(vigor):.1f}",
                    "vigor_index_sd": f"{sd(vigor):.1f}",
                    "n_biological_replicates": len(group),
                }
            )
            for day in range(1, 8):
                vals = [float(r[f"day{day}_count"]) / float(r["total_seeds"]) * 100 for r in group]
                source_rows.append(
                    {
                        "genotype": genotype,
                        "treatment": treatment,
                        "day": day,
                        "germination_mean_pct": f"{mean(vals):.1f}",
                        "germination_sd_pct": f"{sd(vals):.1f}",
                        "n_biological_replicates": len(group),
                    }
                )

    for genotype in genotypes:
        control = endpoints[genotype]["Control"]
        salt = endpoints[genotype]["NaCl-150mM"]
        endpoints[genotype]["retention_pct"] = salt / control * 100 if control else 0.0
    return source_rows, endpoint_rows, endpoints


def bar(svg: list[str], x: float, y: float, w: float, h: float, color: str) -> None:
    svg.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{color}" rx="3"/>')


def text(svg: list[str], x: float, y: float, value: str, size: int = 20, weight: str = "400", color: str | None = None, anchor: str = "start") -> None:
    fill = color or PALETTE["gray_text"]
    svg.append(
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="Arial, Helvetica, sans-serif" '
        f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}">{value}</text>'
    )


def panel(svg: list[str], x: int, y: int, w: int, h: int, letter: str, title: str) -> None:
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="white" stroke="{PALETTE["gray_grid"]}" rx="8"/>')
    text(svg, x + 18, y + 34, letter, 30, "700")
    text(svg, x + 58, y + 31, title, 18, "700")


def make_figure(endpoint_rows: list[dict[str, object]], source_rows: list[dict[str, object]], endpoints: dict[str, dict[str, float]]) -> None:
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    width, height = 1600, 1040
    svg: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        f'<rect width="{width}" height="{height}" fill="{PALETTE["gray_bg"]}"/>',
    ]
    text(svg, 40, 48, "Figure 1. Synthetic wheat germination workflow under salt treatment", 28, "700")
    text(svg, 40, 78, "Candy-color highlights on a premium-gray scaffold; all values are synthetic.", 16, "400", PALETTE["gray_muted"])

    panel(svg, 40, 110, 470, 260, "a", "Runnable wheat demo design")
    for i, label in enumerate(["4 mock wheat genotypes", "2 treatments", "4 biological replicates", "50 seeds per replicate"]):
        y = 165 + i * 43
        svg.append(f'<circle cx="82" cy="{y}" r="14" fill="{[PALETTE["Mock-Wheat-A"], PALETTE["Mock-Wheat-B"], PALETTE["Mock-Wheat-C"], PALETTE["accent_lilac"]][i]}"/>')
        text(svg, 112, y + 6, label, 19)
    text(svg, 62, 342, "Input: CSV -> analysis -> composite SVG -> manuscript -> QC", 15, "400", PALETTE["gray_muted"])

    panel(svg, 550, 110, 500, 260, "b", "Day 7 germination endpoint")
    genotypes = sorted(endpoints)
    x0, y0, plot_w, plot_h = 610, 315, 380, 135
    for tick in range(0, 101, 25):
        yy = y0 - tick / 100 * plot_h
        svg.append(f'<line x1="{x0}" y1="{yy:.1f}" x2="{x0 + plot_w}" y2="{yy:.1f}" stroke="{PALETTE["gray_grid"]}" stroke-width="1"/>')
        text(svg, x0 - 10, yy + 5, str(tick), 12, "400", PALETTE["gray_muted"], "end")
    group_w = plot_w / len(genotypes)
    for idx, genotype in enumerate(genotypes):
        cx = x0 + idx * group_w + 18
        control = endpoints[genotype]["Control"]
        salt = endpoints[genotype]["NaCl-150mM"]
        bar(svg, cx, y0 - control / 100 * plot_h, 26, control / 100 * plot_h, PALETTE["control"])
        bar(svg, cx + 32, y0 - salt / 100 * plot_h, 26, salt / 100 * plot_h, PALETTE[genotype])
        text(svg, cx + 29, y0 + 20, genotype.replace("Mock-Wheat-", ""), 12, "400", PALETTE["gray_text"], "middle")
    text(svg, x0, 165, "Control", 14, "700", PALETTE["gray_muted"])
    svg.append(f'<rect x="{x0 + 70}" y="154" width="18" height="12" fill="{PALETTE["control"]}"/>')
    text(svg, x0 + 105, 165, "NaCl-150mM", 14, "700", PALETTE["gray_muted"])
    svg.append(f'<rect x="{x0 + 202}" y="154" width="18" height="12" fill="{PALETTE["Mock-Wheat-A"]}"/>')
    text(svg, x0 - 24, 176, "Germination (%)", 13, "400", PALETTE["gray_muted"], "end")

    panel(svg, 1090, 110, 470, 260, "c", "Salt-treatment trajectory")
    tx0, ty0, tw, th = 1140, 315, 360, 155
    for tick in range(0, 101, 25):
        yy = ty0 - tick / 100 * th
        svg.append(f'<line x1="{tx0}" y1="{yy:.1f}" x2="{tx0 + tw}" y2="{yy:.1f}" stroke="{PALETTE["gray_grid"]}" stroke-width="1"/>')
    for genotype in genotypes:
        pts = []
        salt_rows = [r for r in source_rows if r["genotype"] == genotype and r["treatment"] == "NaCl-150mM"]
        for row in salt_rows:
            day = int(row["day"])
            value = float(row["germination_mean_pct"])
            x = tx0 + (day - 1) / 6 * tw
            y = ty0 - value / 100 * th
            pts.append(f"{x:.1f},{y:.1f}")
        svg.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{PALETTE[genotype]}" stroke-width="4" stroke-linecap="round"/>')
        last_x, last_y = [float(v) for v in pts[-1].split(",")]
        svg.append(f'<circle cx="{last_x:.1f}" cy="{last_y:.1f}" r="5" fill="{PALETTE[genotype]}"/>')
        text(svg, last_x + 8, last_y + 4, genotype.replace("Mock-Wheat-", ""), 12, "700")
    text(svg, tx0 + tw / 2, ty0 + 32, "Day after sowing", 13, "400", PALETTE["gray_muted"], "middle")

    panel(svg, 40, 410, 470, 285, "d", "Salt-retention ranking")
    rx0, ry0, rw, rh = 140, 640, 300, 170
    ranked = sorted(genotypes, key=lambda g: endpoints[g]["retention_pct"], reverse=True)
    for idx, genotype in enumerate(ranked):
        val = endpoints[genotype]["retention_pct"]
        y = 472 + idx * 48
        bar(svg, rx0, y, val / 85 * rw, 28, PALETTE[genotype])
        text(svg, 62, y + 20, genotype.replace("Mock-Wheat-", ""), 16, "700")
        text(svg, rx0 + val / 85 * rw + 10, y + 20, f"{val:.1f}%", 15, "700")
    text(svg, 62, 670, "Retention = salt Day 7 mean / control Day 7 mean", 14, "400", PALETTE["gray_muted"])

    panel(svg, 550, 410, 500, 285, "e", "Seedling vigor under salt")
    vx0, vy0, vw, vh = 620, 650, 340, 170
    max_vigor = max(endpoints[g]["NaCl-150mM_vigor"] for g in genotypes)
    for idx, genotype in enumerate(genotypes):
        value = endpoints[genotype]["NaCl-150mM_vigor"]
        x = vx0 + idx * 78
        bar(svg, x, vy0 - value / max_vigor * vh, 42, value / max_vigor * vh, PALETTE[genotype])
        text(svg, x + 21, vy0 + 20, genotype.replace("Mock-Wheat-", ""), 12, "400", PALETTE["gray_text"], "middle")
        text(svg, x + 21, vy0 - value / max_vigor * vh - 8, f"{value:.0f}", 12, "700", PALETTE["gray_text"], "middle")
    text(svg, vx0, 460, "Synthetic vigor index = germination % x seedling length", 14, "400", PALETTE["gray_muted"])

    panel(svg, 1090, 410, 470, 285, "f", "Five-pass QC gate")
    qc_labels = ["Evidence", "Citation", "Language", "Figure", "Format"]
    for idx, label in enumerate(qc_labels):
        x = 1135 + idx * 78
        svg.append(f'<circle cx="{x}" cy="535" r="26" fill="{[PALETTE["Mock-Wheat-A"], PALETTE["Mock-Wheat-B"], PALETTE["Mock-Wheat-C"], PALETTE["accent_lilac"], PALETTE["control"]][idx]}"/>')
        text(svg, x, 542, str(idx + 1), 20, "700", PALETTE["gray_text"], "middle")
        text(svg, x, 590, label, 13, "700", PALETTE["gray_text"], "middle")
    text(svg, 1120, 650, "Demo writes qc/five_pass_qc_report.md and qc_results.csv", 15, "400", PALETTE["gray_muted"])

    text(svg, 40, 735, "Claim boundary", 22, "700")
    claim = [
        "Supported: synthetic Mock-Wheat-A ranks highest for Day 7 salt germination and retention.",
        "Not supported: mechanism, real cultivar performance, field tolerance, or breeding recommendation.",
        "Required before real writing: documented search plus 200-paper full-text reading matrix.",
    ]
    for i, line in enumerate(claim):
        text(svg, 70, 775 + i * 32, line, 19)
        svg.append(f'<circle cx="52" cy="{769 + i * 32}" r="6" fill="{PALETTE["accent_lilac"]}"/>')

    svg.append("</svg>")
    (FIGURE_DIR / "figure1_composite.svg").write_text("\n".join(svg), encoding="utf-8")


def citation_keys(text_value: str) -> list[str]:
    keys: list[str] = []
    for match in re.findall(r"\[(R\d+(?:,R\d+)*)\]", text_value):
        keys.extend(part.strip() for part in match.split(","))
    return sorted(set(keys))


def section(text_value: str, heading: str, next_heading: str) -> str:
    match = re.search(rf"## {re.escape(heading)}\n\n(.+?)\n\n## {re.escape(next_heading)}", text_value, re.S)
    return match.group(1) if match else ""


def word_count(text_value: str) -> int:
    return len(re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", text_value))


def manuscript(endpoints: dict[str, dict[str, float]]) -> str:
    a = endpoints["Mock-Wheat-A"]
    b = endpoints["Mock-Wheat-B"]
    c = endpoints["Mock-Wheat-C"]
    wt = endpoints["Mock-Wheat-WT"]
    return f"""# A runnable synthetic wheat demo for figure-led manuscript construction

## Abstract

Research-paper writing workflows need to be tested with materials that resemble a real manuscript package while avoiding exposure of unpublished data, private author information or unverifiable citations. Here, we present a runnable synthetic wheat demo for the `research-paper-builder` skill. The demo models a salt-treatment germination assay in _Triticum aestivum_ using four fictional wheat genotypes, two treatments, four biological replicates per genotype-treatment combination and 50 seeds per replicate. A deterministic build script converts the input CSV into summary tables, source data, an editable multi-panel SVG figure, a figure-led Results section, citation-reference audit and five-pass quality-control report. This makes the demonstration inspectable, repeatable and closer to real manuscript operations than a static sample. Control-treated groups reached high Day 7 germination, with means from {c["Control"]:.1f}% to {a["Control"]:.1f}%. NaCl treatment reduced germination in every mock genotype, but Mock-Wheat-A retained the highest salt-treated Day 7 germination at {a["NaCl-150mM"]:.1f}%, compared with {b["NaCl-150mM"]:.1f}% for Mock-Wheat-B, {c["NaCl-150mM"]:.1f}% for Mock-Wheat-C and {wt["NaCl-150mM"]:.1f}% for Mock-Wheat-WT. The figure uses candy-color genotype highlights on a premium-gray scaffold and records the evidence-to-claim boundary inside the manuscript package. The package also demonstrates how wording, visual design, citations and formatting can be checked in separate rounds. The demo supports only workflow validation and synthetic ranking; it does not support mechanism, cultivar recommendation or field performance. For real high-ambition wheat manuscripts, the skill requires documented searching and a reading matrix covering at least 200 fully read relevant papers before polished writing.

## Introduction

Wheat manuscripts often combine applied urgency with complex biological interpretation. Germination and early seedling establishment influence stand formation, stress recovery and downstream agronomic performance, but a short seedling assay does not automatically explain field tolerance or yield stability [R01,R04]. A paper built from this kind of experiment therefore needs more than fluent prose. It needs a workflow that keeps the system, treatment, genotype labels, source data, figure panels, citations and claim boundaries synchronized from the first outline to the final package [R09,R10,R13]. The present demo uses wheat because it is a realistic crop-science context in which reviewers expect clear experimental design, cautious stress-language and enough methodological detail to separate measured phenotypes from breeding or mechanistic claims [R14,R15].

Salt stress is a useful example for a manuscript-building demo because it introduces a common interpretive trap. Reduced germination under NaCl can reflect osmotic restriction, ionic effects, seed-lot quality, dormancy status, maternal environment, scoring criteria or genotype-specific developmental timing [R02,R03]. A dataset containing daily counts and Day 7 seedling measurements can describe a treatment response and rank fictional genotypes within the assay, but it cannot identify the molecular basis of that response without additional physiology, ion profiling, transcript analysis, genetic validation or independent environments [R08,R16,R18]. The writing workflow must preserve that distinction. If a draft calls the top-ranked line "salt tolerant" without validation, the manuscript has already outrun its evidence.

Wheat also makes the figure problem concrete. Crop-science manuscripts frequently contain endpoint bars, time-course lines, seedling images, vigor traits, statistical summaries and tables of genotype metadata. If these elements are assembled after writing, the Results section can become a list of disconnected values. A figure-led workflow reverses that order. It first asks what each main figure proves, what each panel contributes, where the plotted values come from and which statement the caption is allowed to make [R06,R09,R10]. In this demo, Figure 1 is not a decorative plot. It is the spine of the Results section: design, Day 7 endpoint, salt trajectory, retention ranking, vigor index and quality-control gate.

The wheat context also forces the workflow to distinguish a manuscript demo from a biological claim. A static example can look convincing while leaving no way to verify whether values were recalculated, whether a panel was edited after the text was written or whether a quality-control statement was added by hand. The present demo addresses that problem by treating the example as an operation chain. The same script defines the fictional assay, writes the raw-style CSV, computes means and standard deviations, exports source data, draws the figure and then checks the generated package. This design is closer to how a real manuscript should be built, because every visual and textual claim can be traced back to a reproducible step [R05,R10,R17].

The demo is intentionally synthetic, but the operations are real. The repository includes a build script that writes the input table, recomputes the summaries, draws the composite SVG, builds the citation audit and emits a quality-control report. This matters because static examples can hide drift. A hand-edited figure may not match the CSV. A reference list may contain uncited items. A README can mention one organism while the manuscript describes another. By regenerating the package from a script and then checking the generated files, the demo turns common manuscript risks into testable conditions [R10,R12,R17].

The color specification is also part of the manuscript standard rather than a cosmetic afterthought. Candy colors can make genotype contrasts easier to scan, but they need a restrained scaffold so that the figure does not look informal. The demo therefore uses soft pink, blue, mint, peach and lilac accents only for genotype or workflow emphasis, while axes, grid lines, panel borders, legends and explanatory text use premium-gray tones [R09]. This arrangement gives the figure a lighter visual identity without sacrificing print readability or source-data traceability. For real submissions, the same palette should be checked in grayscale and adjusted for journal requirements.

In wheat papers, visual hierarchy is especially important because the audience may include molecular biologists, physiologists, breeders and editors who look for different evidence. A composite figure should let each reader find the design, primary comparison, secondary phenotype and limitation boundary quickly. The candy colors in the demo are therefore not used as decoration across the whole page. They are reserved for genotype identity and workflow checkpoints, while gray carries the structural information. This keeps the plot readable when printed, inserted into a manuscript draft or compared against source-data tables [R09,R14].

Because the demo includes both endpoint germination and a secondary seedling-vigor calculation, it also shows how a manuscript can introduce supporting phenotypes without letting them dominate the story. The Results text keeps Day 7 germination as the primary endpoint and uses vigor only as a consistency-oriented secondary readout, which mirrors the hierarchy a real paper would need [R06,R07].

Literature intake remains the largest difference between a demo and a field-ready paper. A real high-ambition wheat manuscript should not be written from a small list of remembered papers. The skill now requires a documented search universe, screening record and reading matrix in which at least 200 directly relevant papers have been read in full when the project aims at a full research article for a demanding journal [R11]. The reading matrix should capture study system, method precedent, figure architecture, claim boundaries, limitations and citation roles. If that matrix is missing, the correct output is a search plan, partial matrix and outline, not a polished manuscript [R11,R12].

Citation integrity is another checkable part of the workflow. Every in-text citation should correspond to one reference-list item, and every listed item should be cited at least once [R12]. Citation roles should be explicit: some references support wheat biology, some support salt-stress interpretation, some support figure design, and some support data availability or reviewer-risk control. The synthetic references in this demo are placeholders for testing this machinery only. They are not real literature and should not be reused as scientific support [R12,R17].

Quality control is treated as a multi-pass process because a single final read is not enough for manuscript work. The demo implements five passes: evidence and data consistency; citation and reference matching; scientific language and claim scope; figure and visual-format inspection; and package formatting with privacy checks. Each pass has explicit tests and a saved status file. A real project may need more rounds, including journal-specific checks, author review and statistical review, but the five-pass gate gives the skill a minimum standard for text, language, image and format reliability [R08,R14,R17].

This wheat demo therefore has two purposes. First, it replaces a short plant-germination sketch with a reproducible manuscript-scale example that can be run, inspected and regenerated. Second, it defines how the skill should behave on real manuscripts: read the field before writing, build the story around figures, use restrained but distinctive visuals, maintain citation and data traceability, and perform repeated checks before claiming that a package is ready for review [R09,R11,R17,R18]. Those requirements make the example stricter than a visual mockup and closer to a real submission-preparation workflow.

## Results

### Figure 1 converts the synthetic wheat dataset into a manuscript evidence chain

The runnable demo generated a six-panel composite figure from the synthetic wheat input table. Figure 1a defines the assay structure: four fictional wheat genotypes, two treatments, four biological replicates per genotype-treatment combination and 50 seeds per replicate. Figure 1b reports Day 7 germination under control and NaCl treatment. Figure 1c shows the NaCl germination trajectory from Day 1 to Day 7, allowing the reader to see whether differences emerge early or only at the endpoint. Figure 1d ranks salt-retention percentage, Figure 1e summarizes a synthetic vigor index under salt treatment, and Figure 1f records the five-pass QC gate. This organization demonstrates the expected figure-led Results pattern: every panel has a defined evidence role and a traceable source-data or workflow source [R09,R10].

![Figure 1 composite](figures/figure1_composite.svg)

### NaCl treatment reduced Day 7 germination across all mock wheat genotypes

Control-treated groups reached high Day 7 germination across the fictional wheat panel (Figure 1b; Supplementary Table S1). Mean control germination was {wt["Control"]:.1f}% for Mock-Wheat-WT, {a["Control"]:.1f}% for Mock-Wheat-A, {b["Control"]:.1f}% for Mock-Wheat-B and {c["Control"]:.1f}% for Mock-Wheat-C. NaCl treatment reduced Day 7 germination in every mock genotype. Salt-treated means were {wt["NaCl-150mM"]:.1f}% for Mock-Wheat-WT, {a["NaCl-150mM"]:.1f}% for Mock-Wheat-A, {b["NaCl-150mM"]:.1f}% for Mock-Wheat-B and {c["NaCl-150mM"]:.1f}% for Mock-Wheat-C. These values support a descriptive treatment-response statement within the synthetic assay only [R05,R06,R08].

### Mock-Wheat-A ranked highest for synthetic salt retention and vigor

Salt-retention percentage was calculated as salt-treated Day 7 germination divided by control-treated Day 7 germination for the same genotype. Mock-Wheat-A retained {a["retention_pct"]:.1f}% of its control germination, followed by Mock-Wheat-B at {b["retention_pct"]:.1f}%, Mock-Wheat-C at {c["retention_pct"]:.1f}% and Mock-Wheat-WT at {wt["retention_pct"]:.1f}% (Figure 1d). The synthetic vigor index under salt treatment showed the same ranking pattern, with Mock-Wheat-A having the highest value among the fictional genotypes (Figure 1e). This supports a cautious statement that Mock-Wheat-A ranks highest in this synthetic screen. It does not establish mechanism, field tolerance or breeding value [R07,R08,R15,R18].

## Discussion

This demo shows how the skill should move from raw experimental-style inputs to a traceable manuscript package. The generated wheat dataset supports a limited synthetic result: NaCl treatment reduced germination across all mock genotypes, and Mock-Wheat-A ranked highest for Day 7 germination retention and seedling vigor under the synthetic salt condition. The wording does not convert that ranking into mechanism or cultivar value. That restraint is intentional because real wheat stress manuscripts are vulnerable to overclaiming when screening assays are treated as proof of tolerance [R08,R14,R15].

The demo also shows why figure-led writing is the correct default for research manuscripts. The Results section does not start from prose and then attach a plot. It walks through the composite figure panel by panel, linking each claim to a source-data table or documented workflow role. The candy-color and premium-gray styling gives the figure a consistent visual identity while keeping the quantitative content readable. In a real manuscript, the same approach should be extended to additional figures, source-data workbooks and statistical outputs [R09,R10,R17].

Finally, the demo makes the literature gate explicit. The placeholder references here are synthetic and exist only to test citation-reference matching. A real wheat paper should be preceded by documented search, screening and full-text reading of at least 200 relevant papers when the project targets a high-ambition full manuscript. Without that field-learning step, the skill should stop at a literature plan, reading matrix and outline instead of producing polished prose [R11,R12,R18].

## Methods

The input dataset was manually defined as a fully synthetic wheat germination table. Four fictional genotypes were included: Mock-Wheat-WT, Mock-Wheat-A, Mock-Wheat-B and Mock-Wheat-C. Each genotype was represented under control and NaCl-150mM treatment with four biological replicates per treatment. Each replicate contained 50 seeds. Daily germination counts were recorded from Day 1 to Day 7, and synthetic Day 7 root and shoot lengths were included for seedling-vigor demonstration.

Germination percentage was calculated as germinated seed count divided by total seed count. Salt-retention percentage was calculated as salt-treated Day 7 mean germination divided by control-treated Day 7 mean germination for the same genotype. Seedling vigor index was calculated as Day 7 germination percentage multiplied by root plus shoot length. Summary values are reported as mean +/- SD. No inferential statistics were applied because the dataset is fictional and intended only as a workflow demonstration [R05,R06,R07].

The composite Figure 1 was generated as an editable SVG by `scripts/build_demo.py`. Panels b-e are based on the synthetic source data in `source_data_figure1.csv` and `supplementary_table_s1_summary.csv`. Panels a and f are workflow panels and do not represent additional biological measurements. The same script writes the citation audit and five-pass QC report [R09,R10,R12].

## Data Availability

All data used in this demo are synthetic and included in the repository under `examples/synthetic-wheat-study/`. No real research data, personal data or confidential materials are included. For real manuscripts, this statement must be replaced with repository accession numbers, source-data files, code releases and access restrictions where applicable [R17].

## Author Contributions

This demo does not represent a real study and has no real authorship claim.

## Competing Interests

No competing interests are associated with this synthetic demo.

## References

{chr(10).join(f"{key}. {value}" for key, value in REFERENCES.items())}
"""


def write_literature_status() -> None:
    text_value = """# Literature Intake Status

This runnable wheat demo does not claim that 200 real papers were searched or read. It uses synthetic citation placeholders only to demonstrate citation placement, reference-list matching and quality-control output.

For a real high-ambition wheat manuscript, the skill must require:

- documented search across relevant databases, review papers and citation trails;
- at least 200 directly relevant papers fully read, including main text, figures, methods and supplementary information when available;
- a reading matrix recording study system, method precedent, figure lessons, key findings, claim boundaries, limitations and citation roles;
- a story map created from the reading matrix before polished manuscript writing.

If the 200-paper full-text intake is incomplete, the correct output is a literature plan, partial reading matrix and outline rather than a final manuscript.
"""
    (OUTPUT_DIR / "literature_intake_status.md").write_text(text_value, encoding="utf-8")


def write_readme() -> None:
    text_value = """# Synthetic Wheat Study Demo

This is a fully synthetic and runnable demo for the `research-paper-builder` skill. It uses fictional wheat germination data to show how the skill should produce a manuscript-scale package, not a short report.

## Run The Demo

```bash
python scripts/build_demo.py
```

The script regenerates:

- `input/synthetic_wheat_germination_data.csv`
- `output/source_data_figure1.csv`
- `output/supplementary_table_s1_summary.csv`
- `output/figures/figure1_composite.svg`
- `output/manuscript_draft.md`
- `output/citation_reference_audit.csv`
- `output/qc/five_pass_qc_report.md`
- `output/qc/qc_results.csv`
- `output/package_manifest.md`

## Design Notes

- Organism context: wheat (_Triticum aestivum_), not a generic model-plant placeholder.
- Data status: fully synthetic; no unpublished or private research data.
- Literature status: synthetic citation placeholders only; real manuscripts require documented searching and at least 200 relevant full-text papers in a reading matrix.
- Figure style: candy-color genotype highlights on a premium-gray scaffold.
- QC: five passes covering evidence/data, citations, language/claims, figure/visuals and package formatting/privacy.
"""
    (ROOT / "README.md").write_text(text_value, encoding="utf-8")


def write_supporting_files(endpoint_rows: list[dict[str, object]], endpoints: dict[str, dict[str, float]]) -> None:
    best = max(endpoints, key=lambda g: endpoints[g]["retention_pct"])
    (OUTPUT_DIR / "evidence_map.md").write_text(
        f"""# Evidence Map

## Central Question

Can a runnable synthetic wheat germination dataset demonstrate a figure-led research-paper workflow with traceable source data, candy-color plus premium-gray figure styling and five-pass QC?

## Supported Synthetic Claims

- NaCl-150mM reduced Day 7 germination across all four fictional wheat genotypes.
- {best} ranked highest for synthetic salt-retention percentage.
- The build script regenerates source data, Figure 1, manuscript text, citation audit and QC outputs.

## Unsupported Claims

- Do not claim mechanism, real cultivar performance, field tolerance or breeding recommendation.
- Do not claim that the demo completed the 200-paper full-text literature-intake gate required for a real high-ambition wheat manuscript.
- Do not treat synthetic references as scientific support.
""",
        encoding="utf-8",
    )
    (OUTPUT_DIR / "terminology_ledger.md").write_text(
        """# Terminology Ledger

| canonical term | allowed variants | forbidden variants | note |
|---|---|---|---|
| wheat | _Triticum aestivum_ | generic model-plant placeholder, rice, maize | demo organism context |
| Mock-Wheat-WT | WT | real cultivar name | fictional genotype |
| Mock-Wheat-A | Line A | tolerant cultivar | fictional top-ranked line |
| NaCl-150mM | salt treatment | salinity field stress | controlled synthetic treatment |
| salt retention | retention percentage | field tolerance | descriptive metric only |
| five-pass QC | QC gate | final approval | demo check mechanism |
""",
        encoding="utf-8",
    )
    (OUTPUT_DIR / "figure_plan.md").write_text(
        """# Figure Plan

## Figure 1. Synthetic wheat germination workflow under salt treatment

| panel | content | source data | statistic | manuscript role |
|---|---|---|---|---|
| a | runnable demo design | schematic, no additional data | not applicable | orient reader to operations |
| b | Day 7 germination percentage under Control and NaCl-150mM | `source_data_figure1.csv` | mean +/- SD, n=4 | primary endpoint comparison |
| c | Day 1-7 NaCl germination trajectory | `source_data_figure1.csv` | mean +/- SD, n=4 | temporal pattern |
| d | salt-retention ranking | `supplementary_table_s1_summary.csv` | salt Day 7 mean / control Day 7 mean | descriptive ranking |
| e | seedling vigor index under NaCl | `supplementary_table_s1_summary.csv` | germination % x seedling length | secondary phenotype |
| f | five-pass QC gate | `qc/qc_results.csv` | pass/fail checks | manuscript package reliability |

## Visual Style

- Use candy-color highlights for mock wheat genotypes: soft peach, pink, blue and mint.
- Use premium-gray for page background, grid lines, panel frames, neutral control bars and secondary text.
- Preserve editable SVG text and source data.
- Keep panel letters unique and large enough for print review.
""",
        encoding="utf-8",
    )
    (OUTPUT_DIR / "data_availability.md").write_text(
        """# Data Availability

All data in this demo are synthetic and are included in `examples/synthetic-wheat-study/`. The generated figure is based on `output/source_data_figure1.csv` and `output/supplementary_table_s1_summary.csv`.

Real manuscript work must replace this statement with actual accession numbers, repository links, source-data files, code releases and any justified access restrictions.
""",
        encoding="utf-8",
    )
    (OUTPUT_DIR / "references_demo.md").write_text(
        "# Synthetic References\n\n" + "\n\n".join(f"{k}. {v}" for k, v in REFERENCES.items()) + "\n",
        encoding="utf-8",
    )


def write_citation_audit(manuscript_text: str) -> None:
    keys = citation_keys(manuscript_text)
    body = manuscript_text.split("## References", 1)[0]
    rows = []
    for key in sorted(REFERENCES):
        rows.append(
            {
                "citation_key": key,
                "in_text_count": body.count(key),
                "reference_list_entry_present": str(key in REFERENCES).lower(),
                "citation_role": {
                    "R01": "wheat germination background",
                    "R02": "salt-stress interpretation",
                    "R03": "hormonal context",
                    "R04": "genetic variation",
                    "R05": "experimental design",
                    "R06": "time-course reporting",
                    "R07": "vigor metric",
                    "R08": "claim calibration",
                    "R09": "figure design",
                    "R10": "source-data traceability",
                    "R11": "literature intake",
                    "R12": "citation consistency",
                    "R13": "terminology control",
                    "R14": "reviewer expectations",
                    "R15": "field-tolerance boundary",
                    "R16": "wheat stress systems",
                    "R17": "data availability",
                    "R18": "validation boundary",
                }[key],
                "status": "matched" if key in keys else "uncited",
            }
        )
    write_csv(
        OUTPUT_DIR / "citation_reference_audit.csv",
        ["citation_key", "in_text_count", "reference_list_entry_present", "citation_role", "status"],
        rows,
    )


def write_qc(manuscript_text: str) -> None:
    cited = set(citation_keys(manuscript_text))
    refs = set(REFERENCES)
    abstract_words = word_count(section(manuscript_text, "Abstract", "Introduction"))
    intro_words = word_count(section(manuscript_text, "Introduction", "Results"))
    svg_text = (FIGURE_DIR / "figure1_composite.svg").read_text(encoding="utf-8")
    required_files = [
        INPUT_DIR / "synthetic_wheat_germination_data.csv",
        OUTPUT_DIR / "source_data_figure1.csv",
        OUTPUT_DIR / "supplementary_table_s1_summary.csv",
        FIGURE_DIR / "figure1_composite.svg",
        OUTPUT_DIR / "manuscript_draft.md",
        OUTPUT_DIR / "citation_reference_audit.csv",
    ]
    qc_rows = [
        {
            "round": 1,
            "focus": "evidence and data",
            "checks": "source CSV, summary tables and manuscript values are regenerated by one script",
            "status": "pass" if all(path.exists() for path in required_files[:4]) else "fail",
            "notes": "Synthetic wheat data only; biological claims remain bounded.",
        },
        {
            "round": 2,
            "focus": "citations and references",
            "checks": "all in-text citation keys map to reference entries and all entries are cited",
            "status": "pass" if cited == refs else "fail",
            "notes": f"{len(cited)} citation keys and {len(refs)} reference entries checked.",
        },
        {
            "round": 3,
            "focus": "language and claim scope",
            "checks": "no old model-organism label, no Chinese text, no unsupported cultivar or field-tolerance claim",
            "status": "pass"
            if ("generic model-plant placeholder" not in manuscript_text and not re.search(r"[\u4e00-\u9fff]", manuscript_text))
            else "fail",
            "notes": "Manuscript labels all references and data as synthetic.",
        },
        {
            "round": 4,
            "focus": "figure and visual style",
            "checks": "SVG exists, panels a-f are present, candy colors and premium grays are present",
            "status": "pass"
            if all(f">{letter}<" in svg_text for letter in "abcdef")
            and all(color in svg_text for color in ["#FFB3BA", "#BAE1FF", "#BAFFC9", "#F4F5F7", "#2F3437"])
            else "fail",
            "notes": "Editable SVG uses genotype candy colors on gray scaffold.",
        },
        {
            "round": 5,
            "focus": "format and package",
            "checks": "required files exist; abstract and Introduction lengths match manuscript-scale targets",
            "status": "pass" if all(path.exists() for path in required_files) and 220 <= abstract_words <= 280 and 900 <= intro_words <= 1500 else "fail",
            "notes": f"Abstract {abstract_words} words; Introduction {intro_words} words.",
        },
    ]
    write_csv(QC_DIR / "qc_results.csv", ["round", "focus", "checks", "status", "notes"], qc_rows)
    report = ["# Five-Pass QC Report", ""]
    for row in qc_rows:
        report.extend(
            [
                f"## Round {row['round']}. {row['focus'].title()}",
                "",
                f"- Checks: {row['checks']}",
                f"- Status: {row['status']}",
                f"- Notes: {row['notes']}",
                "",
            ]
        )
    (QC_DIR / "five_pass_qc_report.md").write_text("\n".join(report), encoding="utf-8")


def write_reviewer_risk() -> None:
    (OUTPUT_DIR / "reviewer_risk_audit.md").write_text(
        """# Reviewer-Risk Audit

| risk | severity | scope | mitigation in demo | required action for real manuscript |
|---|---|---|---|---|
| Synthetic data mistaken for biology | high | evidence | every output labels data as synthetic | replace with verified project data |
| 200-paper literature gate not actually run | high | literature | literature status file states limitation | run real search and full-text reading matrix |
| Screening ranking overclaimed as tolerance | high | interpretation | manuscript blocks mechanism and field claims | add validation before stronger claims |
| Figure style too informal | medium | visual | candy colors are constrained by premium gray | check journal style and grayscale readability |
| QC treated as final peer review | medium | package | five-pass QC records scope and limitations | add author, statistician and journal-specific review |
""",
        encoding="utf-8",
    )


def write_manifest() -> None:
    (OUTPUT_DIR / "package_manifest.md").write_text(
        """# Package Manifest

| file | purpose |
|---|---|
| `input/synthetic_wheat_germination_data.csv` | synthetic raw-style wheat germination input |
| `scripts/build_demo.py` | reproducible demo generation script |
| `output/source_data_figure1.csv` | source data for time-course figure panels |
| `output/supplementary_table_s1_summary.csv` | endpoint, length and vigor summaries |
| `output/figures/figure1_composite.svg` | editable candy-color plus premium-gray composite figure |
| `output/manuscript_draft.md` | manuscript-scale draft generated from the synthetic demo |
| `output/citation_reference_audit.csv` | citation-reference matching audit |
| `output/qc/five_pass_qc_report.md` | text, language, image and format checks |
| `output/qc/qc_results.csv` | machine-readable five-pass QC result table |

## Privacy Result

- No real research data included.
- No local absolute paths included.
- No private names, tokens or credentials included.
- Real 200-paper full-text literature review not claimed.
""",
        encoding="utf-8",
    )


def main() -> None:
    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    QC_DIR.mkdir(parents=True, exist_ok=True)

    records = raw_records()
    write_csv(
        INPUT_DIR / "synthetic_wheat_germination_data.csv",
        ["genotype", "treatment", "replicate", "total_seeds", *DAYS, "day7_root_length_cm", "day7_shoot_length_cm"],
        records,
    )
    source_rows, endpoint_rows, endpoints = summarize(records)
    write_csv(
        OUTPUT_DIR / "source_data_figure1.csv",
        ["genotype", "treatment", "day", "germination_mean_pct", "germination_sd_pct", "n_biological_replicates"],
        source_rows,
    )
    write_csv(
        OUTPUT_DIR / "supplementary_table_s1_summary.csv",
        [
            "genotype",
            "treatment",
            "day7_germination_mean_pct",
            "day7_germination_sd_pct",
            "root_length_mean_cm",
            "root_length_sd_cm",
            "shoot_length_mean_cm",
            "shoot_length_sd_cm",
            "vigor_index_mean",
            "vigor_index_sd",
            "n_biological_replicates",
        ],
        endpoint_rows,
    )
    make_figure(endpoint_rows, source_rows, endpoints)
    draft = manuscript(endpoints)
    (OUTPUT_DIR / "manuscript_draft.md").write_text(draft, encoding="utf-8")
    write_literature_status()
    write_readme()
    write_supporting_files(endpoint_rows, endpoints)
    write_citation_audit(draft)
    write_qc(draft)
    write_reviewer_risk()
    write_manifest()
    print(f"Generated synthetic wheat demo at {ROOT}")


if __name__ == "__main__":
    main()
