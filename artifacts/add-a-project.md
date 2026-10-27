# Add a project to the Lab page

Worked example: a new project `myproject` owned by GitHub user `hnxj`. Its site will live at
`https://hnxj.github.io/myproject/` and get a card on https://bastoslab.github.io/lab/.
Replace `hnxj` and `myproject` with your own username and repo name (GitHub lowercases the username in the URL).

## 1. Make the repo (`username/repo`)

On github.com: New repository, owner `hnxj`, name `myproject`, public. (Free accounts need a public repo for Pages.)
Then clone it and add your content:

```bash
git clone git@github.com:hnxj/myproject.git
```

## 2. Publish it with GitHub Pages (`gh-pages`)

Put the built site (a folder containing `index.html`) on a branch named `gh-pages`. Commit the folder on `main`, then publish
it. For a built site in `site/`:

```bash
git add site && git commit -m "Add built site"
```
```bash
git subtree push --prefix site origin gh-pages
```

Repeat the second command after each rebuild (if it is rejected after a rebuild, push with
`git push origin $(git subtree split --prefix site):gh-pages --force`).

(Docs generators usually have a one-step deploy instead, for example `mkdocs gh-deploy`; use that if the project has one.)
If the site is plain files, you can skip the branch: put them in `docs/` on `main` and choose that folder in the next step.

Then in the repo: Settings, Pages, Source "Deploy from a branch", branch `gh-pages`, folder `/ (root)`, Save.
After a minute or two the site is at `https://hnxj.github.io/myproject/`.

**Check it loads before continuing.** Open the URL; a card pointing at a 404 looks broken to visitors.

## 3. Add the card to the Lab page

In a checkout of `BastosLab/bastoslab.github.io`:

```powershell
.\artifacts\tools\add-card.ps1 -Name "myproject docs" -Description "The documentation of myproject for <purpose>." -Url "https://hnxj.github.io/myproject/" -Tags docs
```

This appends one line to `assets/projects.js`:

```js
{name: "myproject docs", description: "The documentation of myproject for <purpose>.", url: "https://hnxj.github.io/myproject/", tags: ["docs"]},
```

Wording used on the site: docs cards say "The documentation of X for <purpose>."; replication cards say
"The replication and validation records of X." Cards show two per row in list order, so add a project's cards next to each
other. Do not use the word "dashboard".

## 4. Check and publish the Lab page

```powershell
.\artifacts\tools\preview.ps1 -Page lab/index.html -Height 1300 -Out $env:TEMP\lab.png
```

Open the PNG and confirm the card shows and the layout is intact. Then commit and push (push command in
`skills/edit-bastoslab-site/SKILL.md`, "Publish"). The card appears at https://bastoslab.github.io/lab/ after Pages rebuilds,
usually within a couple of minutes.

## Troubleshooting

- Project URL shows 404: Pages is not enabled, the branch or folder in Settings, Pages is wrong, or the first build has not finished. Check the repo's Actions tab for the Pages build.
- Project page loads but its CSS or links are broken: the site was built for the domain root. Set its base path to `/myproject/`.
- Card missing after push: Pages rebuilds can take a few minutes; hard-refresh. Make sure `assets/projects.js` still ends with `];` and every entry except the last has a trailing comma (`add-card.ps1` handles this).
