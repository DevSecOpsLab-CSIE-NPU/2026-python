import sys


def count_mines(board, r, c):
    """計算 (r, c) 周圍 8 格的地雷數。"""

    n = len(board)
    m = len(board[0]) if n else 0
    total = 0

    # 8 個方向：左上、上、右上、左、右、左下、下、右下
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue

            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == "*":
                total += 1

    return total


def solve(text):
    """把整段輸入文字轉成題目要求的輸出。"""

    lines = [line.strip() for line in text.splitlines() if line.strip()]
    out = []
    idx = 0
    field_no = 1

    while idx < len(lines):
        n, m = map(int, lines[idx].split())
        idx += 1

        # 0 0 是結束，不需要處理
        if n == 0 and m == 0:
            break

        board = lines[idx:idx + n]
        idx += n

        out.append(f"Field #{field_no}:")

        # 逐格掃描：地雷保留 *，空白格改成周圍地雷數
        for r in range(n):
            row = []
            for c in range(m):
                if board[r][c] == "*":
                    row.append("*")
                else:
                    row.append(str(count_mines(board, r, c)))
            out.append("".join(row))

        field_no += 1

        # 每組測資之間空一行
        if idx < len(lines) and lines[idx].split() != ["0", "0"]:
            out.append("")

    return "\n".join(out)


def main():
    """競賽模式入口。"""

    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()