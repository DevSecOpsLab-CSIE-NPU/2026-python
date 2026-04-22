from __future__ import annotations

from collections import defaultdict
import sys


MOD = 1_000_000_007


def count_ways(grid: list[list[int]]) -> int:
    """
    簡單記法：
    1. 每個可站格子要連到剛好 2 條邊（蛇身在該格的前後）。
    2. 用輪廓 DP，逐格決定「右邊要不要接、下邊要不要接」。
    3. 只要目前格子的四個方向連線數量恰好為 2 就合法。
    4. 最後所有邊都必須收乾淨（狀態回到 0）。
    """
    n = len(grid)
    m = len(grid[0])
    dp: dict[int, int] = {0: 1}

    for r in range(n):
        for c in range(m):
            new_dp: defaultdict[int, int] = defaultdict(int)

            for state, ways in dp.items():
                up = (state >> c) & 1
                left = (state >> m) & 1

                if grid[r][c] == 0:
                    if up or left:
                        continue
                    ns = state & ~(1 << m)
                    new_dp[ns] = (new_dp[ns] + ways) % MOD
                    continue

                right_ok = c + 1 < m and grid[r][c + 1] == 1
                down_ok = r + 1 < n and grid[r + 1][c] == 1

                for right in (0, 1):
                    if right and not right_ok:
                        continue
                    for down in (0, 1):
                        if down and not down_ok:
                            continue

                        if up + left + right + down != 2:
                            continue

                        ns = state
                        ns &= ~(1 << m)
                        ns &= ~(1 << c)
                        if right:
                            ns |= 1 << m
                        if down:
                            ns |= 1 << c

                        new_dp[ns] = (new_dp[ns] + ways) % MOD

            dp = new_dp

        dp = {s: v for s, v in dp.items() if ((s >> m) & 1) == 0}

    return dp.get(0, 0)


def solve(data: str) -> str:
    nums = data.split()
    i = 0
    t = int(nums[i])
    i += 1
    out: list[str] = []

    for case_id in range(1, t + 1):
        n = int(nums[i])
        m = int(nums[i + 1])
        i += 2

        grid = [[0] * m for _ in range(n)]
        for r in range(n):
            for c in range(m):
                grid[r][c] = int(nums[i])
                i += 1

        out.append(f"Case {case_id}: {count_ways(grid)}")

    return "\n".join(out)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
