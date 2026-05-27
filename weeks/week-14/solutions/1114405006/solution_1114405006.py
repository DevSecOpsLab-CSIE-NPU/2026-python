# -*- coding: utf-8 -*-
"""
解題模組：UVA 11349 — Symmetric Matrix

本模組提供：
- `is_symmetric_matrix(matrix)`：檢查給定 n×n 整數矩陣是否符合題目的「對稱」定義
- `main()`：從標準輸入讀取多組測資並輸出結果（與題目輸出格式一致）

所有註解皆為繁體中文。
"""
from typing import List
import sys


def is_symmetric_matrix(matrix: List[List[int]]) -> bool:
    """判斷矩陣是否為題目定義的對稱矩陣（中心點對稱，且所有元素非負）。

    參數:
    - matrix: n×n 的整數矩陣（list of list）

    回傳:
    - 若符合條件則回傳 True，否則回傳 False
    """
    n = len(matrix)
    for i in range(n):
        # 逐行逐列檢查
        for j in range(n):
            val = matrix[i][j]
            # 說明：題目要求矩陣元素必須為非負數，若出現負數則直接判為非對稱
            # 中心對稱的定義：M[i][j] == M[n-1-i][n-1-j]
            # 例如 n=3 時，(0,0) 對應 (2,2)、(0,1) 對應 (2,1) 等
            # 條件 1：元素必須為非負數
            if val < 0:
                return False
            # 條件 2：中心點對稱
            # 注意：此處比較的是中心對稱（central symmetry），不是轉置
            if val != matrix[n - 1 - i][n - 1 - j]:
                return False
    return True


def main() -> None:
    """從標準輸入讀取資料並輸出每組測資是否對稱。

    輸入格式：
    - 第一行為整數 T（測資組數）
    - 每組先有一行 `N = n`，接著 n 行矩陣資料，每行 n 個整數

    輸出格式：
    - `Test #t: Symmetric.` 或 `Test #t: Non-symmetric.`
    """
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
        # 讀取類似 "N = n" 的行，容錯處理
        while idx < len(data) and data[idx].strip() == "":
            idx += 1
        if idx >= len(data):
            break
        header = data[idx].strip()
        idx += 1
        # 解析 n
        if "=" in header:
            try:
                n = int(header.split("=")[1].strip())
            except Exception:
                n = 0
        else:
            try:
                n = int(header)
            except Exception:
                n = 0
        # 讀取 n 行矩陣
        matrix = []
        for _ in range(n):
            if idx >= len(data):
                row = []
            else:
                row = list(map(int, data[idx].strip().split()))
            idx += 1
            matrix.append(row)
        # 檢查
        ok = is_symmetric_matrix(matrix)
        if ok:
            print(f"Test #{t}: Symmetric.")
        else:
            print(f"Test #{t}: Non-symmetric.")


if __name__ == "__main__":
    main()
