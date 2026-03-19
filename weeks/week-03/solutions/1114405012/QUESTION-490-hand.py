#!/usr/bin/env python3
"""UVA 490 手打版。

將輸入文字矩陣順時針旋轉 90 度後輸出。
"""

import sys


def main() -> None:
    lines = [line.rstrip("\n") for line in sys.stdin]
    if not lines:
        return

    height = len(lines)
    width = max(len(line) for line in lines)

    out: list[str] = []

    # 新矩陣列索引 i 對應到原本的欄位 i
    for i in range(width):
        row_chars: list[str] = []
        # 由下往上讀取，形成順時針旋轉
        for j in range(height - 1, -1, -1):
            if i < len(lines[j]):
                row_chars.append(lines[j][i])
            else:
                row_chars.append(" ")
        out.append("".join(row_chars))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
