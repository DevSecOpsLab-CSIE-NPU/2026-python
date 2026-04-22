from __future__ import annotations

import sys


def precompute() -> list[list[int]]:
    # dp[t][k]：t 次測試、k 顆球，最壞情況可判斷的最高樓層
    dp = [[0] * 101 for _ in range(64)]
    cap = 10**19
    for t in range(1, 64):
        for k in range(1, 101):
            val = dp[t - 1][k - 1] + 1 + dp[t - 1][k]
            dp[t][k] = val if val < cap else cap
    return dp


DP = precompute()


def solve(data: str) -> str:
    tokens = data.split()
    i = 0
    out: list[str] = []
    while i + 1 < len(tokens):
        k = int(tokens[i])
        n = int(tokens[i + 1])
        i += 2
        if k == 0:
            break

        ans = None
        kk = min(k, 100)
        for t in range(1, 64):
            if DP[t][kk] >= n:
                ans = t
                break

        if ans is None:
            out.append("More than 63 trials needed.")
        else:
            out.append(str(ans))

    return "\n".join(out)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
