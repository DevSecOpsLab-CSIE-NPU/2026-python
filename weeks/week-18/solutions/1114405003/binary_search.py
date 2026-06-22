"""
第四題 二分搜尋效能
學號: 1114405003
K = 100 + 03 = 103

功能：
- 二分搜尋找出 K，回報比較次數
- 用 timeit 比較線性 vs 二分搜尋
- 畫雷達圖呈現多維權衡
"""
import timeit
import random
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def generate_sorted_array(n: int, seed: int = 42) -> list[int]:
    """
    產生升冪排序的整數陣列

    Args:
        n: 陣列大小
        seed: 隨機種子 (確保可重現)

    Returns:
        排序後的整數陣列
    """
    random.seed(seed)
    arr = sorted(random.sample(range(1, n * 2), n))
    return arr


def linear_search(arr: list[int], target: int) -> tuple[bool, int, int]:
    """
    線性搜尋

    Args:
        arr: 已排序陣列
        target: 目標值

    Returns:
        (是否找到, 索引, 比較次數)
    """
    cmp = 0
    for i, val in enumerate(arr):
        cmp += 1
        if val == target:
            return True, i, cmp
        elif val > target:
            return False, -1, cmp
    return False, -1, cmp


def binary_search(arr: list[int], target: int) -> tuple[bool, int, int]:
    """
    二分搜尋

    Args:
        arr: 已排序陣列
        target: 目標值

    Returns:
        (是否找到, 索引, 比較次數)
    """
    left, right = 0, len(arr) - 1
    cmp = 0

    while left <= right:
        mid = (left + right) // 2
        cmp += 1

        if arr[mid] == target:
            return True, mid, cmp
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False, -1, cmp


def time_search(func, arr: list[int], target: int, repeats: int = 100) -> float:
    """
    量測搜尋函式執行時間

    Args:
        func: 搜尋函式
        arr: 陣列
        target: 目標值
        repeats: 重複次數

    Returns:
        平均執行時間 (秒)
    """
    timer = timeit.Timer(lambda: func(arr, target))
    total_time = timer.timeit(number=repeats)
    return total_time / repeats


def create_radar_chart(out_path: str) -> None:
    """
    畫雷達圖比較線性搜尋與二分搜尋

    Args:
        out_path: 輸出圖片路徑
    """
    # 維度定義 (值越大越好)
    categories = [
        '小n速度',
        '大n速度',
        '不需排序',
        '實作簡易度',
        '最壞情況效能'
    ]
    N = len(categories)

    # 正規化分數 (0-1, 1 為最佳)
    linear_scores = [0.9, 0.2, 1.0, 1.0, 0.1]   # 線性搜尋
    binary_scores = [0.7, 0.9, 0.3, 0.7, 0.9]   # 二分搜尋

    # 計算角度
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]  # 閉合

    # 加上閉合值
    linear_scores += linear_scores[:1]
    binary_scores += binary_scores[:1]

    # 建立雷達圖
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    # 畫線
    ax.plot(angles, linear_scores, 'o-', linewidth=2, label='線性搜尋', color='#FF6B6B')
    ax.fill(angles, linear_scores, alpha=0.25, color='#FF6B6B')

    ax.plot(angles, binary_scores, 'o-', linewidth=2, label='二分搜尋', color='#4ECDC4')
    ax.fill(angles, binary_scores, alpha=0.25, color='#4ECDC4')

    # 設定標籤
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=12)
    ax.set_ylim(0, 1)
    ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_yticklabels(['0.2', '0.4', '0.6', '0.8', '1.0'], fontsize=9)

    # 標題與圖例
    ax.set_title('線性搜尋 vs 二分搜尋 - 多維權衡比較', fontsize=14, fontweight='bold', pad=20)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=11)

    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()


def main():
    """主程式"""
    K = 103  # 學號 1114405003, 末兩碼 03, K = 100 + 3 = 103

    # 產生大型陣列 (≥10^5)
    n = 200000
    arr = generate_sorted_array(n)

    # (1) 二分搜尋找 K
    found, idx, cmp = binary_search(arr, K)
    if found:
        print(f"FOUND {idx} cmp={cmp}")
    else:
        print(f"NOT FOUND cmp={cmp}")

    # (2) timeit 比較
    linear_time = time_search(linear_search, arr, K)
    binary_time = time_search(binary_search, arr, K)

    print(f"linear : {linear_time:.4f} s")
    print(f"binary : {binary_time:.4f} s")

    if linear_time > binary_time:
        print("=> binary faster")
    else:
        print("=> linear faster")

    # (3) 畫雷達圖
    import os
    os.makedirs("assets", exist_ok=True)
    create_radar_chart("assets/radar.png")
    print("雷達圖已儲存: assets/radar.png")


if __name__ == "__main__":
    main()
