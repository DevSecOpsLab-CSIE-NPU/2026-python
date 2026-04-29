# solution_10268_optimized.py
# UVA 10268 優化解決方案
# 計算雞蛋掉落的最少試驗次數
# 優化重點：改進組合數計算；優化二分搜索邏輯；簡化代碼結構

import sys

def binomial_coefficient(n, k):
    """
    計算二項式係數 C(n, k)
    - 優化：使用更有效的計算方法，避免大數溢出
    """
    if k > n or k < 0:
        return 0
    if k == 0 or k == n:
        return 1
    
    # 利用對稱性：C(n, k) = C(n, n-k)
    k = min(k, n - k)
    
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    
    return result

def min_trials_needed(k, n):
    """
    計算最少試驗次數
    - 使用二分搜索找最小 m，使 C(m, 1) + C(m, 2) + ... + C(m, k) >= n
    - 最多試驗 64 次
    """
    if n <= 1:
        return n
    
    # 二分搜索最小試驗次數
    left, right = 1, 64
    result = 64
    
    while left <= right:
        mid = (left + right) // 2
        
        # 計算 C(mid, 1) + C(mid, 2) + ... + C(mid, k)
        total = sum(binomial_coefficient(mid, i) for i in range(1, k + 1))
        
        if total >= n:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return result if result <= 64 else -1

def main():
    """主程式"""
    data = sys.stdin.read().split()
    index = 0
    
    while index < len(data):
        k = int(data[index])
        n = int(data[index + 1])
        index += 2
        
        if k == 0:
            break
        
        result = min_trials_needed(k, n)
        print(result)

if __name__ == "__main__":
    main()
