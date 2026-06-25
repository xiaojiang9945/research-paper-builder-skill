# Release Notes

## v1.1.0 - Evidence-Bounded Manuscript Package Checks

Release date: 2026-06-25

This update strengthens the skill's publication-readiness rules for full research manuscript packages. It is a backward-compatible minor release after `v1.0.0`.

### Highlights

- Tightened title and Abstract claim scope so computational screens, catalog searches, associations, enrichment, synteny, guide trees, or conceptual models are not overstated as mechanism, origin, function, selection, or validated causality.
- Added guidance for separating generic background constraints from the distinctive, study-specific advance, especially when the key story is a small candidate class or operationally defined signal.
- Strengthened figure-led Results rules: result-centered subsection headings, finding-first figure references, clearer panel-to-text contracts, and explicit labeling of synthesis models, hypotheses, or experimental roadmaps.
- Improved citation, data availability, and reproducibility checks, including database freeze dates, query strings, record counts, package-relative checksums, and honest limits when scripts depend on external or local inputs.
- Expanded pre-submission QC and reviewer-risk audit coverage for raw discovery records versus curated candidates, database-bounded non-detection, stage-separated omics integration, package hygiene, and local-path/privacy leakage.

### Validation Expectations

Before publishing this release, run:

```bash
python path/to/skill-creator/scripts/quick_validate.py research-paper-builder
python research-paper-builder/scripts/validate_research_package.py --package examples/synthetic-wheat-study/output --qc-results examples/synthetic-wheat-study/output/qc/qc_results.csv --min-qc-passes 5
```

Also run the repository privacy scan described in `AGENTS.md` before pushing or sharing.
