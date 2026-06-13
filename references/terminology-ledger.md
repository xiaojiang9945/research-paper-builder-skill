# Terminology Ledger

Use this reference when a manuscript has repeated technical terms, mixed Chinese-English notes, many samples or markers, or inconsistent naming across drafts, figures and tables.

## Purpose

Create a small ledger before substantial drafting. The ledger prevents inconsistent terminology from propagating into the manuscript, captions, source data and DOCX XML.

Recommended columns:
- `concept`: what the term refers to.
- `canonical_form`: exact form to use in manuscript text.
- `allowed_short_form`: abbreviation after first definition.
- `do_not_use`: old labels, local shorthand, mistranslations or internal names.
- `where_defined`: section, figure, table or Methods paragraph where the term is first defined.
- `notes`: style, italics, capitalization, units or journal-specific treatment.

## What To Capture

Capture:
- study materials: accessions, genotypes, cultivars, treatments, tissues, time points and environments;
- biological entities: genes, proteins, QTLs, haplotypes, pathways, taxa and traits;
- methods: assays, models, sequencing platforms, thresholds, statistics and software;
- display terms: axis labels, panel labels, color groups and table headers;
- citations and datasets: public dataset IDs, repository names, accession numbers and versioned references.

For Chinese source notes, translate meaning rather than word order. Keep the Chinese source term in `notes` only when it helps audit the mapping.

## Rules

- Use one canonical form everywhere after the ledger is created.
- Define abbreviations once, then use the abbreviation consistently.
- Keep gene/QTL/protein typography aligned with journal and field convention.
- Do not rename a biological entity just to make figure labels shorter. Use a short display label plus a caption definition.
- If a term changed between analysis versions, keep the manuscript-facing term stable and record the old term under `do_not_use`.
- Search manuscript, captions, tables and package manifests for forbidden variants before final delivery.

## Quick Ledger Skeleton

```markdown
| concept | canonical_form | allowed_short_form | do_not_use | where_defined | notes |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
```

## Final Checks

- The title, Abstract and figure captions use the same term for the same object.
- Axis labels and table headers match manuscript terminology.
- Sample names in text match source data or are explicitly mapped.
- No internal folder names, draft labels or analysis nicknames remain in submission files.
