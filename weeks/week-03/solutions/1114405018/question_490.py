"""UVA 490 - Rotating Sentences

將輸入文字順時針旋轉 90 度。
規則：
- 輸出列數為輸入最長行長度。
- 每一列由原輸入「由下到上」取同一欄位組成。
- 缺字元位置補空白，最後移除每列尾端多餘空白。
"""

import sys


def solve(data: str) -> str:
    # splitlines 會保留空行（不含換行符），符合題目 EOF 輸入模式
    lines = data.splitlines()
    if not lines:
        return ""

    width = max(len(line) for line in lines)
    out = []

    for col in range(width):
        row_chars = []
        for row in range(len(lines) - 1, -1, -1):
            if col < len(lines[row]):
                row_chars.append(lines[row][col])
            else:
                row_chars.append(" ")
        out.append("".join(row_chars).rstrip())

    return "\n".join(out)


def main() -> None:
    result = solve(sys.stdin.read())
    if result:
        sys.stdout.write(result)


if __name__ == "__main__":
    main()
