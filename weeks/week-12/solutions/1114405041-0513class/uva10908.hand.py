def is_all_same(grid: list[str], r1: int, c1: int, r2: int, c2: int, ch: str) -> bool:
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            if grid[r][c] != ch:
                return False
    return True


def largest_square_size(grid: list[str], r: int, c: int) -> int:
    rows = len(grid)
    cols = len(grid[0])
    ch = grid[r][c]
    radius = 0
    while True:
        nr = radius + 1
        r1, c1 = r - nr, c - nr
        r2, c2 = r + nr, c + nr
        if r1 < 0 or c1 < 0 or r2 >= rows or c2 >= cols:
            break
        if not is_all_same(grid, r1, c1, r2, c2, ch):
            break
        radius = nr
    return 2 * radius + 1


def main() -> None:
    import sys

    lines = sys.stdin.read().strip().splitlines()
    if not lines:
        return
    idx = 0
    t = int(lines[idx])
    idx += 1
    out = []
    for _ in range(t):
        m, n, q = map(int, lines[idx].split())
        idx += 1
        grid = [lines[idx + i] for i in range(m)]
        idx += m
        out.append(f"{m} {n} {q}")
        for _ in range(q):
            r, c = map(int, lines[idx].split())
            idx += 1
            out.append(str(largest_square_size(grid, r, c)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
