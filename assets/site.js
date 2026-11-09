// Theme toggle + scroll-driven zoom. With reduced motion, the .js class is removed and panels stack statically.
(() => {
  // Zoom and fade tuning, named for the code below (values unchanged from the inline literals).
  const FADE = 1.7;            // opacity falls by FADE per panel of distance
  const ZOOM_OUT = 1.8;        // passed panels grow by ZOOM_OUT per panel of distance
  const ENTRY_MIN = 0.45;      // upcoming panels shrink by ENTRY_MIN per panel of distance...
  const ENTRY_FLOOR = 0.1;     // ...and never below ENTRY_FLOOR
  const POINTER_CUTOFF = 0.5;  // only panels this close to centre take pointer events
  const ZIN_SPAN = 0.55;       // lab cards fade in over the lower 55% of the viewport
  const ZIN_MIN = 0.8;         // lab cards start at scale ZIN_MIN
  const ZIN_GROW = 0.2;        // and grow by ZIN_GROW to full size
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
    try { localStorage.setItem("theme", root.dataset.theme); } catch (e) { /* storage blocked or full: theme applies to this page view only */ }
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
        const o = clamp(1 - a * FADE, 0, 1);
        el.style.transform = "scale(" + (d > 0 ? 1 + d * ZOOM_OUT : Math.max(ENTRY_FLOOR, 1 + d * ENTRY_MIN)) + ")";
        el.style.opacity = o;
        el.style.visibility = o === 0 ? "hidden" : "visible";
        el.style.pointerEvents = a < POINTER_CUTOFF ? "auto" : "none";
      });
    }
    for (const el of zins) {
      const q = clamp((vh - el.getBoundingClientRect().top) / (vh * ZIN_SPAN), 0, 1);
      el.style.transform = "scale(" + (ZIN_MIN + ZIN_GROW * q) + ")";
      el.style.opacity = q;
    }
  };
  const queue = () => { if (!queued) { queued = true; requestAnimationFrame(frame); } };
  addEventListener("scroll", queue, { passive: true });
  addEventListener("resize", queue);
  frame();
})();
