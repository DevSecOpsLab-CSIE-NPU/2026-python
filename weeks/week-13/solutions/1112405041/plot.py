"""Stage 3: 圖表繪製"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei", "SimSun", "Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False


def plot_grouped_bar(year_data: dict[int, dict[str, int]], top_depts: list[str], out_path: str):
    """三年並排長條圖"""
    years = sorted(year_data.keys())

    values = []
    for y in years:
        depts = year_data[y]
        values.append([depts.get(d, 0) for d in top_depts])

    x = np.arange(len(top_depts))
    width = 0.25

    _, ax = plt.subplots(figsize=(12, 6))
    for i, (y, v) in enumerate(zip(years, values)):
        bars = ax.bar(x + i * width, v, width, label=f"{y}年")
        for bar, val in zip(bars, v):
            if val > 0:
                ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                        str(val), ha="center", va="bottom", fontsize=8)

    ax.set_xlabel("系所名稱")
    ax.set_ylabel("人數")
    ax.set_title("各系招生人數比較（112/113/114 學年度）")
    ax.set_xticks(x + width)
    ax.set_xticklabels(top_depts, rotation=30, ha="right")
    ax.legend()
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def plot_heatmap(county_data: dict[int, dict[str, int]], top_counties: list[str], out_path: str):
    """縣市 × 年份熱力圖"""
    years = sorted(county_data.keys())

    matrix = []
    for c in top_counties:
        row = []
        for y in years:
            row.append(county_data[y].get(c, 0))
        matrix.append(row)

    _, ax = plt.subplots(figsize=(10, 8))
    im = ax.imshow(matrix, aspect="auto", cmap="YlOrRd")

    ax.set_xticks(range(len(years)))
    ax.set_xticklabels([f"{y}年" for y in years])
    ax.set_yticks(range(len(top_counties)))
    ax.set_yticklabels(top_counties)
    ax.set_xlabel("學年度")
    ax.set_ylabel("縣市")
    ax.set_title("各縣市招生人數熱力圖（109～114 學年度）")

    for i in range(len(top_counties)):
        for j in range(len(years)):
            ax.text(j, i, str(matrix[i][j]), ha="center", va="center", fontsize=8)

    plt.colorbar(im, ax=ax, label="人數")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()
