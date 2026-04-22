from __future__ import annotations

import sys


def solve_case(k: int, n: int) -> str:
    # n=0 時不用丟。
    if n == 0:
        return "0"

    # dp[e] 表示目前試驗次數下，e 顆蛋最多可覆蓋的樓層數。
    dp = [0] * (k + 1)

    for trial in range(1, 64):
        # 反向更新，避免蓋掉上一層資訊。
        for e in range(k, 0, -1):
            dp[e] = dp[e] + dp[e - 1] + 1
        if dp[k] >= n:
            return str(trial)

    return "More than 63 trials needed."


def main() -> None:
    nums = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    out: list[str] = []

    while idx + 1 < len(nums):
        k = nums[idx]
        n = nums[idx + 1]
        idx += 2
        if k == 0:
            break
        out.append(solve_case(k, n))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()