# Release Checklist

Use this checklist before making the repository public or sharing a release archive.

## Repository Review

- [ ] Repository stayed private during testing and review.
- [ ] First public release version is `1.0.0`, matching the root `VERSION` file.
- [ ] Public tag, if created, is `v1.0.0`; internal optimization commits and demo-improvement milestones are not used as release versions.
- [ ] README contains no local absolute paths or personal machine details.
- [ ] Demo data are clearly marked synthetic.
- [ ] Demo references use the target journal style and all metadata are verified before any public release.
- [ ] README explains that real high-ambition manuscripts require documented literature intake and a 200-paper full-text reading matrix when scope requires it.
- [ ] No real unpublished manuscript, figure, dataset, project name, institution name, collaborator name or reviewer content is included.
- [ ] LICENSE and USE_POLICY are present and consistent.
- [ ] The license is described as source-available non-commercial, not OSI open source.

## Skill Package Review

- [ ] `research-paper-builder/` validates with `quick_validate.py`.
- [ ] Packaging is run from the skill root, not from the Git repository root.
- [ ] The `.skill` archive does not include `.git`, `dist`, cache, temporary files or demo-only materials unless intentionally included.
- [ ] All referenced files in `SKILL.md` exist.
- [ ] The three demo main figures are included and link correctly from README and manuscript draft.

## Privacy And Secret Scan

- [ ] Scan for secrets and credentials.
- [ ] Scan for local user-home paths.
- [ ] Review README, examples and generated output manually.
- [ ] If a leak is found, remove it from Git history before public release.

## Final Approval

- [ ] User has reviewed the private repository.
- [ ] User explicitly approves public sharing of `1.0.0`.
- [ ] Release notes state version `1.0.0`, the license and the non-commercial use boundary.
