import sys

MOD = 1_000_000_007


# 對單列做狀態轉移：
# umask 表示從上一列往下接到本列的垂直邊
# row_bits 第 j 位為 1 代表可用格，0 代表插座（不可占用）
def transitions_for_row(umask, row_bits, m):
    result = {}

    def dfs(col, left_edge, vmask):
        # 一列處理完成，最右邊不能再有往右延伸的邊
        if col == m:
            if left_edge == 0:
                result[vmask] = (result.get(vmask, 0) + 1) % MOD
            return

        top = (umask >> col) & 1
        # 可用格要求度數 2；插座格要求度數 0
        need = 2 if ((row_bits >> col) & 1) else 0

        # r: 往右邊是否連邊, d: 往下一列是否連邊
        for r in (0, 1):
            for d in (0, 1):
                # 四方向度數必須符合 need
                if top + left_edge + r + d != need:
                    continue
                next_vmask = vmask | (d << col)
                dfs(col + 1, r, next_vmask)

    dfs(0, 0, 0)
    return result


def solve_one(n, m, grid):
    row_masks = []
    for row in grid:
        mask = 0
        for j, ch in enumerate(row):
            if ch == "1":
                mask |= 1 << j
        row_masks.append(mask)

    # dp[umask] = 到目前列為止的方法數
    dp = {0: 1}

    for i in range(n):
        ndp = {}
        for umask, cnt in dp.items():
            trans = transitions_for_row(umask, row_masks[i], m)
            for vmask, ways in trans.items():
                ndp[vmask] = (ndp.get(vmask, 0) + cnt * ways) % MOD
        dp = ndp

    # 最後不能有垂直邊伸出棋盤外
    return dp.get(0, 0)


def solve():
    input = sys.stdin.readline
    t = int(input().strip())
    out = []

    for tc in range(1, t + 1):
        n, m = map(int, input().split())
        grid = [input().strip() for _ in range(n)]
        ans = solve_one(n, m, grid)
        out.append(f"Case {tc}: {ans}")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
