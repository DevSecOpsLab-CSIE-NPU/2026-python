"""
Task 1：112、113、114 學年度各系招生人數並排長條圖
"""
from pathlib import Path
import csv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# 資料目錄：往上 5 層到達 repo 根目錄，再進 assets/stu-data
DATA_DIR = Path(__file__).parent.parent.parent.parent.parent / "assets" / "stu-data"

YEAR_FILES = {
    112: "112年新生資料庫.csv",
    113: "113年新生資料庫.csv",
    114: "114年新生資料庫.csv",
}


def load_year(year: int, data_dir: Path) -> dict[str, int]:
    """讀取單一年份 CSV，回傳 {系所名稱: 人數} 的 dict"""
    filename = f"{year}年新生資料庫.csv"
    filepath = data_dir / filename
    counts: dict[str, int] = {}
    with open(filepath, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            dept = row["系所名稱"].strip()
            counts[dept] = counts.get(dept, 0) + 1
    return counts


def get_top_depts(year_data: dict[int, dict], top_n: int = 8) -> list[str]:
    """從多年資料中找出任一年曾進前 top_n 的系所清單"""
    candidates: set[str] = set()
    for counts in year_data.values():
        sorted_depts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        for dept, _ in sorted_depts[:top_n]:
            candidates.add(dept)
    # 依第一個年份總人數排序，讓圖表穩定
    first_counts = next(iter(year_data.values()))
    return sorted(candidates, key=lambda d: first_counts.get(d, 0), reverse=True)


def plot_grouped_bar(year_data: dict[int, dict], top_depts: list[str], output_path: Path) -> None:
    """畫出並排長條圖並存檔"""
    years = sorted(year_data.keys())
    n_depts = len(top_depts)
    n_years = len(years)

    # 每組間距
    bar_height = 0.25
    y = np.arange(n_depts)

    # 嘗試使用系統中文字型
    chinese_fonts = [f.name for f in fm.fontManager.ttflist
                     if any(kw in f.name for kw in ("CJK", "Gothic", "Heiti", "PingFang", "Microsoft JhengHei", "Microsoft YaHei", "SimHei", "SimSun", "Noto"))]
    if chinese_fonts:
        plt.rcParams["font.family"] = chinese_fonts[0]
    plt.rcParams["axes.unicode_minus"] = False

    colors = ["#4C72B0", "#DD8452", "#55A868"]
    fig, ax = plt.subplots(figsize=(12, max(6, n_depts * 0.9)))

    for i, (year, color) in enumerate(zip(years, colors)):
        counts = year_data[year]
        values = [counts.get(dept, 0) for dept in top_depts]
        offset = (i - (n_years - 1) / 2) * bar_height
        bars = ax.barh(y + offset, values, height=bar_height, label=f"{year} 學年", color=color, alpha=0.85)
        for bar, val in zip(bars, values):
            if val > 0:
                ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height() / 2,
                        str(val), va="center", ha="left", fontsize=8)

    ax.set_yticks(y)
    ax.set_yticklabels(top_depts, fontsize=9)
    ax.set_xlabel("招生人數")
    ax.set_title("112～114 學年度各系招生人數並排長條圖（前 8 名系所）", fontsize=13, fontweight="bold")
    ax.legend(loc="lower right")
    ax.invert_yaxis()
    ax.set_xlim(0, max(
        v for counts in year_data.values() for v in counts.values()
    ) * 1.15)

    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"已輸出：{output_path}")


if __name__ == "__main__":
    year_data = {year: load_year(year, DATA_DIR) for year in YEAR_FILES}
    top_depts = get_top_depts(year_data, top_n=8)
    output_path = Path(__file__).parent / "output" / "task1.png"
    plot_grouped_bar(year_data, top_depts, output_path)
