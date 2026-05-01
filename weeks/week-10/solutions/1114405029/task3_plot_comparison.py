from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.font_manager import FontProperties


def main() -> None:
    """使用 seaborn 建立 Task 1 / Task 2 函式耗時比較圖。"""

    functions = [
        "read_csv",
        "write_json",
        "read_json",
        "write_xml",
    ]

    times = [
        0.039912,
        0.001980,
        0.009801,
        0.001806,
    ]

    output_path = Path("output/timing_comparison.png")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # 直接指定 Windows 微軟正黑體字型檔，避免中文變成方塊
    font_path = "C:/Windows/Fonts/msjh.ttc"
    font_prop = FontProperties(fname=font_path)

    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(11, 6))

    colors = sns.color_palette("Set2", len(functions))

    chart = sns.barplot(
        x=functions,
        y=times,
        hue=functions,
        palette=colors,
        legend=False
    )

    chart.set_title(
        "Task 1/2 函式耗時比較",
        fontproperties=font_prop,
        fontsize=20,
        pad=18
    )

    chart.set_xlabel(
        "函式名稱",
        fontproperties=font_prop,
        fontsize=14
    )

    chart.set_ylabel(
        "執行時間（秒）",
        fontproperties=font_prop,
        fontsize=14
    )

    for index, cost in enumerate(times):
        chart.text(
            index,
            cost + 0.0005,
            f"{cost:.6f}s",
            ha="center",
            fontsize=11,
            weight="bold"
        )

    slowest_index = times.index(max(times))

    chart.text(
        slowest_index,
        max(times) * 0.82,
        "CSV 讀取耗時最高",
        ha="center",
        fontproperties=font_prop,
        fontsize=13,
        weight="bold"
    )

    chart.text(
        1.5,
        max(times) * 0.65,
        "結論：CSV 讀取需要解析原始資料欄位，\n因此本次執行時間最長。",
        ha="center",
        fontproperties=font_prop,
        fontsize=12,
        bbox={
            "boxstyle": "round,pad=0.4",
            "facecolor": "white",
            "alpha": 0.8
        }
    )

    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()

    print("圖表已儲存：output/timing_comparison.png")


if __name__ == "__main__":
    main()