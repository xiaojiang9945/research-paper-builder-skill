# Release Checklist

Use this checklist before making the repository public or sharing a release archive.

## Repository Review

- [ ] Repository visibility is still private during testing.
- [ ] README contains no local absolute paths or personal machine details.
- [ ] Demo data are clearly marked synthetic.
- [ ] Demo citation list is clearly marked synthetic and not presented as real literature.
- [ ] README explains that real high-ambition manuscripts require a documented literature intake rather than synthetic references.
- [ ] No real unpublished manuscript, figure, dataset, project name, institution name, collaborator name or reviewer content is included.
- [ ] LICENSE and USE_POLICY are present and consistent.
- [ ] The license is described as source-available non-commercial, not OSI open source.

## Skill Package Review

- [ ] `research-paper-builder/` validates with `quick_validate.py`.
- [ ] Packaging is run from the skill root, not from the Git repository root.
- [ ] The `.skill` archive does not include `.git`, `dist`, cache, temporary files or demo-only materials unless intentionally included.
- [ ] All referenced files in `SKILL.md` exist.
- [ ] The demo composite figure is included and links correctly from README and manuscript draft.

## Privacy And Secret Scan

- [ ] Scan for secrets and credentials.
- [ ] Scan for local user-home paths.
- [ ] Review README, examples and generated output manually.
- [ ] If a leak is found, remove it from Git history before public release.

## Final Approval

- [ ] User has reviewed the private repository.
- [ ] User explicitly approves public sharing.
- [ ] Release notes state the license and non-commercial use boundary.
