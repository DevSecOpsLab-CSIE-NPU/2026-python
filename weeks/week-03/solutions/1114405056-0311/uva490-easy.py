import sys


def solve(data: str) -> str:
    """將輸入文字矩陣順時針旋轉 90 度。"""
    # splitlines() 會保留每行中的空白字元內容（不含換行符本身）。
    lines = data.splitlines()
    if not lines:
        return ""

    # 找最長列，旋轉後會變成輸出的列數。
    width = max(len(line) for line in lines)
    height = len(lines)

    out = []
    for col in range(width):
        row_chars = []

        # 從原本最下面那列往上取，形成新的橫向一列。
        for row in range(height - 1, -1, -1):
            if col < len(lines[row]):
                row_chars.append(lines[row][col])
            else:
                # 原矩陣較短列補空白，維持旋轉後位置正確。
                row_chars.append(" ")

        # UVA 490 通常不要求行尾多餘空白，去除可讓輸出更乾淨。
        out.append("".join(row_chars).rstrip())

    return "\n".join(out)


def main() -> None:
    text = sys.stdin.read()
    ans = solve(text)
    if ans:
        print(ans)


if __name__ == "__main__":
    main()
