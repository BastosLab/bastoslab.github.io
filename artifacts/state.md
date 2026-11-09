# state

Stamp: bastoslab.github.io@_temp_bastos-style@fa3d9fe · 2026-11-09

Overwritten each session. Where this file and git or a gate disagree, git and the gate win.

Lane E:/wt/bastos-style, branch _temp_bastos-style; keeper: this session (desktop app). Main checkout E:/repos/bastoslab.github.io at 5419bb9 [main].

## Works (with evidence)

- Branch _temp_bastos-style at fa3d9fe (stack evidence) on 9cea4ce (phone header clearance). Pushed in this step. Not merged: 9cea4ce is not an ancestor of main (`git merge-base --is-ancestor` exits 1).
- Phone header clearance at 390 px: commit 9cea4ce adds `.page{padding-top:152px}` inside `@media (max-width:600px)` in assets/style.css. Measured in this session: contact and lab h1 cap top 129 px to 161 px; header bottom 140 px; 1440 px unchanged.
- Style checker v2 in this session, base 5419bb9, contact, lab, index and about at 390, 768 and 1440 px, light and dark: 24 cases, 0 regressions.

## Broken or in flight

- The agents manual is not loaded at session start: no root CLAUDE.md or AGENTS.md (P-1, major; T-1 waits on ruling 1).
- 375 px render not verified for seven pages (T-3).
- artifacts/tools/add_card.py usage text names assets/preview.png (T-2).
- Footer grows 48 px at 390 px (ruling 2, T-4).
- collab/bastos-chao keeps window.__drawBridge (ruling 3, T-5).
- Pushes print a notice that the repository moved (ruling 5, T-6).
- goal_stack.md and fact_stack.md opened from templates; owner content pending. agents.md drafted here for owner review (T-8).

## Last gate results

- Style checker v2 at 390, 768 and 1440 px (24 cases): 0 regressions, this session, on 9cea4ce.
- artifacts_check.py on this tree: VERDICT REVISE. One major: the agents manual is not read at session start (P-1, T-1, ruling 1). Minors: 6 entries beyond the seven in artifacts/; goal_stack.md and fact_stack.md unfilled.

## Environment

- Origin: git@github.com:bastoslab/bastoslab.github.io.git (fetch and push); SSH, no token.
- Check base: commit 5419bb9, exported with `git archive`.

## Next action

T-2 and T-3 are ready. T-1 waits on ruling 1 (root CLAUDE.md or AGENTS.md); it clears the one audit major.
