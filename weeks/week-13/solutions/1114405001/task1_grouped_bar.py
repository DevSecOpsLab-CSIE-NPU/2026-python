from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def _resolve_data_dir(start_file: Path) -> Path:
    for parent in start_file.resolve().parents:
        candidate = parent / "assets" / "stu-data"
        if candidate.exists():
            return candidate
    raise FileNotFoundError("Cannot find assets/stu-data directory")


DATA_DIR = _resolve_data_dir(Path(__file__))


def load_year(year: int, data_dir: Path) -> dict[str, int]:
    """讀取單一年份 CSV，回傳 {系所名稱: 人數} 的 dict。"""
    csv_path = data_dir / f"{year}年新生資料庫.csv"
    counter: Counter[str] = Counter()

    with csv_path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            dept = (row.get("系所名稱") or "").strip()
            if dept:
                counter[dept] += 1

    return dict(counter)


def get_top_depts(year_data: dict[int, dict[str, int]], top_n: int = 8) -> list[str]:
    """從多年資料中找出任一年曾進前 top_n 的系所清單。"""
    selected: set[str] = set()

    for data in year_data.values():
        top = sorted(data.items(), key=lambda item: (-item[1], item[0]))[:top_n]
        selected.update(dept for dept, _ in top)

    return sorted(
        selected,
        key=lambda dept: (
            -max(year_data[year].get(dept, 0) for year in year_data),
            -sum(year_data[year].get(dept, 0) for year in year_data),
            dept,
        ),
    )


def create_task1_chart(
    years: tuple[int, int, int] = (112, 113, 114),
    top_n: int = 8,
    output_path: Path | None = None,
) -> Path:
    if output_path is None:
        output_path = Path(__file__).parent / "output" / "task1.png"

    output_path.parent.mkdir(parents=True, exist_ok=True)

    year_data = {year: load_year(year, DATA_DIR) for year in years}
    depts = get_top_depts(year_data, top_n=top_n)

    y_positions = np.arange(len(depts))
    bar_height = 0.22
    offsets = np.linspace(-bar_height, bar_height, len(years))

    plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei", "Arial Unicode MS", "sans-serif"]
    plt.rcParams["axes.unicode_minus"] = False

    fig, ax = plt.subplots(figsize=(12, max(6, len(depts) * 0.5)))

    for idx, year in enumerate(years):
        counts = [year_data[year].get(dept, 0) for dept in depts]
        ax.barh(y_positions + offsets[idx], counts, height=bar_height, label=str(year))

    ax.set_yticks(y_positions)
    ax.set_yticklabels(depts)
    ax.invert_yaxis()
    ax.set_xlabel("人數")
    ax.set_ylabel("系所")
    ax.set_title("112-114 學年度各系招生人數（三年並排）")
    ax.legend(title="學年度")
    ax.grid(axis="x", linestyle="--", alpha=0.3)

    fig.tight_layout()
    fig.savefig(output_path, dpi=200)
    plt.close(fig)
    return output_path


if __name__ == "__main__":
    result = create_task1_chart()
    print(f"Task 1 chart saved to: {result}")
