import sys


def can_expand(grid, r, c, radius, target):
    top = r - radius
    bottom = r + radius
    left = c - radius
    right = c + radius

    if top < 0 or left < 0 or bottom >= len(grid) or right >= len(grid[0]):
        return False

    for row_index in range(top, bottom + 1):
        row = grid[row_index]
        for col_index in range(left, right + 1):
            if row[col_index] != target:
                return False

    return True


def solve():
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    it = iter(tokens)
    test_count = int(next(it))
    output = []

    for _ in range(test_count):
        m = int(next(it))
        n = int(next(it))
        q = int(next(it))

        grid = [next(it) for _ in range(m)]
        output.append(f"{m} {n} {q}")

        for _ in range(q):
            r = int(next(it))
            c = int(next(it))
            target = grid[r][c]
            radius = 0

            while can_expand(grid, r, c, radius, target):
                radius += 1

            output.append(str(radius * 2 - 1))

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    solve()