from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei", "Noto Sans CJK TC", "SimHei", "Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False


DATA_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent / "assets" / "stu-data"
OUTPUT_DIR = Path(__file__).resolve().parent / "output"
TARGET_YEARS = (112, 113, 114)


def load_year(year: int, data_dir: Path) -> dict[str, int]:
    """讀取單一年份 CSV，回傳 {系所名稱: 人數} 的 dict"""

    path = data_dir / f"{year}年新生資料庫.csv"
    counts: Counter[str] = Counter()
    with path.open(encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            department = (row.get("系所名稱") or "").strip()
            if department:
                counts[department] += 1
    return dict(counts)


def get_top_depts(year_data: dict[int, dict[str, int]], top_n: int = 8) -> list[str]:
    """從多年資料中找出任一年曾進前 top_n 的系所清單"""

    candidate_departments: set[str] = set()
    totals: Counter[str] = Counter()

    for counts in year_data.values():
        totals.update(counts)
        top_departments = sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:top_n]
        candidate_departments.update(department for department, _ in top_departments)

    ranked_departments = sorted(candidate_departments, key=lambda department: (-totals[department], department))
    return ranked_departments[:top_n]


def build_grouped_bar_chart(year_data: dict[int, dict[str, int]], output_path: Path) -> None:
    years = sorted(year_data)
    departments = get_top_depts(year_data, top_n=8)
    counts_by_year = [year_data[year] for year in years]
    max_count = max((count for counts in counts_by_year for count in counts.values()), default=0)

    figure_height = max(6, len(departments) * 0.55)
    fig, ax = plt.subplots(figsize=(12, figure_height))

    y_positions = list(range(len(departments)))
    bar_height = 0.22
    palette = ["#2F6BFF", "#FF8A3D", "#2BB673"]

    for index, year in enumerate(years):
        offsets = [position + (index - (len(years) - 1) / 2) * bar_height for position in y_positions]
        counts = [year_data[year].get(department, 0) for department in departments]
        bars = ax.barh(
            offsets,
            counts,
            height=bar_height,
            color=palette[index % len(palette)],
            label=f"{year}學年度",
            edgecolor="white",
            linewidth=0.8,
        )
        for bar, value in zip(bars, counts):
            if value:
                ax.text(
                    bar.get_width() + max(1, max_count * 0.01),
                    bar.get_y() + bar.get_height() / 2,
                    str(value),
                    va="center",
                    ha="left",
                    fontsize=9,
                )

    ax.set_yticks(y_positions)
    ax.set_yticklabels(departments, fontsize=11)
    ax.invert_yaxis()
    ax.set_xlabel("人數", fontsize=12)
    ax.set_ylabel("系所名稱", fontsize=12)
    ax.set_title("112～114學年度各系招生人數比較", fontsize=15, pad=14)
    ax.grid(axis="x", linestyle="--", alpha=0.3)
    ax.legend(frameon=False, ncols=3, loc="lower right")
    ax.set_xlim(0, max_count * 1.18 if max_count else 1)
    fig.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=160, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    year_data = {year: load_year(year, DATA_DIR) for year in TARGET_YEARS}
    build_grouped_bar_chart(year_data, OUTPUT_DIR / "task1.png")


if __name__ == "__main__":
    main()