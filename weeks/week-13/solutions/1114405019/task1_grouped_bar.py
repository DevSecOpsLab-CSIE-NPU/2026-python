import csv
import sys
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from pathlib import Path
from collections import Counter

DATA_DIR = Path(__file__).parent.parent.parent.parent.parent / "assets" / "stu-data"


def _setup_font():
    candidates = ["Microsoft JhengHei", "Arial Unicode MS", "SimHei", "DejaVu Sans"]
    available = {f.name for f in fm.fontManager.ttflist}
    for name in candidates:
        if name in available:
            return name
    return candidates[-1]


def load_year(year: int, data_dir: Path) -> dict:
    filename = data_dir / f"{year}年新生資料庫.csv"
    counts = Counter()
    with open(filename, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            dept = row["系所名稱"].strip()
            if dept:
                counts[dept] += 1
    return dict(counts)


def get_top_depts(year_data: dict, top_n: int = 8) -> list:
    candidates = set()
    for data in year_data.values():
        top = sorted(data, key=lambda d: data[d], reverse=True)[:top_n]
        candidates.update(top)
    totals = {}
    for dept in candidates:
        totals[dept] = sum(data.get(dept, 0) for data in year_data.values())
    ranked = sorted(candidates, key=lambda d: totals[d], reverse=True)
    return ranked[:top_n]


def main():
    years = [112, 113, 114]
    year_data = {y: load_year(y, DATA_DIR) for y in years}
    depts = get_top_depts(year_data, top_n=8)

    font_name = _setup_font()
    matplotlib.rcParams["font.family"] = font_name
    matplotlib.rcParams["axes.unicode_minus"] = False

    fig, ax = plt.subplots(figsize=(12, 8))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    n_depts = len(depts)
    n_years = len(years)
    bar_height = 0.25
    y_pos = np.arange(n_depts)

    colors = ["#4C8BBF", "#E07B39", "#5BA55B"]
    labels = [f"{y} 學年度" for y in years]

    for i, (year, color, label) in enumerate(zip(years, colors, labels)):
        data = year_data[year]
        counts = [data.get(dept, 0) for dept in depts]
        offset = (i - (n_years - 1) / 2) * bar_height
        bars = ax.barh(
            y_pos + offset, counts, bar_height * 0.9,
            color=color, label=label, alpha=0.88,
        )
        for bar, val in zip(bars, counts):
            if val > 0:
                ax.text(
                    val + 0.3, bar.get_y() + bar.get_height() / 2,
                    str(val), va="center", ha="left", fontsize=8.5,
                    color="#333333",
                )

    ax.set_yticks(y_pos)
    ax.set_yticklabels(depts, fontsize=11)
    ax.set_xlabel("招生人數（人）", fontsize=12)
    ax.set_title(
        "國立澎湖科技大學 112–114 學年度各系招生人數比較",
        fontsize=14, fontweight="bold", pad=16,
    )
    ax.legend(loc="lower right", fontsize=10)
    ax.xaxis.grid(True, linestyle="--", linewidth=0.6, color="#cccccc", alpha=0.8)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", left=False)

    out_dir = Path(__file__).parent / "output"
    out_dir.mkdir(exist_ok=True)
    fig.tight_layout()
    fig.savefig(out_dir / "task1.png", dpi=150, bbox_inches="tight")
    print(f"Saved: {out_dir / 'task1.png'}")
    plt.close(fig)


if __name__ == "__main__":
    main()
