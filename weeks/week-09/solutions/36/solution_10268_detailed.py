# solution_10268_detailed.py
# UVA 10268 詳細註解版本解決方案
# 包含詳細的繁體中文註解

import sys

def min_trials(k, n):
    """
    計算雞蛋掉落問題的最少試驗次數。
    參數：
    - k: 雞蛋數量
    - n: 樓層數
    返回：最小次數或字符串
    """
    if n == 0 or n == 1:
        return n  # 0 或 1 層，直接返回
    if k == 1:
        return n  # 1 個雞蛋，試 n 次
    low = 1
    high = 64
    while low < high:
        mid = (low + high) // 2  # 二分中點
        c = 1
        for i in range(1, k+1):
            c = c * (mid - i + 1) // i  # 計算組合數 C(mid, i)
            if c >= n:
                break
        if c >= n:
            high = mid  # 可以試更少次
        else:
            low = mid + 1  # 需要更多次
    if low > 63:
        return "More than 63 trials needed."  # 超過 63 次
    return low

if __name__ == "__main__":
    data = sys.stdin.read().split()  # 讀取所有輸入數據
    index = 0  # 數據索引
    while index < len(data):
        k = int(data[index])  # 雞蛋數
        n = int(data[index+1])  # 樓層數
        index += 2
        if k == 0:
            break  # 結束標記
        print(min_trials(k, n))  # 輸出結果