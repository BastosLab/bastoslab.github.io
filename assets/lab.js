// Renders window.PROJECTS into #cards-webpages and #cards-presentations (or #cards fallback).
// Uses textContent and safe attributes only (no innerHTML).
(function() {
  const el = (t, c, x) => { const e = document.createElement(t); if (c) e.className = c; if (x != null) e.textContent = x; return e; };

  const webRoot = document.getElementById("cards-webpages") || document.getElementById("cards");
  const presRoot = document.getElementById("cards-presentations") || webRoot;

  let webCount = 0;
  let presCount = 0;

  for (const p of window.PROJECTS || []) {
    const isPres = (p.category === "presentation" || (p.tags && p.tags.includes("slides")));
    const target = (isPres && presRoot) ? presRoot : webRoot;
    if (!target) continue;

    if (isPres) presCount++;
    else webCount++;

    const a = el("a", "card zin");
    a.href = p.url;
    a.rel = "noopener";
    if (p.url && p.url.startsWith("http")) a.target = "_blank";

    if (p.image) {
      const img = el("img", "card-thumb");
      img.src = p.image;
      img.alt = p.subject || p.name || "Preview";
      img.loading = "lazy";
      a.append(img);
    } else {
      const ph = el("div", "card-thumb-placeholder", isPres ? "Presentation" : "Webpage");
      a.append(ph);
    }

    a.append(el("h3", null, p.subject || p.name));
    a.append(el("p", null, p.description));

    if (p.tags && p.tags.length > 0) {
      const t = el("div", "tags");
      for (const g of p.tags) t.append(el("span", "tag", g));
      a.append(t);
    }

    a.append(el("span", "go", isPres ? "View slides →" : "Open site →"));
    target.append(a);
  }

  if (presRoot && presCount === 0 && presRoot !== webRoot) {
    const emptyNotice = el("p", "card-empty-hint", "No presentations published yet.");
    presRoot.append(emptyNotice);
  }
})();
