"""
畫 linear vs binary 的多維權衡雷達圖。
無視窗環境（CI / 沒有 DISPLAY）需要在 import pyplot 之前指定 Agg backend。
正規化與維度選擇的理由寫在 README.md。
"""

import math
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

DIMENSIONS = ["small_n_time", "large_n_time", "cmp", "needs_presort"]
LABELS = ["small-n speed", "large-n speed", "fewer comparisons", "no presort needed"]


def _normalize(metrics):
    """
    把每個維度轉成「越大越好、範圍落在 (0, 1]」的分數：
    - 連續且越小越好的維度（時間、cmp）：score = min_value / value，
      贏家恰好等於 1，輸家是 min/value 的比例（避免兩個方法數值差太多時，
      輸家被壓成肉眼看不出來的 0）。
    - 已經是 0/1 類別變數的維度（needs_presort）：直接 score = 1 - value，
      因為「不需要先排序」才是優點。
    """
    scores = {method: [] for method in metrics}
    for dim in DIMENSIONS:
        values = {method: metrics[method][dim] for method in metrics}
        if dim == "needs_presort":
            for method in metrics:
                scores[method].append(1 - values[method])
            continue
        min_v = min(v for v in values.values() if v > 0) if any(values.values()) else 1
        for method in metrics:
            v = values[method]
            scores[method].append(min_v / v if v > 0 else 1.0)
    return scores


def plot_radar(metrics, output_path="assets/radar.png"):
    """metrics: collect_radar_metrics() 回傳的 dict（'linear' / 'binary' 兩個 method）。"""
    scores = _normalize(metrics)
    n = len(DIMENSIONS)
    angles = [i / n * 2 * math.pi for i in range(n)]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={"projection": "polar"})
    for method, color in (("linear", "tab:blue"), ("binary", "tab:orange")):
        values = scores[method] + scores[method][:1]
        ax.plot(angles, values, label=method, color=color)
        ax.fill(angles, values, alpha=0.15, color=color)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(LABELS)
    ax.set_ylim(0, 1)
    ax.set_title("Linear vs Binary Search Trade-offs")
    ax.legend(loc="upper right", bbox_to_anchor=(1.2, 1.1))

    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    fig.savefig(output_path, bbox_inches="tight")
    plt.close(fig)
