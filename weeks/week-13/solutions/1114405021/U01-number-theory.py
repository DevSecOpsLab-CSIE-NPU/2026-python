# U01. 數論整合應用
# 本檔示範三個常見的數論/整數運算題型：
# 1) Beat the Spread (利用和與差求兩個整數)
# 2) 2 the 9s (判斷是否為 9 的倍數並計算 9-degree)
# 3) Can You Solve It? (在對角線排列的螺旋座標系，計算位置差)
# 註：程式碼側重於演算法說明與可讀性，輸出為範例測試結果。

import math
import sys

# ── 應用 1：Beat the Spread!（UVA 10812）────────────────
# 題意：給定兩隊分數之和 S 與差 D，要找出兩隊各自分數。
# 推導：令高分為 h，低分為 l，則 h + l = S，h - l = D。
# 由此可得 h = (S + D) / 2，l = (S - D) / 2。
# 解的必要條件：S 與 D 同奇偶（以免分數為小數），且 l >= 0（分數不能為負）。

def beat_the_spread(s: int, d: int):
    """
    回傳一對整數 (high, low) 表示高分與低分，或回傳 None 表示無解。

    參數：
    - s (int): 兩隊分數的總和 S。
    - d (int): 兩隊分數的差 D（假設為非負，代表 h - l）。

    驗證步驟：
    1. 檢查 S+D 是否為偶數：若為奇數，(S+D)/2 不是整數，無解。
    2. 計算 high = (S+D)//2、low = (S-D)//2（整數除法），並檢查 low 是否為非負。
    3. 若以上條件都滿足，回傳 (high, low)，否則回傳 None。
    """
    # 若 S+D 為奇數，必為小數，故無解
    if (s + d) % 2 != 0:
        return None
    high = (s + d) // 2
    low = (s - d) // 2
    # 低分不得為負數（分數不可為負）
    if low < 0:
        return None
    return (high, low)


print("=== Beat the Spread! ===")
tests = [(40, 20), (20, 40), (10, 10), (10, 11)]
for s, d in tests:
    result = beat_the_spread(s, d)
    if result:
        # 成功找到整數解：印出高分與低分
        print(f"S={s} D={d}  → {result[0]} {result[1]}")
    else:
        # 無解情況（奇偶不合或低分為負）
        print(f"S={s} D={d}  → impossible")


# ── 應用 2：2 the 9s（UVA 10922）────────────────────────
# 題意：判斷一串位數很長的數是否為 9 的倍數，若是則求其 "9-degree"。
# 定義：將數字各位相加成為新數，重複此過程直到剩下一位數字；若最後結果為 9，
# 則原數是 9 的倍數，9-degree 為需要做的加總次數。

def nine_degree(n_str: str):
    """
    判斷數字字串 `n_str` 是否為 9 的倍數，並回傳其 9-degree。

    回傳值：
    - (True, degree) : 如果是 9 的倍數，degree 為進行各位數字和的次數（正整數）。
    - (False, -1)    : 如果不是 9 的倍數。

    注意：輸入以字串形式傳入以支援超大數字（超過內建整數範圍）。
    演算法複雜度：每次將位數縮短，總操作數與位數長度成比例。
    """
    current = n_str
    degree = 0
    # 迴圈目的：不斷把每一位數相加，直到剩下一位數字為止
    while len(current) > 1 or (degree == 0 and len(current) == 1):
        s = sum(int(c) for c in current)
        current = str(s)
        degree += 1
        # 若已縮減成一位數則跳出（下一步可檢查是否為 9）
        if len(current) == 1:
            break
    # 若最後剩下的數字為 '9'，代表原數為 9 的倍數
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


# ── 應用 3：Can You Solve It?（UVA 10642）────────────────
# 題意：在一個依對角線排列的二維格點上，每個座標 (x,y) 都對應到一個唯一的編號。
# 我們要能快速根據 (x,y) 計算該編號，並求兩點之間的步數差。
# 對角線排列規則可由觀察得到公式：若 x >= y，位置可寫成 x*x + x + y；否則為 y*y + x。

def position(x, y):
    """計算格點 (x, y) 在螺旋/對角線編號系中的位置編號（從 0 開始）。

    公式說明：
    - 當 x >= y 時，該點落在由 x 對角延伸出的區段，位置可用 x*x + x + y 計算。
    - 否則該點落在 y 對角延伸出的區段，位置可用 y*y + x 計算。
    以上公式可由觀察對角線分層與填數順序推導而來。
    """
    if x >= y:
        return x * x + x + y
    else:
        return y * y + x

def steps(x1, y1, x2, y2):
    """計算從 (x1,y1) 到 (x2,y2) 的步數（位置編號差的絕對值）。"""
    return abs(position(x2, y2) - position(x1, y1))


print("\n=== Can You Solve It? ===")
cases = [(0, 3, 3, 0), (0, 0, 2, 2), (1, 1, 2, 3)]
for x1, y1, x2, y2 in cases:
    s = steps(x1, y1, x2, y2)
    print(f"({x1},{y1}) → ({x2},{y2})  步數 = {s}")
