"""
UVA 100 / ZeroJudge c039 - The 3n+1 Problem（Collatz 序列）簡易版
===================================================================
【與 q100.py 的差異】
  q100.py  → 遞迴 + 記憶化快取，速度較快但程式碼較難理解
  q100-easy.py → 純迴圈，不用遞迴也不用快取，邏輯直覺易懂

【核心想法】
  直接用 while 迴圈模擬題目描述的步驟：
    ① n 是奇數 → n = 3 * n + 1
    ② n 是偶數 → n = n // 2
    ③ 直到 n == 1 為止
  每走一步就把計數器加 1，最後計數器就是 cycle-length。
"""

import sys


# ─────────────────────────────────────────────────────────────────────────────
def cycle_length(n: int) -> int:
    """
    用 while 迴圈計算 n 的 Collatz cycle-length。

    【為什麼比遞迴簡單？】
      - 不需要宣告快取字典
      - 不需要理解遞迴呼叫的堆疊概念
      - 程式碼就像直接翻譯題目文字，看了就懂

    【步驟說明】
      1. 從 count = 1 開始（把 n 本身算進去）
      2. 每次依規則更新 n，count 加 1
      3. 當 n 變成 1 時，迴圈結束，回傳 count

    參數：
        n (int): 正整數，0 < n < 1,000,000

    回傳：
        int: n 的 cycle-length
    """
    count = 1       # 計數從 1 開始，代表「n 本身」已算一個

    while n != 1:   # 只要還沒走到 1，就繼續
        if n % 2 == 1:
            # 奇數：乘 3 加 1
            n = 3 * n + 1
        else:
            # 偶數：除以 2（整數除法）
            n = n // 2
        count += 1  # 每走一步，序列長度加 1

    return count    # 回傳序列總長度


# ─────────────────────────────────────────────────────────────────────────────
def max_cycle_in_range(i: int, j: int) -> int:
    """
    找出閉區間 [min(i,j), max(i,j)] 內最大的 cycle-length。

    【處理 i > j 的情況】
      題目說輸入可能是 i > j（例如 10 1），
      所以先用 min/max 確保 lo 一定 <= hi，
      再用 for 迴圈從 lo 跑到 hi，逐一計算並更新最大值。

    參數：
        i (int): 區間端點之一
        j (int): 區間端點之一

    回傳：
        int: 區間內最大 cycle-length
    """
    lo, hi = min(i, j), max(i, j)  # 確保 lo <= hi

    best = 0                        # 記錄目前為止看到的最大值

    for n in range(lo, hi + 1):     # 從 lo 到 hi，每個數都算
        cl = cycle_length(n)        # 算出這個數的 cycle-length
        if cl > best:               # 比目前最大值還大就更新
            best = cl

    return best


# ─────────────────────────────────────────────────────────────────────────────
def solve(input_text: str) -> str:
    """
    讀入多行輸入字串，輸出對應的答案字串。

    【輸入格式】每行：i j
    【輸出格式】每行：i j max_cycle_length

    【處理流程】
      1. 把整個輸入依行切割
      2. 跳過空行（避免程式當掉）
      3. 把每行的兩個數字讀出來
      4. 計算區間最大 cycle-length
      5. 按格式組成輸出行

    參數：
        input_text (str): 多行輸入字串

    回傳：
        str: 多行輸出字串（行與行之間用換行分隔）
    """
    output_lines = []   # 用來存放每行的輸出結果

    for line in input_text.strip().splitlines():
        line = line.strip()

        if not line:        # 空行直接跳過
            continue

        # 把這行的兩個整數讀進來
        i, j = map(int, line.split())

        # 計算 [min(i,j), max(i,j)] 區間內的最大 cycle-length
        max_cl = max_cycle_in_range(i, j)

        # 輸出時保留原始 i, j 的順序（題目要求），後面接最大值
        output_lines.append(f"{i} {j} {max_cl}")

    # 把所有輸出行用換行串起來，結尾不多加換行
    return "\n".join(output_lines)


# ── 直接用 python q100-easy.py 執行時，從鍵盤（stdin）讀入並印出答案 ──────────
if __name__ == "__main__":
    print(solve(sys.stdin.read()))
