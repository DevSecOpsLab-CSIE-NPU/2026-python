"""第四題：二分搜尋與線性搜尋的比較分析

學號末兩碼為 56，所以搜尋目標 K = 100 + 56 = 156。

本題需要：
1. 產生或讀入升冪排序的整數陣列
2. 實作二分搜尋找出 K，輸出「是否存在」與「比較次數」
3. 用 timeit 分別量測線性搜尋與二分搜尋的耗時
4. 畫一張雷達圖呈現線性 vs 二分的多維權衡
"""

import sys
import timeit
from typing import Tuple

# 搜尋目標
K = 156

# 大型陣列（升冪排序）
ARRAY_SIZE = 100000


def linear_search(arr: list, target: int) -> Tuple[bool, int]:
    """線性搜尋：從頭到尾逐一比較。
    
    Args:
        arr: 整數陣列（需升冪排序）
        target: 搜尋目標
    
    Returns:
        (是否找到, 比較次數)
    """
    cmp_count = 0
    for idx, num in enumerate(arr):
        cmp_count += 1
        if num == target:
            return True, cmp_count
    return False, cmp_count


def binary_search(arr: list, target: int) -> Tuple[bool, int, int]:
    """二分搜尋：使用分而治之的策略。
    
    Args:
        arr: 整數陣列（需升冪排序）
        target: 搜尋目標
    
    Returns:
        (是否找到, 比較次數, 索引)
    """
    left, right = 0, len(arr) - 1
    cmp_count = 0
    
    while left <= right:
        mid = (left + right) // 2
        cmp_count += 1
        
        if arr[mid] == target:
            return True, cmp_count, mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False, cmp_count, -1


def generate_array(size: int) -> list:
    """產生升冪排序的整數陣列。
    
    Args:
        size: 陣列大小
    
    Returns:
        升冪排序的整數陣列
    """
    return sorted([i * 2 for i in range(size)])  # 偶數陣列


def main():
    """主程式。"""
    # 讀取輸入或產生陣列
    try:
        line = input().strip()
        if line:
            m = int(line)
            arr = list(map(int, input().split()))
        else:
            m = ARRAY_SIZE
            arr = generate_array(m)
    except (EOFError, ValueError):
        # 若無輸入，產生預設陣列
        m = ARRAY_SIZE
        arr = generate_array(m)
    
    # 確保陣列升冪排序
    arr.sort()
    
    # 二分搜尋
    found, cmp_binary, idx = binary_search(arr, K)
    
    # 輸出搜尋結果
    if found:
        print(f"FOUND {idx} cmp={cmp_binary}")
    else:
        print(f"NOT FOUND cmp={cmp_binary}")
    
    # 用 timeit 測量性能
    linear_time = timeit.timeit(
        lambda: linear_search(arr, K),
        number=100
    )
    binary_time = timeit.timeit(
        lambda: binary_search(arr, K),
        number=100
    )
    
    # 標準化時間（每次平均）
    linear_avg = linear_time / 100
    binary_avg = binary_time / 100
    
    # 輸出性能比較
    print(f"linear: {linear_avg:.6f} s")
    print(f"binary: {binary_avg:.6f} s")
    
    # 判斷誰較快
    if binary_avg < linear_avg:
        print("=> binary faster")
    elif linear_avg < binary_avg:
        print("=> linear faster")
    else:
        print("=> same speed")


if __name__ == "__main__":
    main()
