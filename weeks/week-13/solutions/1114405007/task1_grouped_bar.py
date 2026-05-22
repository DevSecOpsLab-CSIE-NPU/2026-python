from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import rcParams

DATA_DIR = Path(__file__).resolve().parents[4] / "assets" / "stu-data"
YEARS = (112, 113, 114)


def configure_font() -> None:
    """設定常見中文字體，避免圖表文字顯示為方塊。"""
    rcParams["font.sans-serif"] = [
        "Microsoft JhengHei",
        "PingFang TC",
        "Noto Sans CJK TC",
        "Arial Unicode MS",
        "DejaVu Sans",
    ]
    rcParams["axes.unicode_minus"] = False


def load_year(year: int, data_dir: Path) -> dict[str, int]:
    """讀取單一年份 CSV，回傳 {系所名稱: 人數}。"""
    csv_path = data_dir / f"{year}年新生資料庫.csv"
    counts: Counter[str] = Counter()

    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            dept = (row.get("系所名稱") or "").strip()
            if dept:
                counts[dept] += 1

    return dict(counts)


def get_top_depts(year_data: dict[int, dict[str, int]], top_n: int = 8) -> list[str]:
    """從多年資料中找出任一年曾進前 top_n 的系所。"""
    selected: set[str] = set()
    all_depts: set[str] = set()

    for data in year_data.values():
        all_depts.update(data.keys())
        top_items = sorted(data.items(), key=lambda item: item[1], reverse=True)[:top_n]
        selected.update(dept for dept, _ in top_items)

    return sorted(
        selected,
        key=lambda dept: max(year_data[y].get(dept, 0) for y in year_data),
        reverse=True,
    )


def plot_grouped_bar(year_data: dict[int, dict[str, int]], depts: list[str], out_path: Path) -> None:
    """繪製 112/113/114 三年並排長條圖。"""
    fig, ax = plt.subplots(figsize=(12, 8))

    y_positions = list(range(len(depts)))
    bar_height = 0.24
    offsets = [-bar_height, 0.0, bar_height]
    colors = ["#9ecae1", "#3182bd", "#08519c"]

    for idx, year in enumerate(YEARS):
        values = [year_data[year].get(dept, 0) for dept in depts]
        bars = ax.barh(
            [y + offsets[idx] for y in y_positions],
            values,
            height=bar_height,
            label=f"{year}",
            color=colors[idx],
            edgecolor="white",
        )

        for bar, val in zip(bars, values):
            ax.text(val + 0.3, bar.get_y() + bar.get_height() / 2, str(val), va="center", fontsize=9)

    ax.set_yticks(y_positions)
    ax.set_yticklabels(depts)
    ax.invert_yaxis()
    ax.set_xlabel("人數")
    ax.set_ylabel("系所")
    ax.set_title("112-114 學年度各系招生人數（三年並排）")
    ax.grid(axis="x", linestyle="--", alpha=0.3)
    ax.legend(title="學年度")

    fig.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=200)
    plt.close(fig)


def main() -> None:
    configure_font()
    year_data = {year: load_year(year, DATA_DIR) for year in YEARS}
    depts = get_top_depts(year_data, top_n=8)
    out_path = Path(__file__).parent / "output" / "task1.png"
    plot_grouped_bar(year_data, depts, out_path)
    print(f"[task1] saved: {out_path}")


if __name__ == "__main__":
    main()
