// Theme toggle + scroll-driven zoom. With reduced motion, the .js class is removed and panels stack statically.
(() => {
  const root = document.documentElement;
  const btn = document.getElementById("theme");
  const paint = () => {
    const light = root.dataset.theme === "light";
    btn.textContent = light ? "☾" : "☀";
    btn.setAttribute("aria-label", "Switch to " + (light ? "dark" : "light") + " theme");
  };
  paint();
  btn.addEventListener("click", () => {
    root.dataset.theme = root.dataset.theme === "light" ? "dark" : "light";
    try { localStorage.setItem("theme", root.dataset.theme); } catch (e) {}
    paint();
  });
  if (matchMedia("(prefers-reduced-motion: reduce)").matches) { root.classList.remove("js"); return; }

  const zooms = [...document.querySelectorAll(".zoom")].map(z => ({ z, panels: [...z.querySelectorAll(".panel")] }));
  const zins = [...document.querySelectorAll(".zin")];
  const clamp = (x, a, b) => Math.min(b, Math.max(a, x));
  let queued = false;
  const frame = () => {
    queued = false;
    const vh = innerHeight;
    root.style.setProperty("--sp", (scrollY / vh).toFixed(3));
    for (const { z, panels } of zooms) {
      // p in [0, n-1]: panel i is centred when p == i. Passed panels grow past the viewer; upcoming ones start small.
      const p = clamp(-z.getBoundingClientRect().top / vh, 0, panels.length - 1);
      panels.forEach((el, i) => {
        const d = p - i, a = Math.abs(d);
        const o = clamp(1 - a * 1.7, 0, 1);
        el.style.transform = "scale(" + (d > 0 ? 1 + d * 1.8 : Math.max(0.1, 1 + d * 0.45)) + ")";
        el.style.opacity = o;
        el.style.visibility = o === 0 ? "hidden" : "visible";
        el.style.pointerEvents = a < 0.5 ? "auto" : "none";
      });
    }
    for (const el of zins) {
      const q = clamp((vh - el.getBoundingClientRect().top) / (vh * 0.55), 0, 1);
      el.style.transform = "scale(" + (0.8 + 0.2 * q) + ")";
      el.style.opacity = q;
    }
  };
  const queue = () => { if (!queued) { queued = true; requestAnimationFrame(frame); } };
  addEventListener("scroll", queue, { passive: true });
  addEventListener("resize", queue);
  frame();
})();
