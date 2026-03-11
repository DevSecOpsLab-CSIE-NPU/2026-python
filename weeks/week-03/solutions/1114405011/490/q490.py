"""
UVA 490 / ZeroJudge c045 - Rotating Text
=========================================
【題目摘要】
  將輸入的多行文字，整體順時針旋轉 90 度後輸出。

【旋轉規則】
  輸入最後一列 → 輸出最左欄（逐行由上往下）
  輸入第一列   → 輸出最右欄（逐行由上往下）

【步驟說明】
  1. 讀進所有行，找出最長行的長度 max_w
  2. 所有行向右補空格到 max_w，形成完整矩形
  3. 對補齊後的矩形做 90 度順時針旋轉：
       新的第 j 列（0-indexed）= 原矩陣第 j 欄，由最下方讀到最上方
  4. 輸出旋轉後的每一列

【範例】
  輸入：
    HELLO
    WORLD
  補齊後矩形（5×2）：
    row 0: H E L L O
    row 1: W O R L D
  順時針旋轉（5 列輸出，每列 2 字元）：
    col 0 由下到上：W, H  → "WH"
    col 1 由下到上：O, E  → "OE"
    col 2 由下到上：R, L  → "RL"
    col 3 由下到上：L, L  → "LL"
    col 4 由下到上：D, O  → "DO"
  輸出：
    WH
    OE
    RL
    LL
    DO

【複雜度】O(n × m)，n = 行數，m = 最寬行的字元數
"""

import sys


# ─────────────────────────────────────────────────────────────────────────────
def rotate_cw(lines: list) -> list:
    """
    將文字行列表順時針旋轉 90 度，回傳旋轉後的行列表。

    【演算法說明】
      設原矩陣有 n 行、最寬 max_w 欄。
      補齊後形成 n × max_w 矩形。
      旋轉後矩形為 max_w × n：
        新矩陣 result[j] = 原矩陣第 j 欄，從 row[n-1] 讀到 row[0]
        即：result[j][k] = padded[n-1-k][j]

    參數：
        lines (list[str]): 每個元素為輸入的一行（不含換行符）

    回傳：
        list[str]: 旋轉後的每一行（可能含尾端空格，維持矩形）
    """
    if not lines:
        return []

    max_w = max(len(line) for line in lines)  # 找最長行的長度

    # 所有行補空格到 max_w（向右對齊成矩形）
    padded = [line.ljust(max_w) for line in lines]

    n = len(padded)       # 原始行數 = 旋轉後每列的字元數
    result = []

    # 對每一欄（索引 j = 0 ... max_w-1）收集由下往上的字元
    for j in range(max_w):
        row_chars = []
        for i in range(n - 1, -1, -1):   # 由最後一行往上讀
            row_chars.append(padded[i][j])
        result.append(''.join(row_chars))

    return result


# ─────────────────────────────────────────────────────────────────────────────
def solve(input_text: str) -> str:
    """
    讀入完整輸入文字，輸出順時針旋轉 90 度後的結果。

    參數：
        input_text (str): 完整輸入文字（含換行）

    回傳：
        str: 旋轉後的完整輸出文字
    """
    lines = input_text.splitlines()   # 保留行內空格，不 strip

    if not lines:
        return ""

    rotated = rotate_cw(lines)
    return '\n'.join(rotated)


# ── 直接執行時：從 stdin 讀入，輸出至 stdout ─────────────────────────────────
if __name__ == "__main__":
    print(solve(sys.stdin.read()))
