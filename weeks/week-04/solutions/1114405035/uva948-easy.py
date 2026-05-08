# UVA 948 - Fibonaccimal Base (簡單好記版)
# 學生：1114405035 賴彥廷

import sys

def solve():
    # 1. 準備斐波那契數列 (到 10^8 大約 40 個)
    fibs = [1, 2]
    for _ in range(40):
        fibs.append(fibs[-1] + fibs[-2])
    
    # 2. 讀取輸入
    lines = sys.stdin.read().split()
    if not lines: return
    
    n_cases = int(lines[0])
    for i in range(1, n_cases + 1):
        num = int(lines[i])
        original_num = num
        
        # 3. 尋找起點
        start_idx = 0
        for idx in range(len(fibs)-1, -1, -1):
            if fibs[idx] <= num:
                start_idx = idx
                break
        
        # 4. 貪婪法湊數字
        res = ""
        for idx in range(start_idx, -1, -1):
            if num >= fibs[idx]:
                res += "1"
                num -= fibs[idx]
            else:
                res += "0"
        
        print(f"{original_num} = {res} (fib)")

if __name__ == "__main__":
    solve()
