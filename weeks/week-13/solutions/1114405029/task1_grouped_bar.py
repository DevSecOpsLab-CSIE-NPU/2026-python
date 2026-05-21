import csv
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def setup_chinese_font() -> None:
    plt.rcParams["font.sans-serif"] = [
        "Microsoft JhengHei",
        "Microsoft YaHei",
        "SimHei",
        "Arial Unicode MS",
    ]
    plt.rcParams["axes.unicode_minus"] = False


def get_data_dir() -> Path:
    return Path(__file__).resolve().parents[4] / "assets" / "stu-data"


def load_year(year: int, data_dir: Path) -> dict[str, int]:
    file_path = data_dir / f"{year}年新生資料庫.csv"
    dept_counter = Counter()

    with open(file_path, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            dept_name = row["系所名稱"].strip()
            if dept_name:
                dept_counter[dept_name] += 1

    return dict(dept_counter)


def get_top_depts(year_data: dict[int, dict], top_n: int = 8) -> list[str]:
    top_depts = set()

    for year_counts in year_data.values():
        sorted_depts = sorted(
            year_counts.items(),
            key=lambda item: item[1],
            reverse=True,
        )

        for dept_name, _ in sorted_depts[:top_n]:
            top_depts.add(dept_name)

    return sorted(
        top_depts,
        key=lambda dept: year_data[114].get(dept, 0),
        reverse=True,
    )


def plot_grouped_bar(
    year_data: dict[int, dict[str, int]],
    depts: list[str],
    output_path: Path,
) -> None:
    setup_chinese_font()

    years = sorted(year_data.keys())
    y_positions = np.arange(len(depts))
    bar_height = 0.24

    fig, ax = plt.subplots(figsize=(14, 9))

    for index, year in enumerate(years):
        values = [year_data[year].get(dept, 0) for dept in depts]
        offset = (index - 1) * bar_height

        bars = ax.barh(
            y_positions + offset,
            values,
            height=bar_height,
            label=f"{year} 學年度",
        )

        ax.bar_label(bars, padding=3, fontsize=8)

    ax.set_yticks(y_positions)
    ax.set_yticklabels(depts, fontsize=11)
    ax.invert_yaxis()

    ax.set_xlabel("招生人數（人）", fontsize=12)
    ax.set_ylabel("系所名稱", fontsize=12)
    ax.set_title(
        "國立澎湖科技大學 112～114 學年度各系招生人數比較",
        fontsize=16,
        pad=15,
    )

    ax.legend(
        title="學年度",
        fontsize=10,
        title_fontsize=11,
    )

    ax.grid(axis="x", linestyle="--", alpha=0.4)

    max_value = max(
        year_data[year].get(dept, 0)
        for year in years
        for dept in depts
    )
    ax.set_xlim(0, max_value + 10)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    fig.tight_layout()
    fig.savefig(output_path, dpi=300)
    plt.close(fig)


def main() -> None:
    data_dir = get_data_dir()

    year_data = {
        112: load_year(112, data_dir),
        113: load_year(113, data_dir),
        114: load_year(114, data_dir),
    }

    depts = get_top_depts(year_data, top_n=8)

    output_path = Path(__file__).resolve().parent / "output" / "task1.png"
    plot_grouped_bar(year_data, depts, output_path)

    print(f"已產生圖表：{output_path}")


if __name__ == "__main__":
    main()