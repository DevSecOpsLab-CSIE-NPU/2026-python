"""
UVA 299 / ZeroJudge e561 - Train Swapping 簡易版
=================================================
【與 q299.py 的差異】
  q299.py     → 自己實作 count_inversions()，概念清晰但需理解逆序數
  q299-easy.py → 直接模擬 Bubble Sort，每次真正交換，並計算交換次數

【核心簡化想法】
  把 Bubble Sort 直接寫出來：
    - 掃描相鄰元素，若前者 > 後者就交換，並把 count 加 1
    - Bubble Sort 跑完之後，count 就是答案
  不需要理解「逆序數」這個抽象概念，直接看程式就知道在做什麼。

  L ≤ 50，Bubble Sort O(L²) 完全沒問題。
"""

import sys


# ─────────────────────────────────────────────────────────────────────────────
def min_swaps(wagons: list) -> int:
    """
    用 Bubble Sort 模擬，計算把 wagons 排成升序所需的最少相鄰交換次數。

    【做法說明】
      Bubble Sort 的邏輯：
        外層迴圈跑 L 輪（每輪保證最大值「浮」到最右邊）
        內層迴圈比較相鄰兩個元素，若前者 > 後者就交換

      每次真正發生的交換，就計數 +1。
      全部跑完後，count 就是最少交換次數。

    【為什麼這樣就對？】
      Bubble Sort 每次只交換相鄰元素，且只在「必要」時交換（前者更大才換），
      所以每次交換都消除一個逆序對，不會多也不會少。
      總交換次數 = 逆序對數 = 最短路徑。

    參數：
        wagons (list): 車廂排列（會被原地排序，若不想改原資料請先複製）

    回傳：
        int: 最少交換次數
    """
    arr   = wagons[:]   # 複製一份，避免修改呼叫者的資料
    count = 0           # 交換次數計數器
    n     = len(arr)

    # Bubble Sort：外層跑 n 輪
    for i in range(n):
        # 內層：把最大的未排序元素「浮」到右側
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # 相鄰元素順序錯誤 → 交換
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1   # 每次交換計數加 1

    return count


# ─────────────────────────────────────────────────────────────────────────────
def solve(input_text: str) -> str:
    """
    讀入完整輸入，輸出每組測試資料的最少交換次數。

    【輸入格式】
      第 1 行：N（測試組數）
      每組資料兩行：
        行 1：L（車廂數）
        行 2：L 個整數（車廂當前排列）

    【輸出格式】
      每組一行："Optimal train swapping takes S swaps."

    參數：
        input_text (str): 完整輸入文字

    回傳：
        str: 完整輸出文字
    """
    lines = [l.strip() for l in input_text.strip().splitlines() if l.strip()]
    idx   = 0

    n_cases = int(lines[idx])   # 第一行：測試組數
    idx += 1

    results = []

    for _ in range(n_cases):
        L = int(lines[idx])     # 車廂數量
        idx += 1

        if L == 0:
            swaps = 0           # 空列車：0 次交換
        else:
            wagons = list(map(int, lines[idx].split()))  # 讀取排列
            idx += 1
            swaps = min_swaps(wagons)   # Bubble Sort 計算交換次數

        results.append(f"Optimal train swapping takes {swaps} swaps.")

    return "\n".join(results)


# ── 直接執行時：從 stdin 讀入，輸出至 stdout ─────────────────────────────────
if __name__ == "__main__":
    print(solve(sys.stdin.read()))
