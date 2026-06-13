# Research Paper Builder Skill

`research-paper-builder` is a Codex skill for turning research materials into a manuscript-ready package: evidence map, figure-led Results, journal-style sections, citation/data checks, reviewer-risk audit, and submission QC.

This repository is currently a **private test repository**. Keep it private until the skill, examples, and license are reviewed.

## What It Helps With

- Plan a research manuscript from raw notes, figures, tables, references, and prior drafts.
- Build an evidence map before writing, so claims stay tied to data.
- Design a figure-led Results structure for journal-style papers.
- Polish title, abstract, introduction, Results, Discussion, Methods, captions, and Data Availability.
- Check terminology consistency, citation/reference consistency, source-data traceability, and submission package hygiene.
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
|   +-- synthetic-plant-study/        # fully synthetic demo input and output
+-- LICENSE
+-- USE_POLICY.md
+-- SECURITY.md
+-- README.md
```

## Quick Demo

The demo uses a fully synthetic plant germination dataset. It is designed to show the skill output shape, not to make a biological claim.

Example prompt:

```text
Use the research-paper-builder skill on examples/synthetic-plant-study/input/synthetic_germination_data.csv.
Target a short plant-science research article. Build the evidence map, terminology ledger, figure plan,
manuscript draft, Data Availability statement, reviewer-risk audit, and package manifest.
```

Expected demo output is already included under:

```text
examples/synthetic-plant-study/output/
```

Start with:

- [Demo overview](examples/synthetic-plant-study/README.md)
- [Synthetic input data](examples/synthetic-plant-study/input/synthetic_germination_data.csv)
- [Example manuscript draft](examples/synthetic-plant-study/output/manuscript_draft.md)
- [Example reviewer-risk audit](examples/synthetic-plant-study/output/reviewer_risk_audit.md)

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
