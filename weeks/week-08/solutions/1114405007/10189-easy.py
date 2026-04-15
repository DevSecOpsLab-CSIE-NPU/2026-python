"""UVA 10189 - easy 版本（含中文註解）。"""

import sys


def solve(data: str) -> str:
    lines = data.strip().splitlines()
    idx = 0
    case_no = 1
    out = []

    while idx < len(lines):
        n, m = map(int, lines[idx].split())
        idx += 1
        if n == 0 and m == 0:
            break

        grid = [list(lines[idx + r].strip()) for r in range(n)]
        idx += n

        # 先建立全 0 的答案表，等等再把地雷和數字填進去
        ans = [["0"] * m for _ in range(n)]

        for r in range(n):
            for c in range(m):
                if grid[r][c] == "*":
                    ans[r][c] = "*"
                    continue

                mines = 0
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == "*":
                            mines += 1
                ans[r][c] = str(mines)

        if case_no > 1:
            out.append("")
        out.append(f"Field #{case_no}:")
        out.extend("".join(row) for row in ans)
        case_no += 1

    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
