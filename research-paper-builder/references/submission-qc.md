# Submission QC

Use this reference before delivering a manuscript package.

## Route-Specific Checks

Before final delivery, confirm which route was used:
- full manuscript package;
- section draft or polish only;
- figure/caption package;
- citation/data availability package;
- reviewer response or revision package.

Do not claim final-package QC passed for a partial route.

## Manuscript Checks

- Section order matches the user request or target journal.
- Title, abstract and result headings are concise and informative.
- Results describe findings before conclusions.
- Discussion does not repeat every result value.
- Methods contain enough detail for reproducibility.
- Technical tasks are not presented as scientific results.
- All placeholder author, affiliation, funding and accession text is clearly marked or replaced.
- The one-sentence argument contract matches the title, Abstract, Results and Discussion.
- The terminology ledger, if created, has no unresolved forbidden variants in final files.

## Citation Checks

- Every in-text citation maps to a reference entry.
- Every reference entry is cited.
- Citation numbers are within range.
- Citation ranges are expanded during checking.
- Reference style is consistent.
- Claims that depend on prior work have support-grade-appropriate citations.
- Style-matching reference papers are not cited unless they also support a scientific claim.

## Figure Checks

- Main figures are complete composites when the journal asks for composite upload.
- Source panels are preserved separately.
- Each panel has one letter only.
- Fonts are readable in the composite.
- No internal titles remain unless required.
- Captions define panel statistics, sample size and abbreviations.
- Every figure panel has traceable source data or a documented non-data role.
- Figure labels, captions and manuscript text use the same canonical terms.

## Data And Table Checks

- Source data are provided for plotted values.
- Supplementary tables have clear sheet names.
- Processed CSV files are included when useful for review.
- Raw data are not overwritten.
- Non-English characters are removed from English submission files unless required.
- Data availability statement names the actual repository, accession, DOI, supplementary table or pending author action.

## Package Checks

Recommended folders:
- `manuscript/`
- `figures/main/`
- `figures/source_panels/`
- `figures/qc/`
- `tables/workbooks/`
- `tables/csv/`
- `source_data/`
- `analysis_scripts/`

Run `scripts/validate_research_package.py` when possible and report the JSON summary in plain language.

## Pre-Submission Risk Checks

For ambitious journal targets, run a reviewer-risk audit before final packaging:
- editor risk: novelty, breadth, journal fit and clear significance;
- methods/statistics risk: controls, replication, correction, model assumptions and reproducibility;
- field-specialist risk: mechanism, literature fit, alternative explanations and scope;
- presentation risk: figure sequence, caption completeness, terminology and density.

Document high-severity risks in delivery notes if they cannot be fixed with the available material.
