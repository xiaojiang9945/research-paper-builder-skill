# Synthetic Plant Germination Demo

This demo is fully synthetic. It exists only to show how `research-paper-builder` organizes a small research manuscript package.

## Input

- `input/synthetic_germination_data.csv`: fictional seed germination counts for three mock genotypes under water and salt treatment.
- Each row is one biological replicate.
- Each replicate contains 25 seeds.

## Demo Prompt

```text
Use the research-paper-builder skill on input/synthetic_germination_data.csv.
Target a short plant-science research article.
Build an evidence map, terminology ledger, figure-led Results structure, manuscript draft,
Data Availability statement, reviewer-risk audit, and package manifest.
Use cautious language and clearly label the data as synthetic.
```

## Expected Output

The `output/` folder contains a complete example package:

- `evidence_map.md`
- `terminology_ledger.md`
- `figure_plan.md`
- `source_data_figure1.csv`
- `supplementary_table_s1_summary.csv`
- `manuscript_draft.md`
- `data_availability.md`
- `reviewer_risk_audit.md`
- `package_manifest.md`

The example demonstrates output shape and quality checks. It should not be cited as a biological study.
