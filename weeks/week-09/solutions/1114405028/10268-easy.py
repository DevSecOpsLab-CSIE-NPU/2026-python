# 10268 題目簡單版
# 用較直觀的 DP 表格計算 k 個水球在 t 次丟擲下可測試的最大樓層。

MAX_K = 100
MAX_T = 63


def solve() -> None:
    import sys

    data = sys.stdin.read().split()
    if not data:
        return

    dp = [[0] * (MAX_K + 1) for _ in range(MAX_T + 1)]
    for t in range(1, MAX_T + 1):
        for k in range(1, MAX_K + 1):
            dp[t][k] = dp[t - 1][k - 1] + dp[t - 1][k] + 1

    it = iter(data)
    outputs: list[str] = []
    while True:
        try:
            k = int(next(it))
        except StopIteration:
            break
        n = int(next(it))
        if k == 0:
            break
        k = min(k, MAX_K)
        ans = None
        for t in range(1, MAX_T + 1):
            if dp[t][k] >= n:
                ans = t
                break
        outputs.append(str(ans) if ans is not None else "More than 63 trials needed.")

    sys.stdout.write("\n".join(outputs) + ("\n" if outputs else ""))


if __name__ == "__main__":
    solve()
