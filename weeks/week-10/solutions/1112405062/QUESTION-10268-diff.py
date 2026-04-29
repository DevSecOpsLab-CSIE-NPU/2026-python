"""
UVA 10268 - 10^78?
===================

題目說明：
- k 個水球，n 層樓
- 找在最糟情況下測出水球破掉樓層的最少次數
- 如果 t > 63，輸出 "More than 63 trials needed."
"""

import sys

def solve():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        k, n = map(int, line.split())
        if k == 0:
            break
        
        ans = min_trials(k, n)
        print(ans)

def min_trials(k, n):
    if n <= 0:
        return 0
    
    k = min(k, 63)
    
    # 二分搜尋最小 t（comb_sum 隨 t 單調遞增）
    lo, hi = 1, 63
    ans = None
    while lo <= hi:
        mid = (lo + hi) // 2
        if comb_sum(mid, k) >= n:
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    
    if ans is not None:
        return ans
    return "More than 63 trials needed."

def comb_sum(t, k):
    """正確計算 C(t,1) + C(t,2) + ... + C(t,k)"""
    total = 0
    c = 1  # C(t, 0)
    for i in range(1, min(k, t) + 1):
        # C(t,i) = C(t,i-1) * (t - i + 1) / i
        c = c * (t - i + 1) // i
        total += c
    return total

if __name__ == "__main__":
    solve()
