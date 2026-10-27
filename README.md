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

## Edit page text

- Home and About: the `<section class="panel">` blocks in `index.html` and `about/index.html`. Each panel is one scroll-zoom step. When you add or remove a panel, update `--n` on the `.zoom` element to the new panel count.
- Contact: `contact/index.html`.
- Colours for both themes: the two `:root` blocks at the top of `assets/style.css`.

## Publish

1. In the `bastoslab` GitHub org, create a public repo named exactly `bastoslab.github.io`.
2. Push this folder to its `main` branch:
   ```bash
   git remote add origin https://github.com/bastoslab/bastoslab.github.io.git
   git push -u origin main
   ```
3. In the repo, go to Settings → Pages and set the source to "Deploy from a branch", branch `main`, folder `/ (root)`.
4. The site goes live at https://bastoslab.github.io/ after a minute or two.

Project sites hosted under other accounts (for example `hnxj.github.io/jaxfne`) are only linked from the Lab page; they are not affected by this repo.
