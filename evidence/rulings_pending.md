# Owner rulings pending

Decisions the owner answers, one number each. None is an open row: no row blocks the top goal or makes a recorded claim untrue, so each todo item that needs one names its item number and waits. Write the answer after "Answer:". Figures marked reported come from a run and were not re-measured in this step. All items concern branch _temp_bastos-style at 9cea4ce.

## 1 agents manual is not loaded (P-1, major)
Symptom: artifacts/agents.md is not read at session start; the repo root has no CLAUDE.md or AGENTS.md.
Evidence: artifacts_check.py reports "agents file not loaded" (major); `ls` of the repo root shows neither file.
Options, ranked: 1 root CLAUDE.md containing `@artifacts/agents.md` (the file Claude Code reads). 2 root AGENTS.md with a pointer to artifacts/agents.md (for tools that read AGENTS.md). 3 leave it unloaded: the audit keeps a major.
Question: which file?
Answer:

## 2 footer grows at 390 px
Symptom: the footer grows 48 px at 390 px from link tap-target padding (reported).
Evidence: assets/style.css:70 `footer a{display:inline-block;padding:12px 0;...}`.
Options, ranked: 1 keep: tap targets stay at least 44 px. 2 reduce the padding: targets drop below 44 px.
Question: keep the footer?
Answer:

## 3 collab window.__drawBridge
Symptom: window.__drawBridge is kept; draw is inside the IIFE, so moving the listeners out would throw a ReferenceError (reported).
Evidence: collab/bastos-chao/index.html:703 (`window.__drawBridge=draw`); the IIFE closes at line 707; callers at lines 708-709.
Options, ranked: 1 keep and document: no code change. 2 restructure the IIFE so draw is reachable: removes the window global, moves the listeners, and risks the ReferenceError above.
Question: restructure, or keep?
Answer:

## 4 merge to main
Symptom: branch not merged; the header fix (9cea4ce) is not on main.
Evidence: 9cea4ce is not an ancestor of main at 5419bb9 (`git merge-base --is-ancestor` exits 1).
Options, ranked: 1 merge after an owner go. 2 hold: main stays at 5419bb9.
Question: merge, or hold?
Answer:

## 5 origin URL
Symptom: pushes print a notice that the repository moved to git@github.com:BastosLab/bastoslab.github.io.git (reported).
Evidence: `git remote -v` shows origin git@github.com:bastoslab/bastoslab.github.io.git (SSH); `git ls-remote origin` succeeds.
Options, ranked: 1 update origin to the location GitHub reports. 2 keep the current origin: it resolves now.
Question: update origin?
Answer:
