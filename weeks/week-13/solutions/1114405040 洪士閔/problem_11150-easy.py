"""
簡易版 Problem 11150（青蛙過橋，最少踩到石子數） — 詳細註解版

問題快速回顧：一隻青蛙要從 0 跳到 L，跳距落在 [S, T]。
河道上有些石子，若落在石子位置會被記為踩到一次；目標是最小化踩到的石子數。

核心技巧：座標壓縮（compress）
- 若某段 gap > T，青蛙不可能從該段內的任意兩點來回跳動，等價地可以把該段的多餘長度移除。
- 壓縮後的位置變小，DP 狀態縮短，便於用 O(newL * (T-S)) 的 DP 求解。

此版本以清楚步驟展現算法邏輯，並在每個函式提供使用說明與範例。
"""

from typing import List, Tuple


def compress_positions(L: int, stones: List[int], T: int) -> Tuple[int, List[int]]:
    """座標壓縮：把原始 0..L 的座標壓縮成 newL，使跳距介於 S..T 的情況下仍等價。

    詳細說明：
    - 先把 0、所有石子座標、L 合併為一個排序列 pts。
    - 對於每個相鄰點，如果 gap > T，則可以減去 (gap - T) 的冗餘長度，累加到 sub。
    - 將後續所有點扣除 sub 得到 new_pts，最終 newL = L - sub。

    這樣做的直觀理由是：任何長度大於 T 的區域，青蛙只要跨過 T 就能到達另一側，中間位置不影響最優解，因此可被壓縮。
    """
    pts = [0] + sorted(stones) + [L]
    sub = 0
    new_pts = [0]
    prev = pts[0]
    for p in pts[1:]:
        gap = p - prev
        if gap > T:
            sub += (gap - T)
        new_pts.append(p - sub)
        prev = p
    newL = L - sub
    return newL, new_pts


def solve_one(L: int, S: int, T: int, stones: List[int]) -> int:
    """直觀 DP：dp[i] = 最少踩石子到達位置 i。

    實作說明：
    - 先呼叫 compress_positions 得到 newL, new_pts
    - 建立 is_stone 陣列標記壓縮後座標是否為石子
    - 用 dp 陣列，初值 dp[0]=0，其它為 INF
    - 從左到右掃描每個 i，對 j=i+S..i+T 做 relax（到終點記為 newL）

    範例：若 newL = 10, S=2, T=3，則從 i=0 可考慮跳到 j=2 或 3，更新 dp[2], dp[3]
    """
    newL, new_pts = compress_positions(L, stones, T)
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
                if dp[newL] > dp[i]:
                    dp[newL] = dp[i]
            else:
                cost = dp[i] + (1 if is_stone[j] else 0)
                if cost < dp[j]:
                    dp[j] = cost
    return dp[newL]


def process(input_str: str) -> str:
    tokens = input_str.strip().split()
    if not tokens:
        return ""
    p = 0
    out_lines: List[str] = []
    # 支援多組輸入：每組依序為 L S T M, 接著 M 個石子座標
    while p < len(tokens):
        L = int(tokens[p]); p += 1
        S = int(tokens[p]); T = int(tokens[p+1]); M = int(tokens[p+2]); p += 3
        stones = []
        for _ in range(M):
            stones.append(int(tokens[p])); p += 1
        # 對於每一組輸出一行結果
        out_lines.append(str(solve_one(L, S, T, stones)))
    return "\n".join(out_lines)


if __name__ == '__main__':
    import sys
    print(process(sys.stdin.read()))
