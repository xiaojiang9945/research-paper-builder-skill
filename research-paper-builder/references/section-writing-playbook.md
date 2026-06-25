# Section Writing Playbook

Use this reference when drafting, rebuilding or diagnosing manuscript sections. Keep every section tied to the evidence map and the one-sentence argument contract.

## Full-Paper Drafting Order

For a data-driven research article, prefer this order:
1. Results and figure sequence.
2. Methods details needed to support the Results.
3. Introduction and Discussion framing.
4. Title and Abstract.
5. Data availability, acknowledgements, author contributions and competing interests.

Do not let the Introduction invent a broader promise than the Results can support.

## Paragraph Jobs

Each paragraph should perform one primary job:
- `context`: orient the reader.
- `gap`: identify the unresolved problem.
- `approach`: state what was done and why it fits.
- `result`: report an observation or analysis.
- `comparison`: contrast groups, baselines or prior work.
- `mechanism`: interpret a supported biological or technical process.
- `implication`: state what follows if the evidence holds.
- `limitation`: define the boundary of the claim.

Split paragraphs that combine unrelated jobs. Reorder paragraphs when the reader meets interpretation before evidence.

## Title

Good titles name the object and the supported advance. Avoid:
- method-only titles when the contribution is biological;
- mechanism titles without direct mechanism evidence;
- broad field claims when the study supports a narrower validation layer;
- unsupported superlatives.

When a study contains both a dominant generic background pattern and a rarer distinctive signal, put the distinctive supported advance in the title and keep the generic pattern as framing unless the generic pattern itself is the novelty. For small candidate classes, prefer bounded title verbs such as `reveals`, `marks`, `links`, `nominates`, `points to` or `is associated with`. Avoid `reshapes`, `reprograms`, `drives`, `controls` or `causes` unless direct time-course, tissue-specific, perturbation or functional data close the causal chain.

If a named class is operational, say so at first use and keep the verb strength aligned with the assay. A threshold-defined, contrast-defined, whole-tissue or stage-separated class can `mark`, `prioritize` or `nominate` candidates; it should not `gate`, `drive`, `control` or `explain` a developmental endpoint unless direct evidence supports that mechanism.

## Abstract

Use a compact progression:
1. Field problem or need.
2. Specific gap.
3. Study approach.
4. Strongest result with enough quantitative detail.
5. Bounded implication.

Write the Abstract last for full manuscripts. If a result value is not final, mark it as a placeholder instead of smoothing over the gap.

For full research articles, target about 250 words unless the journal gives a different limit. A 100-word summary is not an adequate manuscript abstract unless explicitly requested.

When the target format uses keywords, place a keyword line directly below the Abstract. Use 5-7 keywords, ordered from broad topic to specific system, trait, method or evidence layer. Do not repeat the title verbatim as the keyword list.

## Introduction

Move from field relevance to the precise gap the paper can address:
1. Why the topic matters.
2. What is known and what remains unresolved.
3. Why the current system, dataset or method is fit for the question.
4. What this study tests or resolves.

Do not overload the Introduction with methods details, local project history or defensive explanations.

For a full manuscript, build the Introduction/background as a developed literature argument, usually around 1,200 words. Each paragraph should cite the literature it depends on, and the reference list must contain exactly the cited works.

Prefer fewer developed Introduction paragraphs over many short background fragments. For manuscript-scale drafts, 4-6 paragraphs is usually a better default than a chain of brief paragraphs, provided each paragraph has a clear job and the citations still map exactly to the reference list.

## Results

Use figures as the spine when possible:
- open with the comparison or analysis;
- report the observed pattern with sample size, effect direction and key statistics;
- explain the immediate meaning;
- end the subsection with one restrained conclusion.
- For each main figure, write Results text that names panel letters and explains what each panel contributes to the result theme.
- Use result-centered subsection headings. A heading should state the biological finding or candidate claim, not the method used to obtain it. Replace headings like `Triad analysis separates...`, `Metabolomics identifies...`, `Experimental design...` or `Screening nominates...` with the supported biological result.
- Make Results headings conclusion-like, not preparatory. Avoid heading cores such as `entry point`, `links`, `points to`, `nominates`, `screening`, `scan`, `workflow`, `framework`, or `analysis` when they mainly describe a plan, bridge, or method. Use headings that state observed patterns, such as a family expanding, a branch concentrating expansion, a candidate class sharing features, a module retaining conserved anchors, a transcriptome showing detection/compartment bias, or haplotypes carrying population variation.
- Do not let the first Results subsection function as Materials and Methods. If the first analysis is a catalog or scan, title it by the resulting biological/catalog structure and put thresholds, input provenance and filtering logic in Methods.
- Read only the Results headings as a story test. The headings should progress as a coherent evidence chain from baseline repertoire, to pangenome expansion, to the distinctive branch, to conserved/divergent architecture, to candidate features, to external expression support, to bounded population variation. If they read like a chronological methods list, rebuild the outline before editing prose.
- When a rare candidate class is embedded in a larger constrained background, present the background as the discovery boundary, then the rare class, then the focused candidate, then orthogonal controls and downstream states. Do not inflate a small heterogeneous candidate set into a `module` unless the data support shared regulation, enrichment, co-expression or functional coherence.
- Use `support flags`, `co-occurring evidence` or `candidate-prioritization features` for nearby epigenetic, sRNA, methylation, TE/cis or parent-aware annotations unless the study directly tests those features as causal regulators.
- For non-paired or stage-separated omics integration, write Results as group-level compatibility, effect-direction comparison or a candidate framework. Do not imply sample-level correlation, temporal persistence or mechanistic linkage unless the design measures those quantities.
- Do not deliver text-only Results when the project has enough data for integrated figures. Create a figure plan, source data and caption even if final visual rendering is a separate task.

Do not start Results subsections with broad literature background. Do not present file conversion, primer design, plotting or data cleaning as scientific findings.

## Discussion

Organize around 3-4 major interpretive points:
- what changed scientifically;
- how the result agrees or conflicts with prior work;
- what mechanism or model is supported, and what remains unresolved;
- what practical or functional follow-up is justified.

For a full research article or submission-like draft, use at least three visible Discussion subpoints unless the target journal forbids subheadings. Each subpoint should interpret a distinct issue, such as evidence convergence, literature/mechanism fit, validation boundary or practical follow-up.

Avoid repeating every result value. Use limitations to define scope, not to weaken every conclusion.

## Methods

Methods should support reproducibility:
- materials, samples, environments and inclusion/exclusion logic;
- protocols and measurement definitions;
- statistical models, thresholds, correction methods and software versions;
- data processing steps that change biological interpretation.

Keep Methods clear but not narrative-driven. Move exploratory route comparisons to supplementary methods or internal QA unless they affect interpretation.

## Conclusion

For journals that use a conclusion, state:
- the final supported contribution;
- the evidence class that supports it;
- the practical, biological or methodological implication;
- the main boundary.

Do not add new evidence or speculative mechanisms in the conclusion.
