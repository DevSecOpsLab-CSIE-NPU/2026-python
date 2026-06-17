import sys

def solve():
    data = sys.stdin.read().splitlines()
    L = int(data[0])
    S, T, M = map(int, data[1].split())
    stones = list(map(int, data[2].split())) if M > 0 else []

    if S == T:
        print(sum(1 for s in stones if s % S == 0))
        return

    stones = sorted(set(stones))
    # 路徑壓縮：間距過大時縮短
    step = T * (T - S + 1)
    pos = [0]
    for i, s in enumerate(stones):
        if i > 0 and s - stones[i-1] > step:
            pos.append(pos[-1] + step)
        else:
            pos.append(pos[-1] + (s - (stones[i-1] if i > 0 else 0)))
    pos.append(pos[-1] + (L - stones[-1]))
    total = pos[-1]

    stone_at = [False] * (total + 1)
    idx = 1
    for i in range(1, total + 1):
        if idx <= M and i == pos[idx]:
            stone_at[i] = True
            idx += 1

    INF = 10**9
    dp = [INF] * (total + 1)
    dp[0] = 0
    for i in range(1, total + 1):
        for k in range(S, T + 1):
            if i >= k:
                dp[i] = min(dp[i], dp[i-k] + (1 if stone_at[i] else 0))

    ans = min(dp[max(0, total-T):total+1])
    print(ans)

if __name__ == "__main__":
    solve()
