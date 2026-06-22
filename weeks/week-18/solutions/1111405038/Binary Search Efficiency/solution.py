"""
解題檔：二分搜尋效能（Binary Search Efficiency）- 第四題

1. 產生升冪排序整數陣列
2. 執行線性搜尋與二分搜尋，統計比較次數
3. 使用 timeit 比較兩種方法效能
4. 繪製雷達圖比較不同維度
"""

import timeit
import matplotlib.pyplot as plt
import numpy as np


def linear_search(arr, target):
    """線性搜尋：回傳 (found, idx, cmp)"""
    cmp = 0
    for idx, value in enumerate(arr):
        cmp += 1
        if value == target:
            return True, idx, cmp
    return False, -1, cmp


def binary_search(arr, target):
    """二分搜尋：回傳 (found, idx, cmp)"""
    left = 0
    right = len(arr) - 1
    cmp = 0

    while left <= right:
        mid = (left + right) // 2
        cmp += 1

        if arr[mid] == target:
            return True, mid, cmp
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False, -1, cmp


def generate_sorted_array(size, start=1, step=3):
    """產生升冪排序的整數陣列"""
    return [start + i * step for i in range(size)]


def measure_performance(arr, target, search_func, repeat=1000):
    """使用 timeit 量測搜尋效能"""
    timer = timeit.Timer(lambda: search_func(arr, target))
    time_result = timer.timeit(number=repeat)
    return time_result / repeat


def plot_radar_chart(linear_cmp, binary_cmp, linear_time, binary_time):
    """繪製雷達圖比較線性與二分搜尋"""
    # 正規化指標
    max_cmp = max(linear_cmp, binary_cmp)
    max_time = max(linear_time, binary_time)

    categories = ["比較次數", "執行時間", "實作簡易度", "資料排序需求"]
    linear_scores = [
        linear_cmp / max_cmp if max_cmp > 0 else 0,
        linear_time / max_time if max_time > 0 else 0,
        0.8,  # 實作簡易度（線性搜尋更簡單）
        0.2,  # 資料排序需求（線性無需排序）
    ]
    binary_scores = [
        binary_cmp / max_cmp if max_cmp > 0 else 0,
        binary_time / max_time if max_time > 0 else 0,
        0.5,  # 實作簡易度（二分複雜）
        1.0,  # 資料排序需求（二分需排序）
    ]

    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    linear_scores += [linear_scores[0]]
    binary_scores += [binary_scores[0]]
    angles += [angles[0]]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection="polar"))
    ax.plot(angles, linear_scores, "o-", linewidth=2, label="Linear Search")
    ax.fill(angles, linear_scores, alpha=0.25)
    ax.plot(angles, binary_scores, "o-", linewidth=2, label="Binary Search")
    ax.fill(angles, binary_scores, alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_ylim(0, 1)
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))
    ax.set_title("線性搜尋 vs 二分搜尋效能比較", pad=20)
    ax.grid(True)

    plt.savefig("assets/radar.png", dpi=100, bbox_inches="tight")
    print("✓ 雷達圖已保存至 assets/radar.png")
    plt.close()


def main():
    """主程式：按照題目要求執行四步驟"""
    import os

    # Step 1: 產生升冪排序整數陣列
    arr = generate_sorted_array(100, start=1, step=2)
    target = 138

    print("=" * 70)
    print("第四題：二分搜尋效能")
    print("=" * 70)
    print(f"\n陣列大小: {len(arr)}")
    print(f"搜尋目標: {target}")

    # Step 2: 執行搜尋並輸出結果
    print("\n【搜尋結果】")
    linear_found, linear_idx, linear_cmp = linear_search(arr, target)
    binary_found, binary_idx, binary_cmp = binary_search(arr, target)

    if linear_found:
        print(f"Linear : FOUND idx={linear_idx} cmp={linear_cmp}")
    else:
        print(f"Linear : NOT FOUND cmp={linear_cmp}")

    if binary_found:
        print(f"Binary : FOUND idx={binary_idx} cmp={binary_cmp}")
    else:
        print(f"Binary : NOT FOUND cmp={binary_cmp}")

    # Step 3: 使用 timeit 比較效能
    print("\n【效能比較】")
    linear_time = measure_performance(arr, target, linear_search, repeat=1000)
    binary_time = measure_performance(arr, target, binary_search, repeat=1000)

    print(f"Linear : {linear_time:.6f} s")
    print(f"Binary : {binary_time:.6f} s")

    if binary_time < linear_time:
        print("=> binary faster")
    else:
        print("=> linear faster")

    # Step 4: 繪製雷達圖
    print("\n【視覺化結果】")
    if not os.path.exists("assets"):
        os.makedirs("assets")

    plot_radar_chart(linear_cmp, binary_cmp, linear_time, binary_time)
    print("\n完成！")


if __name__ == "__main__":
    main()
