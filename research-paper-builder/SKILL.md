---
name: research-paper-builder
description: Use when Codex needs to plan, write, rewrite, polish, audit, format, or package a research manuscript in any discipline; trigger for SCI, Nature, Cell, Science, PNAS or journal-style paper writing, reference-paper style matching, title/abstract/introduction/results/discussion/methods polishing, figure-led Results, multi-panel figure layout, figure captions, terminology ledgers, tables/source data, citation-reference consistency, Data Availability statements, pre-submission reviewer-risk audits, rebuttal planning, DOCX/PDF generation, or submission-ready research packages.
---

# Research Paper Builder

## Routing Before Loading References

Before writing or revising, classify the request in one short internal pass:
- `scope`: full manuscript, single section, language polish, figure/caption, citation/data availability, reviewer response, or final package.
- `article_type`: research article, methods/resource paper, review, hypothesis/commentary, or computational/algorithmic paper.
- `venue_pressure`: generic journal, society journal, or high-impact broad-audience journal.
- `source_language`: English, Chinese, mixed notes, or bilingual draft.
- `evidence_state`: raw data available, figures available, draft only, literature-only, or missing critical support.

State the selected route briefly when it affects user expectations. Load only the references needed for that route:
- `references/manuscript-framework.md` for structure, section order, display-item planning and section length.
- `references/literature-intake.md` before full manuscript writing, especially when the target is SCI, Nature/Cell/Science-family, Nature Plants, Molecular Plant, The Plant Cell, PNAS or another ambitious venue.
- `references/section-writing-playbook.md` for title, abstract, introduction, Results, Discussion, Methods or conclusion drafting.
- `references/high-impact-journal-style.md` for Nature/Cell/Science-family, Nature Plants, Molecular Plant, PNAS-level framing, or broad-audience summary paragraphs.
- `references/terminology-ledger.md` when a project has repeated terms, abbreviations, sample names, markers, genes, datasets, methods or mixed Chinese-English notes.
- `references/writing-style.md` when polishing language, claims, citations and sentence-level scientific tone.
- `references/figure-layout.md` when building or revising figures, captions, source-data links or multi-panel composites.
- `references/plant-breeding-package.md` for plant breeding, crop genomics, genotype-phenotype, QTL/GWAS, functional-marker, germplasm-introgression or candidate-gene manuscripts.
- `references/citation-data-availability.md` for citation support, DOI/reference checks, bibliography export planning, data availability statements, repository plans and FAIR checks.
- `references/reviewer-risk-audit.md` for pre-submission critique, likely reviewer objections, editorial risk, rebuttal planning or revision triage.
- `references/submission-qc.md` before final delivery.

## Core Workflow

1. Define the target paper before writing.
   - Identify article type, target journal, required section order, word limits, display-item limits, reference style and submission materials.
   - If the user provides journal instructions or reference papers, inspect them first and extract structure, density, figure style, caption style and argument rhythm.
   - Write a one-sentence argument contract before drafting: in what system, what advance is shown, by what approach, with which evidence, and within what boundary.
   - Match the title and framing to the actual evidential object. Do not claim that one data layer explains an entire process when it supports a narrower molecular, spatial or validation layer.
   - When project history forces one data type or angle to be the manuscript focus, do not disclose internal constraints; frame the paper around that layer's intrinsic contribution and defensible scope.
   - Preserve raw files; write generated manuscripts, figures, tables and packages under a dedicated output folder.

