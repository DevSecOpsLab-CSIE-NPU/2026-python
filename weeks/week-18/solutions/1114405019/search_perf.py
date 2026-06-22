"""
第四題：二分搜尋效能比較。

學號末兩碼 = 19，搜尋目標 K = 100 + 19 = 119。
"""

import bisect
import math
import random
import sys
import timeit

K = 119


def linear_search(arr, target):
    """從頭逐一比較，找到回傳 (idx, cmp)；找不到回傳 (None, cmp)。"""
    cmp = 0
    for i, v in enumerate(arr):
        cmp += 1
        if v == target:
            return i, cmp
    return None, cmp


def binary_search(arr, target):
    """
    前提：arr 已升冪排序。
    每次迴圈只做一次 == / < / > 的「決定方向」比較，cmp 計次以此為準，
    這樣才能跟 ceil(log2(m)) + 1 的理論上限對齊。
    """
    cmp = 0
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        cmp += 1
        if arr[mid] == target:
            return mid, cmp
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return None, cmp


def generate_sorted_array(m, target, present, seed=None):
    """
    產生長度為 m 的升冪唯一整數陣列。
    present=True：target 保證恰好出現一次。
    present=False：target 保證不出現。
    做法：在排除 target 的範圍內取樣 m（或 m-1）個唯一值，
    present=True 時再用 bisect.insort 把 target 插入正確位置。
    """
    rng = random.Random(seed)
    span = max(m * 5, 1000)
    pool_low, pool_high = target - span, target + span
    candidates = [v for v in range(pool_low, pool_high) if v != target]

    count = m - 1 if present else m
    sample = rng.sample(candidates, count)
    sample.sort()

    if present:
        bisect.insort(sample, target)
    return sample


def time_searches(arr, target, number=5):
    """用 timeit 量測 linear_search 與 binary_search 各跑 number 次的總秒數。"""
    linear_time = timeit.timeit(lambda: linear_search(arr, target), number=number)
    binary_time = timeit.timeit(lambda: binary_search(arr, target), number=number)
    return {"linear": linear_time, "binary": binary_time}


def collect_radar_metrics(small_n, large_n, target, seed=None):
    """
    為雷達圖準備原始數據（未正規化）：
    - small_n / large_n 兩種規模下，linear 與 binary 各自的耗時
    - 在 large_n 規模下兩者的比較次數 cmp
    - 是否需要先排序（categorical：linear=0 不需要，binary=1 需要）
    """
    small_arr = generate_sorted_array(small_n, target, present=True, seed=seed)
    large_arr = generate_sorted_array(large_n, target, present=True, seed=seed)

    small_time = time_searches(small_arr, target)
    large_time = time_searches(large_arr, target)

    _, linear_cmp = linear_search(large_arr, target)
    _, binary_cmp = binary_search(large_arr, target)

    return {
        "linear": {
            "small_n_time": small_time["linear"],
            "large_n_time": large_time["linear"],
            "cmp": linear_cmp,
            "needs_presort": 0,
        },
        "binary": {
            "small_n_time": small_time["binary"],
            "large_n_time": large_time["binary"],
            "cmp": binary_cmp,
            "needs_presort": 1,
        },
    }


def _read_array_from_stdin():
    """嘗試從 stdin 讀取「第1行 m；第2行 m 個升冪整數」，讀不到就回傳 None。"""
    data = sys.stdin.read().strip()
    if not data:
        return None
    lines = data.splitlines()
    if len(lines) < 2:
        return None
    m = int(lines[0])
    arr = [int(x) for x in lines[1].split()]
    if len(arr) != m:
        raise ValueError(f"輸入的整數個數 ({len(arr)}) 與宣告的 m ({m}) 不一致")
    return arr


def main():
    arr = _read_array_from_stdin()
    if arr is None:
        # 沒有 stdin 輸入：自動生成一個 >= 10^5 的大陣列，並保證 K 在裡面。
        arr = generate_sorted_array(m=200_000, target=K, present=True, seed=0)

    idx, cmp = binary_search(arr, K)
    if idx is not None:
        print(f"FOUND {idx} cmp={cmp}")
    else:
        print(f"NOT FOUND cmp={cmp}")

    times = time_searches(arr, K)
    print(f"linear : {times['linear']:.4f} s")
    print(f"binary : {times['binary']:.4f} s")
    faster = "binary" if times["binary"] < times["linear"] else "linear"
    print(f"=> {faster} faster")

    from plot import plot_radar

    metrics = collect_radar_metrics(small_n=200, large_n=200_000, target=K, seed=0)
    plot_radar(metrics, "assets/radar.png")


if __name__ == "__main__":
    main()
