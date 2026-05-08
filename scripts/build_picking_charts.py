"""build_picking_charts.py — Generate the bar charts embedded in
docs/mouse-picking-optimization.md.

Each chart visualizes one section's "Picking Time (avg, n=100)" measurements
on a logarithmic y-axis so that the parent (slow) value and the optimized
(fast) value are both legible despite spanning up to ~5 orders of magnitude.

The numbers are hard-coded here because they are the exact, citation-worthy
measurements quoted in the document — this script's single responsibility is
to render the figures that go alongside that prose.

Usage
-----
    python scripts/build_picking_charts.py
    python scripts/build_picking_charts.py --output-dir screenshots/charts
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, LogLocator, NullFormatter


# ---------------------------------------------------------------------------
# Style — Korean font + a small consistent palette
# ---------------------------------------------------------------------------

matplotlib.rcParams["font.family"] = "Malgun Gothic"
matplotlib.rcParams["axes.unicode_minus"] = False

COLOR_BEFORE = "#9e9e9e"      # parent / before — neutral grey
COLOR_INTERMEDIATE = "#80cbc4"  # an intermediate optimization step
COLOR_AFTER = "#00897b"       # the optimized state being highlighted


# ---------------------------------------------------------------------------
# Chart definitions
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Bar:
    label: str
    value_ms: float
    color: str


@dataclass(frozen=True)
class Chart:
    filename: str
    title: str
    bars: tuple[Bar, ...]


CHARTS: tuple[Chart, ...] = (
    Chart(
        filename="chart-overall.png",
        title="Mouse Picking Time — 약 128,000× 빨라짐",
        bars=(
            Bar("최적화 전", 1425.66, COLOR_BEFORE),
            Bar("최적화 후", 0.0111, COLOR_AFTER),
        ),
    ),
    Chart(
        filename="chart-cumulative.png",
        title="핵심 최적화 단계별 누적 — 1,425.66 ms → 0.0111 ms (약 128,000× 빨라짐)",
        bars=(
            Bar("최적화 전", 1425.66, COLOR_BEFORE),
            Bar("Scene BVH", 4.04, COLOR_INTERMEDIATE),
            Bar("Primitive cutoff", 0.0973, COLOR_INTERMEDIATE),
            Bar("Node cutoff", 0.0831, COLOR_INTERMEDIATE),
            Bar("Mesh BVH", 0.0200, COLOR_INTERMEDIATE),
            Bar("최종", 0.0111, COLOR_AFTER),
        ),
    ),
    Chart(
        filename="chart-scene-bvh.png",
        title="Scene BVH — 약 353× 빨라짐",
        bars=(
            Bar("적용 전", 1425.66, COLOR_BEFORE),
            Bar("Scene BVH 적용 후", 4.04, COLOR_AFTER),
        ),
    ),
    Chart(
        filename="chart-distance-cutoff.png",
        title="거리 기반 검사 생략 — 최종적으로 약 45× 빨라짐",
        bars=(
            Bar("적용 전", 3.74, COLOR_BEFORE),
            Bar("Primitive cutoff\n도입", 0.0973, COLOR_INTERMEDIATE),
            Bar("Node cutoff\n로 대체", 0.0831, COLOR_AFTER),
        ),
    ),
    Chart(
        filename="chart-mesh-bvh.png",
        title="Mesh BVH — 약 3.88× 빨라짐",
        bars=(
            Bar("적용 전", 0.0777, COLOR_BEFORE),
            Bar("Mesh BVH 적용 후", 0.0200, COLOR_AFTER),
        ),
    ),
)


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def _format_ms(v: float) -> str:
    # Match the precision used in the document: 4-digit grouping above 1 ms,
    # 4 decimal places below.
    if v >= 1.0:
        return f"{v:,.2f} ms"
    return f"{v:.4f} ms"


def _format_tick(v: float, _pos: int) -> str:
    if v >= 1.0:
        return f"{int(v):,}" if v == int(v) else f"{v:g}"
    return f"{v:g}"


def render_chart(chart: Chart, out_path: Path) -> None:
    # Widen the figure when there are more bars so x-tick labels don't crowd.
    n = len(chart.bars)
    fig_width = 7.5 if n <= 3 else 7.5 + 0.7 * (n - 3)
    fig, ax = plt.subplots(figsize=(fig_width, 4.2), dpi=150)

    x = list(range(len(chart.bars)))
    values = [b.value_ms for b in chart.bars]
    colors = [b.color for b in chart.bars]
    labels = [b.label for b in chart.bars]

    bars = ax.bar(x, values, color=colors, width=0.55, edgecolor="#37474f", linewidth=0.6)

    ax.set_yscale("log")
    ax.set_ylabel("Picking Time (ms, log scale)", fontsize=10)
    ax.set_xticks(x, labels, fontsize=10)
    # Title + a smaller subtitle one line below stating the measurement
    # protocol — every bar in every chart is the mean over 100 picking trials
    # on Default.scene.
    ax.set_title(chart.title, fontsize=12, pad=28)
    ax.text(
        0.5, 1.02,
        "100회 picking 시도 평균 (Default.scene)",
        transform=ax.transAxes,
        ha="center", va="bottom",
        fontsize=9, color="#607d8b", style="italic",
    )

    # Headroom above the tallest bar so the value labels don't clip.
    vmax = max(values)
    vmin = min(values)
    ax.set_ylim(vmin / 4.0, vmax * 4.0)

    # Major gridlines on each decade. Format labels as plain decimals
    # ("0.01", "0.1", "1", "10") rather than "10⁻²" — Malgun Gothic doesn't
    # have a Unicode-minus glyph, so the exponent form renders as a tofu box.
    ax.yaxis.set_major_locator(LogLocator(base=10.0))
    ax.yaxis.set_major_formatter(FuncFormatter(_format_tick))
    ax.yaxis.set_minor_formatter(NullFormatter())
    ax.grid(axis="y", which="major", linestyle="--", linewidth=0.5, alpha=0.5)
    ax.set_axisbelow(True)

    # Strip the chart frame down to the two axes that carry information.
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)

    # Value label above each bar.
    for rect, v in zip(bars, values):
        ax.annotate(
            _format_ms(v),
            xy=(rect.get_x() + rect.get_width() / 2.0, v),
            xytext=(0, 6),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold",
            color="#263238",
        )

    fig.tight_layout()
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render the bar charts embedded in docs/mouse-picking-optimization.md.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("screenshots/charts"),
        help="Directory to write PNGs into (default: screenshots/charts).",
    )
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)

    for chart in CHARTS:
        out_path = args.output_dir / chart.filename
        render_chart(chart, out_path)
        print(f"Wrote {out_path}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
