import csv
import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "MingLiU"]
mpl.rcParams["axes.unicode_minus"] = False

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR.parent.parent.parent.parent / "assets" / "stu-data"
OUTPUT_DIR = BASE_DIR / "output"
YEARS = [112, 113, 114]
TOP_N = 8


def load_year(year: int, data_dir: Path = DATA_DIR) -> dict[str, int]:
    filename = data_dir / f"{year}年新生資料庫.csv"
    result = {}
    with open(filename, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            dept = row.get("系所名稱", "未知")
            result[dept] = result.get(dept, 0) + 1
    return result


def get_top_depts(year_data: dict[int, dict], top_n: int = TOP_N) -> list[str]:
    all_depts = set()
    for y, depts in year_data.items():
        sorted_depts = sorted(depts.items(), key=lambda x: -x[1])
        all_depts.update(d for d, _ in sorted_depts[:top_n])
    return list(all_depts)


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    year_data = {y: load_year(y) for y in YEARS}
    top_depts = get_top_depts(year_data)

    values = {y: [year_data[y].get(d, 0) for d in top_depts] for y in YEARS}

    fig, ax = plt.subplots(figsize=(10, 6))
    y_pos = np.arange(len(top_depts))
    bar_height = 0.25
    colors = ["#4C72B0", "#55A868", "#C44E52"]

    for i, y in enumerate(YEARS):
        offset = (i - 1) * bar_height
        bars = ax.barh(y_pos + offset, values[y], bar_height,
                       label=f"{y}學年度", color=colors[i])
        for bar, v in zip(bars, values[y]):
            ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height() / 2,
                    str(v), va="center", fontsize=8)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(top_depts, fontsize=10)
    ax.set_xlabel("人數")
    ax.set_title("112-114 學年度各系招生人數比較")
    ax.legend(loc="lower right")
    ax.invert_yaxis()
    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / "task1.png")
    print(f"圖表已儲存：{OUTPUT_DIR / 'task1.png'}")
    plt.close(fig)


if __name__ == "__main__":
    main()
