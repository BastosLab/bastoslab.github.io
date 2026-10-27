---
name: edit-bastoslab-site
description: Maintain the Bastos Lab GitHub Pages site (bastoslab.github.io) - add or edit Lab cards, edit Home/About/Contact pages, tune the scroll-zoom effect, change themes, logo or favicon, preview, and publish. Use when asked to change anything on this site.
---

# Editing the Bastos Lab site

Plain static HTML/CSS/JS. No build step, no dependencies. GitHub Pages serves the repo root from `main`.
Run tools from the repo root in Windows PowerShell 5.1.

## Layout

| Path | What it is |
|---|---|
| `index.html`, `about/index.html` | Zoom pages: a `.zoom` track holding a sticky `.stage` of `.panel` sections |
| `contact/index.html`, `lab/index.html` | Normal pages (`<main class="page">`), no panel stack |
| `assets/projects.js` | The Lab card list (`window.PROJECTS`); the only file to touch to add a card |
| `assets/lab.js` | Renders the cards (uses `textContent` only, so descriptions cannot inject HTML) |
| `assets/site.js` | Theme toggle and the zoom/scroll effect |
| `assets/style.css` | Both themes, layout, cards |
| `assets/logo.png`, `assets/favicon.png` | Header logo; symbol-only tab icon |

Each page repeats the same header and footer (no templating). A nav or footer change means editing all four pages.

## Add or change a Lab card

```powershell
.\artifacts\tools\add-card.ps1 -Name "foo docs" -Description "The documentation of foo for <purpose>." -Url "https://foo.readthedocs.io/" -Tags docs
```

Or append one object to `assets/projects.js` by hand: `{name, description, url, tags}`. Cards render **two per row, in list order**
(one column under 600 px), so keep a project's docs card and replications card adjacent.
House wording: docs cards say "The documentation of X for <purpose>."; replication cards say
"The replication and validation records of X." Do not use the word "dashboard" on the site.

## Edit page text

- Zoom pages: each `<section class="panel">` is one scroll step. **After adding or removing a panel, set `--n` on the
  `.zoom` element (`style="--n:6"`) to the new panel count**, or the scroll track will be the wrong length.
- Keep panel text short: panels are fixed to one viewport and clipped (`overflow:hidden`), so long content is cut off.
- Contact intentionally shows no email; it links to bastoslabvu.com and lists the postal address.
- Content originates from https://www.bastoslabvu.com/ (mission, research areas, recruiting, address). Do not invent
  members, publications or funding.

## The zoom effect (`assets/site.js`, `.zoom` / `.stage` / `.panel` in `style.css`)

- `.zoom` has height `--n x 100vh`; `.stage` is `position:sticky` and one viewport tall; panels are stacked absolutely inside it.
- Progress `p` = `-zoom.getBoundingClientRect().top / innerHeight`, clamped to `[0, n-1]`. Panel `i` is centred when `p == i`.
- With `d = p - i`: scale is `1 + 1.8*d` when `d > 0` (panel grows past the viewer) and `max(0.1, 1 + 0.45*d)` when `d < 0`
  (upcoming panel starts small). Opacity is `clamp(1 - 1.7*|d|, 0, 1)`; fully faded panels get `visibility:hidden`, and
  only panels within `|d| < 0.5` receive pointer events. To tune: change `1.8` (zoom-out speed), `0.45` (entry size), `1.7` (fade).
- The background rings (`.bg::before`) scale by `1 + 0.55 * scrollY/innerHeight` via the `--sp` CSS variable.
- Lab cards use `.zin`: scale `0.8 -> 1` and fade in as they enter the lower 55% of the viewport.
- Fallbacks: the zoom CSS only applies under `html.js`. The inline script in each `<head>` adds that class before first
  paint, so without JavaScript the panels just stack as normal sections. `prefers-reduced-motion` makes `site.js` remove
  the class again, giving the same stacked layout. Keep the `classList.add("js")` call in every page's head script, and
  do not hard-code `class="js"` in the markup.
- Scale uses `transform` and `opacity` only (no layout work per frame); the handler is throttled with `requestAnimationFrame`.

## Themes

Two `:root` blocks at the top of `style.css`: dark (black / purple / gold) and light (white / purple / gold). The choice is
stored in `localStorage` (wrapped in try/catch) and defaults to the OS setting; an inline script in each `<head>` sets it
before first paint. In light mode gold is accent-only (poor contrast on white); text and links use purple. The logo has
white lettering on a transparent background, so light mode puts it on a dark purple badge (`:root[data-theme="light"] .brand`).

## Logo and favicon

`assets/logo.png` comes from bastoslabvu.com (transparent PNG, white lettering). After replacing it, regenerate the
symbol-only tab icon (crop left of the gap before the text, on a dark rounded square):

```powershell
.\artifacts\tools\make-favicon.ps1
```

The result is similar but not byte-identical to the committed icon; look at it before committing.

## Preview and verify

```powershell
.\artifacts\tools\preview.ps1 -Page lab/index.html -Theme light -Height 1300 -Out $env:TEMP\lab.png
```

Then open the PNG. Or just open `index.html` in a browser (no server needed). The screenshot tool only captures the top of a page.
**Verify the zoom effect by scrolling in a real browser, in both themes**; scrolled headless captures were unreliable here.
Also check phone width (cards collapse to one column) and that the theme toggle works.

## Publish

Remote is `git@github.com:BastosLab/bastoslab.github.io.git` (the org was renamed from bastoslab; the old URL redirects).
Pushing from the original machine used the SSH key `~/.ssh/id_ed25519_github_pypeline`, which is not a default key name:

```bash
GIT_SSH_COMMAND="ssh -i ~/.ssh/id_ed25519_github_pypeline -o IdentitiesOnly=yes" git push origin main
```

Pages (Settings -> Pages, branch `main`, root) rebuilds in a minute or two. Commit and push only when asked.
