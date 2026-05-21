from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt

YEARS = (112, 113, 114)
DEFAULT_OUTPUT = Path(__file__).resolve().parent / "output" / "task1.png"


def resolve_data_dir(base_file: Path) -> Path:
    """Resolve data dir and keep compatibility with assignment sample path."""
    candidates = [
        base_file.parent.parent.parent.parent / "assets" / "stu-data",
        base_file.parent.parent.parent.parent.parent / "assets" / "stu-data",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return candidates[0]


DATA_DIR = resolve_data_dir(Path(__file__).resolve())


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


def get_top_depts(year_data: dict[int, dict], top_n: int = 8) -> list[str]:
    """從多年資料中找出任一年曾進前 top_n 的系所清單。"""
    selected: set[str] = set()

    for _, counts in year_data.items():
        ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:top_n]
        selected.update(dept for dept, _ in ranked)

    totals = {
        dept: sum(counts.get(dept, 0) for counts in year_data.values())
        for dept in selected
    }
    return sorted(selected, key=lambda dept: (-totals[dept], dept))


def plot_grouped_bar(
    year_data: dict[int, dict[str, int]],
    departments: list[str],
    output_path: Path,
) -> None:
    plt.rcParams["font.sans-serif"] = [
        "Microsoft JhengHei",
        "Noto Sans CJK TC",
        "PingFang TC",
        "Heiti TC",
        "Arial Unicode MS",
        "sans-serif",
    ]
    plt.rcParams["axes.unicode_minus"] = False

    fig, ax = plt.subplots(figsize=(12, 8))
    bar_h = 0.22
    y_base = list(range(len(departments)))
    colors = ["#77AADD", "#EE8866", "#44BB99"]

    for idx, year in enumerate(YEARS):
        offsets = [y + (idx - 1) * bar_h for y in y_base]
        values = [year_data[year].get(dept, 0) for dept in departments]
        ax.barh(offsets, values, height=bar_h, color=colors[idx], label=f"{year} 學年度")

        for y, value in zip(offsets, values):
            if value > 0:
                ax.text(value + 0.4, y, str(value), va="center", fontsize=9)

    ax.set_yticks(y_base)
    ax.set_yticklabels(departments)
    ax.invert_yaxis()
    ax.set_xlabel("人數")
    ax.set_ylabel("系所")
    ax.set_title("112-114 學年度各系招生人數（三年並排）", pad=12)
    ax.grid(axis="x", linestyle="--", alpha=0.3)
    ax.legend(loc="lower right")

    fig.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=180)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description="Task 1: Grouped bar chart for 112~114")
    parser.add_argument("--data-dir", type=Path, default=DATA_DIR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    year_data = {year: load_year(year, args.data_dir) for year in YEARS}
    top_depts = get_top_depts(year_data, top_n=8)
    plot_grouped_bar(year_data, top_depts, args.output)
    print(f"Saved: {args.output}")


if __name__ == "__main__":
    main()
