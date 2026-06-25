# Citation And Data Availability

Use this reference when checking citations, finding support for claims, preparing Data Availability statements, planning repositories, or building submission metadata.

## Citation Support Workflow

1. Split manuscript claims into citable units.
2. Mark each unit as background, method precedent, direct comparison, limitation, or interpretation.
3. For each unit, identify the minimum citation needed.
4. Prefer primary literature for specific claims and reviews for broad background.
5. Verify bibliographic metadata from a reliable source before finalizing.

Do not fabricate DOI, page range, volume, issue, accession number or repository metadata. If metadata is unavailable, mark it for author verification.

## Support Strength

Grade candidate references:
- `direct`: same biological/technical claim or method.
- `partial`: supports part of the claim but not the full scope.
- `background`: useful context only.
- `contrast`: relevant disagreement or limitation.
- `metadata-only`: useful for locating the source but not enough to support a claim.

Use direct or partial support for Results and Discussion claims. Background citations are not substitutes for evidence.

## Citation Hygiene

Before delivery:
- every in-text citation has a reference-list entry;
- every reference-list entry is cited;
- citation ranges are valid and ordered;
- references cited in captions are also present in the reference list;
- no reference-paper examples are cited merely because they were used for style matching;
- citation style matches the target journal.
- search logs, reading-matrix size and reference-paper style-learning notes stay outside the formal manuscript unless the manuscript is itself a review or methods paper about that corpus.

## Claim-Support Audit

For full packages and high-stakes revisions, check whether a citation actually supports the claim it is attached to.

Create a claim registry with:

```text
claim_id,claim_text,section,claim_type,cited_source,source_locator,support_grade,verdict,action
```

Claim types:
- `quantitative`: counts, percentages, effect sizes, p-values, fold changes, sample sizes.
- `factual`: species, gene, method, dataset, publication or historical assertions.
- `comparative`: largest, first, higher, lower, enriched, depleted, broader, narrower.
- `trend`: increasing, declining, stable, stage-specific or time-dependent.
- `causal`: causes, regulates, drives, confers, determines or mediates.

Verdicts:
- `verified`: the source supports the claim with matching scope.
- `minor-adjust`: the source supports the claim after wording, rounding or scope tightening.
- `unsupported`: the source does not support the claim.
- `access-limited`: the source exists but the needed passage could not be checked.
- `metadata-missing`: bibliographic, DOI, accession or repository information is incomplete.

Final manuscripts should have no `unsupported` claim and no fabricated reference. `access-limited` claims may remain only if the wording is broad enough for the available evidence or the unresolved action is stated outside the manuscript.

## Nature-Style Reference Pattern

When the target is Nature or a Nature-family journal and no journal-specific override is provided, use numbered citations and a compact reference list.

Text citations:
- use sequential numbered citations;
- in Markdown drafts, represent Nature-style superscript citations as `<sup>1</sup>` or `<sup>1,2</sup>`;
- keep citation numbers outside punctuation only if the target journal requires it; otherwise follow the journal example exactly.

Reference-list pattern:

```text
1. Author, A. A. & Author, B. B. Article title in sentence case. Journal Abbrev. volume, pages (year).
```

For Markdown drafts, preserve visual structure:

```markdown
1. Author, A. A. & Author, B. B. Article title in sentence case. *Journal Abbrev.* **59**, 651-681 (2008).
```

Checks:
- include article titles;
- use abbreviated journal titles when required by the journal;
- bold the volume number in Markdown when preparing a readable draft;
- include page range or article number;
- include year in parentheses;
- do not invent DOI, issue, volume or page metadata.
- for Nature-style full research article examples, keep at least 30 cited references when the user requests manuscript-scale literature depth, while staying within the target journal's maximum;
- verify that every listed reference is cited and every in-text citation has a listed reference.

## Data Availability

Draft the statement around actual access paths:
- repository name and accession/DOI when available;
- files included as supplementary tables or source data;
- code repository, commit, release or archive DOI when available;
- controlled-access or author-request data with reason;
- restrictions from human subjects, proprietary material or unpublished breeding lines.
- actual package directories when a lightweight source-data package is supplied, such as `source_data/`, `tables/`, `figures/`, `analysis_scripts/`, `logs/` or `qc/`.
- raw inputs or external resources that are required for a full rerun but are not included.

Avoid vague statements such as "data are available on request" when repository deposition is expected. If deposition is pending, state what must be deposited before submission.
Do not expose local workstation paths, server paths, private project directories, SSH aliases, usernames, credentials or internal version paths in Data or Code availability.
Do not overstate reproducibility. If a script records the generation workflow but depends on local or external input tables, say that full end-to-end reruns require those inputs instead of calling the package fully reproducible.

## FAIR And Reproducibility Check

For source data and code:
- filenames are stable and descriptive;
- tables have data dictionaries or clear headers;
- units and normalization are stated;
- sample IDs map to metadata;
- scripts can reproduce processed tables and figures;
- large raw files are referenced rather than copied into lightweight manuscript packages unless required.
- database freeze dates, release numbers, query strings, counts and hashes match between manuscript Methods, metadata files and main tables.
- package manifests and checksums are generated after all final QC reports, figures, tables and manuscripts have been copied.
- checksums or logs use package-relative paths rather than local absolute paths.

## Output Pattern

When asked to produce citation or data-availability work, return:
- claim or data item;
- proposed citation/repository support;
- support grade or deposition status;
- unresolved author action.
