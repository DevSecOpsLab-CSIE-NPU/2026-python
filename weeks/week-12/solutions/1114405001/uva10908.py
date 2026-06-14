"""UVA 10908 - Largest Square"""


def largest_square(grid: list[str], r: int, c: int) -> int:
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    target = grid[r][c]

    radius = 0
    while True:
        nr = radius + 1
        top = r - nr
        bottom = r + nr
        left = c - nr
        right = c + nr

        if top < 0 or left < 0 or bottom >= rows or right >= cols:
            break

        # 只檢查新增的一圈邊界，效率比每次重掃整個方塊更好。
        ok = True

        for x in range(left, right + 1):
            if grid[top][x] != target or grid[bottom][x] != target:
                ok = False
                break

        if ok:
            for y in range(top + 1, bottom):
                if grid[y][left] != target or grid[y][right] != target:
                    ok = False
                    break

        if not ok:
            break

        radius = nr

    return 2 * radius + 1


def solve(data: str) -> str:
    lines = [line.rstrip("\n") for line in data.splitlines()]
    ptr = 0
    t = int(lines[ptr].strip())
    ptr += 1

    out = []
    for _ in range(t):
        while ptr < len(lines) and not lines[ptr].strip():
            ptr += 1

        m, n, q = map(int, lines[ptr].split())
        ptr += 1
        grid = []
        for _ in range(m):
            grid.append(lines[ptr].strip())
            ptr += 1

        out.append(f"{m} {n} {q}")
        for _ in range(q):
            r, c = map(int, lines[ptr].split())
            ptr += 1
            out.append(str(largest_square(grid, r, c)))

    return "\n".join(out)


def main() -> None:
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
