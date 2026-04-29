import sys
from functools import lru_cache

MOD = 1000000007


def normalize_row(line, m):
    """
    將輸入的一列轉成整數 list。

    支援兩種格式：
    1. 空白分隔：1 0 1
    2. 黏在一起：101
    """
    parts = line.strip().split()

    if len(parts) == m:
        return [int(x) for x in parts]

    s = "".join(parts)
    return [int(ch) for ch in s]


@lru_cache(maxsize=None)
def get_transitions(row_mask, up_mask, m):
    """
    計算目前這一列的所有合法轉移狀態。

    row_mask：
    - 這一列哪些格子可以走
    - bit = 1 表示可用格
    - bit = 0 表示障礙格

    up_mask：
    - 從上一列往下接到目前這一列的邊

    回傳：
    - tuple((down_mask, count), ...)
    - down_mask 表示目前這一列往下一列連出去的邊
    - count 表示產生這個 down_mask 的方法數
    """
    result = {}

    def dfs(col, left_edge, down_mask):
        """
        逐格處理目前這一列。

        col：
        - 目前處理到第幾欄

        left_edge：
        - 左邊是否有邊接進來
        - 0 表示沒有
        - 1 表示有

        down_mask：
        - 紀錄目前這一列哪些位置會往下一列連線
        """
        if col == m:
            # 一列結束時，不能還有右邊延伸出去的邊
            if left_edge == 0:
                result[down_mask] = (result.get(down_mask, 0) + 1) % MOD
            return

        cell_is_available = (row_mask >> col) & 1
        up_edge = (up_mask >> col) & 1

        # 障礙格不能有任何邊經過
        if cell_is_available == 0:
            if left_edge == 0 and up_edge == 0:
                dfs(col + 1, 0, down_mask)
            return

        # 可用格的度數必須剛好是 2
        need = 2 - left_edge - up_edge

        # need 不合法代表目前狀態無法成立
        if need < 0 or need > 2:
            return

        # 判斷右邊格子是否存在且可用
        right_available = (
            col + 1 < m and ((row_mask >> (col + 1)) & 1) == 1
        )

        if need == 0:
            # 已經有兩條邊，所以不能再往右或往下接
            dfs(col + 1, 0, down_mask)

        elif need == 1:
            # 選擇往下接一條邊
            dfs(col + 1, 0, down_mask | (1 << col))

            # 選擇往右接一條邊
            if right_available:
                dfs(col + 1, 1, down_mask)

        else:
            # need == 2
            # 必須同時往右和往下接
            if right_available:
                dfs(col + 1, 1, down_mask | (1 << col))

    dfs(0, 0, 0)
    return tuple(result.items())


def solve_case(grid):
    """
    解單筆測資。

    grid：
    - 二維 list
    - 1 表示可用格
    - 0 表示障礙格
    """
    n = len(grid)
    m = len(grid[0])

    row_masks = []

    # 將每一列轉成 bitmask，方便 DP 處理
    for row in grid:
        mask = 0

        for col, value in enumerate(row):
            if value == 1:
                mask |= 1 << col

        row_masks.append(mask)

    # dp[up_mask] = 方法數
    # 一開始還沒有任何從上方接下來的邊，所以是 0
    dp = {0: 1}

    for row_mask in row_masks:
        next_dp = {}

        for up_mask, ways in dp.items():
            for down_mask, transition_count in get_transitions(row_mask, up_mask, m):
                next_dp[down_mask] = (
                    next_dp.get(down_mask, 0)
                    + ways * transition_count
                ) % MOD

        dp = next_dp

    # 最後不能有任何邊往下一列接出去
    return dp.get(0, 0)


def main():
    lines = sys.stdin.read().splitlines()

    if not lines:
        return

    case_count = int(lines[0].strip())
    index = 1
    outputs = []

    for case_id in range(1, case_count + 1):
        # 跳過測資前面的空白行
        while index < len(lines) and lines[index].strip() == "":
            index += 1

        n, m = map(int, lines[index].split())
        index += 1

        grid = []

        for _ in range(n):
            grid.append(normalize_row(lines[index], m))
            index += 1

        answer = solve_case(grid)
        outputs.append(f"Case {case_id}: {answer}")

    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    main()