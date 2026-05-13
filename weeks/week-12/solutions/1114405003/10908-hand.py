import sys


def check(grid, r, c, k):
    if r - k < 0 or c - k < 0 or r + k >= len(grid) or c + k >= len(grid[0]):
        return False

    ch = grid[r][c]
    for i in range(r - k, r + k + 1):
        for j in range(c - k, c + k + 1):
            if grid[i][j] != ch:
                return False
    return True


def main():
    data = sys.stdin.read().split()
    if not data:
        return

    p = 0
    t = int(data[p])
    p += 1
    out = []

    for _ in range(t):
        m = int(data[p])
        n = int(data[p + 1])
        q = int(data[p + 2])
        p += 3

        grid = []
        for _ in range(m):
            grid.append(data[p])
            p += 1

        out.append(f"{m} {n} {q}")

        for _ in range(q):
            r = int(data[p])
            c = int(data[p + 1])
            p += 2

            k = 0
            while check(grid, r, c, k):
                k += 1
            out.append(str(k * 2 - 1))

    sys.stdout.write("\n".join(out))


main()