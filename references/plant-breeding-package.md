# Plant Breeding Manuscript Package

Use this reference when turning crop phenotype, genotype, marker, QTL/GWAS, transcriptome, public-expression, germplasm-introgression or breeding-practice data into a submission-ready research article package.

## Evidence Map

Start by separating evidence into five classes:
- raw measured data: phenotypes, genotypes, expression matrices, trials, color classes, pedigrees, environments;
- published or prior-study results: previously reported genes, diagnostic markers, resistant lines, cultivar releases, field summaries;
- derived statistics: correlations, group tests, marker scans, haplotypes, scores, Pareto sets, donor fractions, enrichment summaries;
- interpretation: candidate intervals, modifier models, trait tradeoffs, breeding implications;
- limitations: missing genotypes, one-environment phenotypes, uncertain gene assignment, linkage versus causality, reused published material.

Do not re-present an already published result as a new discovery. Use it as a reference class, prior evidence, validation context or known comparator, and state the new analytical scope clearly in Methods and Results.

## Topic And Story Design

For plant breeding papers, make the central question useful to both genetics and breeding:
- What phenotype matters, and how is it measured?
- Which germplasm, donor or population makes the result valuable?
- Which marker, locus, haplotype or candidate gene evidence is genuinely supported?
- Does the target trait carry a breeding cost in yield, grain weight, quality, emergence, disease resistance or other agronomic traits?
- Which lines, alleles or marker combinations are prioritized for validation?

Prefer a figure-led structure:
1. population/material and primary phenotype distribution;
2. multi-trait structure and tradeoff analysis;
3. genome-wide, candidate-region or sensitivity scans;
4. functional-marker, candidate-gene or public-expression support;
5. line ranking, donor-introgression profile or breeding index.

Keep tables for dense statistics, accession metadata, marker lists, model summaries and supplementary source data. Avoid explanatory tables that only tell readers what the paper is doing.

## Phenotype And Trait Hygiene

Before writing, verify the biological meaning of every phenotype column with source files or notes. Do not infer a trait from a local-language initialism when a measured definition is available.

Convert local or non-English column names to standard English abbreviations in all English submission material. For wheat examples:
- TGW, thousand-grain weight;
- GL, grain length;
- GW, grain width;
- GNS or KNS only when the source definition supports grain number per spike;
- SNS, spikelet number per spike;
- PH, plant height;
- ETN, effective tiller number;
- GY, grain yield.

For sprouting/dormancy traits, use the field's accepted term, not a convenient plotting abbreviation. If the trait is an index, keep it as an index. If it is a day-specific germination percentage, label it as a percentage and describe the timing in Methods.

Use `grain` for wheat grain traits unless a journal or subfield convention requires `kernel`. Avoid mixing both terms casually.

## Existing Gene Or Marker Claims

For known genes, diagnostic markers or candidate intervals:
- distinguish direct genotyping, linked SNP support, haplotype support, expression support and literature support;
- if chip markers cannot diagnose the gene, call the result a linked haplotype or candidate interval;
- avoid phrases that imply the analysis "found" a known gene when the gene was known from prior marker work;
- do sensitivity analyses that remove or adjust for known strong classes before claiming additional loci;
- report whether non-target candidate signals remain after accounting for color, known marker status, relatedness, environment or other confounders.

Gene and QTL symbols should be italicized in manuscript text and figure labels where journal style allows. Protein names and phenotype abbreviations are usually roman unless the field convention differs.

## Multi-Trait And Breeding-Cost Analysis

For trait-improvement stories, explicitly test whether the target trait has a breeding cost:
- continuous target trait versus TGW, GL, GW, yield and spike traits;
- resistant versus susceptible groups;
- known-marker or candidate-haplotype groups;
- low-tail phenotype groups such as top or bottom 10-15 percent;
- marker-score or favorable-allele accumulation groups;
- Pareto ranking for simultaneous target resistance and agronomic performance.

Phrase direction carefully. In PHS or dormancy studies, the breeding concern is usually whether stronger resistance or dormancy reduces grain weight, grain size, emergence or yield, not whether grain weight "affects" resistance.

If the study finds no penalty, discuss it as population- and background-dependent. Do not generalize beyond donor background, elite parent, environments, grain-color class and selection history.

## Functional Annotation And Public Expression

Functional-marker files should be used to add biological context, not to overclaim mechanism. Report:
- marker position and gene/QTL label;
- allele effect and corrected significance;
- whether the signal survives sensitivity tests;
- whether the gene is expressed in relevant tissue or developmental stage;
- whether public-expression comparisons are actually designed to test the candidate.

Put accession IDs, sample series names, exact public dataset identifiers and download mechanics in Methods. Results should state the biological result directly.

## Literature And Style Matching

When the user requests reference-paper style matching, build a local literature corpus and extract:
- common section order and heading style;
- paragraph density in Introduction, Results and Discussion;
- citation placement;
- result verbs and claim strength;
- figure count, panel density, statistics notation and caption format;
- common limitations and validation language.

Use this to match scientific pacing and terminology, not wording. Do not imitate weak or overly defensive writing from poor reference papers.

## Figure Standards For Crop Genetics Papers

Figures must be readable after insertion into DOCX/PDF:
- use consistent palette and semantic color meanings across all figures;
- increase font sizes before enlarging whole panels;
- keep legends close to plots but outside data;
- avoid oversized bars and boxes; reduce bar width and use restrained fills;
- avoid large empty regions and disproportionate panels;
- show statistical annotations directly where expected: stars, adjusted q values, confidence intervals or test labels;
- verify that text, labels and panel letters do not collide;
- make multi-panel layouts visually balanced across desktop and final print scale.

For heatmaps, Manhattan-like scans, PCA plots, bar charts and boxplots, always inspect final rendered figures. A script-generated plot is not acceptable until visually checked.

## Writing Rules From Strong Plant-Breeding Papers

Write the article as research, not as a project report:
- Results begin with data and comparisons, not explanations of why the analysis was done;
- Discussion integrates 3-4 major points rather than many small headings;
- avoid self-justifying, boundary-setting or "we cannot claim X, but..." prose unless needed for scientific accuracy;
- use neutral headings such as "Candidate lines and genetic validation" instead of promotional headings;
- avoid over-selling marker-assisted deployment before validation;
- make limitations specific and connected to interpretation.

The abstract should usually be 150-250 words and contain concrete sample size, primary phenotype, major analysis classes, strongest results and a restrained conclusion.

## Package Contents

A complete package for this kind of project should include:
- manuscript DOCX and extracted plain text;
- main figures and a contact sheet;
- source data for every panel;
- processed CSV tables and a workbook with key statistics;
- scripts that regenerate analyses, figures, manuscript and cover letter;
- public-data summaries and accession notes;
- local literature/style notes if used;
- QC logs and a final zip archive.

Include a cover letter when requested. Keep it journal-neutral unless the target journal is known. The cover letter should state the manuscript title, target journal, research gap, main findings, distinction from related prior publications, originality, non-simultaneous submission, author approval, competing interests and data availability.

## Iterative QC

For high-stakes revision requests, run multiple explicit QC passes and log them. Minimum checks:
- phenotype labels and abbreviations match Methods and source data;
- no non-English characters in English manuscript DOCX XML unless required;
- no forbidden or deprecated terms introduced during revision;
- all citations match references;
- figure count matches journal or user limit;
- every figure is visually inspected after rebuild;
- gene/QTL formatting is consistent;
- manuscript, figures, scripts and zip are synchronized.
