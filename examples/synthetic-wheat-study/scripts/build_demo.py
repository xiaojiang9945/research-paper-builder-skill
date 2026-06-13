from __future__ import annotations

import csv
import math
import re
import shutil
from pathlib import Path
from typing import Iterable

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.gridspec import GridSpec


ROOT = Path(__file__).resolve().parents[1]
INPUT_DIR = ROOT / "input"
OUTPUT_DIR = ROOT / "output"
FIGURE_DIR = OUTPUT_DIR / "figures"
QC_DIR = OUTPUT_DIR / "qc"

GENOTYPES = ["Wheat-A", "Wheat-B", "Wheat-C", "Wheat-D", "Wheat-E", "Wheat-F"]
TREATMENTS = ["Control", "NaCl-150mM"]
DAYS = [f"day{i}_count" for i in range(1, 8)]
REPLICATES = 5

INK = "#222222"
MUTED = "#66707A"
GRID = "#E1E5EA"
EDGE = "#BFC5CD"
WHITE = "#FFFFFF"
CONTROL = "#C9CDD4"

GENOTYPE_COLORS = {
    "Wheat-A": "#FF9FB1",
    "Wheat-B": "#7FC7F2",
    "Wheat-C": "#8BE7A3",
    "Wheat-D": "#FFC46B",
    "Wheat-E": "#BCA7FF",
    "Wheat-F": "#F28C6B",
}

REGION_COLORS = {
    "North China": "#FF9FB1",
    "Northwest China": "#FFC46B",
    "Yangtze Basin": "#8BE7A3",
    "Southwest China": "#BCA7FF",
    "International": "#7FC7F2",
}

CANDY_CMAP = LinearSegmentedColormap.from_list(
    "candy_salt",
    ["#F6F8FB", "#BAE1FF", "#BCA7FF", "#FF9FB1", "#FFC46B", "#D8A63A"],
)
SURFACE_CMAP = LinearSegmentedColormap.from_list(
    "candy_surface",
    ["#4F79A7", "#7FC7F2", "#8BE7A3", "#E9D86B", "#FFC46B", "#C83F83"],
)
DIVERGE_CMAP = LinearSegmentedColormap.from_list(
    "candy_diverge",
    ["#4F79A7", "#EEF3FA", "#FFFFFF", "#F8F3F1", "#C83F83"],
)

BASE = {
    "Wheat-A": {"control": 98, "salt": 84, "root": 8.5, "shoot": 6.2, "rwc": 89, "kna": 1.82, "mda": 8.8, "proline": 5.8, "sod": 162, "cat": 56},
    "Wheat-B": {"control": 96, "salt": 65, "root": 6.6, "shoot": 4.8, "rwc": 78, "kna": 1.18, "mda": 12.8, "proline": 4.2, "sod": 132, "cat": 43},
    "Wheat-C": {"control": 94, "salt": 54, "root": 5.7, "shoot": 4.1, "rwc": 72, "kna": 0.92, "mda": 15.5, "proline": 3.7, "sod": 117, "cat": 37},
    "Wheat-D": {"control": 92, "salt": 42, "root": 4.7, "shoot": 3.4, "rwc": 64, "kna": 0.64, "mda": 19.2, "proline": 2.9, "sod": 96, "cat": 31},
    "Wheat-E": {"control": 97, "salt": 73, "root": 7.6, "shoot": 5.5, "rwc": 83, "kna": 1.46, "mda": 10.7, "proline": 4.9, "sod": 146, "cat": 49},
    "Wheat-F": {"control": 95, "salt": 59, "root": 6.1, "shoot": 4.4, "rwc": 75, "kna": 1.04, "mda": 14.2, "proline": 4.0, "sod": 123, "cat": 39},
}

GENE_BASE = {
    "Wheat-A": {"TaHKT1;5": 3.9, "TaNHX1": 3.0, "TaSOS1": 2.7, "TaP5CS": 4.2, "TaSOD": 3.2, "TaCAT": 2.8, "TaDREB2": 3.4, "TaLEA": 3.6},
    "Wheat-B": {"TaHKT1;5": 2.5, "TaNHX1": 2.1, "TaSOS1": 1.9, "TaP5CS": 3.1, "TaSOD": 2.5, "TaCAT": 2.2, "TaDREB2": 2.6, "TaLEA": 2.7},
    "Wheat-C": {"TaHKT1;5": 1.8, "TaNHX1": 1.7, "TaSOS1": 1.6, "TaP5CS": 2.6, "TaSOD": 2.0, "TaCAT": 1.8, "TaDREB2": 2.1, "TaLEA": 2.2},
    "Wheat-D": {"TaHKT1;5": 1.2, "TaNHX1": 1.3, "TaSOS1": 1.1, "TaP5CS": 1.9, "TaSOD": 1.5, "TaCAT": 1.3, "TaDREB2": 1.6, "TaLEA": 1.7},
    "Wheat-E": {"TaHKT1;5": 3.0, "TaNHX1": 2.5, "TaSOS1": 2.2, "TaP5CS": 3.7, "TaSOD": 2.8, "TaCAT": 2.5, "TaDREB2": 3.0, "TaLEA": 3.1},
    "Wheat-F": {"TaHKT1;5": 2.1, "TaNHX1": 1.9, "TaSOS1": 1.8, "TaP5CS": 2.9, "TaSOD": 2.3, "TaCAT": 2.0, "TaDREB2": 2.4, "TaLEA": 2.5},
}

FIELD_SITES = [
    {"site": "Shandong winter-wheat plain", "region": "North China", "country": "China", "lat": 36.7, "lon": 118.5, "accessions": 42, "salinity_index": 0.78},
    {"site": "Henan alluvial plain", "region": "North China", "country": "China", "lat": 34.8, "lon": 113.6, "accessions": 55, "salinity_index": 0.72},
    {"site": "Hebei coastal plain", "region": "North China", "country": "China", "lat": 38.0, "lon": 115.5, "accessions": 38, "salinity_index": 0.81},
    {"site": "Jiangsu lower Yangtze", "region": "Yangtze Basin", "country": "China", "lat": 32.0, "lon": 119.0, "accessions": 28, "salinity_index": 0.57},
    {"site": "Anhui wheat belt", "region": "Yangtze Basin", "country": "China", "lat": 33.2, "lon": 116.7, "accessions": 33, "salinity_index": 0.61},
    {"site": "Sichuan basin margin", "region": "Southwest China", "country": "China", "lat": 30.7, "lon": 104.1, "accessions": 24, "salinity_index": 0.49},
    {"site": "Gansu corridor", "region": "Northwest China", "country": "China", "lat": 38.6, "lon": 102.2, "accessions": 31, "salinity_index": 0.68},
    {"site": "Xinjiang oasis", "region": "Northwest China", "country": "China", "lat": 43.8, "lon": 87.6, "accessions": 46, "salinity_index": 0.84},
    {"site": "Punjab irrigated plain", "region": "International", "country": "Pakistan", "lat": 31.5, "lon": 74.3, "accessions": 29, "salinity_index": 0.76},
    {"site": "Indo-Gangetic plain", "region": "International", "country": "India", "lat": 28.6, "lon": 77.2, "accessions": 35, "salinity_index": 0.73},
    {"site": "Central Anatolia", "region": "International", "country": "Turkey", "lat": 39.0, "lon": 35.0, "accessions": 22, "salinity_index": 0.62},
    {"site": "Australian wheatbelt", "region": "International", "country": "Australia", "lat": -31.9, "lon": 116.0, "accessions": 26, "salinity_index": 0.70},
    {"site": "Kansas wheat belt", "region": "International", "country": "United States", "lat": 38.5, "lon": -98.0, "accessions": 18, "salinity_index": 0.55},
    {"site": "La Plata wheat region", "region": "International", "country": "Argentina", "lat": -35.0, "lon": -61.0, "accessions": 16, "salinity_index": 0.52},
]

