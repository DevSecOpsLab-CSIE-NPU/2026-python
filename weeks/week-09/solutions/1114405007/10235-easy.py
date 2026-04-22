import sys

MOD = 1000000007


def solve_case(grid):
    n = len(grid)
    m = len(grid[0])

    # 為了減少 bitmask 大小，盡量讓欄數比較小。
    if m > n:
        grid = [list(row) for row in zip(*grid)]
        n, m = m, n

    # dp[mask] = 目前處理到這一列時，上一列往下接的狀態數量。
    dp = {0: 1}

    for r in range(n):
        next_dp = {}

        for mask, ways in dp.items():
            def dfs(c, left, next_mask):
                # 一整列處理完，left 也要清空才是合法狀態。
                if c == m:
                    if left == 0:
                        next_dp[next_mask] = (next_dp.get(next_mask, 0) + ways) % MOD
                    return

                up = (mask >> c) & 1

                # 插座格不能放蛇，所以上下左右都不能有邊經過。
                if grid[r][c] == 0:
                    if up == 0 and left == 0:
                        dfs(c + 1, 0, next_mask)
                    return

                # 環上的每個格子度數都要是 2。
                need = 2 - up - left

                # 不需要再接邊。
                if need == 0:
                    dfs(c + 1, 0, next_mask)

                # 還差一條邊：可以往右接，或往下接。
                elif need == 1:
                    if c + 1 < m:
                        dfs(c + 1, 1, next_mask)
                    if r + 1 < n:
                        dfs(c + 1, 0, next_mask | (1 << c))

                # 還差兩條邊：一定是右和下都要接。
                else:
                    if c + 1 < m and r + 1 < n:
                        dfs(c + 1, 1, next_mask | (1 << c))

            dfs(0, 0, 0)

        dp = next_dp

    return dp.get(0, 0)


def main():
    t = int(sys.stdin.readline())
    ans = []

    for case_id in range(1, t + 1):
        n, m = map(int, sys.stdin.readline().split())
        grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
        ans.append(f"Case {case_id}: {solve_case(grid)}")

    sys.stdout.write("\n".join(ans))


if __name__ == "__main__":
    main()