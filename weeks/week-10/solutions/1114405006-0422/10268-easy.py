
"""UVA 10268：Dropping water balloons 的簡單版。

這份程式把想法寫得更直白：
先用一維 DP 累積每一次試驗最多能測出的樓層數，再找最小次數。
"""

from __future__ import annotations

import sys


LIMIT = 63
MORE_THAN_LIMIT = "More than 63 trials needed."


def solve(data: str) -> str:
    """逐行讀入每筆測資並輸出答案。"""

    answers: list[str] = []

    for line in data.splitlines():
        if not line.strip():
            continue

        balls, floors = map(int, line.split())
        if balls == 0:
            break

        # dp[i] 代表「目前這一輪」用 i 顆球最多能測幾層樓。
        dp = [0] * (balls + 1)
        found = False

        for trial in range(1, LIMIT + 1):
            # 反向更新，避免把上一輪的資料覆蓋掉。
            for ball in range(balls, 0, -1):
                dp[ball] = min(floors, dp[ball] + dp[ball - 1] + 1)

            if dp[balls] >= floors:
                answers.append(str(trial))
                found = True
                break

        if not found:
            answers.append(MORE_THAN_LIMIT)

    return "\n".join(answers)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()