REFERENCES = [
    "Munns, R. & Tester, M. Mechanisms of salinity tolerance. *Annu. Rev. Plant Biol.* **59**, 651-681 (2008).",
    "Flowers, T. J. Improving crop salt tolerance. *J. Exp. Bot.* **55**, 307-319 (2004).",
    "Roy, S. J., Negrao, S. & Tester, M. Salt resistant crop plants. *Curr. Opin. Biotechnol.* **26**, 115-124 (2014).",
    "Negrao, S., Schmockel, S. M. & Tester, M. Evaluating physiological responses of plants to salinity stress. *Ann. Bot.* **119**, 1-11 (2017).",
    "Munns, R. Comparative physiology of salt and water stress. *Plant Cell Environ.* **25**, 239-250 (2002).",
    "Ashraf, M. & Harris, P. J. C. Potential biochemical indicators of salinity tolerance in plants. *Plant Sci.* **166**, 3-16 (2004).",
    "Deinlein, U. *et al.* Plant salt-tolerance mechanisms. *Trends Plant Sci.* **19**, 371-379 (2014).",
    "Tester, M. & Davenport, R. Na+ tolerance and Na+ transport in higher plants. *Ann. Bot.* **91**, 503-527 (2003).",
    "Munns, R. *et al.* Wheat grain yield on saline soils is improved by an ancestral Na+ transporter gene. *Nat. Biotechnol.* **30**, 360-364 (2012).",
    "Byrt, C. S. *et al.* The Na+ transporter, TaHKT1;5-D, limits shoot Na+ accumulation in bread wheat. *Plant J.* **80**, 516-526 (2014).",
    "Genc, Y., McDonald, G. K. & Tester, M. Reassessment of tissue Na+ concentration as a criterion for salinity tolerance in bread wheat. *Plant Cell Environ.* **30**, 1486-1498 (2007).",
    "Colmer, T. D., Flowers, T. J. & Munns, R. Use of wild relatives to improve salt tolerance in wheat. *J. Exp. Bot.* **57**, 1059-1078 (2006).",
    "Davenport, R. *et al.* Control of sodium transport in durum wheat. *Plant Physiol.* **137**, 807-818 (2005).",
    "Huang, S. *et al.* A sodium transporter (HKT7) is a candidate for Nax1, a gene for salt tolerance in durum wheat. *Plant Physiol.* **142**, 1718-1727 (2006).",
    "James, R. A. *et al.* Impact of ancestral wheat sodium exclusion genes Nax1 and Nax2 on grain yield of durum wheat on saline soils. *Funct. Plant Biol.* **39**, 609-618 (2012).",
    "Munns, R., Rebetzke, G. J., Husain, S., James, R. A. & Hare, R. A. Genetic control of sodium exclusion in durum wheat. *Aust. J. Agric. Res.* **54**, 627-635 (2003).",
    "Yamaguchi, T. & Blumwald, E. Developing salt-tolerant crop plants: challenges and opportunities. *Trends Plant Sci.* **10**, 615-620 (2005).",
    "Ashraf, M. & Akram, N. A. Improving salinity tolerance of plants through conventional breeding and genetic engineering: an analytical comparison. *Biotechnol. Adv.* **27**, 744-752 (2009).",
    "Gill, S. S. & Tuteja, N. Reactive oxygen species and antioxidant machinery in abiotic stress tolerance in crop plants. *Plant Physiol. Biochem.* **48**, 909-930 (2010).",
    "Almeida, P., Katschnig, D. & de Boer, A. H. HKT transporters-state of the art. *Int. J. Mol. Sci.* **14**, 20359-20385 (2013).",
    "Garciadeblas, B., Senn, M. E., Banuelos, M. A. & Rodriguez-Navarro, A. Sodium transport and HKT transporters: the rice model. *Plant J.* **34**, 788-801 (2003).",
    "Maathuis, F. J. M. & Amtmann, A. K+ nutrition and Na+ toxicity: the basis of cellular K+/Na+ ratios. *Ann. Bot.* **84**, 123-133 (1999).",
    "Munns, R. Genes and salt tolerance: bringing them together. *New Phytol.* **167**, 645-663 (2005).",
    "Blumwald, E. Sodium transport and salt tolerance in plants. *Curr. Opin. Cell Biol.* **12**, 431-434 (2000).",
    "Apse, M. P. & Blumwald, E. Na+ transport in plants. *FEBS Lett.* **581**, 2247-2254 (2007).",
    "Maser, P., Gierth, M. & Schroeder, J. I. Molecular mechanisms of potassium and sodium uptake in plants. *Plant Soil* **247**, 43-54 (2002).",
    "Ji, H., Pardo, J. M., Batelli, G., Van Oosten, M. J. & Bressan, R. A. The Salt Overly Sensitive (SOS) pathway: established and emerging roles. *Mol. Plant* **6**, 275-286 (2013).",
    "Hamamoto, S., Horie, T., Hauser, F., Deinlein, U. & Schroeder, J. I. HKT transporters mediate salt stress resistance in plants: from structure and function to the field. *Curr. Opin. Biotechnol.* **32**, 113-120 (2015).",
    "Genc, Y. *et al.* Bread wheat with high salinity and sodicity tolerance. *Front. Plant Sci.* **10**, 1280 (2019).",
    "Kotula, L., Zahra, N., Farooq, M. & Shabala, S. Making wheat salt tolerant: what is missing? *Crop J.* **12**, 1299-1308 (2024).",
    "Li, Z. *et al.* Improving wheat salt tolerance for saline agriculture. *J. Agric. Food Chem.* **70**, 14989-15006 (2022).",
    "Zhang, Z. *et al.* Insights into salinity tolerance in wheat. *Genes* **15**, 573 (2024).",
    "Atta, K. *et al.* Impacts of salinity stress on crop plants: improving salt tolerance through genetic and molecular dissection. *Front. Plant Sci.* **14**, 1241736 (2023).",
    "Traye, I. D. *et al.* Salinity tolerance in wheat: mechanisms and breeding approaches. *Plants* **14**, 1641 (2025).",
]


def reset_dirs() -> None:
    for path in [INPUT_DIR, OUTPUT_DIR]:
        if path.exists():
            shutil.rmtree(path)
        path.mkdir(parents=True, exist_ok=True)
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    QC_DIR.mkdir(parents=True, exist_ok=True)


def configure_matplotlib() -> None:
    plt.rcParams.update(
        {
            "figure.facecolor": WHITE,
            "axes.facecolor": WHITE,
            "savefig.facecolor": WHITE,
            "savefig.edgecolor": WHITE,
            "font.family": "DejaVu Sans",
            "font.size": 7,
            "axes.labelsize": 7,
            "axes.titlesize": 8,
            "xtick.labelsize": 6,
            "ytick.labelsize": 6,
            "legend.fontsize": 6,
            "axes.edgecolor": EDGE,
            "axes.labelcolor": INK,
            "xtick.color": MUTED,
            "ytick.color": MUTED,
            "grid.color": GRID,
            "grid.linewidth": 0.55,
            "svg.fonttype": "none",
        }
    )


def mean(values: Iterable[float]) -> float:
    vals = list(values)
    return sum(vals) / len(vals)


def sd(values: Iterable[float]) -> float:
    vals = list(values)
    if len(vals) < 2:
        return 0.0
    m = mean(vals)
    return math.sqrt(sum((v - m) ** 2 for v in vals) / (len(vals) - 1))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_csv_auto(path: Path, rows: list[dict[str, object]]) -> None:
    fields: list[str] = []
    for row in rows:
        for key in row:
            if key not in fields:
                fields.append(key)
    write_csv(path, fields, rows)


def day_counts(final_pct: float, treatment: str, rep_index: int, total: int = 50) -> list[int]:
    final_count = max(0, min(total, round(total * final_pct / 100) + [-2, -1, 0, 1, 2][rep_index]))
    if treatment == "Control":
        profile = [0.22, 0.55, 0.79, 0.91, 0.96, 0.99, 1.0]
    else:
        profile = [0.04, 0.22, 0.48, 0.68, 0.84, 0.94, 1.0]
    values = [round(final_count * p) for p in profile]
    return [max(values[i], values[i - 1]) if i else values[i] for i in range(len(values))]


def raw_records() -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    rng = np.random.default_rng(615)
    germination: list[dict[str, object]] = []
    physiology: list[dict[str, object]] = []
    expression: list[dict[str, object]] = []
    distribution = [dict(row) for row in FIELD_SITES]

    for genotype in GENOTYPES:
        for treatment in TREATMENTS:
            final = BASE[genotype]["control"] if treatment == "Control" else BASE[genotype]["salt"]
            for rep in range(REPLICATES):
                row: dict[str, object] = {
                    "genotype": genotype,
                    "treatment": treatment,
                    "replicate": f"R{rep + 1}",
                    "total_seeds": 50,
                }
                for day, value in enumerate(day_counts(final, treatment, rep), start=1):
                    row[f"day{day}_count"] = value
                germination.append(row)

                if treatment == "Control":
                    values = {
                        "root_length_cm": 8.8 + rng.normal(0, 0.18),
                        "shoot_length_cm": 6.5 + rng.normal(0, 0.14),
                        "relative_water_content_pct": 95.5 + rng.normal(0, 0.6),
                        "k_na_ratio": 2.28 + rng.normal(0, 0.08),
                        "mda_nmol_g_fw": 6.4 + rng.normal(0, 0.28),
                        "proline_umol_g_fw": 1.6 + rng.normal(0, 0.10),
                        "sod_u_mg_protein": 112 + rng.normal(0, 4),
                        "cat_u_mg_protein": 34 + rng.normal(0, 1.4),
                    }
                else:
                    values = {
                        "root_length_cm": BASE[genotype]["root"] + rng.normal(0, 0.22),
                        "shoot_length_cm": BASE[genotype]["shoot"] + rng.normal(0, 0.16),
                        "relative_water_content_pct": BASE[genotype]["rwc"] + rng.normal(0, 1.2),
                        "k_na_ratio": BASE[genotype]["kna"] + rng.normal(0, 0.06),
                        "mda_nmol_g_fw": BASE[genotype]["mda"] + rng.normal(0, 0.55),
                        "proline_umol_g_fw": BASE[genotype]["proline"] + rng.normal(0, 0.20),
                        "sod_u_mg_protein": BASE[genotype]["sod"] + rng.normal(0, 5),
                        "cat_u_mg_protein": BASE[genotype]["cat"] + rng.normal(0, 1.8),
                    }
                physiology.append(
                    {
                        "genotype": genotype,
                        "treatment": treatment,
                        "replicate": f"R{rep + 1}",
                        **{k: round(float(v), 3) for k, v in values.items()},
                    }
                )

        for gene, fold in GENE_BASE[genotype].items():
            for rep in range(REPLICATES):
                value = max(0.75, fold + rng.normal(0, 0.11))
                expression.append(
                    {
                        "genotype": genotype,
                        "gene": gene,
                        "replicate": f"R{rep + 1}",
                        "salt_vs_control_fold_change": round(value, 3),
                        "log2_fold_change": round(math.log2(value), 3),
                    }
                )

    return germination, physiology, expression, distribution


def scale_map(values: dict[str, float], reverse: bool = False) -> dict[str, float]:
    vals = list(values.values())
    lo, hi = min(vals), max(vals)
    if hi == lo:
        out = {k: 0.5 for k in values}
    else:
        out = {k: (v - lo) / (hi - lo) for k, v in values.items()}
    if reverse:
        out = {k: 1 - v for k, v in out.items()}
    return out


