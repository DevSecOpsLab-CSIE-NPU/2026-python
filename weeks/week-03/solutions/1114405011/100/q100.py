"""
UVA 100 / ZeroJudge c039 - The 3n+1 Problem（Collatz 序列）
=============================================================
【題目概要】
  對任意正整數 n，反覆執行以下規則，直到 n 等於 1 為止：
    ① 若 n 為奇數  → n = 3 * n + 1
    ② 若 n 為偶數  → n = n / 2
  從起始 n 到最終印出 1，整個數列的長度稱為 n 的 cycle-length。

【範例】
  n = 22 產生：22 → 11 → 34 → 17 → 52 → 26 → 13 → 40 → 20 → 10 → 5
               → 16 → 8 → 4 → 2 → 1，共 16 個數字，故 cycle-length = 16。

【輸入格式】
  每行兩個正整數 i, j（0 < i, j < 1,000,000）

【輸出格式】
  每行輸出：i  j  max_cycle_length
  （max_cycle_length 為 [min(i,j), max(i,j)] 區間內所有整數的最大 cycle-length）

【解題策略】
  1. 遞迴計算 cycle_length(n)
  2. 使用 _cache 字典做記憶化（Memoization），避免重複計算相同的 n
  3. 因題目允許 i > j，取區間時先用 min/max 校正順序
"""

import sys

# ── 記憶化快取 ──────────────────────────────────────────────────────────────
# 以字典儲存「已計算過」的 n 對應 cycle-length，避免重複遞迴
# 初始值：n=1 的 cycle-length 為 1（序列只有 [1] 本身）
_cache: dict[int, int] = {1: 1}


# ─────────────────────────────────────────────────────────────────────────────
def cycle_length(n: int) -> int:
    """
    計算單一正整數 n 的 Collatz cycle-length。

    演算法：
      - 若 n 已在快取中，直接回傳快取值（記憶化剪枝）
      - 否則依奇偶性遞迴計算下一個 n 的 cycle-length，再加 1
      - 計算結果存回快取，供後續查詢使用

    參數：
        n (int): 正整數，0 < n < 1,000,000

    回傳：
        int: n 的 cycle-length（數列長度，包含起始值 n 與結尾 1）
    """
    # 快取命中：直接使用已知結果，不再遞迴
    if n in _cache:
        return _cache[n]

    # 依奇偶性套用 Collatz 規則，遞迴求出下一步的 cycle-length 後加 1
    if n % 2 == 1:
        # 奇數情況：下一個數為 3n + 1
        result = 1 + cycle_length(3 * n + 1)
    else:
        # 偶數情況：下一個數為 n / 2（整數除法）
        result = 1 + cycle_length(n // 2)

    # 將計算結果存入快取，下次查詢 O(1) 直接取得
    _cache[n] = result
    return result


# ─────────────────────────────────────────────────────────────────────────────
def max_cycle_in_range(i: int, j: int) -> int:
    """
    計算閉區間 [min(i,j), max(i,j)] 內所有整數的最大 cycle-length。

    由於題目允許 i > j 的輸入，此函式會先自動調整區間順序，
    確保 lo <= hi，再對區間內每個整數呼叫 cycle_length() 取最大值。

    參數：
        i (int): 區間端點之一（正整數）
        j (int): 區間端點之一（正整數）

    回傳：
        int: 區間內最大 cycle-length
    """
    # 自動校正：無論輸入順序為何，lo 永遠 <= hi
    lo, hi = min(i, j), max(i, j)

    # 對區間內每個整數計算 cycle-length，利用 max() 取最大值
    # 搭配快取後，已計算過的 n 不會重複遞迴
    return max(cycle_length(n) for n in range(lo, hi + 1))


# ─────────────────────────────────────────────────────────────────────────────
def solve(input_text: str) -> str:
    """
    解析多行輸入字串，回傳對應的多行輸出字串。

    輸入格式（每行）：i j
    輸出格式（每行）：i j max_cycle_length

    處理流程：
      1. 逐行讀取輸入
      2. 跳過空白行（容錯處理）
      3. 解析 i, j 後呼叫 max_cycle_in_range()
      4. 依「原始 i j max」格式組合輸出行

    參數：
        input_text (str): 包含多組測試資料的字串

    回傳：
        str: 多行輸出字串（各行以換行符分隔，結尾無多餘換行）
    """
    output_lines = []  # 收集每行輸出結果

    for line in input_text.strip().splitlines():
        line = line.strip()

        # 跳過空白行，避免解析錯誤
        if not line:
            continue

        # 將一行中的兩個整數解析為 i, j
        i, j = map(int, line.split())

        # 計算 [min(i,j), max(i,j)] 區間內最大 cycle-length
        max_cl = max_cycle_in_range(i, j)

        # 輸出保留原始 i, j 順序（題目規定），後接最大 cycle-length
        output_lines.append(f"{i} {j} {max_cl}")

    # 用換行符串接所有輸出行，結尾不加額外換行
    return "\n".join(output_lines)


# ── 作為獨立程式執行時：從標準輸入讀取，輸出至標準輸出 ──────────────────────
if __name__ == "__main__":
    # 一次讀取全部 stdin，交由 solve() 處理後印出
    print(solve(sys.stdin.read()))
