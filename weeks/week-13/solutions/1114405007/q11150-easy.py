"""11150 簡單版：青蛙過河最少踩石頭數。"""

import sys


INF = 10**9
MAX_GAP = 100  # 距離壓縮上限，避免 L 太大


def min_stones(L, S, T, stones):
    stones = sorted(stones)
    stone_set = set(stones)

    # 固定步長時，會落在固定位置，直接數即可
    if S == T:
        cnt = 0
        x = S
        while x < L:
            if x in stone_set:
                cnt += 1
            x += S
        return cnt

    # 座標壓縮：大空白區間不需要完整展開
    c_stones = []
    prev = 0
    cur = 0

    for pos in stones + [L]:
        gap = pos - prev
        cur += min(gap, MAX_GAP)
        if pos != L:
            c_stones.append(cur)
        prev = pos

    cL = cur
    mark = set(c_stones)

    dp = [INF] * (cL + T + 1)
    dp[0] = 0

    for i in range(cL + T + 1):
        if dp[i] == INF:
            continue
        for jump in range(S, T + 1):
            ni = i + jump
            if ni >= len(dp):
                continue
            add = 1 if ni in mark else 0
            if dp[i] + add < dp[ni]:
                dp[ni] = dp[i] + add

    return min(dp[cL : cL + T + 1])


def solve(text):
    arr = text.split()
    if not arr:
        return ""

    p = 0
    L = int(arr[p])
    p += 1
    S = int(arr[p])
    T = int(arr[p + 1])
    M = int(arr[p + 2])
    p += 3

    stones = list(map(int, arr[p : p + M]))
    return str(min_stones(L, S, T, stones))


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