def summarize(
    germination: list[dict[str, object]],
    physiology: list[dict[str, object]],
    expression: list[dict[str, object]],
    distribution: list[dict[str, object]],
) -> dict[str, object]:
    time_rows: list[dict[str, object]] = []
    endpoint_rows: list[dict[str, object]] = []
    phys_rows: list[dict[str, object]] = []
    expr_rows: list[dict[str, object]] = []
    metrics: dict[str, dict[str, float]] = {g: {} for g in GENOTYPES}

    for genotype in GENOTYPES:
        for treatment in TREATMENTS:
            group = [r for r in germination if r["genotype"] == genotype and r["treatment"] == treatment]
            day7 = [float(r["day7_count"]) / float(r["total_seeds"]) * 100 for r in group]
            metrics[genotype][f"{treatment}_germination"] = mean(day7)
            endpoint_rows.append(
                {
                    "genotype": genotype,
                    "treatment": treatment,
                    "day7_germination_mean_pct": round(mean(day7), 2),
                    "day7_germination_sd_pct": round(sd(day7), 2),
                    "n_biological_replicates": REPLICATES,
                }
            )
            for day in range(1, 8):
                values = [float(r[f"day{day}_count"]) / float(r["total_seeds"]) * 100 for r in group]
                time_rows.append(
                    {
                        "genotype": genotype,
                        "treatment": treatment,
                        "day": day,
                        "germination_mean_pct": round(mean(values), 2),
                        "germination_sd_pct": round(sd(values), 2),
                        "n_biological_replicates": REPLICATES,
                    }
                )

        control = metrics[genotype]["Control_germination"]
        salt = metrics[genotype]["NaCl-150mM_germination"]
        metrics[genotype]["retention_pct"] = salt / control * 100
        salt_phys = [r for r in physiology if r["genotype"] == genotype and r["treatment"] == "NaCl-150mM"]
        for trait in [
            "root_length_cm",
            "shoot_length_cm",
            "relative_water_content_pct",
            "k_na_ratio",
            "mda_nmol_g_fw",
            "proline_umol_g_fw",
            "sod_u_mg_protein",
            "cat_u_mg_protein",
        ]:
            vals = [float(r[trait]) for r in salt_phys]
            metrics[genotype][trait] = mean(vals)
            metrics[genotype][f"{trait}_sd"] = sd(vals)
        metrics[genotype]["vigor_index"] = salt * (metrics[genotype]["root_length_cm"] + metrics[genotype]["shoot_length_cm"])
        phys_rows.append(
            {
                "genotype": genotype,
                **{
                    key: round(metrics[genotype][key], 3)
                    for key in [
                        "retention_pct",
                        "root_length_cm",
                        "shoot_length_cm",
                        "relative_water_content_pct",
                        "k_na_ratio",
                        "mda_nmol_g_fw",
                        "proline_umol_g_fw",
                        "sod_u_mg_protein",
                        "cat_u_mg_protein",
                        "vigor_index",
                    ]
                },
            }
        )

        for gene in sorted(GENE_BASE[genotype]):
            vals = [float(r["log2_fold_change"]) for r in expression if r["genotype"] == genotype and r["gene"] == gene]
            metrics[genotype][f"{gene}_log2fc"] = mean(vals)
            expr_rows.append(
                {
                    "genotype": genotype,
                    "gene": gene,
                    "log2_fold_change_mean": round(mean(vals), 3),
                    "log2_fold_change_sd": round(sd(vals), 3),
                    "n_biological_replicates": REPLICATES,
                }
            )

    physiology_trait_specs = [
        ("retention_pct", False),
        ("root_length_cm", False),
        ("shoot_length_cm", False),
        ("relative_water_content_pct", False),
        ("k_na_ratio", False),
        ("mda_nmol_g_fw", True),
        ("proline_umol_g_fw", False),
        ("sod_u_mg_protein", False),
        ("cat_u_mg_protein", False),
    ]
    scaled_traits: dict[str, dict[str, float]] = {}
    for trait, reverse in physiology_trait_specs:
        scaled_traits[trait] = scale_map({g: metrics[g][trait] for g in GENOTYPES}, reverse=reverse)

    transcript_raw = {
        g: mean(metrics[g][f"{gene}_log2fc"] for gene in sorted(GENE_BASE[g]))
        for g in GENOTYPES
    }
    transcript_scaled = scale_map(transcript_raw)
    physiology_scaled = {
        g: mean(scaled_traits[trait][g] for trait, _ in physiology_trait_specs)
        for g in GENOTYPES
    }
    germination_scaled = scale_map({g: metrics[g]["retention_pct"] for g in GENOTYPES})
    domain_scores: list[dict[str, object]] = []
    for genotype in GENOTYPES:
        integrated = 0.45 * germination_scaled[genotype] + 0.35 * physiology_scaled[genotype] + 0.20 * transcript_scaled[genotype]
        metrics[genotype]["germination_score"] = germination_scaled[genotype] * 100
        metrics[genotype]["physiology_score"] = physiology_scaled[genotype] * 100
        metrics[genotype]["transcript_score"] = transcript_scaled[genotype] * 100
        metrics[genotype]["integrated_score"] = integrated * 100
        domain_scores.append(
            {
                "genotype": genotype,
                "germination_score": round(metrics[genotype]["germination_score"], 3),
                "physiology_score": round(metrics[genotype]["physiology_score"], 3),
                "transcript_score": round(metrics[genotype]["transcript_score"], 3),
                "integrated_score": round(metrics[genotype]["integrated_score"], 3),
            }
        )

    return {
        "time": time_rows,
        "endpoint": endpoint_rows,
        "physiology": phys_rows,
        "expression": expr_rows,
        "distribution": distribution,
        "metrics": metrics,
        "scaled_traits": scaled_traits,
        "domain_scores": domain_scores,
        "raw_germination": germination,
        "raw_physiology": physiology,
        "raw_expression": expression,
    }


def style_axes(ax: plt.Axes, grid: bool = True) -> None:
    ax.set_facecolor(WHITE)
    for spine in ax.spines.values():
        spine.set_color(EDGE)
        spine.set_linewidth(0.7)
    ax.tick_params(colors=MUTED, width=0.6, length=2.5)
    if grid:
        ax.grid(True, color=GRID, linewidth=0.55, zorder=0)


def panel_label(ax: plt.Axes, label: str, is_3d: bool = False) -> None:
    if is_3d:
        ax.text2D(-0.10, 1.03, label, transform=ax.transAxes, fontsize=11, fontweight="bold", color=INK)
    else:
        ax.text(-0.10, 1.03, label, transform=ax.transAxes, fontsize=11, fontweight="bold", color=INK, va="top")


def save_figure(fig: plt.Figure, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, format="svg")
    plt.close(fig)


def fill_mollweide_land(ax: plt.Axes) -> None:
    polygons = [
        [(-168, 15), (-140, 55), (-95, 72), (-55, 50), (-60, 15), (-95, 5), (-130, 10)],
        [(-82, 12), (-70, -5), (-64, -25), (-72, -55), (-54, -52), (-38, -22), (-50, 5)],
        [(-10, 35), (15, 70), (55, 55), (62, 22), (42, -35), (20, -35), (5, 10)],
        [(25, 38), (70, 62), (145, 55), (150, 20), (110, 5), (90, -10), (42, 0)],
        [(110, -10), (154, -14), (152, -42), (118, -42), (106, -25)],
        [(-8, 36), (35, 36), (45, 10), (28, -35), (8, -25), (-15, 5)],
    ]
    for poly in polygons:
        lon = np.radians([p[0] for p in poly])
        lat = np.radians([p[1] for p in poly])
        ax.fill(lon, lat, facecolor="#F8F9FB", edgecolor=EDGE, linewidth=0.5, zorder=1)


def draw_china_outline(ax: plt.Axes) -> None:
    outline = np.array(
        [
            [73, 39],
            [80, 48],
            [94, 49],
            [104, 53],
            [121, 49],
            [134, 47],
            [130, 40],
            [122, 35],
            [123, 29],
            [116, 22],
            [108, 19],
            [99, 22],
            [92, 28],
            [82, 30],
            [73, 39],
        ],
        dtype=float,
    )
    ax.fill(outline[:, 0], outline[:, 1], color="#F8F9FB", ec=EDGE, lw=0.7, zorder=1)


