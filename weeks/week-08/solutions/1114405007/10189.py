"""UVA 10189 - 手打版本。"""

import sys


def solve(data: str) -> str:
    lines = data.strip().splitlines()
    pos = 0
    field_id = 1
    result = []

    while pos < len(lines):
        n, m = map(int, lines[pos].split())
        pos += 1
        if n == 0 and m == 0:
            break

        board = [lines[pos + i].strip() for i in range(n)]
        pos += n

        output_board = []
        for r in range(n):
            row_chars = []
            for c in range(m):
                if board[r][c] == "*":
                    row_chars.append("*")
                    continue

                count = 0
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if dr == 0 and dc == 0:
                            continue
                        rr = r + dr
                        cc = c + dc
                        if 0 <= rr < n and 0 <= cc < m and board[rr][cc] == "*":
                            count += 1
                row_chars.append(str(count))
            output_board.append("".join(row_chars))

        if field_id > 1:
            result.append("")
        result.append(f"Field #{field_id}:")
        result.extend(output_board)
        field_id += 1

    return "\n".join(result)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
