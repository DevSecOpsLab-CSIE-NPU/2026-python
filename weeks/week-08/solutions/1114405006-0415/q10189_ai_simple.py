"""
UVA 10189 - Minesweeper
AI 教學簡單版本（含中文註解）
"""

import sys


def solve(data: str) -> str:
    # 先把所有輸入行切開，方便逐行讀取
    lines = data.splitlines()
    i = 0
    field_no = 1
    out = []

    # 八個方向：上、下、左、右、四個斜角
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    while i < len(lines):
        line = lines[i].strip()
        i += 1

        # 跳過空白行（有些測資可能會夾空行）
        if not line:
            continue

        n, m = map(int, line.split())
        if n == 0 and m == 0:
            break

        # 讀入原始地圖
        grid = []
        for _ in range(n):
            grid.append(list(lines[i].rstrip("\n")))
            i += 1

        # 先建立答案地圖：地雷保留 '*', 空白先放 '0'
        ans = [["0"] * m for _ in range(n)]
        for r in range(n):
            for c in range(m):
                if grid[r][c] == "*":
                    ans[r][c] = "*"

        # 對每個地雷，去把周圍 8 格的數字 +1
        for r in range(n):
            for c in range(m):
                if grid[r][c] != "*":
                    continue

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and ans[nr][nc] != "*":
                        ans[nr][nc] = str(int(ans[nr][nc]) + 1)

        if field_no > 1:
            out.append("")
        out.append(f"Field #{field_no}:")
        for row in ans:
            out.append("".join(row))

        field_no += 1

    return "\n".join(out)


def main() -> None:
    data = sys.stdin.read()
    print(solve(data))


if __name__ == "__main__":
    main()
