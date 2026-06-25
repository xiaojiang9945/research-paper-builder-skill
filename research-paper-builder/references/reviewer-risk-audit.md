# Reviewer Risk Audit

Use this reference for pre-submission critique, internal mock review, rebuttal planning or major revision triage.

## Audit Roles

Evaluate the manuscript through four lenses:
- `editor`: novelty, breadth, fit, clarity and likely desk-reject risk.
- `methods/statistics reviewer`: design, controls, replication, models, correction, robustness and reproducibility.
- `field specialist`: biological or technical interpretation, literature fit, mechanism boundary and missing alternative explanations.
- `presentation reviewer`: figure logic, caption completeness, section flow, terminology and writing density.

Keep critique grounded in the manuscript and supplied evidence. Do not invent missing experiments as if they already exist.

## Pre-Submission Risk Table

Use this table shape:

```markdown
| risk | severity | where it appears | why it matters | fix now | longer-term fix |
|---|---|---|---|---|---|
|  | high/medium/low |  |  |  |  |
```

Severity guide:
- `high`: likely desk rejection, major reviewer objection or claim invalidation.
- `medium`: weakens confidence but can be fixed by wording, figure redesign or additional analysis from existing data.
- `low`: presentation, clarity or minor completeness issue.

## Common High-Risk Patterns

- Title or Abstract claims mechanism but evidence is association, annotation or external validation.
- Title or Abstract claims origin timing, diversification, formation mechanism, selection, retention or function when evidence is only catalog distribution, representative guide tree, conserved architecture, synteny or repeat-neighbor screening.
- Raw database hits, profile co-occurrences or screen records are treated as curated genes, orthologs, copy numbers or validated candidates.
- Absence in a database snapshot is written as biological absence rather than catalog-bounded non-detection.
- A model, schematic or experimental roadmap is presented as a Result without clearly labeling it as synthesis or hypothesis.
- Data or Code availability overstates reproducibility, exposes local paths, or disagrees with package metadata, manifests, database dates or checksums.
- A central figure lacks source data, statistics, sample size or clear controls.
- Results are organized by analysis chronology rather than scientific question.
- A known gene, marker or dataset is presented as a new discovery.
- The Discussion generalizes beyond population, environment, tissue, time point or assay.
- The manuscript depends on a public dataset without explaining its design or limitations.
- Supplementary material contains the evidence needed for a main-text claim but is not cited clearly.

## Rebuttal Planning

For reviewer comments, triage each comment:
- `accept and revise`: valid point; make text, figure or analysis change.
- `clarify`: reviewer misunderstood because the manuscript was unclear.
- `bounded disagreement`: reviewer asks beyond the study scope; explain boundary and soften claim.
- `new experiment required`: cannot be solved with wording alone.

For every response, map:
- reviewer concern;
- manuscript change;
- evidence location;
- revised wording;
- residual limitation.

## Output Standard

Return findings first, ordered by severity. Then add:
- highest-leverage revision steps;
- claims that should be softened;
- missing evidence that cannot be fixed by wording;
- optional rebuttal language only after the action map is clear.
