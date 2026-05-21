"""
U01. 數論整合應用（繁體中文詳細註解版）

此檔案包含三個典型的數論應用題目，對應 UVA 練習題：
  1) Beat the Spread! (UVA 10812)
  2) 2 the 9s       (UVA 10922)
  3) Can You Solve It? (UVA 10642)

註解說明的目標：每個函式加入步驟性說明、邊界條件處理，方便教學與閱讀。

作者：課堂範例，Week 12 數論整合
"""

import math
import sys


# ---------------------------------------------------------------------------
# 應用 1：Beat the Spread!（UVA 10812）
# 題意：給定兩隊分數的總和 S 與差 D，求出兩隊各自的分數（整數且非負）
# 數學推導：若高分為 H、低分為 L，則
#   H + L = S
#   H - L = D
# 解得：H = (S + D) / 2,  L = (S - D) / 2
# 必須注意的條件：
#   1) S + D 必須為偶數（才能整除 2 得到整數分數）
#   2) L >= 0（低分不能為負）
# 若不滿足上述條件即無解 (impossible)
# ---------------------------------------------------------------------------

def beat_the_spread(s: int, d: int):
    """
    計算兩隊分數（高分, 低分）或回傳 None 表示無解。

    參數：
        s: int - 兩隊分數總和 S
        d: int - 兩隊分數差 D

    回傳：
        (high, low) 或 None

    內部邏輯：
    1. 檢查 (S + D) 是否為偶數：若為奇數則括號除以 2 後不是整數，無解。
    2. 計算 high = (S + D) // 2
    3. 計算 low  = (S - D) // 2
    4. 檢查 low 是否為非負：若 low < 0 則無解。
    """
    # 若 S + D 為奇數，則不能整除 2 -> 無整數解
    if (s + d) % 2 != 0:
        return None

    # 整除後得到高分與低分（整數除法）
    high = (s + d) // 2
    low = (s - d) // 2

    # 低分不得為負數，否則不符合題意
    if low < 0:
        return None

    return (high, low)


if __name__ == "__main__":
    # 簡單測試範例
    print("=== Beat the Spread! ===")
    tests = [(40, 20), (20, 40), (10, 10), (10, 11)]
    for s, d in tests:
        result = beat_the_spread(s, d)
        if result:
            print(f"S={s} D={d}  → {result[0]} {result[1]}")
        else:
            print(f"S={s} D={d}  → impossible")


# ---------------------------------------------------------------------------
# 應用 2：2 the 9s（UVA 10922）
# 題意：判斷一個（可能很大的）數字是否為 9 的倍數，並計算其 9-degree。
# 9-degree 定義：對數位和（digit sum）反覆做求和操作，直到剩下一位數為止，
# 若最後得到 9，則該數是 9 的倍數；而進行求和的次數即為其 9-degree。
# 例如：999 → 9+9+9=27 → 2+7=9，degree = 2
# 注意：輸入可能是非常大的數字，以字串形式處理較安全，避免整數溢位。
# ---------------------------------------------------------------------------


def nine_degree(n_str: str):
    """
    判斷 n_str 是否為 9 的倍數，並回傳其 9-degree。

    參數：
        n_str: 數字的字串表示（例如 '999999999999'）

    回傳：
        (True, degree) 若為 9 的倍數，degree 為求和次數；
        (False, -1)   若不是 9 的倍數。

    演算法說明：
    - 以字串逐位取數相加得到新的和（仍以字串處理），重複直到長度為 1
    - 每次求和都將 degree 加 1
    - 最後檢查剩下的一位是否為 '9'
    """
    current = n_str
    degree = 0

    # 當字串長度大於 1 時持續運算；特別情況：若初始字串長度就是 1（例如 '9'），
    # 仍希望 degree 能被正確計為 1（題目通常將單位 9 的 degree 視為 1）
    while len(current) > 1 or (degree == 0 and len(current) == 1):
        # 將目前字串的每一位數字相加
        s = sum(int(c) for c in current)

        # 更新 current 為新的字串表示，並增加 degree
        current = str(s)
        degree += 1

        # 若已縮短為單一位數則跳出（下一輪不再需要再求和）
        if len(current) == 1:
            break

    # 若最後結果是 '9'，表示原數為 9 的倍數
    if current == "9":
        return True, degree
    return False, -1


if __name__ == "__main__":
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
# 題意簡述：在一個按對角線延伸的整數螺旋中，每個座標 (x, y) 對應一唯一的編號，
# 給定兩個座標，計算它們之間的步數差（可用位置編號的差值來取得）。
# 下面提供一個能直接計算 (x,y) 對應編號的函式，與用編號差求步數的函式。
# 公式來源：觀察螺旋的組織方式，可以推導出分支情況（x >= y 與 x < y）對應的編號表達式。
# ---------------------------------------------------------------------------


def position(x, y):
    """
    計算座標 (x, y) 在螺旋編號中的位置（從 0 開始）。

    推導說明（簡要）：
    - 若 x >= y，代表該點位於某一條右側或下側的分支，可用 x 的平方與偏移量表示：x*x + x + y
    - 若 x < y，則位於上或左的分支，使用 y 的平方加上 x 作為編號：y*y + x

    這些表達式是根據觀察螺旋圖形與對角線分層後得到的封閉式結果。
    """
    if x >= y:
        return x * x + x + y
    else:
        return y * y + x


def steps(x1, y1, x2, y2):
    """
    計算 (x1,y1) 與 (x2,y2) 兩點在編號（position）上的差，取絕對值即為步數。

    注意：此處並非計算曼哈頓距離或歐氏距離，而是題目定義的「編號差值」。
    """
    return abs(position(x2, y2) - position(x1, y1))


if __name__ == "__main__":
    print("\n=== Can You Solve It? ===")
    cases = [(0, 3, 3, 0), (0, 0, 2, 2), (1, 1, 2, 3)]
    for x1, y1, x2, y2 in cases:
        s = steps(x1, y1, x2, y2)
        print(f"({x1},{y1}) → ({x2},{y2})  步數 = {s}")
