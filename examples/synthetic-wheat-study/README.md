# Synthetic Wheat Study Demo

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
