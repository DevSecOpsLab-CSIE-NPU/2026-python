"""
UVA 490 - Rotating Sentences（簡易版）

核心想法（一句話）：
  把文字矩形「轉一轉」——每一欄由下到上讀，變成新的一行。

簡易版說明：
  - 函式名稱縮短，易於記憶。
  - rot()  ← rotate（旋轉）
  - out()  ← output（輸出格式化）
  - 邏輯與正式版完全相同，只是命名更短。
"""

from __future__ import annotations

import sys


def rot(lines: list[str]) -> list[str]:
    """
    順時針旋轉 90 度。

    記憶口訣：「補齊→逐欄→由下往上」

    步驟拆解：
      ① max_len  → 找最長行的寬度
      ② padded   → 每行補空白到 max_len（ljust = 補右側）
      ③ for col  → 逐欄掃描（col = 0..max_len-1）
      ④ row 倒序 → 從最後一行讀到第一行（才是順時針效果）
    """
    if not lines:          # 空輸入直接回傳
        return []

    # ① 最長寬度
    max_len = max(len(l) for l in lines)

    # ② 每行補齊到等寬
    padded = [l.ljust(max_len) for l in lines]

    result: list[str] = []
    # ③ 逐欄
    for col in range(max_len):
        # ④ 由最後一行（index = len-1）往第一行（index = 0）讀取
        new_line = "".join(padded[row][col] for row in range(len(padded) - 1, -1, -1))
        result.append(new_line)

    return result


def out(lines: list[str]) -> str:
    """
    把串列組成輸出字串。

    只是把所有行用換行連起來，沒有其他處理。
    """
    return "\n".join(lines)  # 用 \n 把每行拼在一起


# ===========================================================
# 主程式
# ===========================================================

def main() -> None:
    """讀取標準輸入 → 旋轉 → 輸出。"""
    # rstrip("\n") 去掉換行符號，保留行內空白
    lines = [line.rstrip("\n") for line in sys.stdin]

    if not lines:     # 空輸入就不印
        return

    print(out(rot(lines)))   # 旋轉後直接印出


if __name__ == "__main__":
    main()
