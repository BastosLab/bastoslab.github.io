# artifacts/

Maintenance material for this site. Nothing here is served or needed by the pages themselves.

- `add-a-project.md`: step-by-step guide to create a repo, publish it with GitHub Pages, and add its card to the Lab page (worked example included).
- `add-a-slide.md`: how to add an HTML slide deck (reveal.js, Slidev, Marp, Vite/TSX) to the Lab page, hosted in its own repo or inside this one.
- `skills/edit-bastoslab-site/SKILL.md`: how the site is built and how to change it (cards, pages, zoom effect, themes, logo, publish). To use it as a Claude Code skill, copy that folder to `.claude/skills/` in this repo or `~/.claude/skills/`. A copy lives in `.claude/skills/` so Claude Code agents in this repo load it automatically; keep the two in sync.
- `tools/add-card.ps1`: append a Lab card to `assets/projects.js` (rejects duplicate names and non-https URLs).
- `tools/make-favicon.ps1`: rebuild `assets/favicon.png` (symbol half of the logo) after the logo changes.
- `tools/preview.ps1`: headless Edge screenshot of a page in either theme.

All tools are Windows PowerShell 5.1 scripts; `preview.ps1` needs Microsoft Edge. They work on a copy or on this checkout's own files only.
