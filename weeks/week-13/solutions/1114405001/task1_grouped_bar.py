from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


DATA_DIR = Path(__file__).resolve().parents[4] / "assets" / "stu-data"
OUTPUT_DIR = Path(__file__).resolve().parent / "output"


def load_year(year: int, data_dir: Path) -> dict[str, int]:
    """讀取單一年份 CSV，回傳 {系所名稱: 人數} 的 dict"""
    path = data_dir / f"{year}年新生資料庫.csv"
    counts: Counter[str] = Counter()
    with path.open(encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            department = (row.get("系所名稱") or "").strip()
            if department:
                counts[department] += 1
    return dict(counts)


def get_top_depts(year_data: dict[int, dict[str, int]], top_n: int = 8) -> list[str]:
    """從多年資料中找出任一年曾進前 top_n 的系所清單"""
    yearly_ranks: dict[str, list[tuple[int, int]]] = {}
    for year, counts in year_data.items():
        ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
        for rank, (department, count) in enumerate(ranked[:top_n], start=1):
            yearly_ranks.setdefault(department, []).append((year, count))

    candidates = []
    for department, hits in yearly_ranks.items():
        total = sum(count for _, count in hits)
        best_count = max(count for _, count in hits)
        first_year = min(year for year, _ in hits)
        candidates.append((total, best_count, -first_year, department))

    candidates.sort(key=lambda item: (-item[0], -item[1], item[2], item[3]))
    return [department for _, _, _, department in candidates[:top_n]]


def build_grouped_bar_chart(years: list[int] | None = None, top_n: int = 8) -> Path:
    """產生三年並排長條圖並存檔。"""
    years = years or [112, 113, 114]
    year_data = {year: load_year(year, DATA_DIR) for year in years}
    departments = get_top_depts(year_data, top_n=top_n)

    plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei", "Noto Sans CJK TC", "DejaVu Sans"]
    plt.rcParams["axes.unicode_minus"] = False

    fig, ax = plt.subplots(figsize=(12, 7))
    positions = list(range(len(departments)))
    bar_height = 0.22
    offsets = [-(bar_height), 0.0, bar_height]
    colors = ["#5b8ff9", "#61d9a3", "#f6bd16"]

    for offset, year, color in zip(offsets, years, colors, strict=False):
        counts = [year_data[year].get(department, 0) for department in departments]
        ax.barh([position + offset for position in positions], counts, height=bar_height, label=f"{year}學年度", color=color)

    ax.set_yticks(positions)
    ax.set_yticklabels(departments)
    ax.invert_yaxis()
    ax.set_xlabel("人數")
    ax.set_title("112-114學年度各系招生人數比較")
    ax.legend()
    ax.grid(axis="x", linestyle="--", alpha=0.3)

    fig.tight_layout()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / "task1.png"
    fig.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    return output_path


def main() -> None:
    build_grouped_bar_chart()


if __name__ == "__main__":
    main()