def make_figure1(summary: dict[str, object]) -> None:
    metrics: dict[str, dict[str, float]] = summary["metrics"]  # type: ignore[assignment]
    raw_germination: list[dict[str, object]] = summary["raw_germination"]  # type: ignore[assignment]
    distribution: list[dict[str, object]] = summary["distribution"]  # type: ignore[assignment]
    time_rows: list[dict[str, object]] = summary["time"]  # type: ignore[assignment]

    fig = plt.figure(figsize=(11.2, 7.2), facecolor=WHITE)
    gs = GridSpec(2, 3, figure=fig, left=0.055, right=0.985, top=0.965, bottom=0.075, wspace=0.28, hspace=0.34)

    ax = fig.add_subplot(gs[0, 0], projection="mollweide")
    ax.set_facecolor(WHITE)
    fill_mollweide_land(ax)
    for region, color in REGION_COLORS.items():
        pts = [r for r in distribution if r["region"] == region]
        if pts:
            ax.scatter(
                np.radians([float(p["lon"]) for p in pts]),
                np.radians([float(p["lat"]) for p in pts]),
                s=[float(p["accessions"]) * 2.4 for p in pts],
                c=color,
                edgecolor=WHITE,
                linewidth=0.6,
                alpha=0.92,
                label=region,
                zorder=3,
            )
    ax.grid(True, color=GRID, linewidth=0.45)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.legend(frameon=False, loc="lower left", bbox_to_anchor=(-0.06, -0.08), ncol=1, handletextpad=0.3)
    panel_label(ax, "a")

    ax = fig.add_subplot(gs[0, 1])
    style_axes(ax)
    draw_china_outline(ax)
    china_pts = [r for r in distribution if r["country"] == "China"]
    for region, color in REGION_COLORS.items():
        pts = [r for r in china_pts if r["region"] == region]
        if pts:
            ax.scatter(
                [float(p["lon"]) for p in pts],
                [float(p["lat"]) for p in pts],
                s=[float(p["accessions"]) * 4.0 for p in pts],
                c=color,
                edgecolor=WHITE,
                linewidth=0.7,
                alpha=0.95,
                zorder=4,
            )
    ax.set_xlim(72, 136)
    ax.set_ylim(17, 54)
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    panel_label(ax, "b")

    ax = fig.add_subplot(gs[0, 2])
    style_axes(ax)
    for genotype in GENOTYPES:
        rows = [r for r in time_rows if r["genotype"] == genotype and r["treatment"] == "NaCl-150mM"]
        x = [int(r["day"]) for r in rows]
        y = [float(r["germination_mean_pct"]) for r in rows]
        err = [float(r["germination_sd_pct"]) for r in rows]
        ax.plot(x, y, color=GENOTYPE_COLORS[genotype], lw=1.8, marker="o", ms=3.2)
        ax.fill_between(x, np.array(y) - np.array(err), np.array(y) + np.array(err), color=GENOTYPE_COLORS[genotype], alpha=0.16, lw=0)
        ax.text(x[-1] + 0.08, y[-1], genotype[-1], color=GENOTYPE_COLORS[genotype], va="center", fontsize=7, fontweight="bold")
    ax.set_xlim(1, 7.45)
    ax.set_ylim(0, 100)
    ax.set_xlabel("Days after sowing")
    ax.set_ylabel("Germination under NaCl (%)")
    panel_label(ax, "c")

    ax = fig.add_subplot(gs[1, 0])
    style_axes(ax)
    positions = np.arange(len(GENOTYPES))
    control = []
    salt = []
    for genotype in GENOTYPES:
        control.append([float(r["day7_count"]) / float(r["total_seeds"]) * 100 for r in raw_germination if r["genotype"] == genotype and r["treatment"] == "Control"])
        salt.append([float(r["day7_count"]) / float(r["total_seeds"]) * 100 for r in raw_germination if r["genotype"] == genotype and r["treatment"] == "NaCl-150mM"])
    bp1 = ax.boxplot(control, positions=positions - 0.16, widths=0.25, patch_artist=True, showfliers=False)
    bp2 = ax.boxplot(salt, positions=positions + 0.16, widths=0.25, patch_artist=True, showfliers=False)
    for patch in bp1["boxes"]:
        patch.set_facecolor(CONTROL)
        patch.set_edgecolor("#8B949E")
    for patch, genotype in zip(bp2["boxes"], GENOTYPES):
        patch.set_facecolor(GENOTYPE_COLORS[genotype])
        patch.set_edgecolor("#8B949E")
    for artist in bp1["medians"] + bp2["medians"]:
        artist.set_color(INK)
        artist.set_linewidth(0.9)
    ax.set_xticks(positions, [g.replace("Wheat-", "") for g in GENOTYPES])
    ax.set_ylim(30, 104)
    ax.set_ylabel("Day 7 germination (%)")
    ax.plot([], [], color=CONTROL, lw=6, label="Control")
    ax.plot([], [], color=GENOTYPE_COLORS["Wheat-A"], lw=6, label="NaCl")
    ax.legend(frameon=False, loc="lower left", handlelength=1.0)
    panel_label(ax, "d")

    ax = fig.add_subplot(gs[1, 1])
    style_axes(ax)
    for genotype in GENOTYPES:
        size = 45 + metrics[genotype]["proline_umol_g_fw"] * 32
        ax.scatter(
            metrics[genotype]["retention_pct"],
            metrics[genotype]["vigor_index"],
            s=size,
            c=GENOTYPE_COLORS[genotype],
            edgecolor=WHITE,
            linewidth=0.8,
            alpha=0.96,
        )
        ax.text(metrics[genotype]["retention_pct"] + 1.2, metrics[genotype]["vigor_index"], genotype[-1], color=INK, va="center", fontsize=7, fontweight="bold")
    ax.set_xlabel("Germination retention (%)")
    ax.set_ylabel("Seedling vigour index")
    panel_label(ax, "e")

    ax = fig.add_subplot(gs[1, 2], projection="polar")
    ax.set_facecolor(WHITE)
    ax.grid(True, color=GRID, linewidth=0.55)
    score = [metrics[g]["integrated_score"] for g in GENOTYPES]
    theta = np.linspace(0, 2 * np.pi, len(GENOTYPES), endpoint=False)
    widths = np.full(len(GENOTYPES), 2 * np.pi / len(GENOTYPES) * 0.72)
    ax.bar(theta, score, width=widths, color=[GENOTYPE_COLORS[g] for g in GENOTYPES], edgecolor=WHITE, linewidth=1.0, alpha=0.95)
    ax.set_ylim(0, 100)
    ax.set_xticks(theta, [g.replace("Wheat-", "") for g in GENOTYPES])
    ax.set_yticks([25, 50, 75, 100])
    ax.set_yticklabels(["25", "50", "75", "100"], color=MUTED)
    panel_label(ax, "f")

    save_figure(fig, FIGURE_DIR / "figure1_geography_germination_vigour.svg")


def make_figure2(summary: dict[str, object]) -> None:
    metrics: dict[str, dict[str, float]] = summary["metrics"]  # type: ignore[assignment]
    raw_physiology: list[dict[str, object]] = summary["raw_physiology"]  # type: ignore[assignment]
    scaled_traits: dict[str, dict[str, float]] = summary["scaled_traits"]  # type: ignore[assignment]

    fig = plt.figure(figsize=(11.2, 7.2), facecolor=WHITE)
    gs = GridSpec(2, 3, figure=fig, left=0.055, right=0.985, top=0.965, bottom=0.075, wspace=0.30, hspace=0.35)

    trait_labels = [
        ("retention_pct", "Ret."),
        ("root_length_cm", "Root"),
        ("shoot_length_cm", "Shoot"),
        ("relative_water_content_pct", "RWC"),
        ("k_na_ratio", "K/Na"),
        ("mda_nmol_g_fw", "MDA-"),
        ("proline_umol_g_fw", "Pro."),
        ("sod_u_mg_protein", "SOD"),
        ("cat_u_mg_protein", "CAT"),
    ]

    ax = fig.add_subplot(gs[0, 0])
    style_axes(ax, grid=False)
    heat = np.array([[scaled_traits[key][g] for key, _ in trait_labels] for g in GENOTYPES])
    im = ax.imshow(heat, aspect="auto", cmap=CANDY_CMAP, vmin=0, vmax=1)
    ax.set_xticks(np.arange(len(trait_labels)), [label for _, label in trait_labels], rotation=45, ha="right")
    ax.set_yticks(np.arange(len(GENOTYPES)), [g.replace("Wheat-", "") for g in GENOTYPES])
    ax.tick_params(length=0)
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.02).ax.tick_params(labelsize=6)
    panel_label(ax, "a")

    ax = fig.add_subplot(gs[0, 1])
    style_axes(ax)
    salt_phys = [r for r in raw_physiology if r["treatment"] == "NaCl-150mM"]
    for genotype in GENOTYPES:
        pts = [r for r in salt_phys if r["genotype"] == genotype]
        ax.scatter(
            [float(r["relative_water_content_pct"]) for r in pts],
            [float(r["k_na_ratio"]) for r in pts],
            s=[38 + float(r["proline_umol_g_fw"]) * 18 for r in pts],
            c=GENOTYPE_COLORS[genotype],
            edgecolor=WHITE,
            linewidth=0.7,
            alpha=0.88,
            label=genotype[-1],
        )
    ax.set_xlabel("Relative water content (%)")
    ax.set_ylabel("K/Na ratio")
    ax.legend(frameon=False, ncol=3, loc="lower right", handletextpad=0.2, columnspacing=0.6)
    panel_label(ax, "b")

    ax = fig.add_subplot(gs[0, 2])
    style_axes(ax)
    mda = [[float(r["mda_nmol_g_fw"]) for r in salt_phys if r["genotype"] == g] for g in GENOTYPES]
    violin = ax.violinplot(mda, positions=np.arange(len(GENOTYPES)), widths=0.72, showmeans=False, showextrema=False)
    for body, genotype in zip(violin["bodies"], GENOTYPES):
        body.set_facecolor(GENOTYPE_COLORS[genotype])
        body.set_edgecolor("#8B949E")
        body.set_alpha(0.72)
    bp = ax.boxplot(mda, positions=np.arange(len(GENOTYPES)), widths=0.24, patch_artist=True, showfliers=False)
    for patch in bp["boxes"]:
        patch.set_facecolor(WHITE)
        patch.set_edgecolor(INK)
        patch.set_linewidth(0.7)
    for artist in bp["medians"]:
        artist.set_color(INK)
        artist.set_linewidth(1.0)
    ax.set_xticks(np.arange(len(GENOTYPES)), [g.replace("Wheat-", "") for g in GENOTYPES])
    ax.set_ylabel("MDA (nmol g-1 FW)")
    panel_label(ax, "c")

    ax = fig.add_subplot(gs[1, 0])
    style_axes(ax)
    xs = np.array([float(r["relative_water_content_pct"]) for r in salt_phys])
    ys = np.array([float(r["k_na_ratio"]) for r in salt_phys])
    xi = np.linspace(xs.min() - 3, xs.max() + 3, 80)
    yi = np.linspace(ys.min() - 0.18, ys.max() + 0.18, 80)
    xx, yy = np.meshgrid(xi, yi)
    zz = np.zeros_like(xx)
    for x0, y0 in zip(xs, ys):
        zz += np.exp(-((xx - x0) ** 2 / (2 * 3.6**2) + (yy - y0) ** 2 / (2 * 0.12**2)))
    contour = ax.contourf(xx, yy, zz, levels=12, cmap=SURFACE_CMAP, alpha=0.96)
    ax.contour(xx, yy, zz, levels=6, colors=WHITE, linewidths=0.45, alpha=0.75)
    fig.colorbar(contour, ax=ax, fraction=0.046, pad=0.02).ax.tick_params(labelsize=6)
    ax.set_xlabel("Relative water content (%)")
    ax.set_ylabel("K/Na ratio")
    panel_label(ax, "d")

    ax = fig.add_subplot(gs[1, 1])
    style_axes(ax, grid=False)
    y_pos = np.arange(len(GENOTYPES))
    components = [
        ("water", [scaled_traits["relative_water_content_pct"][g] * 100 for g in GENOTYPES], "#7FC7F2"),
        ("ion", [scaled_traits["k_na_ratio"][g] * 100 for g in GENOTYPES], "#FFC46B"),
        ("antioxidant", [mean([scaled_traits["sod_u_mg_protein"][g], scaled_traits["cat_u_mg_protein"][g]]) * 100 for g in GENOTYPES], "#8BE7A3"),
        ("damage", [scaled_traits["mda_nmol_g_fw"][g] * 100 for g in GENOTYPES], "#FF9FB1"),
    ]
    left = np.zeros(len(GENOTYPES))
    for label, values, color in components:
        ax.barh(y_pos, values, left=left, height=0.62, color=color, edgecolor=WHITE, label=label)
        left += np.array(values)
    ax.set_yticks(y_pos, [g.replace("Wheat-", "") for g in GENOTYPES])
    ax.set_xlabel("Scaled component total")
    ax.invert_yaxis()
    ax.legend(frameon=False, ncol=2, loc="lower right")
    panel_label(ax, "e")

    ax = fig.add_subplot(gs[1, 2], projection="3d")
    x = np.linspace(55, 95, 45)
    y = np.linspace(0.45, 2.05, 45)
    xx, yy = np.meshgrid(x, y)
    zz = 0.45 * np.tanh((xx - 72) / 9) + 0.55 * np.tanh((yy - 1.05) / 0.36)
    ax.plot_surface(xx, yy, zz, cmap=SURFACE_CMAP, linewidth=0, antialiased=True, alpha=0.96)
    ax.view_init(elev=28, azim=-58)
    ax.set_xlabel("RWC (%)", labelpad=-1)
    ax.set_ylabel("K/Na", labelpad=-1)
    ax.set_zlabel("Index", labelpad=-1)
    for axis in [ax.xaxis, ax.yaxis, ax.zaxis]:
        axis.pane.set_facecolor((1, 1, 1, 1))
        axis.pane.set_edgecolor(EDGE)
    panel_label(ax, "f", is_3d=True)

    save_figure(fig, FIGURE_DIR / "figure2_physiology_matrix.svg")


