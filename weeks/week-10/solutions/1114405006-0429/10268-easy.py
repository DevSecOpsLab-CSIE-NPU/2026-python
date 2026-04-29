
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
    it = iter(map(int, data.split()))
    limit = LIMIT

    while True:
        try:
            balls = next(it)
        except StopIteration:
            break
        if balls == 0:
            break
        try:
            floors = next(it)
        except StopIteration:
            break

        # dp[i] 代表「目前這一輪」用 i 顆球最多能測幾層樓。
        dp = [0] * (balls + 1)
        found = False

        for trial in range(1, limit + 1):
            # 反向更新，避免把上一輪的資料覆蓋掉。
            dp_local = dp
            # 使用局部變數與直接算術，避免每次呼叫 min()
            for ball in range(balls, 0, -1):
                s = dp_local[ball] + dp_local[ball - 1] + 1
                dp_local[ball] = floors if s > floors else s

            if dp_local[balls] >= floors:
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