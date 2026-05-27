from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

from task1_grouped_bar import load_year, get_top_depts, DATA_DIR
from task2_zipcode_heatmap import load_county_counts, get_top_counties

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


def build_dashboard() -> None:
    years3 = [112, 113, 114]
    years6 = [109, 110, 111, 112, 113, 114]

    year_data = {y: load_year(y, DATA_DIR) for y in years3}
    top_depts = get_top_depts(year_data, top_n=8)

    dept_total = {d: sum(year_data[y].get(d, 0) for y in years3) for d in top_depts}
    dept_sorted = sorted(dept_total.items(), key=lambda x: x[1], reverse=True)

    county_114 = load_county_counts(114, DATA_DIR)
    county_114_known = {k: v for k, v in county_114.items() if k != "其他"}
    pie_items = sorted(county_114_known.items(), key=lambda x: x[1], reverse=True)[:5]
    pie_labels = [k for k, _ in pie_items]
    pie_values = [v for _, v in pie_items]
    others = sum(county_114.values()) - sum(pie_values)
    if others > 0:
        pie_labels.append("其他")
        pie_values.append(others)

    total_by_year = [sum(load_year(y, DATA_DIR).values()) for y in years6]

    top3_for_lines = [d for d, _ in dept_sorted[:3]]
    series = {d: [load_year(y, DATA_DIR).get(d, 0) for y in years3] for d in top3_for_lines}

    fig = plt.figure(figsize=(16, 10))

    ax1 = plt.subplot(2, 2, 1)
    ax1.barh([d for d, _ in dept_sorted], [c for _, c in dept_sorted], color="#3E7CB1")
    ax1.invert_yaxis()
    ax1.set_title("長條圖：112-114 系所招生總量 Top 8", fontweight="bold")
    ax1.set_xlabel("人數")

    ax2 = plt.subplot(2, 2, 2)
    colors = plt.cm.Set3(np.linspace(0, 1, len(pie_labels)))
    ax2.pie(pie_values, labels=pie_labels, autopct="%1.1f%%", startangle=90, colors=colors)
    ax2.set_title("圓餅圖：114 年來源縣市占比", fontweight="bold")

    ax3 = plt.subplot(2, 2, 3)
    x = np.array(years6)
    y = np.array(total_by_year)
    z = np.polyfit(x, y, 2)
    p = np.poly1d(z)
    x_smooth = np.linspace(x.min(), x.max(), 120)
    ax3.plot(x_smooth, p(x_smooth), color="#2A9D8F", linewidth=2.5)
    ax3.scatter(years6, total_by_year, color="#1D3557", s=28)
    ax3.set_title("曲線圖：109-114 全校招生趨勢（二次趨勢）", fontweight="bold")
    ax3.set_xlabel("學年度")
    ax3.set_ylabel("人數")
    ax3.grid(alpha=0.3)

    ax4 = plt.subplot(2, 2, 4)
    for dept, vals in series.items():
        ax4.plot(years3, vals, marker="o", linewidth=2.0, label=dept)
    ax4.set_title("折線圖：112-114 熱門系所比較", fontweight="bold")
    ax4.set_xlabel("學年度")
    ax4.set_ylabel("人數")
    ax4.grid(alpha=0.3)
    ax4.legend(fontsize=9)

    fig.suptitle("Week 13 招生資料儀表板", fontsize=16, fontweight="bold")
    fig.tight_layout(rect=[0, 0.02, 1, 0.96])
    out = OUTPUT_DIR / "task3_dashboard.png"
    fig.savefig(out, dpi=170)
    plt.close(fig)
    print("完成：output/task3_dashboard.png")


if __name__ == "__main__":
    build_dashboard()
