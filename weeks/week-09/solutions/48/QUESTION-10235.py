import sys

MOD = 1_000_000_007


def transitions_for_row(umask, row_bits, m):
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
