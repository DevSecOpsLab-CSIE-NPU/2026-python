"""
UVA 10189 - Minesweeper
簡單版（CPE 現場可手打）
"""


def solve() -> None:
    import sys

    lines = sys.stdin.read().splitlines()
    i = 0
    field_no = 1
    out = []

    while i < len(lines):
        if not lines[i].strip():
            i += 1
            continue

        n, m = map(int, lines[i].split())
        i += 1

        if n == 0 and m == 0:
            break

        board = [list(lines[i + r].rstrip()) for r in range(n)]
        i += n

        # 先把答案陣列全部設成 '0'，之後再把地雷與數字填入
        ans = [["0"] * m for _ in range(n)]

        for r in range(n):
            for c in range(m):
                if board[r][c] == "*":
                    ans[r][c] = "*"
                    continue

                cnt = 0
                # 檢查 8 個方向鄰居（含斜角）
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if dr == 0 and dc == 0:
                            continue

                        nr = r + dr
                        nc = c + dc

                        # 邊界判斷：必須在棋盤內
                        if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == "*":
                            cnt += 1

                ans[r][c] = str(cnt)

        if field_no > 1:
            out.append("")

        out.append(f"Field #{field_no}:")
        for row in ans:
            out.append("".join(row))

        field_no += 1

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
