"""
UVA 299 / ZeroJudge e561 - Train Swapping（火車車廂交換）
=========================================================
【題目概要】
  給定一列火車車廂的排列，每次只能交換「相鄰」兩節車廂。
  求最少需要幾次交換，才能讓車廂按 1, 2, 3, ..., L 的順序排好。

【核心觀察】
  「相鄰元素交換的最少次數」等於數列的「逆序數（inversions）」。
  逆序對定義：i < j 但 a[i] > a[j]，這樣的 (i, j) 組合就是一個逆序對。
  Bubble Sort 每次交換相鄰元素，恰好消除一個逆序對，
  因此最少交換次數 = 逆序對總數。

【演算法選擇】
  - Bubble Sort 計數法：O(L²)，L ≤ 50 完全夠用，程式碼簡單直觀。
  - Merge Sort 計數法：O(L log L)，適合大資料，但此題不需要。

【輸入格式】
  第 1 行：N（測試資料組數）
  之後每組資料：
    行 1：L（車廂數量，0 ≤ L ≤ 50）
    行 2：1 到 L 的排列（空格分隔）

【輸出格式】
  每組資料輸出一行：
  "Optimal train swapping takes S swaps."
"""

import sys


# ─────────────────────────────────────────────────────────────────────────────
def count_inversions(wagons: list) -> int:
    """
    計算數列的逆序數（inversions）。

    【逆序對定義】
      若 i < j 且 wagons[i] > wagons[j]，則 (i, j) 是一個逆序對。
      逆序數就是所有逆序對的總數。

    【方法：模擬 Bubble Sort】
      Bubble Sort 每次比較相鄰兩個元素，若前者 > 後者就交換。
      實際計算逆序數時，我們只計算「需要交換的次數」，不真正修改資料。

      用雙層迴圈：
        外層 i 從 0 到 L-2
        內層 j 從 i+1 到 L-1
        若 wagons[i] > wagons[j]，count 加 1

    參數：
        wagons (list): 車廂編號的排列（整數列表）

    回傳：
        int: 逆序數（等於 Bubble Sort 的最少交換次數）
    """
    count = 0
    n     = len(wagons)

    # 雙層迴圈：檢查所有 i < j 的配對
    for i in range(n):
        for j in range(i + 1, n):
            if wagons[i] > wagons[j]:
                # wagons[i] 在前但比 wagons[j] 大 → 這是一個逆序對
                count += 1

    return count


# ─────────────────────────────────────────────────────────────────────────────
def solve(input_text: str) -> str:
    """
    解析完整輸入，回傳所有測試資料的輸出字串。

    【輸入解析流程】
      1. 讀取第 1 行取得測試組數 N
      2. 每組資料讀兩行：
         a. 第 1 行：車廂數 L
         b. 第 2 行：L 個整數組成的排列
      3. 若 L == 0，逆序數為 0，直接輸出 0

    【輸出格式】
      "Optimal train swapping takes S swaps."

    參數：
        input_text (str): 完整輸入文字

    回傳：
        str: 完整輸出文字（各行以換行分隔）
    """
    # 過濾空白行後逐行解析
    lines = [l.strip() for l in input_text.strip().splitlines() if l.strip()]
    idx   = 0

    # 第一行：測試資料組數
    n_cases = int(lines[idx])
    idx += 1

    results = []    # 收集每組輸出

    for _ in range(n_cases):
        # 讀取車廂數 L
        L = int(lines[idx])
        idx += 1

        if L == 0:
            # 空列車：不需要任何交換
            swaps = 0
        else:
            # 讀取車廂排列（L 個整數）
            wagons = list(map(int, lines[idx].split()))
            idx += 1
            # 計算逆序數即為最少交換次數
            swaps = count_inversions(wagons)

        results.append(f"Optimal train swapping takes {swaps} swaps.")

    return "\n".join(results)


# ── 直接執行時：從 stdin 讀入，輸出至 stdout ─────────────────────────────────
if __name__ == "__main__":
    print(solve(sys.stdin.read()))
