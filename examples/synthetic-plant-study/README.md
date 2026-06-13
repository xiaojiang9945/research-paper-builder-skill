# Synthetic Plant Germination Demo

This demo is fully synthetic. It exists only to show how `research-paper-builder` organizes a publication-scale manuscript package.

## Input

- `input/synthetic_germination_data.csv`: fictional seed germination counts for three mock genotypes under water and salt treatment.
- Each row is one biological replicate.
- Each replicate contains 25 seeds.

## Demo Prompt

```text
Use the research-paper-builder skill on input/synthetic_germination_data.csv.
Target a plant-science research article package rather than a short report.
Before writing, produce a literature-intake status note. For a real manuscript, require a 200-paper
screening/full-text reading matrix; for this synthetic demo, use the provided synthetic citation set only
to demonstrate citation-reference matching.

Build an evidence map, terminology ledger, integrated multi-panel Figure 1, figure-led Results,
approximately 250-word Abstract, approximately 1,200-word Introduction/background with citation keys,
reference list, citation-reference audit, Data Availability statement, reviewer-risk audit, and package manifest.
Use cautious language and clearly label the data as synthetic.
```

## Expected Output

The `output/` folder contains a complete example package:

- `evidence_map.md`
- `terminology_ledger.md`
- `figure_plan.md`
- `figures/figure1_composite.svg`
- `source_data_figure1.csv`
- `supplementary_table_s1_summary.csv`
- `manuscript_draft.md`
- `references_demo.md`
- `citation_reference_audit.csv`
- `literature_intake_status.md`
- `data_availability.md`
- `reviewer_risk_audit.md`
- `package_manifest.md`

The example demonstrates output shape and quality checks. The citation set is synthetic and should not be cited as real literature.
