"""UVA 10062（簡單好記版）。

這份版本刻意選「最好背」而不是「最快」的寫法，
適合課堂手打與口頭解釋。

題目資料定義：
- 第 1 行是 N（牛的數量）
- 接下來 N-1 行，描述第 2 到第 N 個位置
- a[pos] 的意思是：在第 pos 個位置前面，有幾頭牛編號比它小

關鍵轉換：
1. 建立 remaining = [1, 2, ..., N]，表示還沒被拿走的編號（且保持遞增）。
2. 當我們決定第 pos 個位置時，它要拿的是「目前 remaining 中第 a[pos]+1 小的值」。
3. 為什麼是 +1：
    若前面有 a[pos] 個比它小，那它自己就是第 a[pos]+1 小。
4. 為什麼從右往左：
    右邊位置先決定，拿走一些編號後，
    左邊位置看到的 remaining 才會正好對應題目的計數。

複雜度：
- 這版使用 list.pop(index) 從中間移除元素，單次最差 O(N)
- 總共做 N 次，所以整體 O(N^2)
- 優點是程式短、步驟直覺，缺點是大資料時較慢
"""

from __future__ import annotations

import sys


def solve(data: list[int]) -> list[int]:
    """根據題目輸入整數陣列，回傳最終隊伍編號順序。

    參數 data 格式：
    - data[0] = N
    - data[1:] = 題目給的 N-1 個計數值

    回傳值：
    - 長度為 N 的陣列，依序對應第 1..N 個位置的牛編號
    """
    if not data:
        # 空輸入時直接回傳空結果，避免後續索引錯誤。
        return []

    n = data[0]

    # a[pos]：第 pos 個位置前面有幾個較小編號。
    # 為了讓索引與題目「第幾個位置」一致，使用 1-based：a[1]..a[n]。
    # 題目沒有提供第 1 個位置的值，因為它前面沒有人，所以補 0。
    a = [0] * (n + 1)
    for pos in range(2, n + 1):
        # data 的第 pos-1 個數，對應到題目的第 pos 個位置。
        a[pos] = data[pos - 1]

    # 尚未使用的編號（永遠保持遞增）。
    # 例如 remaining = [1, 2, 4, 5]，代表編號 3 已經被右側位置拿走。
    remaining = list(range(1, n + 1))

    # ans[pos]：第 pos 個位置的牛編號（同樣使用 1-based，最後再切片）。
    ans = [0] * (n + 1)

    # 從右往左放，避免影響尚未決定的左側位置。
    # 這是本題最關鍵的順序。
    for pos in range(n, 0, -1):
        # 第 a[pos]+1 小 => list 的 0-based 索引是 a[pos]。
        # 直接 pop 代表「選到這個值並把它從可用編號中移除」。
        ans[pos] = remaining.pop(a[pos])

    # ans[0] 是佔位，不屬於答案。
    return ans[1:]


def main() -> None:
    # 從標準輸入一次讀入所有整數，符合線上評測常見格式。
    data = list(map(int, sys.stdin.buffer.read().split()))
    result = solve(data)

    # 題目要求每行輸出一個編號。
    if result:
        sys.stdout.write("\n".join(map(str, result)))


if __name__ == "__main__":
    main()
