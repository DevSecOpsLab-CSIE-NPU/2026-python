import sys

def min_stones(L, S, T, stones):
    """
    計算青蛙過河最少踩到的石子數。
    採用狀態壓縮 DP：因 L 可達 10^9，但石子數 ≤ 100，
    將石子間距壓縮（超過 T*(T-S+1) 的間距可直接縮短）。
    """
    # S = T 時只需檢查倍數位置
    if S == T:
        return sum(1 for s in stones if s % S == 0)

    stones = sorted(set(stones))
    M = len(stones)
    if M == 0:
        return 0

    # 狀態壓縮：若兩石子間距過大，縮短至合理範圍
    compress = [0]
    for i, s in enumerate(stones):
        if i > 0 and s - stones[i-1] > T * (T - S + 1):
            compress.append(compress[-1] + T * (T - S + 1))
        else:
            compress.append(compress[-1] + (s - (stones[i-1] if i > 0 else 0)))
    compress.append(compress[-1] + (L - stones[-1]))
    total = compress[-1]

    # 標記壓縮後哪些位置有石子
    is_stone = [False] * (total + 1)
    stone_idx = 0
    for i in range(1, total + 1):
        if stone_idx < M and i == compress[stone_idx + 1]:
            is_stone[i] = True
            stone_idx += 1

    # DP：dp[i] = 到達位置 i 的最少踩石子數
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for i in range(1, total + 1):
        for k in range(S, T + 1):
            if i - k >= 0:
                dp[i] = min(dp[i], dp[i - k] + (1 if is_stone[i] else 0))

    # 青蛙跳到或跳過 L 即成功，取終點附近最小值
    ans = float('inf')
    for i in range(total, max(0, total - T) - 1, -1):
        ans = min(ans, dp[i])
    return ans

def solve(data=None):
    """讀取輸入、計算並回傳結果"""
    if data is None:
        data = sys.stdin.read()
    lines = data.strip().splitlines()
    L = int(lines[0])
    S, T, M = map(int, lines[1].split())
    stones = list(map(int, lines[2].split())) if M > 0 else []
    return str(min_stones(L, S, T, stones))

if __name__ == "__main__":
    sys.stdout.write(solve())
