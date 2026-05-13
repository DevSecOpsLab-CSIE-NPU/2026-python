import sys


def largest_square(grid: list[str], r: int, c: int) -> int:
    m = len(grid)
    n = len(grid[0]) if m else 0
    target = grid[r][c]
    radius = 0

    while True:
        nr = radius + 1
        top, bottom = r - nr, r + nr
        left, right = c - nr, c + nr
        if top < 0 or left < 0 or bottom >= m or right >= n:
            break

        valid = True
        for col in range(left, right + 1):
            if grid[top][col] != target or grid[bottom][col] != target:
                valid = False
                break

        if valid:
            for row in range(top, bottom + 1):
                if grid[row][left] != target or grid[row][right] != target:
                    valid = False
                    break

        if not valid:
            break

        radius = nr

    return 2 * radius + 1


def main() -> None:
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    t = int(lines[0].strip())
    idx = 1
    out = []

    for _ in range(t):
        while idx < len(lines) and lines[idx].strip() == "":
            idx += 1

        m, n, q = map(int, lines[idx].split())
        idx += 1
        grid = [lines[idx + r].strip() for r in range(m)]
        idx += m

        out.append(f"{m} {n} {q}")
        for _ in range(q):
            r, c = map(int, lines[idx].split())
            idx += 1
            out.append(str(largest_square(grid, r, c)))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
