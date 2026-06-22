import os
import matplotlib
import numpy as np

# 無視窗環境設定，必須在匯入 pyplot 之前設定
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def draw_radar_chart():
    # 建立輸出目錄
    os.makedirs("assets", exist_ok=True)

    # 五個評估維度（依期末考 PDF 建議維度設計）
    categories = [
        "Small N Speed\n(小 N 速度)",
        "Large N Speed\n(大 N 速度)",
        "No Pre-sorting\n(免排序度)",
        "Simplicity\n(實作簡易度)",
        "Worst-case Cmp\n(最壞比較優度)",
    ]
    N = len(categories)

    # 線性搜尋分數 (1-5 分)
    # 小N快(5), 大N慢(1), 不需排序(5), 極簡單(5), 最壞情況比較多(1)
    linear_scores = [5, 1, 5, 5, 1]

    # 二分搜尋分數 (1-5 分)
    # 小N快(4), 大N極快(5), 需要先排序(1), 較複雜(3), 最壞情況比較少(5)
    binary_scores = [4, 5, 1, 3, 5]

    # 雷達圖角度計算
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]  # 閉合雷達圖

    # 閉合分數資料
    linear_scores += linear_scores[:1]
    binary_scores += binary_scores[:1]

    # 初始化繪圖
    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(projection="polar"))

    # 設定極座標角度與標籤
    plt.xticks(angles[:-1], categories, color="grey", size=10)

    # 設定半徑限制與標籤
    ax.set_rlabel_position(0)
    plt.yticks([1, 2, 3, 4, 5], ["1", "2", "3", "4", "5"], color="grey", size=8)
    plt.ylim(0, 5)

    # 繪製與填充區域
    # Linear Search
    ax.plot(
        angles,
        linear_scores,
        linewidth=2,
        linestyle="solid",
        label="Linear Search",
        color="#1f77b4",
    )
    ax.fill(angles, linear_scores, color="#1f77b4", alpha=0.1)

    # Binary Search
    ax.plot(
        angles,
        binary_scores,
        linewidth=2,
        linestyle="solid",
        label="Binary Search",
        color="#ff7f0e",
    )
    ax.fill(angles, binary_scores, color="#ff7f0e", alpha=0.1)

    # 增加圖例與標題
    plt.title(
        "Linear vs Binary Search Trade-offs\n(線性 vs 二分搜尋多維度雷達圖)",
        size=12,
        color="black",
        y=1.1,
    )
    plt.legend(loc="upper right", bbox_to_anchor=(0.1, 0.1))

    # 存檔
    plt.savefig("assets/radar.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("[*] 雷達圖 assets/radar.png 繪製成功！")


if __name__ == "__main__":
    draw_radar_chart()
