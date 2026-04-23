# 10038-easy.py
# UVA 10038：Jolly Jumpers (簡單版)
# 核心邏輯：把差值都放進一個集合 (set)，最後看 1 到 n-1 是否都在裡面

import sys

def solve():
    # 逐行讀取，因為題目可能有多個測試案例
    for line in sys.stdin:
        parts = list(map(int, line.split()))
        if not parts:
            continue

        n = parts[0]
        elements = parts[1:]

        # 如果只有一個數字，根據定義是 Jolly
        if n == 1:
            print("Jolly")
            continue

        # 1. 計算所有相鄰差的絕對值
        diffs = set()
        for i in range(len(elements) - 1):
            d = abs(elements[i] - elements[i+1])
            # 只紀錄在 1 ~ n-1 範圍內的差值
            if 1 <= d <= n - 1:
                diffs.add(d)

        # 2. 檢查差值的種類是否剛好等於 n-1
        # 因為 set 會去重，且我們有限制範圍，所以數量對了就代表 1~n-1 都有
        if len(diffs) == n - 1:
            print("Jolly")
        else:
            print("Not jolly")

if __name__ == "__main__":
    solve()
