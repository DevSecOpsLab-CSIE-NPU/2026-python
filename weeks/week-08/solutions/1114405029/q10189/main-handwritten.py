import sys


def solve_field(n, m, grid):
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    result = []

    for i in range(n):
        row = []
        for j in range(m):
            if grid[i][j] == '*':
                row.append('*')
            else:
                count = 0
                for dx, dy in directions:
                    ni = i + dx
                    nj = j + dy
                    if 0 <= ni < n and 0 <= nj < m:
                        if grid[ni][nj] == '*':
                            count += 1
                row.append(str(count))
        result.append(''.join(row))

    return result


def main():
    lines = sys.stdin.read().splitlines()

    idx = 0
    field_number = 1
    all_outputs = []

    while idx < len(lines):
        n, m = map(int, lines[idx].split())
        idx += 1

        if n == 0 and m == 0:
            break

        grid = []
        for _ in range(n):
            grid.append(lines[idx])
            idx += 1

        answer = solve_field(n, m, grid)

        all_outputs.append(f"Field #{field_number}:")
        for line in answer:
            all_outputs.append(line)

        field_number += 1

    current = []
    blocks = []

    for line in all_outputs:
        if line.startswith("Field #") and current:
            blocks.append('\n'.join(current))
            current = [line]
        else:
            current.append(line)

    if current:
        blocks.append('\n'.join(current))

    print('\n\n'.join(blocks))


if __name__ == "__main__":
    main()