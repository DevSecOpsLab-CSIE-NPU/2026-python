"""UVA 490 的簡易版本。

這個版本刻意把思路寫得最容易記：
1. 先找出最寬的一行
2. 先把每一行補成同樣寬
3. 之後從左到右掃欄位
4. 每一欄都由下往上讀

背誦口訣：
「補齊寬度，倒著讀欄，組成新行」
"""

from __future__ import annotations

import sys


def rotate_lines_easy(lines: list[str]) -> list[str]:
    """用最簡單、最容易記憶的方式旋轉文字。

    這裡的做法非常直觀：
    - 先把每行用空白補到同樣長度
    - 再從欄位的角度重新組合
    - 每一欄都從最後一行往第一行讀
    
    這樣做的好處是：
    - 不需要特別處理缺字元的位置
    - 每一行都已經是完整矩形
    - 程式結構接近紙上手算
    """
    if not lines:
        return []

    width = max(len(line) for line in lines)
    if width == 0:
        return []

    # 先補齊成矩形，讓後面的欄位存取更單純。
    padded_lines = [line.ljust(width) for line in lines]
    rotated = []

    # 旋轉後的每一行，對應原本的一個欄位。
    for col in range(width):
        # 這一欄要從下往上讀，所以直接反轉行順序。
        rotated_line = ''.join(line[col] for line in reversed(padded_lines))
        rotated.append(rotated_line)

    return rotated


def solve_text(text: str) -> str:
    """讀入整份文字並輸出旋轉後結果。"""
    if not text:
        return ""

    lines = text.splitlines()
    rotated_lines = rotate_lines_easy(lines)
    if not rotated_lines:
        return ""

    return '\n'.join(rotated_lines) + '\n'


def main() -> None:
    """主函式：從標準輸入讀取並輸出結果。"""
    input_text = sys.stdin.read()
    sys.stdout.write(solve_text(input_text))


if __name__ == '__main__':
    main()
