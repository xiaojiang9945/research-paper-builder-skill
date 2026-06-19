# Research Paper Builder Skill

`research-paper-builder` is a Codex skill for turning research materials into a manuscript-ready package: evidence map, figure-led Results, journal-style sections, citation/data checks, reviewer-risk audit, and submission QC.

This repository is currently a **private test repository**. Keep it private until the skill, examples, and license are reviewed.

## What It Helps With

- Plan a research manuscript from raw notes, figures, tables, references, and prior drafts.
- Build an evidence map before writing, so claims stay tied to data.
- Require a documented literature-intake phase before high-ambition full manuscript writing.
- Design a figure-led Results structure for journal-style papers.
- Polish title, abstract, introduction, Results, Discussion, Methods, captions, and Data Availability.
- Check terminology consistency, citation/reference consistency, source-data traceability, and submission package hygiene.
- Maintain a manuscript passport for full-package work so long projects keep their target journal, literature status, evidence map, figure registry, claim checks, author actions, and validation log synchronized.
- Verify whether citations actually support manuscript claims, not only whether the references exist.
- Keep process notes, QC gates, passports, and author actions outside formal manuscript text and figures.
- Run a pre-submission reviewer-risk audit before sharing a draft.

## Repository Layout

```text
research-paper-builder-skill/
+-- research-paper-builder/          # Codex skill root
|   +-- SKILL.md
|   +-- agents/
|   +-- references/
|   +-- scripts/
+-- examples/
|   +-- synthetic-wheat-study/        # runnable synthetic wheat demo input and output
+-- AGENTS.md                         # repo-level editing and validation instructions
+-- LICENSE
+-- USE_POLICY.md
+-- SECURITY.md
+-- README.md
```

## Operating Principles

- Start with route selection: plan-first, full package, section-only, revision, figure package, citation check, format-only, reviewer-risk audit, or rebuttal planning.
- For ambitious full manuscripts, require documented literature intake before polished drafting. If the 200-paper full-text standard is not met, output a literature plan, reading matrix, outline, and blockers instead of pretending the manuscript is field-ready.
- Treat user files, source data, and verified literature as the factual source of truth. Missing methods, data, citation locators, accessions, funding, author details, or permissions become author actions.
- Choose figures from the actual data and result question. Rich visuals are welcome only when the data support them.
- Before committing repository changes, follow [AGENTS.md](AGENTS.md) for validation and privacy checks.

## Quick Demo

The demo uses runnable wheat-style example data. It is designed to show a publication-scale output shape and a reproducible operation chain, not to make a biological claim.

Example prompt:

```text
Use the research-paper-builder skill on examples/synthetic-wheat-study/.
Target a wheat salt-response research article package rather than a short report.
Before writing, produce a literature-intake status note. For a real manuscript, require a 200-paper
full-text reading matrix after documented search and screening.

Run examples/synthetic-wheat-study/scripts/build_demo.py, then build a formal manuscript-style package with
three white-background six-panel main figures, figure captions below each figure, figure-led Results,
candy-colour highlights on premium-gray axes and grid lines, Cartopy/Natural Earth map rendering when available, larger publication-readable fonts and strokes,
approximately 250-word Abstract with 5-7 keywords directly below it,
approximately 1,200-word Introduction/background in fewer developed paragraphs, at least 30 Nature-style numbered references,
citation-reference audit, Data Availability statement, reviewer-risk audit, five-pass QC report, and package manifest.
```

Expected demo output is already included under:

```text
examples/synthetic-wheat-study/output/
```

Start with:

- [Demo overview](examples/synthetic-wheat-study/README.md)
- [Synthetic wheat input data](examples/synthetic-wheat-study/input/synthetic_wheat_germination_data.csv)
- [Demo build script](examples/synthetic-wheat-study/scripts/build_demo.py)
- [Example manuscript draft](examples/synthetic-wheat-study/output/manuscript_draft.md)
- [Example Figure 1](examples/synthetic-wheat-study/output/figures/figure1_geography_germination_vigour.svg)
- [Example Figure 2](examples/synthetic-wheat-study/output/figures/figure2_physiology_matrix.svg)
- [Example Figure 3](examples/synthetic-wheat-study/output/figures/figure3_transcript_and_integration.svg)
- [Example five-pass QC report](examples/synthetic-wheat-study/output/qc/five_pass_qc_report.md)
- [Example citation-reference audit](examples/synthetic-wheat-study/output/citation_reference_audit.csv)
- [Example reviewer-risk audit](examples/synthetic-wheat-study/output/reviewer_risk_audit.md)

Real manuscript work should use verified literature and should not claim a 200-paper full-text review unless a reading matrix exists.
For real user data, choose figures from the data and result question. Do not add maps, 3D surfaces or contours unless the data contain the spatial coordinates, continuous variables or matrices needed to support those panels.

## Install Or Test Locally

Copy or symlink the skill root into your Codex skills directory:

```text
research-paper-builder/
```

Validate with the skill-creator validation script available in your Codex environment:

```bash
python path/to/skill-creator/scripts/quick_validate.py research-paper-builder
```

Package for local testing:

```bash
PYTHONIOENCODING=utf-8 python path/to/skill-creator/scripts/package_skill.py research-paper-builder dist
```

On Windows PowerShell:

```powershell
$env:PYTHONIOENCODING='utf-8'
python path\to\skill-creator\scripts\package_skill.py .\research-paper-builder .\dist
```

## Privacy And Safety

This repository should not contain:

- local absolute paths;
- private user names, email addresses, passwords, tokens, or API keys;
- unpublished project data;
- real patient, participant, collaborator, reviewer, or institution identifiers;
- manuscript drafts or figures from confidential projects.

Before sharing, run a secret/privacy scan and review [SECURITY.md](SECURITY.md).

## License

This project is released for non-commercial, lawful use only under the terms described in [LICENSE](LICENSE) and [USE_POLICY.md](USE_POLICY.md).

Because the license restricts commercial use, this is a **source-available non-commercial project**, not an OSI-approved open-source license. Commercial use requires separate permission from the copyright holder.
