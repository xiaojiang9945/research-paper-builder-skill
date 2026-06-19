# AGENTS.md

## Scope

These instructions apply to this repository. Follow them when editing the skill, demo, validation scripts, documentation, examples, or release package.

## Repository Layout

- `research-paper-builder/`: Codex skill root. Keep `SKILL.md` concise and place detailed operating rules in `references/`.
- `research-paper-builder/references/`: reusable manuscript, literature, citation, figure, QC, and style guidance.
- `research-paper-builder/scripts/`: deterministic package validation helpers.
- `examples/synthetic-wheat-study/`: synthetic demo input, build script, generated manuscript-style output, figures, and QC artifacts.
- `dist/`: packaged local test output. Regenerate when the skill changes.

## Editing Rules

- Preserve a public-ready repository: no private local paths, account names, unpublished user data, credentials, tokens, or real confidential manuscripts.
- Do not copy wording from external skills or documentation. Adapt ideas into this repository's own workflow and style.
- Keep formal manuscript outputs clean. Process notes, claim checks, passports, QC gates, reviewer-risk audits, and author actions belong in separate QC or planning files, not inside manuscript text or figure panels.
- Keep demo data synthetic and clearly labelled as synthetic outside the formal manuscript example.
- Add new files only when they directly improve the reusable skill or repository workflow.
- Treat the first public release as `1.0.0`. Do not use internal optimization commits, testing iterations, or demo-improvement milestones as release versions.

## Validation

Before committing meaningful changes, run the relevant checks:

```bash
python path/to/skill-creator/scripts/quick_validate.py research-paper-builder
python research-paper-builder/scripts/validate_research_package.py --package examples/synthetic-wheat-study/output --qc-results examples/synthetic-wheat-study/output/qc/qc_results.csv --min-qc-passes 5
```

If packaging changes are made, rebuild `dist/`:

```bash
PYTHONIOENCODING=utf-8 python path/to/skill-creator/scripts/package_skill.py research-paper-builder dist
```

Run a privacy scan before pushing or sharing:

```bash
rg -n "(Users[\\\\/][A-Za-z0-9._-]+|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9]{20,}|api[_-]?key|password\\s*=|token\\s*=)" . -g "!AGENTS.md"
```

## Done Means

- The skill validates.
- Demo package validation still passes when demo-affecting files change.
- Documentation and examples agree with the actual workflow.
- The root `VERSION` file matches any intended release tag.
- New guidance is actionable, scoped, and not duplicated across files.
- The git diff is reviewable and free of private information.
