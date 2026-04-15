import sys

DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]


def solve(data: str) -> str:
    lines = data.splitlines()
    index = 0
    field_no = 1
    outputs = []

    while index < len(lines):
        line = lines[index].strip()
        index += 1
        if not line:
            continue

        n, m = map(int, line.split())
        if n == 0 and m == 0:
            break

        grid = lines[index:index + n]
        index += n
        result_grid = []

        for row in range(n):
            current_row = []
            for col in range(m):
                if grid[row][col] == "*":
                    current_row.append("*")
                else:
                    count = 0
                    for dr, dc in DIRECTIONS:
                        nr = row + dr
                        nc = col + dc
                        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == "*":
                            count += 1
                    current_row.append(str(count))
            result_grid.append("".join(current_row))

        outputs.append(f"Field #{field_no}:\n" + "\n".join(result_grid))
        field_no += 1

    return "\n\n".join(outputs)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
