from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib import font_manager


DATA_DIR = Path(__file__).resolve().parents[4] / "assets" / "stu-data"
OUTPUT_DIR = Path(__file__).resolve().parent / "output"


def load_year(year: int, data_dir: Path) -> dict[str, int]:
    """讀取單一年份 CSV，回傳 {系所名稱: 人數} 的 dict"""
    path = data_dir / f"{year}年新生資料庫.csv"
    counts: Counter[str] = Counter()

    with path.open(encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            dept = (row.get("系所名稱") or "").strip()
            if dept:
                counts[dept] += 1

    return dict(counts)


def get_top_depts(year_data: dict[int, dict], top_n: int = 8) -> list[str]:
    """從多年資料中找出任一年曾進前 top_n 的系所清單"""
    candidates: set[str] = set()

    for year in sorted(year_data):
        ranked = sorted(year_data[year].items(), key=lambda item: (-item[1], item[0]))[:top_n]
        for dept, _ in ranked:
            candidates.add(dept)

    def sort_key(dept: str) -> tuple[int, int, str]:
        values = [year_data[year].get(dept, 0) for year in sorted(year_data)]
        return (-sum(values), -max(values), dept)

    return sorted(candidates, key=sort_key)[:top_n]


def _configure_font() -> None:
    font_path = Path(r"C:\Windows\Fonts\msjh.ttc")
    if font_path.exists():
        font_manager.fontManager.addfont(str(font_path))
        plt.rcParams["font.family"] = "Microsoft JhengHei"


def plot_grouped_bar(year_data: dict[int, dict[str, int]], output_path: Path) -> None:
    years = sorted(year_data)
    depts = get_top_depts(year_data, top_n=8)

    if not depts:
        raise ValueError("沒有可繪圖的系所資料")

    _configure_font()

    x_positions = list(range(len(depts)))
    width = 0.25
    offsets = [(index - (len(years) - 1) / 2) * width for index in range(len(years))]
    colors = ["#4e79a7", "#f28e2b", "#59a14f"]

    plt.figure(figsize=(14, 8))
    for index, year in enumerate(years):
        counts = [year_data[year].get(dept, 0) for dept in depts]
        plt.bar(
            [position + offsets[index] for position in x_positions],
            counts,
            width=width,
            label=f"{year}學年度",
            color=colors[index % len(colors)],
        )

    plt.xticks(x_positions, depts, rotation=20, ha="right")
    plt.ylabel("人數")
    plt.xlabel("系所名稱")
    plt.title("112-114學年度各系招生人數並排長條圖")
    plt.legend()
    plt.tight_layout()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=160)
    plt.close()


def main() -> None:
    parser = argparse.ArgumentParser(description="繪製 112-114 學年度並排長條圖")
    parser.add_argument("--data-dir", type=Path, default=DATA_DIR)
    parser.add_argument("--output", type=Path, default=OUTPUT_DIR / "task1.png")
    args = parser.parse_args()

    year_data = {year: load_year(year, args.data_dir) for year in [112, 113, 114]}
    plot_grouped_bar(year_data, args.output)
    print(f"saved to {args.output}")


if __name__ == "__main__":
    main()