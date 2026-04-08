#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
UVA 490 - 旋轉文字矩陣（最簡單版）

題目：將文字矩陣順時針旋轉 90 度輸出

例如：
  輸入：           輸出：
  HELLO           W H
  WORLD           O E
                 R L
                 L L
                 D O

想法：順時針旋轉 = 顛倒 + 轉置
  1. 顛倒：最後一行變最前（由下往上）
  2. 轉置：行列互換
"""

import sys


def rotate(lines):
    """
    旋轉文字矩陣 90 度（順時針）

    參數：
        lines: list - 輸入的文字行列表

    回傳：
        list - 旋轉後的文字行列表

    原理：
        Excel 表格旋轉 90 度，就像把照片轉一樣
        - 原本最後一行會跑到最左邊
        - 原本第一行會跑到最右邊
    """
    # 空列表直接回傳
    if not lines:
        return []

    # === 第一步：墊高 ===
    # 找出最寬那行的長度，當作矩陣寬度
    # 因為每行長度可能不同，短的要補空格
    w = max(len(x) for x in lines)

    # 把每行都補成相同長度（向右對齊，空格補在右邊）
    # 例如："AB".ljust(3) -> "AB "
    p = [x.ljust(w) for x in lines]
    # p 現在是一个標準矩陣，像這樣：
    # p[0] = "HELLO"  (5個字)
    # p[1] = "WORLD"  (5個字)

    # === 第二步：旋轉（顛倒 + 轉置）===
    # 新矩陣的寬度 = 原本的高度
    # 新矩陣的高度 = 原本的寬度
    #
    # for c in range(w):  // 遍历每一欄（新矩陣的每一行）
    #   for r in range(len(p)-1, -1, -1):  // 從最後一列往前收集
    #     把 p[r][c] 加進來
    #
    # 圖解：
    #   墊高後：          旋轉後：
    #   H E L L O         W H
    #   W O R L D         O E
    #                    R L
    #                    L L
    #                    D O

    return ["".join(p[r][c] for r in range(len(p) - 1, -1, -1)) for c in range(w)]


# ===== 主程式 =====
if __name__ == "__main__":
    # 從輸入讀取所有行
    input_lines = sys.stdin.read().splitlines()

    # 旋轉
    result = rotate(input_lines)

    # 輸出（每行用換行分隔）
    print("\n".join(result))
