"""UVA/ZeroJudge 10062 簡單版（easy）。

題意（依課程版本）：
- 共有 N 個位置，每個位置最後要放一個 1..N 的唯一編號。
- 已知 a[i]（i >= 2）：在第 i 個位置之前，比它小的編號有幾個。
- 要還原整個排列。

這版主打「好懂、好記」：
1. 先準備目前還可用的編號清單 available = [1, 2, ..., N]。
2. 從最後一格往前填答案（i = N -> 1）。
3. 第 i 格要選「剩下編號中的第 a[i] + 1 小」，
     在 0-based 清單索引就是 available[a[i]]。
4. 取出後從 available 刪掉，繼續處理前一格。

為什麼要「從後往前」：
- a[i] 的定義只和「i 前面有多少較小編號」有關。
- 若先決定後面的格子，等於逐步縮小可用編號集合，
    就能直接用 a[i] 當作索引取第 k 小元素。

複雜度：
- 這份 easy 寫法每次 pop(index) 可能搬動元素，整體 O(N^2)。
- 優點是邏輯直觀、容易手寫。
- 若要應對大輸入，請改用 Fenwick Tree 版（solution.py），可到 O(N log N)。
"""

from __future__ import annotations

import sys


def solve(input_data: str) -> str:
    """接收整份輸入字串，回傳題目要求的輸出字串。"""

    # split() 可同時處理空白與換行，轉成整數後更容易依序讀取。
    nums = [int(x) for x in input_data.split()]
    if not nums:
        # 空輸入時直接回傳空字串，避免後續索引錯誤。
        return ""

    # 第 1 個數字是 N（牛的數量 / 排列長度）。
    n = nums[0]

    # 使用 1-based 陣列，讓程式索引和題目符號 a[1..N] 一致。
    # a[1] 題目沒有給，視為 0；a[2..n] 依序讀入。
    a = [0] * (n + 1)
    for i in range(2, n + 1):
        a[i] = nums[i - 1]

    # available 維持「當前還沒被使用」且遞增排序的編號。
    # 一開始全部可用，因此是 [1..N]。
    available = list(range(1, n + 1))

    # ans[1..N] 存最終答案，ans[0] 不使用（配合 1-based）。
    ans = [0] * (n + 1)

    # 反向還原：從第 N 格一路決定到第 1 格。
    for i in range(n, 0, -1):
        # a[i] 代表「前面有幾個比它小」，也就是在剩餘編號中的 0-based 索引。
        idx = a[i]

        # pop(idx) 會回傳第 idx 個元素，並從 available 中移除。
        # 這一步同時完成「選值」與「標記已使用」。
        ans[i] = available.pop(idx)

    # 依題目格式輸出：每行一個編號。
    return "\n".join(map(str, ans[1:]))


def main() -> None:
    # 一次讀入所有標準輸入，符合線上評測常見模式。
    data = sys.stdin.read()
    out = solve(data)
    if out:
        # 額外補一個換行，符合一般 CLI 輸出習慣。
        sys.stdout.write(out + "\n")


if __name__ == "__main__":
    main()
