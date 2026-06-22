import os
import matplotlib
import numpy as np

# 無視窗環境設定，必須在匯入 pyplot 之前設定
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def draw_radar_chart():
    # 建立輸出目錄
    os.makedirs("assets", exist_ok=True)

    # 五個評估維度
    categories = [
        "Query Efficiency\n(查詢效率)",
        "Prep Cost\n(預處理省易度)",
        "Memory Efficiency\n(記憶體省用度)",
        "Update Performance\n(動態新增效能)",
        "Simplicity\n(實作簡意度)",
    ]
    N = len(categories)

    # 三種演算法的分數 (1-5 分，分數越高越好)
    # 1. Linear: 查詢慢(1)，不需預處理(5)，省記憶體(5)，新增極快(5)，極簡單(5)
    linear_scores = [1, 5, 5, 5, 5]
    # 2. Binary: 查詢快(4)，需排序(3)，省記憶體(5)，新增慢(2)，較複雜(3)
    binary_scores = [4, 3, 5, 2, 3]
    # 3. Set: 查詢極快(5)，需建雜湊(2)，耗記憶體(1)，新增快(5)，中等(4)
    set_scores = [5, 2, 1, 5, 4]

    # 雷達圖角度計算
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]  # 閉合雷達圖

    # 閉合分數資料
    linear_scores += linear_scores[:1]
    binary_scores += binary_scores[:1]
    set_scores += set_scores[:1]

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

    # Set Search
    ax.plot(
        angles,
        set_scores,
        linewidth=2,
        linestyle="solid",
        label="Set Search",
        color="#2ca02c",
    )
    ax.fill(angles, set_scores, color="#2ca02c", alpha=0.1)

    # 增加圖例與標題
    plt.title("Multidimensional Trade-offs of Search Algorithms\n(三種搜尋演算法的多維權衡雷達圖)", size=12, color="black", y=1.1)
    plt.legend(loc="upper right", bbox_to_anchor=(0.1, 0.1))

    # 存檔
    plt.savefig("assets/radar.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("[*] 雷達圖 assets/radar.png 繪製成功！")


if __name__ == "__main__":
    draw_radar_chart()
