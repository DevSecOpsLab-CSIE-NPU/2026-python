import sys
def solve():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    L, S, T, M = data[0], data[1], data[2], data[3]
    stones = sorted(data[4 : 4 + M])
    if S == T:
        print(sum(1 for x in stones if x % S == 0))
        return
    pos = [0] + stones + [L]
    new_stones = set()
    curr = 0
    for i in range(1, len(pos)):
        diff = pos[i] - pos[i - 1]
        curr += min(diff, 90)
        if i < len(pos) - 1:
            new_stones.add(curr)
    new_L = curr 
    dp = [0] + [float("inf")] * (new_L + T)
    for i in range(1, new_L + T + 1):
        dp[i] = min(dp[i - T : i - S + 1]) + (1 if i in new_stones else 0)
    print(min(dp[new_L : new_L + T + 1]))
if __name__ == "__main__":
    solve()