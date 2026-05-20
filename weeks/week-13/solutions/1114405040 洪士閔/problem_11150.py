"""
Problem 11150 - 青蛙過橋（最少踩到石子數）

此檔提供壓縮座標的解法並包含 process(input_str) 方便 unit test。
繁體中文註解說明關鍵步驟：座標壓縮、動態規劃。
"""

from typing import List, Tuple


def compress_positions(L: int, stones: List[int], T: int) -> Tuple[int, List[int]]:
    """將原始座標壓縮，移除可以直接跳過的長段。

    原理：若鄰兩點 gap > T，青蛙可以不用考慮 gap 中的中間點，
    壓縮後座標為原座標減去之前所有 (gap-T) 的累計值。
    回傳 (newL, new_points_list)，其中 new_points_list 包含 0 與 newL。
    """
    pts = [0] + sorted(stones) + [L]
    sub = 0
    new_pts = []
    prev = pts[0]
    new_pts.append(0)
    for p in pts[1:]:
        gap = p - prev
        if gap > T:
            sub += (gap - T)
        new_pts.append(p - sub)
        prev = p
    newL = L - sub
    return newL, new_pts


def solve_one(L: int, S: int, T: int, stones: List[int]) -> int:
    """計算最少需要踩到的石子數（使用壓縮座標 + BFS/DP）。"""
    newL, new_pts = compress_positions(L, stones, T)

    # 建立石子標記陣列（索引為壓縮後座標）
    is_stone = [False] * (newL + 1)
    for p in new_pts[1:-1]:
        if 0 <= p <= newL:
            is_stone[p] = True

    INF = 10**9
    dp = [INF] * (newL + 1)
    dp[0] = 0

    for i in range(newL + 1):
        if dp[i] == INF:
            continue
        for jump in range(S, T + 1):
            j = i + jump
            if j >= newL:
                # 到達或越過終點，不會踩終點上的石子（題目保證終點無石子）
                if dp[newL] > dp[i]:
                    dp[newL] = dp[i]
            else:
                cost = dp[i] + (1 if is_stone[j] else 0)
                if cost < dp[j]:
                    dp[j] = cost

    return dp[newL]


def process(input_str: str) -> str:
    """解析多組輸入並輸出每組的最少踩石子數（每組一行）。"""
    tokens = input_str.strip().split()
    if not tokens:
        return ""
    p = 0
    out_lines: List[str] = []
    while p < len(tokens):
        L = int(tokens[p]); p += 1
        S = int(tokens[p]); T = int(tokens[p+1]); M = int(tokens[p+2]); p += 3
        stones = []
        for _ in range(M):
            stones.append(int(tokens[p])); p += 1
        out_lines.append(str(solve_one(L, S, T, stones)))
    return "\n".join(out_lines)


def main():
    import sys
    print(process(sys.stdin.read()))


if __name__ == '__main__':
    main()
