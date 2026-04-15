"""
UVA 10189 - Minesweeper
手打版本
"""

import sys


def run(inp: str) -> str:
    rows = inp.splitlines()
    p = 0
    case_id = 1
    result = []
    around = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1),
    ]

    while p < len(rows):
        header = rows[p].strip()
        p += 1

        if header == "":
            continue

        n, m = map(int, header.split())
        if n == 0 and m == 0:
            break

        board = []
        for _ in range(n):
            board.append(list(rows[p].strip()))
            p += 1

        out = [["0"] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if board[i][j] == "*":
                    out[i][j] = "*"

        for i in range(n):
            for j in range(m):
                if board[i][j] != "*":
                    continue
                for di, dj in around:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and out[ni][nj] != "*":
                        out[ni][nj] = str(int(out[ni][nj]) + 1)

        if case_id > 1:
            result.append("")
        result.append(f"Field #{case_id}:")

        for line in out:
            result.append("".join(line))

        case_id += 1

    return "\n".join(result)


def main() -> None:
    text = sys.stdin.read()
    print(run(text))


if __name__ == "__main__":
    main()