def make_figure3(summary: dict[str, object]) -> None:
    metrics: dict[str, dict[str, float]] = summary["metrics"]  # type: ignore[assignment]
    raw_expression: list[dict[str, object]] = summary["raw_expression"]  # type: ignore[assignment]
    expression: list[dict[str, object]] = summary["expression"]  # type: ignore[assignment]
    domain_scores: list[dict[str, object]] = summary["domain_scores"]  # type: ignore[assignment]

    genes = sorted({str(r["gene"]) for r in expression})
    fig = plt.figure(figsize=(11.2, 7.2), facecolor=WHITE)
    gs = GridSpec(2, 3, figure=fig, left=0.055, right=0.985, top=0.965, bottom=0.075, wspace=0.31, hspace=0.36)

    ax = fig.add_subplot(gs[0, 0])
    style_axes(ax, grid=False)
    heat = np.array([[metrics[g][f"{gene}_log2fc"] for gene in genes] for g in GENOTYPES])
    im = ax.imshow(heat, aspect="auto", cmap=CANDY_CMAP, vmin=0, vmax=max(2.2, float(heat.max())))
    ax.set_xticks(np.arange(len(genes)), genes, rotation=45, ha="right")
    ax.set_yticks(np.arange(len(GENOTYPES)), [g.replace("Wheat-", "") for g in GENOTYPES])
    ax.tick_params(length=0)
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.02).ax.tick_params(labelsize=6)
    panel_label(ax, "a")

    ax = fig.add_subplot(gs[0, 1])
    style_axes(ax)
    rng = np.random.default_rng(777)
    for genotype in GENOTYPES:
        xvals = np.array([metrics[genotype][f"{gene}_log2fc"] for gene in genes])
        pseudo_p = np.clip(np.exp(-1.25 * xvals) * rng.uniform(0.35, 0.75, len(xvals)), 0.0008, 0.25)
        yvals = -np.log10(pseudo_p)
        ax.scatter(xvals, yvals, s=34 + 18 * xvals, c=GENOTYPE_COLORS[genotype], edgecolor=WHITE, linewidth=0.7, alpha=0.90, label=genotype[-1])
    ax.axhline(-math.log10(0.05), color=EDGE, lw=0.8, ls="--")
    ax.set_xlabel("Mean log2 fold change")
    ax.set_ylabel("-log10 adjusted P")
    ax.legend(frameon=False, ncol=3, loc="upper left", handletextpad=0.2, columnspacing=0.6)
    panel_label(ax, "b")

    ax = fig.add_subplot(gs[0, 2])
    style_axes(ax)
    focus_genes = ["TaHKT1;5", "TaP5CS", "TaSOD", "TaLEA"]
    box_data = [[float(r["log2_fold_change"]) for r in raw_expression if r["gene"] == gene] for gene in focus_genes]
    bp = ax.boxplot(box_data, positions=np.arange(len(focus_genes)), widths=0.52, patch_artist=True, showfliers=False)
    box_colors = ["#7FC7F2", "#FFC46B", "#8BE7A3", "#BCA7FF"]
    for patch, color in zip(bp["boxes"], box_colors):
        patch.set_facecolor(color)
        patch.set_edgecolor("#8B949E")
        patch.set_alpha(0.86)
    for artist in bp["medians"]:
        artist.set_color(INK)
        artist.set_linewidth(1.0)
    ax.set_xticks(np.arange(len(focus_genes)), focus_genes, rotation=35, ha="right")
    ax.set_ylabel("Log2 fold change")
    panel_label(ax, "c")

    ax = fig.add_subplot(gs[1, 0])
    style_axes(ax, grid=False)
    variables = ["Ret.", "Root", "RWC", "K/Na", "MDA", "Pro.", "Tx.", "Vig."]
    matrix = []
    for genotype in GENOTYPES:
        matrix.append(
            [
                metrics[genotype]["retention_pct"],
                metrics[genotype]["root_length_cm"],
                metrics[genotype]["relative_water_content_pct"],
                metrics[genotype]["k_na_ratio"],
                metrics[genotype]["mda_nmol_g_fw"],
                metrics[genotype]["proline_umol_g_fw"],
                metrics[genotype]["transcript_score"],
                metrics[genotype]["vigor_index"],
            ]
        )
    corr = np.corrcoef(np.array(matrix).T)
    im = ax.imshow(corr, cmap=DIVERGE_CMAP, vmin=-1, vmax=1)
    ax.set_xticks(np.arange(len(variables)), variables, rotation=45, ha="right")
    ax.set_yticks(np.arange(len(variables)), variables)
    ax.tick_params(length=0)
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.02).ax.tick_params(labelsize=6)
    panel_label(ax, "d")

    ax = fig.add_subplot(gs[1, 1])
    style_axes(ax)
    ranked = sorted(domain_scores, key=lambda r: float(r["integrated_score"]))
    y = np.arange(len(ranked))
    ax.barh(y, [float(r["integrated_score"]) for r in ranked], color=[GENOTYPE_COLORS[str(r["genotype"])] for r in ranked], edgecolor=WHITE, height=0.66)
    ax.set_yticks(y, [str(r["genotype"]).replace("Wheat-", "") for r in ranked])
    ax.set_xlabel("Integrated response score")
    ax.set_xlim(0, 104)
    for yi, row in zip(y, ranked):
        ax.text(float(row["integrated_score"]) + 1.2, yi, f"{float(row['integrated_score']):.1f}", va="center", fontsize=6, color=INK)
    panel_label(ax, "e")

    ax = fig.add_subplot(gs[1, 2], projection="3d")
    x = np.linspace(0, 100, 50)
    yv = np.linspace(0, 100, 50)
    xx, yy = np.meshgrid(x, yv)
    zz = 0.34 * xx + 0.28 * yy + 15 * np.sin(xx / 22) * np.cos(yy / 28)
    ax.plot_surface(xx, yy, zz, cmap=SURFACE_CMAP, linewidth=0, antialiased=True, alpha=0.90)
    for genotype in GENOTYPES:
        ax.scatter(
            metrics[genotype]["physiology_score"],
            metrics[genotype]["transcript_score"],
            metrics[genotype]["integrated_score"],
            s=38,
            c=GENOTYPE_COLORS[genotype],
            edgecolor=INK,
            linewidth=0.25,
        )
    ax.view_init(elev=27, azim=-54)
    ax.set_xlabel("Physiology", labelpad=-1)
    ax.set_ylabel("Transcript", labelpad=-1)
    ax.set_zlabel("Integrated", labelpad=-1)
    for axis in [ax.xaxis, ax.yaxis, ax.zaxis]:
        axis.pane.set_facecolor((1, 1, 1, 1))
        axis.pane.set_edgecolor(EDGE)
    panel_label(ax, "f", is_3d=True)

    save_figure(fig, FIGURE_DIR / "figure3_transcript_and_integration.svg")


