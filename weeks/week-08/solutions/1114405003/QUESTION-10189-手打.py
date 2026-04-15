import sys


def solve_case(n, m, grid):
    # 八個方向位移：上、下、左、右、四個斜角
    dirs = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    ans = [["0"] * m for _ in range(n)]

    for r in range(n):
        for c in range(m):
            if grid[r][c] == "*":
                ans[r][c] = "*"
                continue

            count = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == "*":
                    count += 1
            ans[r][c] = str(count)

    return ["".join(row) for row in ans]


def main():
    lines = sys.stdin.read().splitlines()
    idx = 0
    field_no = 1
    out = []

    while idx < len(lines):
        if not lines[idx].strip():
            idx += 1
            continue

        n, m = map(int, lines[idx].split())
        idx += 1
        if n == 0 and m == 0:
            break

        grid = lines[idx: idx + n]
        idx += n

        solved = solve_case(n, m, grid)

        if field_no > 1:
            out.append("")
        out.append(f"Field #{field_no}:")
        out.extend(solved)
        field_no += 1

    sys.stdout.write("\n".join(out))
    if out:
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
