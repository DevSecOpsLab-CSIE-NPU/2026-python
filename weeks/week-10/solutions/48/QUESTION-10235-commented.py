"""
註解版本：說明狀態壓縮 DP 的想法。
基本想法：對每列計算從上一列過來的垂直邊狀態到本列垂直邊狀態的轉換數，
再以字典（vmask）做列間 DP，使用快取加速重複轉換。
"""
import sys
from functools import lru_cache

MOD = 1_000_000_007

@lru_cache(maxsize=None)
def transitions_for_row(umask, row_bits, m):
    result = {}
    # col: 0..m-1 處理一列；left_edge = 是否有左邊向右延伸的邊
    def dfs(col, left_edge, vmask):
        if col == m:
            if left_edge == 0:
                result[vmask] = (result.get(vmask, 0) + 1) % MOD
            return
        top = (umask >> col) & 1
        need = 2 if ((row_bits >> col) & 1) else 0
        for r in (0, 1):
            for d in (0, 1):
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
    dp = {0: 1}
    for i in range(n):
        ndp = {}
        for umask, cnt in dp.items():
            trans = transitions_for_row(umask, row_masks[i], m)
            for vmask, ways in trans.items():
                ndp[vmask] = (ndp.get(vmask, 0) + cnt * ways) % MOD
        dp = ndp
    return dp.get(0, 0)


def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it)); m = int(next(it))
        grid = []
        for _ in range(n):
            grid.append(next(it))
        ans = solve_one(n, m, grid)
        out.append(f"Case {_+1}: {ans}")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
