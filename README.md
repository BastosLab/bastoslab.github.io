# bastoslab.github.io

Static site for the Bastos Lab (Home / Lab / About / Contact). Plain HTML, CSS and JS; there is no build step.

## Preview locally

Open `index.html` in a browser. No server is needed.

## Add or change a lab card

Edit [assets/projects.js](assets/projects.js) and append one object to `window.PROJECTS`:

```js
{name: "my-tool", description: "One-line description.", url: "https://example.github.io/my-tool/", tags: ["docs"]},
```

`tags` is optional. Cards appear on the Lab page in list order. Commit and push; nothing else needs editing.
For the full flow from a new repo to a card, see [artifacts/add-a-project.md](artifacts/add-a-project.md). For slide decks, see [artifacts/add-a-slide.md](artifacts/add-a-slide.md).

## Edit page text

- Home and About: the `<section class="panel">` blocks in `index.html` and `about/index.html`. Each panel is one scroll-zoom step. When you add or remove a panel, update `--n` on the `.zoom` element to the new panel count.
- Contact: `contact/index.html`.
- Colours for both themes: the two `:root` blocks at the top of `assets/style.css`.

## Publish

Push to `main`; GitHub Pages (Settings, Pages, branch `main`, folder `/ (root)`) rebuilds https://bastoslab.github.io/ in a minute or two.
Remote: `git@github.com:BastosLab/bastoslab.github.io.git`. See `artifacts/skills/edit-bastoslab-site/SKILL.md` for the SSH key command.

Project sites hosted under other accounts (for example `hnxj.github.io/jaxfne`) are only linked from the Lab page; they are not affected by this repo.
