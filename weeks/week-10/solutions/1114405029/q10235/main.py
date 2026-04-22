import sys
from functools import lru_cache

MOD = 1000000007


def normalize_row(line, m):
    parts = line.strip().split()

    # 若本來就是空白分隔，例如：1 0 1
    if len(parts) == m:
        return [int(x) for x in parts]

    # 否則視為黏在一起，例如：101
    s = "".join(parts)
    return [int(ch) for ch in s]


@lru_cache(maxsize=None)
def transitions(row_mask, up_mask, m):
    result = {}

    def dfs(col, left_edge, down_mask):
        if col == m:
            if left_edge == 0:
                result[down_mask] = (result.get(down_mask, 0) + 1) % MOD
            return

        cell_is_empty = (row_mask >> col) & 1
        up_edge = (up_mask >> col) & 1

        # 插座格：不能有任何邊經過
        if not cell_is_empty:
            if left_edge == 0 and up_edge == 0:
                dfs(col + 1, 0, down_mask)
            return

        # 可用格：度數必須恰好為 2
        need = 2 - left_edge - up_edge

        if need < 0 or need > 2:
            return

        next_cell_empty = (col + 1 < m) and (((row_mask >> (col + 1)) & 1) == 1)

        if need == 0:
            # down = 0, right = 0
            dfs(col + 1, 0, down_mask)

        elif need == 1:
            # 選 down = 1, right = 0
            dfs(col + 1, 0, down_mask | (1 << col))

            # 選 down = 0, right = 1
            if next_cell_empty:
                dfs(col + 1, 1, down_mask)

        else:  # need == 2
            # 只能 down = 1, right = 1
            if next_cell_empty:
                dfs(col + 1, 1, down_mask | (1 << col))

    dfs(0, 0, 0)
    return tuple(result.items())


def solve_case(grid):
    n = len(grid)
    m = len(grid[0])

    row_masks = []
    for row in grid:
        mask = 0
        for c, val in enumerate(row):
            if val == 1:
                mask |= (1 << c)
        row_masks.append(mask)

    dp = {0: 1}

    for row_mask in row_masks:
        new_dp = {}

        for up_mask, ways_so_far in dp.items():
            for down_mask, count_transition in transitions(row_mask, up_mask, m):
                new_dp[down_mask] = (
                    new_dp.get(down_mask, 0) + ways_so_far * count_transition
                ) % MOD

        dp = new_dp

    return dp.get(0, 0)


def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    t = int(lines[0].strip())
    index = 1
    outputs = []

    for case_id in range(1, t + 1):
        while index < len(lines) and lines[index].strip() == "":
            index += 1

        n, m = map(int, lines[index].split())
        index += 1

        grid = []
        for _ in range(n):
            grid.append(normalize_row(lines[index], m))
            index += 1

        ans = solve_case(grid)
        outputs.append(f"Case {case_id}: {ans}")

    print("\n".join(outputs))


if __name__ == "__main__":
    main()