# -*- coding: utf-8 -*-
"""
簡易版解法（-easy）：UVA 11349 — Symmetric Matrix

說明（繁體中文詳細註解）：

- 題目重點：判斷 n×n 矩陣是否為「中心對稱」且所有元素非負。
  中心對稱定義為：對任意 i, j 有 M[i][j] == M[n-1-i][n-1-j]。

- 實作思路（易記法）：
  1. 先檢查所有元素是否都 >= 0（若有負數可立即回傳 False）；
  2. 利用 Python 的序列操作把整個矩陣反轉：
     - `matrix[::-1]` 會把列上下顛倒（第 0 列變最後一列）；
     - 每列用 `row[::-1]` 會把該列左右顛倒（第 0 欄變最後一欄）；
    若對整個矩陣做上下顛倒後，再將每列左右顛倒，結果等於原矩陣，則代表中心對稱。

  以式子表達：matrix == [row[::-1] for row in matrix[::-1]]

- 優點：語法簡潔、直觀，容易記憶；缺點：在非常大的矩陣上會建立額外的暫存結構（不過題目 n ≤ 100，影響可忽略）。

- 時間與空間複雜度：
  - 時間：O(n^2)，需遍歷所有元素檢查非負與比較；
  - 空間：比較式會建立一個反轉後的矩陣副本，額外空間為 O(n^2)（可接受於題目限制）。

此檔案提供：
- `is_symmetric_matrix_easy(matrix)`：簡潔判斷函式（可直接匯入測試）
- `main()`：讀取 stdin 並依題目格式輸出結果

使用範例：
  echo -e "1\nN = 3\n5 1 3\n2 0 2\n3 1 5" | python solution_1114405006-easy.py

註：所有註解皆為繁體中文。
"""
from typing import List
import sys


def is_symmetric_matrix_easy(matrix: List[List[int]]) -> bool:
    """簡潔判斷矩陣是否滿足題目要求。

    步驟：
    1. 若矩陣為空（n=0），視為對稱（題目範圍不包含 n=0，但此處保險處理）；
    2. 檢查每個元素是否為非負數；
    3. 比較原矩陣與上下顛倒且每列左右顛倒後的矩陣是否相等。

    參數:
    - matrix: List[List[int]]，n×n 矩陣

    回傳:
    - bool：若為中心對稱且所有元素非負則回傳 True，否則 False。
    """
    # 1) 空矩陣視為對稱（題目未提供，但做周全處理）
    if not matrix:
        return True

    n = len(matrix)
    # 2) 檢查所有元素是否為非負；若任一元素 < 0，立即回傳 False
    for i, row in enumerate(matrix):
        if len(row) != n:
            # 若行長不足或超出（不符合 n×n）則視為非對稱
            return False
        for j, v in enumerate(row):
            if v < 0:
                # 發現負數，依題意為 Non-symmetric
                return False

    # 3) 使用簡潔的序列反轉比對中心對稱
    #    matrix[::-1] 會把列上下翻轉，row[::-1] 把列內左右翻轉
    #    若結果相等，說明 M[i][j] == M[n-1-i][n-1-j]
    return matrix == [r[::-1] for r in matrix[::-1]]


def main() -> None:
    """讀取 stdin 的多組測資，並輸出每組是否對稱（符合題目格式）。"""
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return
    idx = 0
    try:
        T = int(data[idx].strip())
    except Exception:
        return
    idx += 1

    for t in range(1, T + 1):
        # 跳過可能的空白行
        while idx < len(data) and data[idx].strip() == "":
            idx += 1
        if idx >= len(data):
            break
        header = data[idx].strip(); idx += 1
        # 支援 "N = n" 或直接 "n" 的格式
        if '=' in header:
            try:
                n = int(header.split('=')[1].strip())
            except Exception:
                n = 0
        else:
            try:
                n = int(header)
            except Exception:
                n = 0

        matrix = []
        for _ in range(n):
            if idx < len(data):
                row = list(map(int, data[idx].strip().split()))
            else:
                row = []
            idx += 1
            matrix.append(row)

        ok = is_symmetric_matrix_easy(matrix)
        print(f"Test #{t}: {'Symmetric.' if ok else 'Non-symmetric.'}")


if __name__ == '__main__':
    main()
