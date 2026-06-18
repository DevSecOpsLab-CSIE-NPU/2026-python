import json
import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# 使用 Agg 後端以支援無視窗環境
matplotlib.use("Agg")


def generate_radar_chart(data_path: str, output_path: str) -> None:
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"基準測試數據檔案不存在: {data_path}")

    with open(data_path, "r") as f:
        results = json.load(f)

    # 取得 N=80000 的搜尋速度數據
    benchmark = results["benchmark"]
    sizes = benchmark["sizes"]
    try:
        idx_80k = sizes.index(80000)
    except ValueError:
        raise ValueError("資料中缺少 N=80000 的基準測試數據")

    t_lin = benchmark["linear"][idx_80k]
    t_bin = benchmark["binary"][idx_80k]
    t_set_opt = benchmark["set_optimized"][idx_80k]

    # 搜尋速度正規化分數 (Min-Max，越快得分越高，範圍 1 ~ 5)
    t_max = max(t_lin, t_bin, t_set_opt)
    t_min = min(t_lin, t_bin, t_set_opt)

    def calc_speed_score(t):
        if t_max == t_min:
            return 5.0
        return 1.0 + 4.0 * (t_max - t) / (t_max - t_min)

    score_lin_speed = calc_speed_score(t_lin)
    score_bin_speed = calc_speed_score(t_bin)
    score_set_speed = calc_speed_score(t_set_opt)

    # 評估維度與標籤
    categories = [
        "Search Speed\n(搜尋速度)",
        "Pre-processing Cost\n(預處理代價)",
        "Space Efficiency\n(記憶體節約度)",
        "Unsorted Support\n(未排序支援度)",
        "Code Simplicity\n(實作難易度)",
    ]
    num_vars = len(categories)

    # 各演算法在五個維度上的評分 [速度, 預處理, 空間, 未排序支援, 簡單度]
    scores_linear = [score_lin_speed, 5.0, 5.0, 5.0, 5.0]
    scores_binary = [score_bin_speed, 2.0, 5.0, 1.0, 3.0]
    scores_set = [score_set_speed, 3.0, 1.0, 5.0, 5.0]

    # 計算極座標角度
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # 封閉雷達圖多邊形
    scores_linear += scores_linear[:1]
    scores_binary += scores_binary[:1]
    scores_set += scores_set[:1]
    angles += angles[:1]

    # 建立極座標畫布
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    # 設定刻度與網格
    plt.xticks(angles[:-1], categories, color="#2c3e50", size=10)
    ax.set_rlabel_position(0)
    plt.yticks([1, 2, 3, 4, 5], ["1", "2", "3", "4", "5"], color="#95a5a6", size=9)
    plt.ylim(0, 5)

    # 繪製各搜尋演算法
    # 1. Linear Search
    ax.plot(
        angles,
        scores_linear,
        linewidth=2,
        linestyle="solid",
        label="Linear Search",
        color="#e74c3c",
    )
    ax.fill(angles, scores_linear, color="#e74c3c", alpha=0.15)

    # 2. Binary Search
    ax.plot(
        angles,
        scores_binary,
        linewidth=2,
        linestyle="solid",
        label="Binary Search",
        color="#3498db",
    )
    ax.fill(angles, scores_binary, color="#3498db", alpha=0.15)

    # 3. Set Search (Optimized)
    ax.plot(
        angles,
        scores_set,
        linewidth=2,
        linestyle="solid",
        label="Set Search (Optimized)",
        color="#2ecc71",
    )
    ax.fill(angles, scores_set, color="#2ecc71", alpha=0.15)

    # 圖例與標題
    plt.legend(loc="upper right", bbox_to_anchor=(0.1, 0.1), frameon=True)
    plt.title(
        "Search Algorithms Comparison\n(搜尋演算法多維度權衡圖)",
        size=13,
        color="#2c3e50",
        y=1.1,
        weight="bold",
    )

    # 確保輸出目錄存在
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # 存檔
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    generate_radar_chart("results.json", "assets/radar.png")