2. Build the evidence map.
   - Inventory all available data, analyses, figures, notes, references and prior drafts.
   - Separate measured results, derived statistics, interpretation, limitations and future work.
   - Build or update a terminology ledger for canonical gene names, sample labels, trait abbreviations, datasets, methods, statistical terms and forbidden variants before drafting substantial prose.
   - Identify the central research question and 3 to 6 result themes that can be supported by data.
   - Reconstruct the study design and core objective before ranking samples, genes, pathways, mechanisms or visual themes.
   - Adjudicate competing analysis routes by the experimental design, controls, statistical assumptions and biological validity; do not present a manuscript as "old version versus new version" or ask the paper to justify an internal analysis switch.
   - Treat earlier drafts, previous figures, user-noticed examples and named candidate types as hypotheses to audit, not as evidence that those items are intrinsically important.
   - Evaluate all plausible mechanism classes under the same evidence standard. A mechanism becomes central only when the data, design and literature support that role.
   - Keep adjacent projects, modules and unpublished side stories out of the main manuscript unless the user explicitly asks to integrate them.
   - Preserve evidence order: primary study result, then derived prediction or prioritization, then external validation or support.
   - Use external datasets as validation/support in normal scientific prose; do not make "overlap with a reported dataset" the Results narrative unless the overlap is itself the planned method.
   - When adjacent species, public datasets or previous studies are available, use the primary study as the main story and deploy external data for module context, conservation tests, validation or contrast after the core analysis is stable.

3. Learn the field before locking the story.
   - For high-ambition full manuscripts, complete a documented literature intake before drafting: normally at least 200 directly relevant papers screened, with full-text reading notes for the core set unless the user explicitly asks for a smaller scoping task.
   - Do not claim that a manuscript is field-ready if the literature intake is incomplete. In that case, deliver a literature plan, search strategy, reading matrix, outline and writing blockers rather than a polished final manuscript.
   - Prioritize full text, figures, methods, supplementary tables, dataset accessions and cited methods over abstract-only reading.
   - Extract common analysis types, figure architectures, result-section rhythm, claim boundaries and validation expectations from the literature. Reuse only analyses that match the current design and data.
   - Study at least 20 high-impact figure examples when asked to target Nature Plants, Molecular Plant, Cell/Nature/Science-family, The Plant Cell or equivalent venues; record what each example teaches about panel logic, density, hierarchy and caption style, not wording or design imitation.
   - Convert literature learning into a story map before writing: central question, design logic, figure sequence, main claim, alternative explanations, validation boundary and novelty statement.

4. Design the manuscript around figures.
   - Use figures as the spine of Results when the dataset supports it.
   - Each main figure should support one result theme, with panel count determined by evidence needs rather than a forced number.
   - Keep tables for dense values, models, sample metadata, statistics, supplementary material and source data.
   - Build figures from the manuscript's evidence map, not from whatever plot exists already. Existing plots can supply data or cautionary examples, but they should not lock the final visual logic.
   - If AI image generation is used for visual exploration, treat generated images as style concepts only. Redraw data-bearing panels from traceable source data before manuscript delivery.

5. Write as a paper, not as a report.
   - Default section order: Title, Abstract with keywords, Introduction, Results, Discussion, Methods, Data availability, Acknowledgements, Author contributions, Competing interests and References.
   - For full research articles unless the journal says otherwise, aim for an Abstract of about 220 to 280 words and an Introduction/background of about 900 to 1,500 words; do not deliver a short report-style introduction when the user requested a manuscript.
   - Draft in evidence-first order when building a full research article: Results and figures, then Introduction/Discussion framing, then title and Abstract.
   - Give each paragraph one job: context, gap, approach, result, comparison, mechanism, implication or limitation. Split paragraphs that try to do two jobs at once.
   - Results should report observations first, then end each subsection with one restrained scientific conclusion.
   - Discussion should interpret mechanisms, connect literature, state limitations and define functional or practical follow-up without presenting future technical steps as the scientific goal.
   - For English manuscripts, remove non-English characters from main text, figure labels, tables and DOCX XML unless the journal explicitly allows them.
   - State the positive scientific finding directly. Avoid rhetorical reversals such as "not X but Y", "rather than", "cannot prove", process defenses, and sentences that explain why an analysis route was chosen.
   - Keep method adjudication, sensitivity screens and discarded analysis routes in internal QA or supplementary methods only when they are scientifically necessary; do not make them the manuscript's narrative engine.

