# q11150_hand.py
# 題目：青蛙過獨木橋 (魔改版：座標壓縮 DP)
# 關鍵：L=10^9, 石子數=100. 必須壓縮空間。

import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return
    L = int(data[0])
    S, T, M = map(int, data[1:4])
    stones = sorted([int(x) for x in data[4:4+M]])

    # 座標壓縮核心：S, T <= 10, 若間距 > S*T 則可縮小
    # 這裡採簡單策略：間距超過 90 則設為 90
    pos = [0] * (M + 2)
    last_real = 0
    last_compressed = 0
    for i in range(M):
        dist = stones[i] - last_real
        if dist > 90: dist = 90
        last_compressed += dist
        pos[i+1] = last_compressed
        last_real = stones[i]

    # 終點處理
    dist = L - last_real
    if dist > 90: dist = 90
    final_L = last_compressed + dist

    stone_set = set(pos[1:-1])
    dp = [float('inf')] * (final_L + T)
    dp[0] = 0

    for i in range(final_L + 1):
        if dp[i] == float('inf'): continue
        for step in range(S, T + 1):
            next_p = i + step
            cost = 1 if next_p in stone_set else 0
            if next_p >= final_L:
                dp[final_L] = min(dp[final_L], dp[i] + cost)
            else:
                dp[next_p] = min(dp[next_p], dp[i] + cost)

    print(dp[final_L])

if __name__ == "__main__":
    solve()
