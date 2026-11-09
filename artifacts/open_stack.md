# open stack

Problems that block the top goal or make a recorded claim untrue, most urgent first. Severity is `blocker` (the top goal cannot advance) or `major` (a recorded claim is untrue). P-1 is major because the audit requires a loaded agents manual (match-workspace-hygiene, Wrap up step 5). Owner decisions are in evidence/rulings_pending.md; each todo item that needs one names its item and waits. Delete a row when it is resolved; the evidence goes in the commit message.

| ID | Severity | Symptom | Evidence | Fix item |
|---|---|---|---|---|
| P-1 | major | The agents manual is not read at session start: artifacts/agents.md exists, but no root CLAUDE.md or AGENTS.md loads it | The audit reports "agents file not loaded" as major; the repo root has no CLAUDE.md or AGENTS.md (checked with ls) | T-1 |
