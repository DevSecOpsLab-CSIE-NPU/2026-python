# 948-easy.py
# UVA 948：Fibonaccimal Base (簡單版)
# 核心邏輯：先算出一堆斐波那契數，再從大的開始扣

import sys

def solve():
    # 1. 預先算好斐波那契數列 (到 10^8 左右)
    # 數列：1, 2, 3, 5, 8, 13, 21... (從 1, 2 開始比較好處理題目要求)
    fibs = [1, 2]
    while fibs[-1] < 100000000:
        fibs.append(fibs[-1] + fibs[-2])

    # 2. 讀取測資數量
    input_lines = sys.stdin.read().split()
    if not input_lines: return
    n_cases = int(input_lines[0])

    # 3. 處理每一筆測資
    for i in range(1, n_cases + 1):
        num = int(input_lines[i])
        original_num = num

        # 4. 貪婪演算法：從最大的斐波那契數開始試
        res = ""
        started = False
        # 反著跑 fibs (由大到小)
        for f in reversed(fibs):
            if num >= f:
                res += "1"
                num -= f
                started = True
            elif started:
                res += "0"

        # 5. 輸出結果
        print(f"{original_num} = {res} (fib)")

if __name__ == "__main__":
    solve()
