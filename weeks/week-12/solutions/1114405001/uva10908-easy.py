"""UVA 10908 - Largest Square (easy version)"""


def get_size(grid: list[str], r: int, c: int) -> int:
    m = len(grid)
    n = len(grid[0])
    ch = grid[r][c]
    size = 1

    step = 1
    while True:
        r1 = r - step
        r2 = r + step
        c1 = c - step
        c2 = c + step

        if r1 < 0 or c1 < 0 or r2 >= m or c2 >= n:
            break

        same = True
        for rr in range(r1, r2 + 1):
            for cc in range(c1, c2 + 1):
                if grid[rr][cc] != ch:
                    same = False
                    break
            if not same:
                break

        if not same:
            break

        size += 2
        step += 1

    return size


def solve(data: str) -> str:
    arr = [x.strip() for x in data.splitlines() if x.strip()]
    p = 0
    t = int(arr[p])
    p += 1
    ans = []

    for _ in range(t):
        m, n, q = map(int, arr[p].split())
        p += 1

        grid = []
        for _ in range(m):
            grid.append(arr[p])
            p += 1

        ans.append(f"{m} {n} {q}")
        for _ in range(q):
            r, c = map(int, arr[p].split())
            p += 1
            ans.append(str(get_size(grid, r, c)))

    return "\n".join(ans)


def main() -> None:
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
