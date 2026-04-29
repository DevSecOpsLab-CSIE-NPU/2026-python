import sys
from functools import lru_cache

"""
優化說明：
- 先正規化格子方向，縮小狀態寬度，提升 DP 效率。
- 快取每列轉移結果，避免重複計算相同輪廓轉移。
- 拆成多個輔助函式，提高可讀性與單元測試便利性。
"""


MOD = 1_000_000_007


def normalize_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    if cols <= rows:
        return grid
    return [list(row) for row in zip(*grid)]


def row_to_mask(row):
    mask = 0
    for column, value in enumerate(row):
        if value:
            mask |= 1 << column
    return mask


def count_loop_coverings(grid):
    grid = normalize_grid(grid)
    rows = len(grid)
    cols = len(grid[0])
    row_masks = [row_to_mask(row) for row in grid]

    @lru_cache(maxsize=None)
    def transitions(open_mask, has_next_row, incoming_mask):
        results = {}

        def dfs(column, left_edge, outgoing_mask):
            if column == cols:
                if left_edge == 0:
                    results[outgoing_mask] = (results.get(outgoing_mask, 0) + 1) % MOD
                return

            up_edge = (incoming_mask >> column) & 1
            cell_is_open = (open_mask >> column) & 1

            if not cell_is_open:
                if up_edge == 0 and left_edge == 0:
                    dfs(column + 1, 0, outgoing_mask)
                return

            needed_edges = 2 - up_edge - left_edge
            if needed_edges < 0:
                return

            if needed_edges == 0:
                dfs(column + 1, 0, outgoing_mask)
                return

            if needed_edges == 1:
                if column + 1 < cols:
                    dfs(column + 1, 1, outgoing_mask)
                if has_next_row:
                    dfs(column + 1, 0, outgoing_mask | (1 << column))
                return

            if needed_edges == 2 and column + 1 < cols and has_next_row:
                dfs(column + 1, 1, outgoing_mask | (1 << column))

        dfs(0, 0, 0)
        return tuple(results.items())

    dp = {0: 1}
    for row_index, open_mask in enumerate(row_masks):
        next_dp = {}
        has_next_row = row_index + 1 < rows

        for incoming_mask, ways in dp.items():
            for outgoing_mask, count in transitions(open_mask, has_next_row, incoming_mask):
                next_dp[outgoing_mask] = (next_dp.get(outgoing_mask, 0) + ways * count) % MOD

        dp = next_dp

    return dp.get(0, 0)


def solve(reader):
    test_count = int(reader.readline())
    answers = []

    for case_index in range(1, test_count + 1):
        rows, cols = map(int, reader.readline().split())
        grid = [list(map(int, reader.readline().split())) for _ in range(rows)]
        answers.append(f"Case {case_index}: {count_loop_coverings(grid)}")

    return "\n".join(answers)


def main():
    sys.stdout.write(solve(sys.stdin))


if __name__ == "__main__":
    main()