"""
UVA 10268 - 10^78? (Easy Version)
==================================

題目說明：
- k 個水球，n 層樓
- 找在最糟情況下測出水球破掉樓層的最少次數
- 如果 t > 63，輸出 "More than 63 trials needed."

更簡單的寫法：
- 直接使用 math.comb 計算組合數
- 一行程式計算 comb_sum
"""

import sys
import math

def solve():
    """主函式：讀取輸入、輸出結果"""
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
    """
    找到最少嘗試次數
    
    參數：
    - k: 水球數量
    - n: 樓層數
    
    回傳：最少嘗試次數，或 "More than 63 trials needed."
    """
    if n <= 1:
        return 1
    
    # 最多考慮 63 次（因為 n 是 64 位元）
    k = min(k, 63)
    
    # 嘗試 t = 1 到 63 次
    for t in range(1, 64):
        # t 次嘗試、k 個水球最多能測試 C(t,1)+C(t,2)+...+C(t,k) 層
        total = sum(math.comb(t, i) for i in range(1, min(k, t) + 1))
        
        if total >= n:
            return t
    
    return "More than 63 trials needed."

if __name__ == "__main__":
    solve()