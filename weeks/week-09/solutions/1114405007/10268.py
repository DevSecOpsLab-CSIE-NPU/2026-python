import sys

# dp[i][j] = 用 i 次測試、j 顆水球時，最多能測幾層樓。
dp = [[0] * 101 for _ in range(64)]
for i in range(1, 64):
    for j in range(1, 101):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + 1

out = []
for line in sys.stdin:
    k, n = map(int, line.split())
    if k == 0:
        break

    ans = 64
    for i in range(1, 64):
        if dp[i][k] >= n:
            ans = i
            break

    if ans == 64:
        out.append("More than 63 trials needed.")
    else:
        out.append(str(ans))

sys.stdout.write("\n".join(out))