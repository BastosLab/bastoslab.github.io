"""Draw two figure pages for the jnwb "Spike and Field" deck from sfc_C31o_230823.csv and insert them.

The CSV is the one-session spike-field summary the deck's numbers come from: session sub-C31o_ses-230823,
read from the omission unit feature bank (outputs/unit_feature_bank/ufbp_units.csv) by the omission
session's _temp_peer_sfc.py; units with >= 30 spikes in the epoch; own-probe LFP at a fixed offset
from the peak channel. This script only plots its rows; it computes nothing new beyond sums and ranks.

Usage (from the site root):
    python slides/jnwb/figures/make_sfc_pages.py            # write the two page PDFs and PNGs here
    python slides/jnwb/figures/make_sfc_pages.py --insert   # also insert them into slides.pdf and pages/

--insert refuses unless slides.pdf has the original 11 pages. Exit codes: 0 ok, 1 a check failed.
"""
import argparse
import csv
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

HERE = Path(__file__).resolve().parent
DECK = HERE.parent
CSV = HERE / "sfc_C31o_230823.csv"

# Page box and colours of the existing deck (slides.pdf page size; colours sampled from pages/page-05.png).
W_IN, H_IN = 453.543 / 72, 255.118 / 72
BG, GOLD, TEXT, MUTED, GRID = "#000000", "#cfb87c", "#e6e6e6", "#9a9a9a", "#3a3a3a"
EPOCHS = {"stim": ("Stimulus", "#2f6b8a"), "delay": ("Delay", "#7fa7b8"), "omit": ("Omission", "#d08a3c")}
AREAS = ["V1", "V3d/a/v", "V2", "MST+FST", "FEF"]  # the deck's order
BANDS = ["theta (4-8 Hz)", "low_gamma (30-50 Hz)", "high_gamma (50-80 Hz)"]
BAND_LABEL = {BANDS[0]: "Theta 4–8 Hz", BANDS[1]: "Low γ 30–50 Hz", BANDS[2]: "High γ 50–80 Hz"}
SOURCE = "Session sub-C31o_ses-230823 · units with ≥30 spikes in the epoch · own-probe LFP · omission unit feature bank"

plt.rcParams.update({
    "font.family": ["Arial", "DejaVu Sans"], "pdf.fonttype": 42, "font.size": 8,
    "text.color": TEXT, "axes.labelcolor": TEXT, "xtick.color": TEXT, "ytick.color": MUTED,
    "axes.edgecolor": MUTED, "axes.facecolor": BG, "figure.facecolor": BG, "savefig.facecolor": BG,
    "axes.linewidth": 0.6, "xtick.major.width": 0.6, "ytick.major.width": 0.6,
    "axes.spines.top": False, "axes.spines.right": False, "axes.unicode_minus": True,
})


def load():
    rows = list(csv.DictReader(CSV.open(encoding="utf-8")))
    data = {(r["epoch"], r["band"], r["area"]): r for r in rows}
    if len(data) != len(EPOCHS) * len(BANDS) * len(AREAS):
        sys.exit(f"expected {len(EPOCHS) * len(BANDS) * len(AREAS)} epoch x band x area rows, got {len(data)}")
    return data


def frame(title, number):
    """A blank deck page: gold title, gold rule, footer, page number."""
    fig = plt.figure(figsize=(W_IN, H_IN))
    fig.text(0.057, 0.885, title, fontsize=15, fontweight="bold", color=GOLD, va="baseline")
    fig.add_artist(plt.Line2D([0.057, 0.194], [0.845, 0.845], color=GOLD, lw=1.2))
    fig.text(0.057, 0.06, "H. Nejat · jnwb: Spike and Field", fontsize=7.5, color=MUTED, va="baseline")
    fig.text(0.943, 0.06, f"{number} / 10", fontsize=7.5, color=MUTED, ha="right", va="baseline")
    fig.text(0.057, 0.135, SOURCE, fontsize=6.5, color=MUTED, va="baseline")
    return fig


def legend(fig, y):
    handles = [plt.Rectangle((0, 0), 1, 1, color=c) for _, c in EPOCHS.values()]
    fig.legend(handles, [n for n, _ in EPOCHS.values()], loc="center", bbox_to_anchor=(0.5, y), ncol=3,
               frameon=False, fontsize=8, handlelength=0.9, handleheight=0.9, columnspacing=1.6)


def bars(ax, values, rotate=0):
    """Grouped bars: one group per area, one bar per epoch. values[epoch][i] is the area-i value."""
    w = 0.26
    for k, ep in enumerate(EPOCHS):
        xs = [i + (k - 1) * w for i in range(len(AREAS))]
        ax.bar(xs, values[ep], width=w * 0.92, color=EPOCHS[ep][1], linewidth=0)
    ax.set_xticks(range(len(AREAS)), AREAS, fontsize=7, rotation=rotate,
                  ha="right" if rotate else "center", rotation_mode="anchor")
    ax.tick_params(axis="x", length=0, pad=3)
    ax.axhline(0, color=MUTED, lw=0.6)
    ax.grid(axis="y", color=GRID, lw=0.5)
    ax.set_axisbelow(True)


