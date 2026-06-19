# Literature Intake

Use this reference before writing a full manuscript, especially for SCI, Nature, Cell, Science, PNAS, Nature Plants, Molecular Plant, The Plant Cell or similar targets.

## Minimum Standard

For a high-ambition full manuscript, do not start polished manuscript writing until the field has been mapped.

Default intake target:
- build the search universe through databases, review papers and forward/backward citation trails;
- fully read at least 200 directly relevant papers, including main text, figures, methods and supplementary information when available;
- enter every fully read paper into the reading matrix with evidence learned, figure lessons, method precedent and claim boundaries;
- record why screened papers outside the full-text set were excluded;
- extract figure architecture, methods precedent, terminology, claim boundaries and validation expectations;
- convert the literature map into a story map before drafting.

If 200 relevant full-text papers are not available, not accessible, or not needed for a clearly narrow task, state the reason and document the smaller scope. Do not pretend the 200-paper full-text standard was met.

## Reading Matrix

Create a table or CSV with these columns:

```text
id,title,year,venue,doi_or_url,full_text_status,read_depth,relevance_tier,study_system,
data_types,methods_to_learn,figure_lessons,key_findings,claim_boundary,
limitations,how_it_informs_this_manuscript,citation_role,include_in_references
```

Relevance tiers:
- `core`: directly shapes the manuscript argument, methods or interpretation.
- `supporting`: supports background, discussion or terminology.
- `contrast`: useful disagreement, limitation or alternative model.
- `method`: needed for assay, statistic, dataset or software precedent.
- `exclude`: screened but not used; record reason.

## Search Strategy

Use multiple query families:
- organism/system plus process;
- phenotype or assay plus stress/treatment;
- core mechanism or pathway terms;
- method/data type terms;
- target journal or review-paper citation trails;
- recent review papers, then forward/backward citation expansion.

For each family, record database/source, query, date, hit count, screening rule and retained papers.

The search log should also record:
- searcher or tool used;
- filters applied, including language, date range, article type and species/system;
- full-text access route or access limitation;
- backward/forward citation expansion source;
- duplicate-removal rule;
- exclusion reason for papers screened out after title/abstract or full-text review;
- freshness check date before final manuscript drafting.

## What To Extract From Full Text

For each core paper, extract:
- central question and experimental design;
- sample size, controls, statistics and validation depth;
- figure sequence and panel density;
- what result types are treated as main evidence;
- what claims are avoided or hedged;
- terminology and abbreviations;
- limitations and alternative explanations;
- datasets, accessions, software and supplementary material that matter.
- source locators for claim checking: page, figure, table, supplementary item, dataset accession or section heading when available.

For high-impact papers, do not stop at extracting topic summaries. Record what each paper teaches about evidential standards: what controls were expected, what validation depth made the claim credible, what claims the authors avoided, and how figures carried the argument.

## Writing Gate

Before drafting a full manuscript, confirm:
- literature matrix exists and is saved in the output folder;
- at least 200 relevant papers were fully read for high-ambition manuscripts, or a smaller justified scope is documented;
- every Introduction paragraph has citation support;
- every reference-list item is cited, and every in-text citation maps to the reference list;
- no reference is invented from memory.
- core claims have locator-ready citation notes, not only paper titles or DOI strings;
- papers unavailable in full text are marked as limited-access and not used to support detailed factual claims that cannot be verified.

If the gate is not satisfied, produce a literature plan and writing outline rather than a final manuscript.
