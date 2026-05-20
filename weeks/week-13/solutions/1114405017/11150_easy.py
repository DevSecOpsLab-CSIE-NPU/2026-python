import sys


def solve():
    # 1. 一行讀入所有數據，不用管換行或空格
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    L, S, T, M = data[0], data[1], data[2], data[3]
    stones = sorted(data[4 : 4 + M])

    # 特判：如果步長固定，直接看有幾顆石子是 S 的倍數
    if S == T:
        print(sum(1 for x in stones if x % S == 0))
        return

    # 2. 路徑壓縮：距離大於 90 的直接變成 90
    pos = [0] + stones + [L]
    new_stones = set()
    curr = 0

    for i in range(1, len(pos)):
        diff = pos[i] - pos[i - 1]
        # 核心記憶點：太遠就縮減到 90
        curr += min(diff, 90)
        # 如果不是最後一個點（最後一個點是終點 L），就把壓縮後的石子位置存起來
        if i < len(pos) - 1:
            new_stones.add(curr)

    new_L = curr  # 壓縮後的終點

    # 3. 簡單的 DP
    # dp[i] 代表到座標 i 的最少石子數，長度開到新終點 + 最大步長 T
    dp = [0] + [float("inf")] * (new_L + T)

    for i in range(1, new_L + T + 1):
        # 轉移方程：從 [i-T, i-S] 區間找最小值跳過來
        dp[i] = min(dp[i - T : i - S + 1]) + (1 if i in new_stones else 0)

    # 答案就是「達到終點」或「跳過終點」之後的最小值
    print(min(dp[new_L : new_L + T + 1]))


if __name__ == "__main__":
    solve()