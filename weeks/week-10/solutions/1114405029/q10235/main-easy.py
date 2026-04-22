import sys
from functools import lru_cache

MOD = 1000000007


def normalize_row(line, m):
    # 這題的每一列有時候可能長這樣：
    # 1 0 1
    # 也可能長這樣：
    # 101
    # 所以這裡要兩種格式都能處理
    parts = line.strip().split()

    if len(parts) == m:
        return [int(x) for x in parts]

    s = "".join(parts)
    return [int(ch) for ch in s]


@lru_cache(maxsize=None)
def transitions(row_mask, up_mask, m):
    # 這個函式要計算：
    # 對固定的一列 row_mask
    # 以及固定的從上面接下來的狀態 up_mask
    # 共有多少種方法可以轉移到各種 down_mask

    result = {}

    def dfs(col, left_edge, down_mask):
        # col：目前處理到第幾欄
        # left_edge：左邊是否有一條水平邊接到這格
        # down_mask：目前已經決定好哪些格子往下接邊

        if col == m:
            # 一整列處理完畢時，不能還有一條邊往右伸出去
            if left_edge == 0:
                result[down_mask] = (result.get(down_mask, 0) + 1) % MOD
            return

        cell_is_empty = (row_mask >> col) & 1
        up_edge = (up_mask >> col) & 1

        # 如果這格是插座格（不可用）
        # 那它四個方向都不能有邊
        if not cell_is_empty:
            if left_edge == 0 and up_edge == 0:
                dfs(col + 1, 0, down_mask)
            return

        # 如果這格可用，最後度數一定要恰好等於 2
        # 目前已知的邊有：
        # 上邊 up_edge
        # 左邊 left_edge
        # 所以還需要補的邊數是：
        need = 2 - left_edge - up_edge

        if need < 0 or need > 2:
            return

        next_cell_empty = (col + 1 < m) and (((row_mask >> (col + 1)) & 1) == 1)

        if need == 0:
            # 代表 down = 0, right = 0
            dfs(col + 1, 0, down_mask)

        elif need == 1:
            # 第一種：往下接一條邊
            dfs(col + 1, 0, down_mask | (1 << col))

            # 第二種：往右接一條邊
            # 但右邊格子必須存在且可用
            if next_cell_empty:
                dfs(col + 1, 1, down_mask)

        else:
            # need == 2
            # 只能同時往下和往右各接一條
            if next_cell_empty:
                dfs(col + 1, 1, down_mask | (1 << col))

    dfs(0, 0, 0)
    return tuple(result.items())


def solve_case(grid):
    n = len(grid)
    m = len(grid[0])

    # 先把每一列轉成 bitmask
    # bit = 1 代表該格可用
    row_masks = []
    for row in grid:
        mask = 0
        for c, val in enumerate(row):
            if val == 1:
                mask |= (1 << c)
        row_masks.append(mask)

    # dp[mask] = 處理到目前列之前，下一列從上方接下來的垂直邊狀態為 mask 的方案數
    dp = {0: 1}

    for row_mask in row_masks:
        new_dp = {}

        for up_mask, ways_so_far in dp.items():
            for down_mask, count_transition in transitions(row_mask, up_mask, m):
                new_dp[down_mask] = (
                    new_dp.get(down_mask, 0) + ways_so_far * count_transition
                ) % MOD

        dp = new_dp

    # 所有列都處理完後，不能還有邊往地板外面延伸
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