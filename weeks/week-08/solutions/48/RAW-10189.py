import sys


def main():
    data = sys.stdin.read().split()
    index = 0
    field_number = 1
    outputs = []

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    while index < len(data):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2

        if n == 0 and m == 0:
            break

        grid = data[index:index + n]
        index += n

        outputs.append(f'Field #{field_number}:')

        for row in range(n):
            answer_row = []
            for col in range(m):
                if grid[row][col] == '*':
                    answer_row.append('*')
                    continue

                mine_count = 0
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '*':
                        mine_count += 1

                answer_row.append(str(mine_count))

            outputs.append(''.join(answer_row))

        field_number += 1

        if index < len(data):
            outputs.append('')

    sys.stdout.write('\n'.join(outputs))


if __name__ == '__main__':
    main()
