from pathlib import Path
import csv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

DATA_DIR = Path(__file__).parent.parent.parent.parent.parent / "assets" / "stu-data"
OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


def _find_chinese_font() -> str | None:
    candidates = [
        "Microsoft JhengHei",
        "Microsoft YaHei",
        "PingFang TC",
        "Noto Sans CJK TC",
        "SimHei",
    ]
    available = {f.name for f in fm.fontManager.ttflist}
    for c in candidates:
        if c in available:
            return c
    return None


_font = _find_chinese_font()
if _font:
    plt.rcParams["font.family"] = _font
plt.rcParams["axes.unicode_minus"] = False


def load_year(year: int, data_dir: Path) -> dict[str, int]:
    filename = data_dir / f"{year}年新生資料庫.csv"
    counts: dict[str, int] = {}
    with open(filename, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            dept = row["系所名稱"].strip()
            counts[dept] = counts.get(dept, 0) + 1
    return counts


def get_top_depts(year_data: dict[int, dict], top_n: int = 8) -> list[str]:
    selected = set()
    for counts in year_data.values():
        sorted_depts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        selected.update([dept for dept, _ in sorted_depts[:top_n]])

    def total_count(dept: str) -> int:
        return sum(counts.get(dept, 0) for counts in year_data.values())

    ranked = sorted(selected, key=total_count, reverse=True)
    return ranked[:top_n]


def plot_grouped_bar(year_data: dict[int, dict], top_depts: list[str], output_path: Path) -> None:
    years = sorted(year_data.keys())
    n_depts = len(top_depts)
    n_years = len(years)

    bar_height = 0.25
    y_base = np.arange(n_depts)
    colors = ["#4C72B0", "#DD8452", "#55A868"]

    fig, ax = plt.subplots(figsize=(12, max(6, n_depts * 0.9)))
    for i, (year, color) in enumerate(zip(years, colors)):
        counts = year_data[year]
        values = [counts.get(dept, 0) for dept in top_depts]
        y_pos = y_base - (n_years - 1) * bar_height / 2 + i * bar_height
        bars = ax.barh(y_pos, values, height=bar_height * 0.9, label=f"{year} 學年", color=color, alpha=0.9)
        for bar, val in zip(bars, values):
            if val > 0:
                ax.text(val + 0.5, bar.get_y() + bar.get_height() / 2, str(val), va="center", ha="left", fontsize=8)

    ax.set_yticks(y_base)
    ax.set_yticklabels(top_depts, fontsize=10)
    ax.invert_yaxis()
    ax.set_xlabel("招生人數")
    ax.set_title("112-114 學年度各系招生人數比較（前 8 名）", fontweight="bold")
    ax.legend(loc="lower right")
    ax.grid(axis="x", linestyle="--", alpha=0.35)
    ax.set_xlim(left=0)

    plt.tight_layout()
    plt.savefig(output_path, dpi=160, bbox_inches="tight")
    plt.close()


def main() -> None:
    years = [112, 113, 114]
    year_data = {y: load_year(y, DATA_DIR) for y in years}
    top_depts = get_top_depts(year_data, top_n=8)
    plot_grouped_bar(year_data, top_depts, OUTPUT_DIR / "task1.png")
    print("完成：output/task1.png")


if __name__ == "__main__":
    main()
