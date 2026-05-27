from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


DATA_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent / "assets" / "stu-data"
OUTPUT_DIR = Path(__file__).resolve().parent / "output"


def _configure_matplotlib() -> None:
    matplotlib.rcParams["font.sans-serif"] = [
        "Microsoft JhengHei",
        "Noto Sans CJK TC",
        "DejaVu Sans",
    ]
    matplotlib.rcParams["axes.unicode_minus"] = False


def load_year(year: int, data_dir: Path) -> dict[str, int]:
    """讀取單一年份 CSV，回傳 {系所名稱: 人數} 的 dict"""
    csv_path = data_dir / f"{year}年新生資料庫.csv"
    counts: Counter[str] = Counter()

    with csv_path.open(encoding="utf-8-sig", newline="") as file_obj:
        reader = csv.DictReader(file_obj)
        for row in reader:
            dept = (row.get("系所名稱") or "").strip()
            if dept:
                counts[dept] += 1

    return dict(counts)


def get_top_depts(year_data: dict[int, dict], top_n: int = 8) -> list[str]:
    """從多年資料中找出任一年曾進前 top_n 的系所清單"""
    appearance_counts: Counter[str] = Counter()
    total_counts: Counter[str] = Counter()

    for counts in year_data.values():
        ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:top_n]
        for dept, count in ranked:
            appearance_counts[dept] += 1
            total_counts[dept] += count

    ranked_depts = sorted(
        appearance_counts,
        key=lambda dept: (-appearance_counts[dept], -total_counts[dept], dept),
    )
    return ranked_depts[:top_n]


def plot_task1(year_data: dict[int, dict[str, int]], output_dir: Path = OUTPUT_DIR) -> Path:
    _configure_matplotlib()
    output_dir.mkdir(parents=True, exist_ok=True)

    years = sorted(year_data)
    depts = get_top_depts(year_data, top_n=8)

    fig_height = max(6, len(depts) * 0.55)
    fig, ax = plt.subplots(figsize=(13, fig_height))

    positions = list(range(len(depts)))
    group_height = 0.78
    bar_height = group_height / max(len(years), 1)
    offsets = [(-group_height / 2) + bar_height * (index + 0.5) for index in range(len(years))]
    colors = ["#4C78A8", "#F58518", "#54A24B"]

    for year_index, year in enumerate(years):
        counts = year_data[year]
        values = [counts.get(dept, 0) for dept in depts]
        y_positions = [position + offsets[year_index] for position in positions]
        bars = ax.barh(
            y_positions,
            values,
            height=bar_height * 0.9,
            color=colors[year_index % len(colors)],
            label=f"{year} 學年度",
            alpha=0.92,
        )
        for bar, value in zip(bars, values, strict=True):
            if value > 0:
                ax.text(
                    bar.get_width() + 0.7,
                    bar.get_y() + bar.get_height() / 2,
                    str(value),
                    va="center",
                    ha="left",
                    fontsize=9,
                )

    ax.set_yticks(positions)
    ax.set_yticklabels(depts)
    ax.invert_yaxis()
    ax.set_xlabel("人數")
    ax.set_ylabel("系所名稱")
    ax.set_title("112-114 學年度各系招生人數並排長條圖")
    ax.legend(loc="lower right")
    ax.grid(axis="x", linestyle="--", alpha=0.25)

    fig.tight_layout()
    output_path = output_dir / "task1.png"
    fig.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    return output_path


def main() -> None:
    year_data = {year: load_year(year, DATA_DIR) for year in (112, 113, 114)}
    output_path = plot_task1(year_data)
    print(f"saved to {output_path}")


if __name__ == "__main__":
    main()