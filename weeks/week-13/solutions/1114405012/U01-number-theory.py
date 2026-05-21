# U01. 數論整合應用
# 本檔案包含數論常見應用題的範例，重點示範：
#  - 使用整數運算解決分數/差值問題
#  - 處理大數字串以判定是否為 9 的倍數（及其 "degree"）
#  - 螺旋編號映射（座標 ↔ 序號）及距離計算

import math
import sys

# ---------------------------------------------------------------------------
# 應用 1：Beat the Spread!（UVA 10812）
# 題意：已知兩隊分數的總和 S 與 差 D，求兩隊的個別分數（非負整數）
# 推導：假設較高分為 H，較低分為 L，則
#   H + L = S
#   H - L = D
# 解得：H = (S + D) / 2,  L = (S - D) / 2
# 必要條件：S+D 與 S-D 均為偶數（等同於 S 與 D 同奇偶），且 L >= 0
# 若不滿足必要條件，該題無解（印出 impossible）
def beat_the_spread(s: int, d: int):
    """
    回傳 (high, low) 或 None（若無解）

    參數：
      s -- 兩隊分數和 S（整數）
      d -- 兩隊分數差 D（整數）

    回傳值：
      (high, low) 當有一組合理的解；否則回傳 None

    注意：此函式以整數除法處理，並檢查負數與奇偶性以判別是否無解。
    """
    # 若 S+D 為奇數，則無法整除 2 → 無解
    if (s + d) % 2 != 0:
        return None
    # 利用整數除法取得 H 與 L（已確保可被 2 整除）
    high = (s + d) // 2
    low = (s - d) // 2
    # 低分不能為負數，否則無解（比賽分數為非負整數）
    if low < 0:
        return None
    return (high, low)


print("=== Beat the Spread! ===")
tests = [(40, 20), (20, 40), (10, 10), (10, 11)]
for s, d in tests:
    result = beat_the_spread(s, d)
    if result:
        # 輸出格式：高分 低分
        print(f"S={s} D={d}  → {result[0]} {result[1]}")
    else:
        print(f"S={s} D={d}  → impossible")


# ---------------------------------------------------------------------------
# 應用 2：2 the 9s（UVA 10922）
# 題意重點：給一個（可能很大）整數字串，判斷是否為 9 的倍數，
# 並計算其 "9-degree"（不斷把數位和縮減為一位數直到停止的次數；若最終為 9，則為 9 的倍數）
# 例如：999 → 27 → 9，degree = 3（999、27、9 三次縮減）
def nine_degree(n_str: str):
    """
    檢查字串 `n_str` 是否為 9 的倍數，並回傳其 degree。

    參數：
      n_str -- 表示整數的字串（可能超過內建整數範圍）

    回傳：
      (True, degree) 若最終縮減為 9；否則 (False, -1)

    實作說明：
      - 利用數位和 (digit sum) 的性質：一數若為 9 的倍數，則其數位和亦為 9 的倍數。
      - 把數字表示為字串，在每次迴圈計算各位數總和，轉回字串繼續處理。
      - degree 代表縮減步數（包含原始字串的第一次縮減）。
    """
    current = n_str
    degree = 0
    # 迴圈直到 current 縮減為 1 位數（或剛開始即為 1 位數）
    while len(current) > 1 or (degree == 0 and len(current) == 1):
        # 計算所有位數的和（將字元轉為整數相加）
        s = sum(int(c) for c in current)
        current = str(s)
        degree += 1
        # 若已為一位數，跳出迴圈（避免無限迴圈）
        if len(current) == 1:
            break
    # 若最終的一位數為 '9'，代表原數為 9 的倍數
    if current == "9":
        return True, degree
    return False, -1


print("\n=== 2 the 9s ===")
cases = ["9", "18", "999", "100", "729"]
for n in cases:
    is_mult, deg = nine_degree(n)
    if is_mult:
        print(f"9-degree of {n} is {deg}.")
    else:
        print(f"{n} is not a multiple of 9.")


# ---------------------------------------------------------------------------
# 應用 3：Can You Solve It?（UVA 10642）
# 題意：在一個特殊排列的無限格子（沿對角線成螺旋/斜列排列）上，給定座標 (x,y)，
# 可用公式直接計算該座標對應的序號（從 0 開始編號）。
# 公式由觀察排列方式得出：對於 x >= y 與 x < y 兩種情況，序號計算略有不同。
# 這裡實作 position() 取得座標對應的編號，steps() 回傳兩座標之間的絕對差值（步數）。
def position(x, y):
    """計算座標 (x, y) 在螺旋/斜列編號中的序號（從 0 開始）。

    觀察規律可得：
      - 若 x >= y，則該位置落在以 x 為主的區塊，編號為 x*x + x + y
      - 若 x < y，則落在以 y 為主的區塊，編號為 y*y + x

    這個公式可由題目給定的圖形或數值範例推導出來。
    """
    if x >= y:
        return x * x + x + y
    else:
        return y * y + x


def steps(x1, y1, x2, y2):
    """計算從 (x1,y1) 到 (x2,y2) 的步數（兩者對應編號的絕對差）。"""
    return abs(position(x2, y2) - position(x1, y1))


print("\n=== Can You Solve It? ===")
cases = [(0, 3, 3, 0), (0, 0, 2, 2), (1, 1, 2, 3)]
for x1, y1, x2, y2 in cases:
    s = steps(x1, y1, x2, y2)
    print(f"({x1},{y1}) → ({x2},{y2})  步數 = {s}")
