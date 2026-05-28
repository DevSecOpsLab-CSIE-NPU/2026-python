from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def resolve_data_dir() -> Path:
    """Find the repository data folder regardless of current working directory."""
    current = Path(__file__).resolve()
    for parent in [current.parent, *current.parents]:
        candidate = parent / "assets" / "stu-data"
        if candidate.exists():
            return candidate
    raise FileNotFoundError("Cannot find assets/stu-data directory")


def load_year(year: int, data_dir: Path) -> dict[str, int]:
    """讀取單一年份 CSV，回傳 {系所名稱: 人數} 的 dict"""
    csv_path = data_dir / f"{year}年新生資料庫.csv"
    counts: dict[str, int] = defaultdict(int)

    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            dept = (row.get("系所名稱") or "").strip()
            if dept:
                counts[dept] += 1

    return dict(counts)


def get_top_depts(year_data: dict[int, dict[str, int]], top_n: int = 8) -> list[str]:
    """從多年資料中找出任一年曾進前 top_n 的系所，並限制回傳數量不超過 top_n。"""
    candidates: set[str] = set()
    score: dict[str, int] = defaultdict(int)

    for _, dept_counts in year_data.items():
        ranked = sorted(dept_counts.items(), key=lambda x: x[1], reverse=True)
        top_items = ranked[:top_n]
        for dept, count in top_items:
            candidates.add(dept)
            score[dept] += count

    return sorted(candidates, key=lambda d: (-score[d], d))[:top_n]


def plot_grouped_bar(year_data: dict[int, dict[str, int]], depts: list[str], output_path: Path) -> None:
    years = sorted(year_data.keys())
    values = np.array([[year_data[y].get(dept, 0) for y in years] for dept in depts])

    plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei", "Arial Unicode MS", "sans-serif"]
    plt.rcParams["axes.unicode_minus"] = False

    fig, ax = plt.subplots(figsize=(12, 7))
    y = np.arange(len(depts))
    bar_h = 0.22
    center_idx = (len(years) - 1) / 2

    for idx, year in enumerate(years):
        ax.barh(y + (idx - center_idx) * bar_h, values[:, idx], height=bar_h, label=str(year))

    ax.set_title("112-114 學年度各系招生人數（三年並排）", fontsize=14)
    ax.set_xlabel("人數")
    ax.set_yticks(y)
    ax.set_yticklabels(depts)
    ax.invert_yaxis()
    ax.legend(title="學年度")
    ax.grid(axis="x", linestyle="--", alpha=0.3)
    fig.tight_layout()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=200)
    plt.close(fig)


def main() -> None:
    data_dir = resolve_data_dir()
    years = [112, 113, 114]
    year_data = {year: load_year(year, data_dir) for year in years}
    top_depts = get_top_depts(year_data, top_n=8)

    output = Path(__file__).parent / "output" / "task1.png"
    plot_grouped_bar(year_data, top_depts, output)
    print(f"Task1 image generated: {output}")


if __name__ == "__main__":
    main()
