# todo stack

Top = next. Problem fixes first (T-1), then ready items, then items blocked by an owner ruling (evidence/rulings_pending.md, item numbers in the blocked-by text). Prerequisites sit above dependents. Delete an item when it is done; git holds history.

## now

- T-1 Add a loading pointer for artifacts/agents.md (fix for P-1). Options are in the ruling. Closes when: the answer is written in evidence/rulings_pending.md, the chosen root file (CLAUDE.md or AGENTS.md) contains `@artifacts/agents.md` or the pointer, and `python <match-workspace-hygiene>/scripts/artifacts_check.py .` prints VERDICT ACCEPT. Blocked by: owner ruling, evidence/rulings_pending.md item 1.
- T-2 Fix the usage text in artifacts/tools/add_card.py (lines 10 and 13 show assets/preview.png; projects.js and the cards use assets/cards/<name>.jpg). Closes when: `grep -c "assets/preview.png" artifacts/tools/add_card.py` prints 0 and the usage names assets/cards/<name>.jpg. Blocked by: none.
- T-3 Run the style checker at 375 px on index.html, about/index.html, contact/index.html, lab/index.html, collab/bastos-chao/index.html, slides/jaxfne/index.html and slides/jnwb/index.html. Base: export commit 5419bb9 with `git archive 5419bb9 | tar -x -C <tmp>`. Closes when: `python evidence/tools/style_check_v2.py <tmp> . <out> <the seven pages>` prints 0 regressions. Blocked by: none.
- T-4 Apply the footer ruling (tap-target padding, 390 px). Closes when: the answer is written and the checker prints 0 regressions for index.html, about/index.html, contact/index.html and lab/index.html at 390 px with the ruled option. Blocked by: owner ruling, evidence/rulings_pending.md item 2.
- T-5 Apply the collab bridge ruling (window.__drawBridge). Closes when: the answer is written, `grep -n "__drawBridge" collab/bastos-chao/index.html` matches the ruled option, and the checker prints 0 regressions for collab/bastos-chao/index.html. Blocked by: owner ruling, evidence/rulings_pending.md item 3.
- T-6 Apply the origin URL ruling. Closes when: the answer is written and `git remote get-url origin` shows the ruled URL. Blocked by: owner ruling, evidence/rulings_pending.md item 5.
- T-7 Apply the merge ruling. Merge only on an owner go, never on an agent's own decision. Closes when: the answer is written and, if merged, `git merge-base --is-ancestor 9cea4ce main` exits 0. Blocked by: owner ruling, evidence/rulings_pending.md item 4.
- T-8 Owner fills artifacts/goal_stack.md and artifacts/fact_stack.md (opened from templates; the owner writes them) and reviews artifacts/agents.md (drafted in this step). Closes when: the audit shows no unfilled-marker finding for the two stacks. Blocked by: owner content.