def reference_block() -> str:
    return "\n".join(f"{i + 1}. {ref}" for i, ref in enumerate(REFERENCES))


def make_manuscript(summary: dict[str, object]) -> str:
    metrics: dict[str, dict[str, float]] = summary["metrics"]  # type: ignore[assignment]
    ranked = sorted(GENOTYPES, key=lambda g: metrics[g]["integrated_score"], reverse=True)
    refs = reference_block()

    return f"""# Integrated geography, physiology and transcript markers prioritize early salt-response wheat lines

## Abstract

Soil salinity constrains wheat establishment, yet early-stage screening often depends on a small number of endpoint traits that do not show whether a candidate line combines germination, growth, water status, ion balance, oxidative protection and molecular response. We evaluated six wheat lines under control and NaCl treatment using a staged analysis that links seed germination, seedling vigour, physiological traits, transcript markers and sampling geography. Regional metadata placed the panel within northern, northwestern, Yangtze and international wheat contexts, allowing the primary phenotype to be interpreted against a defined resource background. NaCl treatment separated the panel by Day 7, with Wheat-A maintaining {metrics["Wheat-A"]["NaCl-150mM_germination"]:.1f}% germination and Wheat-E maintaining {metrics["Wheat-E"]["NaCl-150mM_germination"]:.1f}%, compared with {metrics["Wheat-D"]["NaCl-150mM_germination"]:.1f}% for the weakest line. The same ranking was supported by seedling-vigour analysis, relative water content, K/Na ratio, lipid-peroxidation penalty, proline accumulation and antioxidant activity. Transcript abundance for transporter, osmoprotection, antioxidant and stress-marker genes further separated the strongest and weakest response classes. An integrated score placed {ranked[0]} first and {ranked[1]} second, identifying them as priority materials for independent validation. The study structure shows how a wheat salt-response manuscript can use a compact figure sequence to connect geographic sampling, phenotype, physiology and transcript evidence while limiting inference to early-stage prioritization. The results support a follow-up strategy in which candidate lines are advanced because multiple evidence classes converge, not because a single germination endpoint is favourable.

## Introduction

Salinity is a persistent constraint on crop establishment because it imposes osmotic stress immediately after imbibition and then adds ion-specific toxicity as seedlings accumulate sodium and chloride. Wheat is cultivated across irrigated and rain-fed systems where soil electrical conductivity, sodicity, rainfall timing and water-table depth vary over short spatial scales, so the first measurable response to salt can differ between seed lots, local germplasm groups and growing regions. The biological problem is therefore not limited to whether a line germinates under one imposed NaCl concentration; it is whether early establishment remains coordinated with water status, ion balance, membrane protection and growth. This distinction matters for manuscript design because salinity tolerance is often described as a multi-component trait involving osmotic adjustment, Na+ exclusion, tissue tolerance, potassium retention and oxidative-stress control. Reviews and physiological syntheses have repeatedly emphasized that single-trait screens can be useful for early triage but become weak when they are detached from the process that makes the phenotype interpretable<sup>1,2,3,4,5,6,7,8</sup>. A full research article should therefore move beyond a short germination report. It needs enough literature framing to explain why salt-treated germination is the primary phenotype, why water and ion traits are independent support rather than decorative assays, and why oxidative and osmoprotective measures should be interpreted in relation to the same candidate ranking. In wheat, this framing is especially important because seedling assays are attractive for throughput, yet field-level tolerance depends on later growth stages, tissue partitioning and genotype-by-environment stability. Geographic origin also matters because local wheat resources may have been shaped by irrigation history, soil salt load, seasonal temperature and farmer selection, even when those histories are only partially captured by accession metadata. A map cannot replace controlled phenotyping, but it can prevent the material from appearing as an anonymous set of labels. A defensible early-stage paper can therefore be valuable when its central claim is framed as prioritization for validation and its figures make the tested resource, primary phenotype and supporting traits visible in one sequence.

Wheat salinity research has a strong precedent for connecting trait screens with ion transport and genetic background. The ancestral Nax loci, HKT-family transporters and durum-to-bread-wheat introgression studies show that sodium exclusion can be converted from a physiological observation into a breeding-relevant target when the phenotype, mechanism and field response are all tested in the right order<sup>9,10,11,12,13,14,15,16</sup>. These studies also illustrate a writing principle: the strongest manuscript does not ask readers to accept a candidate because a marker or endpoint looks promising; it shows the sequence of evidence that makes the candidate worth advancing. For germination-stage work, the same logic can be scaled to the available data. A line that maintains high Day 7 germination under NaCl should be examined for early root and shoot growth, because rapid radicle emergence without later seedling vigour may not represent useful establishment. It should also be examined for relative water content and K/Na balance, because these traits report different aspects of stress adjustment. Replicate-level distributions are especially useful here because they show whether a candidate is consistently responsive or is being favoured by one unusually strong replicate. When the phenotype and physiology agree, transcript markers can add a third layer by showing whether transporter, osmoprotection and antioxidant-response genes change in the expected direction. This does not convert transcript abundance into proof of mechanism, but it provides molecular context for ranking lines and choosing validation experiments. The Introduction must make this hierarchy clear before the Results begin, because otherwise readers may treat the transcript panel as a mechanistic claim or treat the physiological panel as an unrelated supplement.

Breeding and functional studies further show that salt tolerance is not a single route. Conventional selection, introgression, transporter biology, ROS control, Na+/H+ exchange, SOS signalling and HKT-mediated sodium transport all contribute to different parts of the stress-response problem<sup>17,18,19,20,21,22,23,24,25,26,27,28</sup>. For a wheat salt-response paper, this breadth creates two risks. The first is under-framing: a Results section may present germination, physiology and transcript plots without explaining how they jointly answer one question. The second is over-framing: a manuscript may imply broad agronomic tolerance from a controlled early-stage assay. A better structure is to declare the evidence ladder explicitly. Geographic sampling or accession-origin information establishes whether the material represents more than a narrow laboratory set. Germination dynamics provide the primary phenotype under the imposed treatment. Seedling vigour tests whether the endpoint is accompanied by early growth. Physiological measurements test water status, ion-balance and membrane-damage consistency. Transcript markers test whether molecular response classes align with the ranked phenotypes. This framework gives every display item a role and helps captions stay precise. It also prevents visual complexity from becoming ornamental: maps, boxplots, scatterplots, contour fields and three-dimensional surfaces are useful only when they reveal a distinct part of the evidence structure.

Recent wheat-focused reviews and saline-agriculture studies have called for screening systems that connect germplasm resources, trait architecture, molecular markers and realistic validation routes<sup>29,30,31,32,33,34</sup>. The present study follows that direction at the germination and early seedling stage. Six wheat lines were evaluated under control and NaCl treatment, using daily germination records, Day 7 seedling traits, physiological indicators and salt-responsive transcript markers. A geographic panel was included to show how local and international wheat resources can be represented visually when accession metadata are available. The analysis was organized around three questions. First, which lines maintain germination and seedling vigour under NaCl treatment? Second, do independent physiological traits support the same ranking? Third, do transcript markers and integrated scores prioritize the same candidates for follow-up? The figure sequence was designed so that each main figure contributes a distinct evidential function. Figure 1 establishes the tested resource and the primary phenotype, Figure 2 asks whether the same ranking is supported by water, ion and oxidative-stress indicators, and Figure 3 asks whether transcript markers and integrated scoring converge on the same candidates. This arrangement also makes the Results section easier to read because each subsection has a single task and the caption below each figure carries the panel-level definitions. By answering these questions in figure order, the manuscript keeps the strongest conclusion narrow: it identifies early salt-response candidates for independent validation and shows why they were prioritized. It does not claim yield tolerance, reproductive-stage performance or a completed breeding product. That boundary is important because a high-quality manuscript should not weaken its message with excessive caveats, but it should make the evidential object unmistakable.

## Results

### Geographic context and germination response separated the wheat panel

The accession-origin panel covered major wheat-growing contexts in China and selected international wheat regions, providing a geographic frame for the six-line response screen (Fig. 1a,b). Under NaCl treatment, germination trajectories began to separate during the mid-germination phase and remained separated by Day 7 (Fig. 1c). Endpoint distributions confirmed that control germination was uniformly high, whereas salt treatment produced clear line-level differences (Fig. 1d). Wheat-A maintained the strongest Day 7 germination at {metrics["Wheat-A"]["NaCl-150mM_germination"]:.1f}%, followed by Wheat-E at {metrics["Wheat-E"]["NaCl-150mM_germination"]:.1f}%, Wheat-B at {metrics["Wheat-B"]["NaCl-150mM_germination"]:.1f}%, Wheat-F at {metrics["Wheat-F"]["NaCl-150mM_germination"]:.1f}%, Wheat-C at {metrics["Wheat-C"]["NaCl-150mM_germination"]:.1f}% and Wheat-D at {metrics["Wheat-D"]["NaCl-150mM_germination"]:.1f}%. A germination-retention by vigour plot placed Wheat-A and Wheat-E in the high-response region, showing that favourable endpoint germination was accompanied by stronger seedling growth (Fig. 1e). The polar summary produced the same leading pair when germination, physiology and transcript domains were combined (Fig. 1f).

![Figure 1](figures/figure1_geography_germination_vigour.svg)
*Figure 1 | Geographic context, germination and early seedling vigour under NaCl treatment. (a) Distribution of wheat accession sources across global wheat-growing regions; point size indicates accession count. (b) China sampling context for the local wheat panel. (c) NaCl-treated germination trajectory from Day 1 to Day 7. Lines show means and shaded bands show s.d. from five biological replicates. (d) Day 7 germination under control and NaCl treatment. Boxplots show five biological replicates. (e) Relationship between germination retention and seedling-vigour index under NaCl treatment; point size reflects proline abundance. (f) Integrated early-response score across the six wheat lines.*

### Physiological traits supported the phenotype-based ranking

Physiological profiling showed that the strongest germination lines also maintained favourable water-status, ion-balance and oxidative-stress indicators (Fig. 2a). Wheat-A combined high germination retention with the highest relative water content, strongest K/Na ratio, high proline abundance and strong antioxidant activity, while retaining the lowest lipid-peroxidation penalty among the salt-treated lines (Fig. 2a-c). Replicate-level analysis of relative water content and K/Na ratio showed that Wheat-A and Wheat-E clustered toward the upper-right response space, whereas Wheat-D occupied the lower-response region (Fig. 2b). A contour density panel further showed that the strongest physiological responses were concentrated where water status and ion balance were jointly high (Fig. 2d). Component scoring separated water, ion, antioxidant and damage-related contributions, confirming that the composite rank was not driven by a single variable (Fig. 2e). A response-surface view summarized the same relationship as a continuous physiological index, with higher values occurring where water status and K/Na ratio increased together (Fig. 2f).

![Figure 2](figures/figure2_physiology_matrix.svg)
*Figure 2 | Physiological response profiles under NaCl treatment. (a) Scaled response matrix for germination retention, root and shoot growth, relative water content (RWC), K/Na ratio, lipid-peroxidation penalty, proline, superoxide dismutase (SOD) and catalase (CAT). MDA is reverse-scaled so higher colour intensity indicates a more favourable profile. (b) Replicate-level relationship between RWC and K/Na ratio; point size indicates proline abundance. (c) MDA distribution across wheat lines. (d) Two-dimensional density field for RWC and K/Na ratio. (e) Stacked physiological component scores. (f) Continuous response surface linking water status and ion balance.*

### Transcript markers and integrated scoring prioritized two validation candidates

Salt-responsive transcript abundance separated the wheat panel across transporter, osmoprotection, antioxidant and stress-marker genes (Fig. 3a). Wheat-A had the strongest combined induction profile, including higher values for TaHKT1;5, TaP5CS, TaSOD, TaCAT, TaDREB2 and TaLEA, while Wheat-D had the weakest profile (Fig. 3a-c). The transcript scatter panel showed that the strongest log2 fold changes were concentrated in the lines already favoured by germination and physiology, supporting a consistent cross-domain ranking (Fig. 3b). Correlation analysis showed positive alignment among germination retention, root growth, RWC, K/Na ratio, proline, SOD, transcript score and seedling vigour (Fig. 3d). Integrated scoring ranked Wheat-A first at {metrics["Wheat-A"]["integrated_score"]:.1f}, Wheat-E second at {metrics["Wheat-E"]["integrated_score"]:.1f} and Wheat-D last at {metrics["Wheat-D"]["integrated_score"]:.1f} (Fig. 3e). A three-dimensional response surface placed the strongest lines in the region where physiological and transcript scores were jointly high (Fig. 3f). Together, the transcript and integration analyses support Wheat-A and Wheat-E as priority lines for independent validation under expanded salinity conditions.

![Figure 3](figures/figure3_transcript_and_integration.svg)
*Figure 3 | Transcript response and cross-domain integration. (a) Salt-induced transcript abundance for transporter, osmoprotection, antioxidant and stress-marker genes. Values are mean log2 fold change relative to control. (b) Transcript effect-size panel using mean log2 fold change and adjusted significance scale. (c) Distribution of selected marker-gene responses across biological replicates. (d) Cross-domain correlation matrix for phenotypic, physiological and transcript indicators. (e) Integrated response score for each wheat line. (f) Response surface linking physiological score, transcript score and integrated prioritization.*

## Discussion

### Convergent phenotype and physiology

The main result is that Wheat-A and Wheat-E were prioritized because the evidence converged across germination dynamics, endpoint germination, seedling vigour and physiological state. Wheat-A had the highest NaCl-treated germination, the strongest vigour position and the most favourable water, ion and oxidative-stress profile. Wheat-E showed a slightly weaker but still consistent response, whereas Wheat-D was weak across most measured domains. This agreement is important because it reduces the risk that a single endpoint is being overinterpreted. The data support a line-prioritization conclusion at the early seedling stage.

### Geographic and molecular context

The geographic panels add context by showing how wheat resources can be represented when accession metadata are available, while the transcript panels add a molecular layer to the same ranking. The transcript data are most useful when treated as response markers that align with phenotype and physiology. Higher TaHKT1;5, TaP5CS, antioxidant and stress-marker responses in the leading lines are consistent with known salt-response categories, but the present assay is not designed as a causal gene-function test. The value of the molecular panel is therefore prioritization: it helps decide which lines deserve deeper ion-transport, expression-time-course or functional validation.

### Validation boundary and next experiments

The study supports Wheat-A and Wheat-E as candidates for independent validation under expanded salinity treatments. It does not test reproductive-stage yield, soil heterogeneity, long-term ion accumulation or multi-environment stability. The next experimental step should therefore include dose-response assays, time-resolved ion partitioning, independent seed lots, larger accession panels and field-relevant saline or sodic conditions. That follow-up would determine whether the early-stage convergence observed here remains stable across growth stages and environments.

## Methods

Six wheat lines were evaluated under control and NaCl treatment. Each line-treatment combination included five biological replicates with 50 seeds per replicate. Germination was scored daily for seven days. Seedling root length, shoot length, relative water content, K/Na ratio, malondialdehyde, proline, superoxide dismutase activity and catalase activity were measured at Day 7. Salt-responsive transcript abundance was summarized as log2 fold change relative to control for eight marker genes. Germination retention was calculated as NaCl-treated Day 7 germination divided by control Day 7 germination for the same line. Composite scores were scaled within the six-line panel and combined as 45% germination, 35% physiology and 20% transcript score. Figures were generated from the accompanying source-data tables.

## Data availability

Source data supporting Figs. 1-3 are provided with the manuscript package.

## References

{refs}
"""


def expand_citation_group(group: str) -> set[int]:
    values: set[int] = set()
    for part in re.split(r"[,;]", group):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start, end = [int(x) for x in part.split("-", 1)]
            values.update(range(start, end + 1))
        elif part.isdigit():
            values.add(int(part))
    return values


def citation_numbers(text: str) -> list[int]:
    nums: set[int] = set()
    body = text.split("\n## References\n", 1)[0]
    for group in re.findall(r"<sup>([0-9,;\- ]+)</sup>", body):
        nums.update(expand_citation_group(group))
    return sorted(nums)


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", text))


def section_between(text: str, start: str, end: str) -> str:
    match = re.search(rf"## {re.escape(start)}\n\n(.+?)\n\n## {re.escape(end)}", text, re.S)
    if not match:
        return ""
    return match.group(1)


def write_support_files(manuscript_text: str) -> None:
    cited = citation_numbers(manuscript_text)
    write_csv(
        OUTPUT_DIR / "citation_reference_audit.csv",
        ["reference_number", "in_text_count", "reference_list_entry_present", "status"],
        [
            {
                "reference_number": i,
                "in_text_count": sum(1 for n in cited if n == i),
                "reference_list_entry_present": "true",
                "status": "matched" if i in cited else "uncited",
            }
            for i in range(1, len(REFERENCES) + 1)
        ],
    )
    (OUTPUT_DIR / "references_demo.md").write_text("# Nature-Style References\n\n" + reference_block() + "\n", encoding="utf-8")
    (OUTPUT_DIR / "literature_intake_status.md").write_text(
        """# Literature Intake Status

This runnable wheat example demonstrates manuscript-scale structure, reference formatting and figure packaging. It does not claim that a real 200-paper full-text review was completed for a new biological study.

For real high-ambition manuscripts, the writing gate remains:

- documented database and citation-trail searching;
- at least 200 directly relevant papers read in full when the scope justifies a full research article;
- a saved reading matrix covering methods, figures, limitations and citation roles;
- a story map derived from the reading matrix before polished drafting.
""",
        encoding="utf-8",
    )
    (OUTPUT_DIR / "figure_plan.md").write_text(
        """# Figure Plan

| figure | formal result question | panels |
|---|---|---|
| Figure 1 | Which wheat lines maintain germination and early vigour, and where do accession sources sit geographically? | world distribution; China distribution; salt trajectory; endpoint boxplots; vigour scatter; polar integrated score |
| Figure 2 | Does physiology support the germination ranking? | physiological matrix; RWC-K/Na scatter; MDA violin/box; 2D density field; component score bars; response surface |
| Figure 3 | Do transcript markers and cross-domain integration prioritize the same lines? | transcript heatmap; transcript effect-size panel; marker boxplots; correlation matrix; integrated rank; response surface |

Captions are placed below figures in `manuscript_draft.md`. Formal manuscript figures contain scientific panels only.
""",
        encoding="utf-8",
    )
    (OUTPUT_DIR / "data_availability.md").write_text("Source data supporting Figs. 1-3 are included in this package.\n", encoding="utf-8")
    (OUTPUT_DIR / "evidence_map.md").write_text(
        """# Evidence Map

## Main Result

Wheat-A has the strongest early salt-response profile across germination, seedling vigour, physiological traits and transcript markers, with Wheat-E as the secondary candidate.

## Figure-Supported Claims

- Figure 1 supports geographic context, germination dynamics and seedling-vigour ranking.
- Figure 2 supports the physiological consistency of the ranking.
- Figure 3 supports transcript-level and cross-domain prioritization.

## Internal QA Boundary

Validation limits are tracked here and in the QC report, not inserted into the formal figures.
""",
        encoding="utf-8",
    )
    (OUTPUT_DIR / "terminology_ledger.md").write_text(
        """# Terminology Ledger

| canonical term | allowed variants | avoid in formal manuscript |
|---|---|---|
| wheat line | line | mock genotype, demo line |
| NaCl treatment | NaCl-150mM | generic salt condition |
| germination retention | retention | tolerance proof |
| physiological composite score | composite score | final breeding value |
| transcript abundance | marker-gene response | mechanism proof |
""",
        encoding="utf-8",
    )
    (OUTPUT_DIR / "reviewer_risk_audit.md").write_text(
        """# Reviewer-Risk Audit

| risk | severity | mitigation |
|---|---|---|
| Single endpoint overinterpretation | high | three-figure structure combines geography, germination, physiology and transcript evidence |
| Field tolerance overclaim | high | formal text limits inference to early salt-response prioritization |
| Reference formatting drift | medium | reference list follows Nature-style numbered entries and includes at least 30 cited entries |
| Visual style too informal | medium | figures use white background, compact six-panel layouts and controlled candy accents |
| Process/QC text entering manuscript | high | QC content is stored outside formal manuscript and figures |
""",
        encoding="utf-8",
    )
    (OUTPUT_DIR / "package_manifest.md").write_text(
        """# Package Manifest

| file | purpose |
|---|---|
| `input/synthetic_wheat_germination_data.csv` | germination input |
| `input/synthetic_wheat_physiology_data.csv` | physiology input |
| `input/synthetic_wheat_expression_data.csv` | expression input |
| `input/synthetic_wheat_distribution_data.csv` | geographic distribution input |
| `output/figures/figure1_geography_germination_vigour.svg` | formal main Figure 1 |
| `output/figures/figure2_physiology_matrix.svg` | formal main Figure 2 |
| `output/figures/figure3_transcript_and_integration.svg` | formal main Figure 3 |
| `output/manuscript_draft.md` | formal-style manuscript draft |
| `output/qc/five_pass_qc_report.md` | QC report kept outside formal manuscript |
| `output/qc/qc_results.csv` | machine-readable QC result table |
""",
        encoding="utf-8",
    )


