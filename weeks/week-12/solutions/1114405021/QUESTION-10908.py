#!/usr/bin/env python3
import sys

def max_square_centered(grid, r, c):
    ch = grid[r][c]
    m = len(grid); n = len(grid[0])
    max_k = 0
    # k is radius: square side = 2*k+1
    k = 0
    while True:
        if r-k < 0 or r+k >= m or c-k < 0 or c+k >= n:
            break
        ok = True
        for i in range(r-k, r+k+1):
            for j in range(c-k, c+k+1):
                if grid[i][j] != ch:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            break
        max_k = k
        k += 1
    return 2*max_k + 1


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0]); idx = 1
    outputs = []
    for _ in range(t):
        M = int(data[idx]); N = int(data[idx+1]); Q = int(data[idx+2]); idx += 3
        grid = []
        for _ in range(M):
            grid.append(list(data[idx])); idx += 1
        outputs.append(f"{M} {N} {Q}")
        for _ in range(Q):
            r = int(data[idx]); c = int(data[idx+1]); idx += 2
            outputs.append(str(max_square_centered(grid, r, c)))
    sys.stdout.write('\n'.join(outputs))

if __name__ == '__main__':
    main()