def page_ppc(data):
    """Median PPC for every area x band x epoch cell, one shared y scale."""
    top2 = {(ep, b): sorted(AREAS, key=lambda a: -float(data[(ep, b, a)]["ppc_median"]))[:2]
            for ep in EPOCHS for b in BANDS}
    lead = all(set(v) == {"V1", "V3d/a/v"} for v in top2.values())
    if not lead:
        sys.exit(f"title claim fails: top two areas per cell {top2}")
    fig = frame("V1 and V3d/a/v lead in all nine band × epoch cells", "6b")
    ymax = max(float(r["ppc_median"]) for r in data.values())
    axes = [fig.add_axes([0.105 + i * 0.295, 0.36, 0.25, 0.39]) for i in range(3)]
    for i, (ax, b) in enumerate(zip(axes, BANDS)):
        bars(ax, {ep: [float(data[(ep, b, a)]["ppc_median"]) for a in AREAS] for ep in EPOCHS}, rotate=35)
        ax.set_ylim(-0.001, 0.03)
        ax.set_yticks([0, 0.01, 0.02, 0.03])
        ax.tick_params(axis="y", labelsize=7, labelleft=(i == 0))
        ax.set_title(BAND_LABEL[b], fontsize=8.5, color=TEXT, pad=4)
    axes[0].set_ylabel("Median PPC", fontsize=8)
    assert ymax < 0.03, ymax
    legend(fig, 0.215)
    return fig


def page_spikes(data):
    """Units and spikes per area and epoch; spikes on a log axis as points (no bars on a log scale)."""
    b0 = BANDS[0]
    for ep in EPOCHS:  # unit and spike counts do not depend on the band
        for a in AREAS:
            if len({(data[(ep, b, a)]["n_units"], data[(ep, b, a)]["n_spikes"]) for b in BANDS}) != 1:
                sys.exit(f"counts differ across bands for {ep} {a}")
    spikes = {ep: sum(int(data[(ep, b0, a)]["n_spikes"]) for a in AREAS) for ep in EPOCHS}
    units = {ep: sum(int(data[(ep, b0, a)]["n_units"]) for a in AREAS) for ep in EPOCHS}
    ratio = spikes["stim"] / spikes["omit"]
    if not 7.5 <= ratio < 8.5 or units["omit"] < 0.98 * units["stim"]:
        sys.exit(f"title claim fails: spikes {spikes}, units {units}")
    fig = frame(f"Omission has {ratio:.0f}× fewer spikes than stimulus", "7b")
    ax1 = fig.add_axes([0.105, 0.32, 0.37, 0.43])
    bars(ax1, {ep: [int(data[(ep, b0, a)]["n_units"]) for a in AREAS] for ep in EPOCHS})
    ax1.set_ylim(0, 165)
    ax1.tick_params(axis="y", labelsize=7)
    ax1.set_ylabel("Units", fontsize=8)
    ax1.set_title("Units per area, nearly equal (" + " / ".join(str(units[e]) for e in EPOCHS) + ")",
                  fontsize=8.5, pad=4)
    ax2 = fig.add_axes([0.58, 0.32, 0.37, 0.43])
    for k, ep in enumerate(EPOCHS):
        xs = [i + (k - 1) * 0.22 for i in range(len(AREAS))]
        ax2.scatter(xs, [int(data[(ep, b0, a)]["n_spikes"]) for a in AREAS], s=16, color=EPOCHS[ep][1], zorder=3)
    ax2.set_yscale("log")
    ax2.set_ylim(3e3, 5e6)
    ax2.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v / 1e6:g}M" if v >= 1e6 else f"{v / 1e3:g}k"))
    ax2.set_xticks(range(len(AREAS)), AREAS, fontsize=7)
    ax2.tick_params(axis="x", length=0, pad=3)
    ax2.tick_params(axis="y", labelsize=7)
    ax2.grid(axis="y", color=GRID, lw=0.5)
    ax2.set_axisbelow(True)
    ax2.set_ylabel("Spikes (log)", fontsize=8)
    ax2.set_title("Spikes summed over units", fontsize=8.5, pad=4)
    legend(fig, 0.215)
    return fig


def build():
    data = load()
    return {"sfc_ppc_bands": page_ppc(data), "sfc_units_spikes": page_spikes(data)}


def insert(pdfs):
    """Insert the PPC page after deck page 7 and the counts page after old page 8; shift pages/ PNGs."""
    import fitz

    deck_pdf = DECK / "slides.pdf"
    doc = fitz.open(deck_pdf)
    if doc.page_count != 11:
        sys.exit(f"slides.pdf has {doc.page_count} pages, expected the original 11; not inserting twice")
    # Insert the later one first so the earlier position is unchanged.
    for name, after in (("sfc_units_spikes", 8), ("sfc_ppc_bands", 7)):
        doc.insert_pdf(fitz.open(pdfs[name]), start_at=after)
    tmp = deck_pdf.with_suffix(".tmp.pdf")
    doc.save(tmp, garbage=3, deflate=True)
    doc.close()
    tmp.replace(deck_pdf)
    pages = DECK / "pages"
    new_index = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 9, 9: 11, 10: 12, 11: 13}
    for old in sorted(new_index, reverse=True):
        (pages / f"page-{old:02d}.png").replace(pages / f"page-{new_index[old]:02d}.png")
    for name, n in (("sfc_ppc_bands", 8), ("sfc_units_spikes", 10)):
        (pages / f"page-{n:02d}.png").write_bytes((HERE / f"{name}.png").read_bytes())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--insert", action="store_true")
    args = ap.parse_args()
    import fitz

    pdfs = {}
    for name, fig in build().items():
        pdfs[name] = HERE / f"{name}.pdf"
        fig.savefig(pdfs[name])
        plt.close(fig)
        # Raster from the page PDF at 300 dpi: 1890 x 1063 px, the size of the other pages/ PNGs.
        pix = fitz.open(pdfs[name])[0].get_pixmap(dpi=300)
        if (pix.width, pix.height) != (1890, 1063):
            sys.exit(f"{name}: {pix.width} x {pix.height} px, expected 1890 x 1063")
        pix.save(HERE / f"{name}.png")
    if args.insert:
        insert(pdfs)
    return 0


if __name__ == "__main__":
    sys.exit(main())