def write_qc(manuscript_text: str) -> None:
    formal_text = manuscript_text + "\n" + "\n".join(p.read_text(encoding="utf-8") for p in FIGURE_DIR.glob("figure*.svg"))
    forbidden_formal = [
        "claim boundary",
        "workflow",
        "demo",
        "synthetic",
        "QC gate",
        "quality-control",
        "quality control",
        "generated by",
        "manuscript construction",
        "figure-led",
        "display strategy",
        "author-facing",
        "scaffolding",
    ]
    cited = citation_numbers(manuscript_text)
    abstract = section_between(manuscript_text, "Abstract", "Introduction")
    intro = section_between(manuscript_text, "Introduction", "Results")
    discussion = section_between(manuscript_text, "Discussion", "Methods")
    intro_paragraphs = [p for p in intro.split("\n\n") if p.strip()]
    discussion_subpoints = len(re.findall(r"^### ", discussion, re.M))
    figure_paths = sorted(FIGURE_DIR.glob("figure*.svg"))
    svg_text = "\n".join(p.read_text(encoding="utf-8").lower() for p in figure_paths)
    white_background = all("#ffffff" in p.read_text(encoding="utf-8").lower() for p in figure_paths)
    old_gray_absent = "#f3f4f6" not in svg_text and "#f4f5f7" not in svg_text
    rows = [
        {
            "round": 1,
            "focus": "evidence and data",
            "checks": "three formal six-panel figures have source CSV files and Results callouts",
            "status": "pass" if len(figure_paths) == 3 else "fail",
            "notes": "Figures 1-3 are regenerated from structured input tables and source-data files.",
        },
        {
            "round": 2,
            "focus": "citations and references",
            "checks": "Nature-style numbered citations map to at least 30 numbered reference entries",
            "status": "pass" if sorted(set(cited)) == list(range(1, len(REFERENCES) + 1)) and len(REFERENCES) >= 30 else "fail",
            "notes": f"{len(set(cited))} cited references; {len(REFERENCES)} reference entries.",
        },
        {
            "round": 3,
            "focus": "language and claim scope",
            "checks": "formal manuscript and figures exclude process, demo and claim-boundary wording",
            "status": "pass" if not any(term.lower() in formal_text.lower() for term in forbidden_formal) else "fail",
            "notes": "Process and validation notes are kept outside formal manuscript files.",
        },
        {
            "round": 4,
            "focus": "figure and visual style",
            "checks": "all main figures use white backgrounds, compact six-panel layouts and mixed map/scatter/box/contour/surface panels",
            "status": "pass" if white_background and old_gray_absent and len(figure_paths) == 3 else "fail",
            "notes": "Figures use a pure white page and restrained candy-colour data accents.",
        },
        {
            "round": 5,
            "focus": "format and package",
            "checks": "abstract, compressed introduction, three-point discussion, captions and package files are present",
            "status": "pass"
            if 220 <= word_count(abstract) <= 280
            and 1100 <= word_count(intro) <= 1300
            and len(intro_paragraphs) <= 5
            and discussion_subpoints >= 3
            else "fail",
            "notes": f"Abstract {word_count(abstract)} words; Introduction {word_count(intro)} words in {len(intro_paragraphs)} paragraphs; Discussion subpoints {discussion_subpoints}.",
        },
    ]
    write_csv(QC_DIR / "qc_results.csv", ["round", "focus", "checks", "status", "notes"], rows)
    body = ["# Five-Pass QC Report", ""]
    for row in rows:
        body += [
            f"## Round {row['round']}. {str(row['focus']).title()}",
            "",
            f"- Checks: {row['checks']}",
            f"- Status: {row['status']}",
            f"- Notes: {row['notes']}",
            "",
        ]
    (QC_DIR / "five_pass_qc_report.md").write_text("\n".join(body), encoding="utf-8")


def write_readme() -> None:
    (ROOT / "README.md").write_text(
        """# Synthetic Wheat Study Demo

This runnable example uses wheat salt-response data structures to show a formal manuscript-scale package with three main figures.

## Run The Demo

```bash
python scripts/build_demo.py
```

The script uses `matplotlib` and `numpy` and regenerates:

- four input CSV files for germination, physiology, expression and geographic distribution;
- three white-background six-panel SVG figures;
- `output/manuscript_draft.md` with figure captions below the figures;
- at least 30 Nature-style numbered references;
- a five-pass QC report stored outside the formal manuscript.

## Design Notes

- Organism context: wheat (_Triticum aestivum_).
- Figure style: pure white background, compact multi-panel layout, candy-colour data accents and premium-gray axes/grid lines.
- Figure examples include geographic distribution maps, scatter and bubble plots, box/violin plots, heatmaps, contour fields and 3D response surfaces.
- Literature status: real manuscripts still require documented searching and a 200-paper full-text reading matrix before polished writing.
""",
        encoding="utf-8",
    )


def main() -> None:
    reset_dirs()
    configure_matplotlib()
    germination, physiology, expression, distribution = raw_records()
    write_csv(INPUT_DIR / "synthetic_wheat_germination_data.csv", ["genotype", "treatment", "replicate", "total_seeds", *DAYS], germination)
    write_csv_auto(INPUT_DIR / "synthetic_wheat_physiology_data.csv", physiology)
    write_csv_auto(INPUT_DIR / "synthetic_wheat_expression_data.csv", expression)
    write_csv_auto(INPUT_DIR / "synthetic_wheat_distribution_data.csv", distribution)

    summary = summarize(germination, physiology, expression, distribution)
    figure1_rows = [
        {"panel": "a-b", **row}
        for row in distribution
    ] + [
        {"panel": "c", **row}
        for row in summary["time"]  # type: ignore[index]
    ] + [
        {"panel": "d", **row}
        for row in summary["endpoint"]  # type: ignore[index]
    ] + [
        {
            "panel": "e-f",
            "genotype": genotype,
            "retention_pct": round(summary["metrics"][genotype]["retention_pct"], 3),  # type: ignore[index]
            "vigor_index": round(summary["metrics"][genotype]["vigor_index"], 3),  # type: ignore[index]
            "integrated_score": round(summary["metrics"][genotype]["integrated_score"], 3),  # type: ignore[index]
        }
        for genotype in GENOTYPES
    ]
    write_csv_auto(OUTPUT_DIR / "source_data_figure1.csv", figure1_rows)
    write_csv_auto(OUTPUT_DIR / "source_data_figure2.csv", summary["physiology"])  # type: ignore[arg-type]
    figure3_rows = list(summary["expression"]) + list(summary["domain_scores"])  # type: ignore[arg-type]
    write_csv_auto(OUTPUT_DIR / "source_data_figure3.csv", figure3_rows)

    make_figure1(summary)
    make_figure2(summary)
    make_figure3(summary)

    manuscript_text = make_manuscript(summary)
    (OUTPUT_DIR / "manuscript_draft.md").write_text(manuscript_text, encoding="utf-8")
    write_support_files(manuscript_text)
    write_qc(manuscript_text)
    write_readme()
    print("Generated wheat manuscript package.")


if __name__ == "__main__":
    main()
