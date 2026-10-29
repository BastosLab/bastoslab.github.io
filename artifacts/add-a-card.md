# Add a card to the Lab page

Cards appear on the Lab page (`/lab/`) in two distinct sections:
- **Top**: Webpages (tools, docs, software, replication sites)
- **Bottom**: Presentations (slides, talks)

Each card displays:
1. **Image**: Preview thumbnail (or clean geometric placeholder if omitted)
2. **Subject**: Card title / topic
3. **Description**: Short one- or two-line summary
4. **Action Link**: "Open site →" or "View slides →"

---

## 1. Fast command (recommended)

Run the Python tool from the repository root:

```bash
# Add a webpage card (top section):
python3 artifacts/tools/add_card.py \
  --subject "my-tool" \
  --desc "A fast ephys analysis tool." \
  --url "https://example.github.io/my-tool/" \
  --image "assets/preview.png"

# Add a presentation card (bottom section):
python3 artifacts/tools/add_card.py \
  --subject "Laminar Ephys Slides" \
  --desc "Talk at CoSyNe 2026." \
  --url "https://bastoslab.github.io/slides/laminar/" \
  --image "assets/preview.png" \
  --presentation
```

---

## 2. Manual edit

Alternatively, open `assets/projects.js` and append an object before `];`:

```js
{
  subject: "my-tool",
  description: "One-line description.",
  url: "https://example.github.io/my-tool/",
  image: "assets/preview.png",
  category: "webpage"  // or "presentation"
}
```

Commit and push; GitHub Pages will update within 1–2 minutes.
