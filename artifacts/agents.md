# agents

Bastos lab site (bastoslab.github.io): a static GitHub Pages site with no build step, used by lab members and readers.

## Layout

- index.html, about/, contact/, lab/: public pages. Lab cards come from assets/projects.js and assets/lab.js; images are in assets/cards/.
- collab/bastos-chao/: the collaboration graph page.
- slides/jaxfne/, slides/jnwb/: slide pages.
- assets/style.css: light and dark theme tokens. assets/site.js: zoom and parallax.
- artifacts/tools/: add_card.py and the PowerShell helpers. artifacts/add-a-*.md: how-tos.
- evidence/tools/style_check_v2.py: style checker (Playwright and Pillow); compares a baseline export with the lane at 375, 390, 768 and 1440 px.

## Commands and gates

- Serve the folder with any static server. There is no build step.
- Style check: `git archive <base> | tar -x -C <tmp>`, then `python evidence/tools/style_check_v2.py <tmp> . <out> <page> ...`. It prints `STYLE CHECK v2: N cases, M regressions`.
- Audit: `python <match-workspace-hygiene>/scripts/artifacts_check.py .`. ACCEPT needs zero majors.

## Laws and stop conditions

- Never push to main, merge, delete, or publish without an owner go.
- Push only `_temp_` branches, and only after the checks you ran pass.
- Never commit a secret or a URL that carries a token.
- Stop and ask when an owner ruling is needed (evidence/rulings_pending.md).

## Working state

Working state lives in this folder: `goal_stack.md`, `todo_stack.md`, `open_stack.md`, `fact_stack.md`, `state.md`, `memory.md`.

- Start: read `open_stack.md` first, then the top goal and the top of `todo_stack.md`. Trust git over the `state.md` stamp.
- Problems: a row in `open_stack.md` with evidence, and its fix at the top of `todo_stack.md`.
- Facts and goals: propose them with evidence; the owner writes them.
- End: commit the work, overwrite `state.md` with the new commit's stamp, run the checker of the `match-workspace-hygiene` skill, commit `artifacts/`, push.
