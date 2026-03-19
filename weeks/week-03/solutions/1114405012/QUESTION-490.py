#!/usr/bin/env python3
"""UVA 490 - Rotating Sentences.

將多行文字順時針旋轉 90 度。
"""

from __future__ import annotations

import sys


def main() -> None:
    lines = [line.rstrip("\n") for line in sys.stdin]
    if not lines:
        return

    max_len = max(len(line) for line in lines)
    row_count = len(lines)
    outputs: list[str] = []

    # 旋轉後的每一列，對應原本的每一個欄位
    for col in range(max_len):
        rotated_row_chars: list[str] = []
        for row in range(row_count - 1, -1, -1):
            if col < len(lines[row]):
                rotated_row_chars.append(lines[row][col])
            else:
                rotated_row_chars.append(" ")
        outputs.append("".join(rotated_row_chars))

    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    main()
