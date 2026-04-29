import sys
from functools import lru_cache

MOD = 1_000_000_007

@lru_cache(maxsize=None)
def transitions_for_row(umask, row_bits, m):
    # 優化點：同一列型態的轉移結果會重複出現，先快取避免重算。
    result = {}
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
    # 優化點：把每一列壓成 bitmask，DP 只在 mask 狀態間轉移。
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
