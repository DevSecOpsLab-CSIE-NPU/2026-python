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

# 設置中文字體
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False


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
    """繪製雷達圖比較線性與二分搜尋
    
    四個維度：
    1. 執行時間 - 實際執行耗時
    2. 平均性能 - 平均比較次數（越少越好）
    3. 最壞性能 - 最壞情況下的比較次數
    4. 緩存效率 - 記憶體存取效率
    """
    # 正規化指標
    max_cmp = max(linear_cmp, binary_cmp)
    max_time = max(linear_time, binary_time)
    
    # 計算最壞情況比較次數（假設陣列大小為 100）
    arr_size = 100
    linear_worst = arr_size  # 線性最壞情況：全部比較
    binary_worst = int(np.log2(arr_size)) + 1  # 二分最壞情況：log n
    
    categories = ["執行時間", "平均性能", "最壞性能", "緩存效率"]
    linear_scores = [
        linear_time / max_time if max_time > 0 else 0,  # 執行時間
        linear_cmp / max_cmp if max_cmp > 0 else 0,  # 平均性能（比較次數越少越好）
        1.0 - (linear_worst / arr_size),  # 最壞性能（越接近 0 越好）
        0.3,  # 緩存效率（線性搜尋：存取順序規律，但每次檢查後跳到下一個）
    ]
    binary_scores = [
        binary_time / max_time if max_time > 0 else 0,  # 執行時間
        binary_cmp / max_cmp if max_cmp > 0 else 0,  # 平均性能（比較次數越少越好）
        1.0 - (binary_worst / arr_size),  # 最壞性能（越接近 1 越好）
        0.9,  # 緩存效率（二分搜尋：二分邏輯導致更好的快取局部性）
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

    # ===== 參數設定 =====
    # 學號末兩碼：38
    # K = 100 + 末兩碼 = 100 + 38 = 138
    student_id_last_two_digits = 38
    target = 100 + student_id_last_two_digits  # = 138

    # Step 1: 產生升冪排序整數陣列
    arr = generate_sorted_array(100, start=1, step=2)

    print("=" * 70)
    print("第四題：二分搜尋效能")
    print("=" * 70)
    print(f"\n【參數設定】")
    print(f"學號末兩碼：{student_id_last_two_digits}")
    print(f"搜尋目標 K：100 + {student_id_last_two_digits} = {target}")
    print(f"\n【搜尋配置】")
    print(f"陣列大小：{len(arr)}")
    print(f"陣列範圍：[1, 3, 5, ..., {arr[-1]}]")

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
