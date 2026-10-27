# Add a slide deck to the Lab page

A "slide" here is an HTML slide deck: reveal.js, Slidev, Marp, or your own JS/TS/TSX app built with Vite. Whatever the
source language, the build output is static files with an `index.html`, and that is all GitHub Pages and a Lab card need.
The card just links to the deck's URL, so a deck is still "gh-pages", exactly like any other project.

Pick where the deck lives:

| | A. Its own repo (recommended) | B. Inside this repo |
|---|---|---|
| Deck URL | `https://<username>.github.io/<repo>/` | `https://bastoslab.github.io/slides/<name>/` |
| Good for | A deck with its own source, history, or build | A small deck with no build, or built output you commit |
| Publish | Follow [add-a-project.md](add-a-project.md) steps 1-2 | Copy the built deck into `slides/<name>/` and push this repo |

## A. Deck in its own repo

1. Make the repo and publish the built deck to `gh-pages`: [add-a-project.md](add-a-project.md), steps 1 and 2.
2. **Set the deck's base path to `/<repo>/`** before building, or its scripts and styles will 404 on Pages. Common settings
   (confirm against each tool's docs):
   - Vite (JS/TS/TSX): `base: '/<repo>/'` in `vite.config`.
   - Slidev: `slidev build --base /<repo>/`.
   - Marp CLI: `marp deck.md -o index.html` (single self-contained file; no base path needed).
   - reveal.js written by hand: relative paths, no setting needed.
3. Open `https://<username>.github.io/<repo>/` and check it loads and the keyboard arrows work.
4. Add the card (step C below).

## B. Deck inside this repo

1. Build the deck, then copy the output so it is served at `slides/<name>/index.html`:
   ```powershell
   New-Item -ItemType Directory -Force slides\my-talk | Out-Null
   Copy-Item path\to\build\* slides\my-talk -Recurse
   ```
2. Set the deck's base path to `/slides/my-talk/` (same tools as above), or use relative paths.
3. Preview by opening `slides/my-talk/index.html` in a browser, or screenshot it:
   ```powershell
   .\artifacts\tools\preview.ps1 -Page slides/my-talk/index.html -Out $env:TEMP\deck.png
   ```
4. Add the card (step C), with the URL `https://bastoslab.github.io/slides/my-talk/`.

Note: `preview.ps1` and the repo's zoom/theme scripts do not apply to a deck; a deck keeps its own look. Large built decks (images,
fonts) count against the repo size, so prefer A for anything heavy.

## C. Add the card

```powershell
.\artifacts\tools\add-card.ps1 -Name "my-talk slides" -Description "The slides of my-talk." -Url "https://bastoslab.github.io/slides/my-talk/" -Tags slides
```

For option A, use the deck's own URL instead. Suggested wording: "The slides of <talk title>." with the tag `slides`
(adjust the wording to taste in `assets/projects.js`). Cards show two per row in list order, so put a project's cards next
to its slides card. Do not use the word "dashboard". Then check `lab/index.html` with `preview.ps1`, commit and push.

## Check list

- The deck URL loads in a private window (no cached or logged-in state).
- Arrow keys and any speaker-notes or fullscreen keys work; nothing 404s in the browser's network panel.
- The card opens the deck, not a directory listing or 404.