6. Polish and package.
   - Use `references/manuscript-framework.md` when designing structure or section length.
   - Use `references/literature-intake.md` before drafting high-ambition full manuscripts or when the user requests a literature-grounded paper.
   - Use `references/writing-style.md` when polishing language, claims, citations and scientific tone.
   - Use `references/figure-layout.md` when building or revising figures.
   - Use `references/plant-breeding-package.md` for plant breeding, crop genomics, genotype-phenotype, QTL/GWAS, functional-marker, germplasm-introgression or candidate-gene manuscripts.
   - Use `references/submission-qc.md` before final delivery.
   - Run a pre-submission risk audit for ambitious manuscripts: likely editor concern, likely methods/statistics concern, likely field-specialist concern and what evidence or wording reduces each risk.
   - Before packaging, reconcile manuscript claims with source data, claim banks, figure registry, captions and source workbooks. Update stale intermediate files instead of reusing prior-draft numbers.
   - If figures or modules are removed or renumbered, update every reference in text, captions, source data, figure registry, DOCX/build scripts, package manifests and QC scripts.
   - Exclude obsolete module outputs, old filenames and out-of-scope source sheets from clean submission packages.
   - Keep key stage results, processed matrices, source data, figures, reports and manuscript packages synchronized to the working output directory. Do not copy large raw or intermediate files into manuscript packages unless explicitly required.
   - Rebuild all outputs from scripts after revising text, figures or package contents.

## Figure Rules

Minimum figure checks:
- No duplicate panel letters; one letter corresponds to one data panel.
- No internal plot titles when captions describe panels.
- Axis labels sit close to plots without excessive margin.
- Font sizes remain legible in the final composite figure, not only in source panels.
- Legends do not cover data.
- Colors are restrained, journal-appropriate and semantically consistent.
- Source data are traceable for every panel.

## Writing Rules

Minimum writing checks:
- Do not overclaim causality from correlation, association, enrichment or exploratory screens.
- Do not frame a technical assay, primer design, screenshot, code step or data-cleaning step as a biological or scientific result.
- Avoid self-descriptive prose such as "this draft", "as requested", "kept out", "not shown", "we followed the user's instructions" or "the figure shows a story".
- Remove internal process details, local paths, TODO placeholders, old version names, author-side rationale and project-management language from manuscript text, captions, tables and package files.
- Avoid repeated filler words such as `layer`, `landscape`, `robust`, `comprehensive`, `rather than`, `not only`, `not merely`, `cannot prove` and excessive hyphenated phrasing unless scientifically necessary.
- Verify every in-text citation maps to a reference-list entry and every listed reference is cited.
- Verify every numerical claim against a traceable source file rather than a previous draft.

## Revision and QC Rules

When revising an existing paper:
- Read the whole manuscript after structural edits and check title, Abstract, Results, Discussion, Methods, captions and source data for the same story boundary.
- Search for forbidden or removed-topic terms, internal notes, stale figure numbers and stale result numbers before final delivery.
- Confirm each main figure has a matching caption, source-data entry and registry record.
- For English manuscripts, check DOCX headings, inline figure count, zip integrity and unexpected CJK characters.
- Perform at least three focused revision passes when the user asks for a polished manuscript: scientific logic and claim scope; figure-text-caption-source consistency; language, formatting, citations and forbidden-phrase cleanup.
- If layout rendering or visual inspection cannot be performed because required tools are missing, state that limitation in the delivery notes.

## Validation Script

When a manuscript package exists, run:

```powershell
& python .\scripts\validate_research_package.py `
  --package "path\to\submission_package" `
  --docx "path\to\manuscript.docx" `
  --zip "path\to\submission_package.zip"
```

Use `--forbidden "term1,term2"` for project-specific terms that must not appear in final text or package files.

## Output Standard

Finish with concise delivery notes:
- what changed,
- where the final manuscript, figures, tables and package are,
- which checks passed,
- any unresolved journal-specific or author-side items.
