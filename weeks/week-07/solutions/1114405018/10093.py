from __future__ import annotations

import sys
from typing import List


def bit_count(x: int) -> int:
    """回傳二進位中 1 的數量（代表該列放了幾支炮兵）。"""
    return x.bit_count()


def generate_valid_states(m: int) -> List[int]:
    """產生單列所有合法狀態。

    合法條件（同一列內）：
    1. 不能相鄰放置（距離 1）。
    2. 不能隔 1 格放置（距離 2）。
    """
    states: List[int] = []
    limit = 1 << m
    for s in range(limit):
        if (s & (s << 1)) != 0:
            continue
        if (s & (s << 2)) != 0:
            continue
        states.append(s)
    return states


def max_artillery(grid: List[str]) -> int:
    """回傳在給定地圖下可部署的最大炮兵數。"""

    n = len(grid)
    if n == 0:
        return 0

    m = len(grid[0])
    valid_states = generate_valid_states(m)
    state_cnt = len(valid_states)

    # blocked[i] 的 bit=1 表示第 i 列該格是山地 H，不能放炮兵
    blocked = [0] * n
    for i in range(n):
        mask = 0
        for j, ch in enumerate(grid[i]):
            if ch == "H":
                mask |= 1 << j
        blocked[i] = mask

    # row_candidates[i]：第 i 列可用的狀態索引（需避開山地）
    row_candidates: List[List[int]] = [[] for _ in range(n)]
    for i in range(n):
        b = blocked[i]
        for idx, s in enumerate(valid_states):
            if (s & b) == 0:
                row_candidates[i].append(idx)

    # dp_prev[a][b]：處理到第 i-1 列時，
    # i-2 列狀態索引為 a、i-1 列狀態索引為 b 的最大炮兵數。
    # 轉移到第 i 列時要檢查：
    # 1. 與 i-1 列不能同欄（垂直距離 1）
    # 2. 與 i-2 列不能同欄（垂直距離 2）
    NEG = -10**9
    dp_prev = [[NEG] * state_cnt for _ in range(state_cnt)]

    # 初始化第 0 列：
    # 由於還沒有前一列、前二列，統一視為空狀態 0 來簡化轉移。
    zero_idx = valid_states.index(0)
    for b in row_candidates[0]:
        dp_prev[zero_idx][b] = bit_count(valid_states[b])

    for i in range(1, n):
        dp_cur = [[NEG] * state_cnt for _ in range(state_cnt)]

        for a in range(state_cnt):
            for b in range(state_cnt):
                base = dp_prev[a][b]
                if base <= NEG:
                    continue

                sb = valid_states[b]
                for c in row_candidates[i]:
                    sc = valid_states[c]

                    # i 列與 i-1 列不能同欄
                    if (sc & sb) != 0:
                        continue

                    # i 列與 i-2 列不能同欄
                    sa = valid_states[a]
                    if (sc & sa) != 0:
                        continue

                    val = base + bit_count(sc)
                    if val > dp_cur[b][c]:
                        dp_cur[b][c] = val

        dp_prev = dp_cur

    # 取所有尾端狀態中的最大值。
    # n=1 時答案其實已在初始化時寫入 dp_prev。
    ans = 0
    for a in range(state_cnt):
        for b in range(state_cnt):
            if dp_prev[a][b] > ans:
                ans = dp_prev[a][b]
    return ans


def solve(data: str) -> str:
    """接收整段輸入文字並回傳答案字串。"""

    # 輸入格式：
    # 第一行 N M
    # 接下來 N 行，每行長度 M，字元為 P 或 H
    tokens = data.strip().split()
    if not tokens:
        return "0"

    n = int(tokens[0])
    m = int(tokens[1])

    # 接下來 n 個 token 是每一列地圖字串（長度 m）
    rows = tokens[2:2 + n]
    if len(rows) != n:
        rows = rows[:n]

    # 若某些列長度與 m 不符，仍切到 m，避免資料異常造成越界。
    grid = [r[:m] for r in rows]
    return str(max_artillery(grid))


def main() -> None:
    # 競賽模式：讀 stdin，輸出單一整數答案。
    data = sys.stdin.read()
    sys.stdout.write(solve(data))


if __name__ == "__main__":
    main()
