# Research Paper Builder Skill

Private test repository for the `research-paper-builder` Codex skill.

The actual skill root is:

```text
research-paper-builder/
```

Validate:

```powershell
python C:\Users\xiaoj\.codex\skills\skill-creator\scripts\quick_validate.py .\research-paper-builder
```

Package for local testing:

```powershell
$env:PYTHONIOENCODING='utf-8'
python C:\Users\xiaoj\.codex\skills\skill-creator\scripts\package_skill.py .\research-paper-builder .\dist
```

Keep this repository private until the skill is reviewed and approved for sharing.
