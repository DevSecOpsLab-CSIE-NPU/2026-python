import sys
from collections import defaultdict

MOD = 1000000007


def count_cycles(grid, N, M):
    dp = {(0, 0): 1}
    for i in range(N):
        for j in range(M):
            nd = defaultdict(int)
            for (mask, left), cnt in dp.items():
                up = (mask >> j) & 1
                l = left
                avail = grid[i][j] == 1
                right_ok = (j + 1 < M) and (grid[i][j + 1] == 1)
                down_ok = (i + 1 < N) and (grid[i + 1][j] == 1)
                if not avail:
                    if l == 0 and up == 0:
                        nd[(mask & ~(1 << j), 0)] = (nd[(mask & ~(1 << j), 0)] + cnt) % MOD
                    continue
                need = 2 - l - up
                if need == 0:
                    nd[(mask & ~(1 << j), 0)] = (nd[(mask & ~(1 << j), 0)] + cnt) % MOD
                elif need == 2:
                    if right_ok and down_ok:
                        nd[((mask & ~(1 << j)) | (1 << j), 1)] = (nd[((mask & ~(1 << j)) | (1 << j), 1)] + cnt) % MOD
                else:  # need == 1
                    if right_ok:
                        nd[(mask & ~(1 << j), 1)] = (nd[(mask & ~(1 << j), 1)] + cnt) % MOD
                    if down_ok:
                        nd[((mask & ~(1 << j)) | (1 << j), 0)] = (nd[((mask & ~(1 << j)) | (1 << j), 0)] + cnt) % MOD
            dp = nd
    return dp.get((0, 0), 0)


def main():
    it = iter(sys.stdin.read().split())
    T = int(next(it, 0))
    out = []
    for tc in range(1, T + 1):
        N = int(next(it)); M = int(next(it))
        grid = [[int(next(it)) for _ in range(M)] for _ in range(N)]
        out.append(f"Case {tc}: {count_cycles(grid, N, M)}")
    sys.stdout.write("\n".join(out))


if __name__ == '__main__':
    main()
