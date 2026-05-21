import csv
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from pathlib import Path
from collections import Counter

DATA_DIR = Path(__file__).parent.parent.parent.parent.parent / "assets" / "stu-data"

TRACK_DEPTS = ["觀光休閒系", "資訊工程系", "電機工程系", "電信工程系", "航運管理系", "餐旅管理系"]
YEARS = list(range(109, 115))


def _setup_font():
    candidates = ["Microsoft JhengHei", "Arial Unicode MS", "SimHei", "DejaVu Sans"]
    available = {f.name for f in fm.fontManager.ttflist}
    for name in candidates:
        if name in available:
            return name
    return candidates[-1]


def _load_year(year: int) -> dict:
    counts = Counter()
    with open(DATA_DIR / f"{year}年新生資料庫.csv", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            counts[row["系所名稱"].strip()] += 1
    return dict(counts)


def _load_methods(year: int) -> dict:
    counts = Counter()
    with open(DATA_DIR / f"{year}年新生資料庫.csv", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            counts[row["入學方式"].strip()] += 1
    return dict(counts)


def main():
    font_name = _setup_font()
    matplotlib.rcParams["font.family"] = font_name
    matplotlib.rcParams["axes.unicode_minus"] = False

    all_year_data = {y: _load_year(y) for y in YEARS}
    totals = [sum(all_year_data[y].values()) for y in YEARS]
    methods_114 = _load_methods(114)
    dept_114 = all_year_data[114]
    top10_depts = sorted(dept_114, key=lambda d: dept_114[d], reverse=True)[:10]
    top10_counts = [dept_114[d] for d in top10_depts]

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.patch.set_facecolor("white")
    fig.suptitle(
        "國立澎湖科技大學 109 – 114 學年度招生分析",
        fontsize=16, fontweight="bold", y=0.98,
    )

    # ── 左上：全校招生趨勢折線圖 ──────────────────────────────────────────
    ax1 = axes[0, 0]
    ax1.set_facecolor("white")
    ax1.plot(YEARS, totals, color="#C0392B", linewidth=2.5, marker="o",
             markersize=7, zorder=3)
    ax1.fill_between(YEARS, totals, alpha=0.12, color="#C0392B")
    for x, y in zip(YEARS, totals):
        ax1.text(x, y + 12, str(y), ha="center", va="bottom", fontsize=10,
                 color="#555555")
    ax1.set_title("全校招生趨勢", fontsize=13, pad=8)
    ax1.set_xlabel("學年度", fontsize=10)
    ax1.set_ylabel("人數", fontsize=10)
    ax1.set_xticks(YEARS)
    ax1.set_ylim(0, max(totals) * 1.18)
    ax1.yaxis.grid(True, linestyle="--", linewidth=0.6, color="#dddddd")
    ax1.set_axisbelow(True)
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)

    # ── 右上：114 入學方式圓餅圖 ──────────────────────────────────────────
    ax2 = axes[0, 1]
    ax2.set_facecolor("white")
    labels = list(methods_114.keys())
    sizes = list(methods_114.values())
    colors_pie = [
        "#4C8BBF", "#E07B39", "#5BA55B", "#C0392B", "#9B59B6",
        "#F39C12", "#1ABC9C", "#E74C3C", "#95A5A6", "#2C3E50",
    ]
    wedges, texts, autotexts = ax2.pie(
        sizes, labels=None, autopct="%1.1f%%",
        startangle=90, colors=colors_pie[:len(sizes)],
        pctdistance=0.82, wedgeprops={"linewidth": 0.8, "edgecolor": "white"},
    )
    for at in autotexts:
        at.set_fontsize(8)
    ax2.legend(
        wedges, labels,
        loc="lower center", bbox_to_anchor=(0.5, -0.22),
        ncol=2, fontsize=8, frameon=False,
    )
    ax2.set_title("114 入學方式", fontsize=13, pad=8)

    # ── 左下：114 各系前 10 名水平長條圖 ──────────────────────────────────
    ax3 = axes[1, 0]
    ax3.set_facecolor("white")
    y_pos = np.arange(len(top10_depts))
    bars = ax3.barh(y_pos, top10_counts, color="#4C8BBF", alpha=0.88)
    for bar, val in zip(bars, top10_counts):
        ax3.text(val + 0.4, bar.get_y() + bar.get_height() / 2,
                 str(val), va="center", ha="left", fontsize=9, color="#333333")
    ax3.set_yticks(y_pos)
    ax3.set_yticklabels(top10_depts, fontsize=10)
    ax3.set_xlabel("招生人數（人）", fontsize=10)
    ax3.set_title("114 各系招生人數（前 10）", fontsize=13, pad=8)
    ax3.xaxis.grid(True, linestyle="--", linewidth=0.6, color="#dddddd")
    ax3.set_axisbelow(True)
    ax3.spines["top"].set_visible(False)
    ax3.spines["right"].set_visible(False)
    ax3.spines["left"].set_visible(False)
    ax3.tick_params(axis="y", left=False)

    # ── 右下：主要系所歷年招生趨勢 ────────────────────────────────────────
    ax4 = axes[1, 1]
    ax4.set_facecolor("white")
    line_colors = ["#C0392B", "#4C8BBF", "#E07B39", "#5BA55B", "#9B59B6", "#F39C12"]
    for dept, color in zip(TRACK_DEPTS, line_colors):
        trend = [all_year_data[y].get(dept, 0) for y in YEARS]
        ax4.plot(YEARS, trend, marker="o", markersize=5, linewidth=2,
                 color=color, label=dept)
    ax4.set_title("主要系所招生趨勢", fontsize=13, pad=8)
    ax4.set_xlabel("學年度", fontsize=10)
    ax4.set_ylabel("人數", fontsize=10)
    ax4.set_xticks(YEARS)
    ax4.legend(loc="upper right", fontsize=8.5, frameon=True, framealpha=0.8)
    ax4.yaxis.grid(True, linestyle="--", linewidth=0.6, color="#dddddd")
    ax4.set_axisbelow(True)
    ax4.spines["top"].set_visible(False)
    ax4.spines["right"].set_visible(False)

    fig.tight_layout(rect=[0, 0, 1, 0.97])
    out_dir = Path(__file__).parent / "output"
    out_dir.mkdir(exist_ok=True)
    fig.savefig(out_dir / "task3_dashboard.png", dpi=150, bbox_inches="tight")
    print(f"Saved: {out_dir / 'task3_dashboard.png'}")
    plt.close(fig)


if __name__ == "__main__":
    main()
