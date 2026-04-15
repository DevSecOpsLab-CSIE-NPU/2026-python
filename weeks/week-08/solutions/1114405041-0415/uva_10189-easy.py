from __future__ import annotations

import sys


# 8 個方向：上、下、左、右，加上 4 個斜角。
DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]


def solve(data: str) -> str:
    """
    簡單版想法：
    1. 一組一組讀地圖。
    2. 如果這格本來就是地雷，直接保留 `*`。
    3. 如果是空格，就把周圍 8 個方向的地雷數量加起來。
    4. 按題目格式印出 Field #1、Field #2 ...
    """
    lines = data.splitlines()
    index = 0
    field_no = 1
    answers: list[str] = []

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
        finished_grid: list[str] = []

        for row in range(n):
            row_result: list[str] = []
            for col in range(m):
                if grid[row][col] == "*":
                    row_result.append("*")
                else:
                    mines = 0
                    for dr, dc in DIRECTIONS:
                        nr = row + dr
                        nc = col + dc
                        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == "*":
                            mines += 1
                    row_result.append(str(mines))
            finished_grid.append("".join(row_result))

        answers.append(f"Field #{field_no}:\n" + "\n".join(finished_grid))
        field_no += 1

    return "\n\n".join(answers)


def main() -> None:
    raw_data = sys.stdin.read()
    sys.stdout.write(solve(raw_data))


if __name__ == "__main__":
    main()
