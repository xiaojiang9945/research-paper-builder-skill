# Security And Privacy

## Private Data

Do not commit:

- API keys, tokens, passwords, cookies, SSH keys, or credentials;
- local absolute paths that reveal user names, organizations, or private folders;
- confidential manuscripts, unpublished datasets, reviewer comments, or collaborator communications;
- patient, participant, student, reviewer, author, or collaborator personal data;
- journal system screenshots or submission portal exports containing private metadata.

## Recommended Checks Before Sharing

Run a local scan from the repository root:

```bash
git status --short
rg -n --hidden --glob '!.git/**' --glob '!dist/**' --glob '!*.skill' \
  '(token|password|secret|api[_-]?key|ghp_|github_pat_|/Users/[^/]+|/home/[^/]+)'
```

Also inspect:

- README and demo files for local paths;
- example outputs for real sample names, unpublished project names, or author names;
- package archives for accidental `.git`, `dist`, cache, or temporary files.

## Reporting

If you find a privacy leak or security issue, keep the repository private and remove the affected file from history before public release.
