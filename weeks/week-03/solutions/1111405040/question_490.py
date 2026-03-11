"""
UVA 490 - 句子旋轉。
"""

from __future__ import annotations

import sys


def rotate_clockwise(lines: list[str]) -> list[str]:
    """
    將文字矩陣順時針旋轉 90 度。

    旋轉前先將每行右側補空白，形成完整矩形。
    """
    if not lines:
        return []

    max_width = max(len(line) for line in lines)
    padded = [line.ljust(max_width) for line in lines]
    height = len(padded)

    rotated: list[str] = []
    for col in range(max_width):
        chars = [padded[row][col] for row in range(height - 1, -1, -1)]
        rotated.append("".join(chars).rstrip())
    return rotated


def solve(text: str) -> str:
    """處理完整輸入文字並回傳旋轉後結果。"""
    lines = text.splitlines()
    return "\n".join(rotate_clockwise(lines))


def main() -> None:
    """主程式進入點。"""
    data = sys.stdin.read()
    result = solve(data)
    if result:
        sys.stdout.write(result + "\n")


if __name__ == "__main__":
    main()
