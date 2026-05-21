# U01. 數論整合應用
# 整合 GCD / 線性方程 / 大數整除，對應 Week 12 解題題目

import math
import sys

# ── 應用 1：Beat the Spread!（UVA 10812）────────────────
# 題目概念：
# 給定兩隊分數的「總和 S」以及「差距 D」，
# 要反推出兩隊各自的分數。
#
# 假設：
# high = 較高分的隊伍分數
# low  = 較低分的隊伍分數
#
# 根據題目可得到兩個關係式：
# high + low = S
# high - low = D
#
# 將兩式相加：
# 2 * high = S + D
# high = (S + D) / 2
#
# 將兩式相減：
# 2 * low = S - D
# low = (S - D) / 2
#
# 但分數必須符合：
# 1. high 和 low 都必須是整數
# 2. low 不能小於 0
# 3. high 必須大於或等於 low
#
# 給定兩隊分數之和 S 與差 D，求各自得分
# high = (S+D)/2, low = (S-D)/2，必須是非負整數

def beat_the_spread(s: int, d: int):
    """
    回傳 (高分, 低分) 或 None（無解）
    條件：s+d 為偶數、高分 >= 低分 >= 0
    """
    # 如果 s + d 是奇數，代表 (s + d) / 2 不是整數。
    # 分數不可能是小數，所以這種情況一定無解。
    if (s + d) % 2 != 0:
        return None

    # 根據公式計算較高分。
    # 使用 // 是整數除法，因為前面已經確認 s + d 是偶數。
    high = (s + d) // 2

    # 根據公式計算較低分。
    # low = (總和 - 差距) / 2。
    low  = (s - d) // 2

    # 如果 low 小於 0，代表差距 D 比總分 S 還大。
    # 例如 S=20, D=40，這不可能成立。
    if low < 0:
        return None

    # 如果條件都合法，就回傳兩隊分數。
    # 題目通常要求輸出高分在前、低分在後。
    return (high, low)


# 印出應用 1 的標題，方便觀察測試結果。
print("=== Beat the Spread! ===")

# 測試資料：
# 每一組資料都是 (總分 S, 差距 D)。
tests = [(40, 20), (20, 40), (10, 10), (10, 11)]

# 逐一測試每組資料。
for s, d in tests:
    # 呼叫 beat_the_spread()，取得結果。
    # 如果有解，result 會是 (high, low)。
    # 如果無解，result 會是 None。
    result = beat_the_spread(s, d)

    # 如果 result 不是 None，代表成功算出兩隊分數。
    if result:
        print(f"S={s} D={d}  → {result[0]} {result[1]}")
    else:
        # 如果 result 是 None，代表此組資料無解。
        print(f"S={s} D={d}  → impossible")

# ── 應用 2：2 the 9s（UVA 10922）────────────────────────
# 題目概念：
# 判斷一個很大的數字是不是 9 的倍數，
# 並且計算它的 9-degree。
#
# 9 的倍數判斷法：
# 一個整數是否為 9 的倍數，可以看它「所有位數相加」後，
# 結果是否為 9 的倍數。
#
# 例如：
# 999 → 9 + 9 + 9 = 27
# 27  → 2 + 7 = 9
# 最後得到 9，所以 999 是 9 的倍數。
#
# 9-degree：
# 從原數開始，不斷把每一位數相加，
# 直到變成單位數 9 為止。
# 做了幾次位數相加，degree 就是多少。
#
# 因為題目可能給非常大的數字，
# 所以不能直接用 int 處理，改用字串 n_str 逐位讀取。

def nine_degree(n_str: str):
    """
    回傳 (是否為 9 的倍數, 深度) 或 (False, -1)
    n_str：數字字串（大數）
    """
    # current 用來記錄目前正在處理的數字字串。
    # 一開始就是原本輸入的 n_str。
    current = n_str

    # degree 用來記錄已經做了幾次「各位數相加」。
    degree = 0

    # 當 current 還不是最終結果時，就持續做位數相加。
    #
    # len(current) > 1：
    # 代表目前還是多位數，需要繼續加總位數。
    #
    # degree == 0 and len(current) == 1：
    # 這是為了處理一開始輸入就是單位數的情況。
    # 例如 n_str = "9"，雖然它一開始就是單位數，
    # 但題目仍然要判斷它是不是 9 的倍數，
    # 並且它的 9-degree 為 1。
    while len(current) > 1 or (degree == 0 and len(current) == 1):

        # 將 current 裡面的每一個字元轉成整數後加總。
        # 例如 current = "729"
        # sum(int(c) for c in current) = 7 + 2 + 9 = 18
        s = sum(int(c) for c in current)

        # 把加總結果轉回字串，方便下一輪繼續逐位相加。
        current = str(s)

        # 每做一次位數相加，degree 就增加 1。
        degree += 1

        # 如果 current 已經變成單位數，
        # 就可以停止繼續相加。
        if len(current) == 1:
            break

    # 如果最後結果是 "9"，
    # 代表原本的數字是 9 的倍數。
    if current == "9":
        return True, degree

    # 如果最後結果不是 9，
    # 代表不是 9 的倍數。
    # 回傳 False 和 -1 表示沒有 9-degree。
    return False, -1


# 印出應用 2 的標題。
print("\n=== 2 the 9s ===")

# 測試資料：
# 這些數字用字串表示，模擬大數輸入。
cases = ["9", "18", "999", "100", "729"]

# 逐一測試每個數字。
for n in cases:
    # 呼叫 nine_degree() 判斷是否為 9 的倍數，以及 degree 是多少。
    is_mult, deg = nine_degree(n)

    # 如果 is_mult 是 True，代表是 9 的倍數。
    if is_mult:
        print(f"9-degree of {n} is {deg}.")
    else:
        # 如果 is_mult 是 False，代表不是 9 的倍數。
        print(f"{n} is not a multiple of 9.")

# ── 應用 3：Can You Solve It?（UVA 10642）────────────────
# 題目概念：
# 題目給定一種特殊的座標排列方式，
# 每個座標 (x, y) 都會對應到一個位置編號。
#
# 只要能算出：
# 起點座標的位置編號
# 終點座標的位置編號
#
# 那麼兩點之間需要走的步數就是：
# abs(終點位置編號 - 起點位置編號)
#
# 這題的重點不是使用 BFS 或模擬走路，
# 而是找出座標和位置編號之間的數學公式。
#
# 螺旋座標到步數的映射
# 沿對角線排列，(x,y) 的座標值可以用公式計算

def position(x, y):
    """計算 (x,y) 在螺旋中的位置編號（從 0 開始）"""

    # 如果 x >= y，
    # 代表這個座標位於某一條對角線的一側，
    # 可以使用公式 x * x + x + y 計算位置。
    if x >= y:
        return x * x + x + y

    # 如果 x < y，
    # 代表這個座標位於另一側，
    # 可以使用公式 y * y + x 計算位置。
    else:
        return y * y + x

def steps(x1, y1, x2, y2):
    """從 (x1,y1) 到 (x2,y2) 的步數"""

    # 先分別計算起點與終點的位置編號。
    # 再用 abs() 取絕對值，避免結果是負數。
    #
    # 因為步數只看距離差，不管方向，
    # 所以使用 abs() 是必要的。
    return abs(position(x2, y2) - position(x1, y1))


# 印出應用 3 的標題。
print("\n=== Can You Solve It? ===")

# 測試資料：
# 每一組都是：
# (起點 x1, 起點 y1, 終點 x2, 終點 y2)
cases = [(0, 3, 3, 0), (0, 0, 2, 2), (1, 1, 2, 3)]

# 逐一計算每組座標需要的步數。
for x1, y1, x2, y2 in cases:
    # 呼叫 steps() 計算從起點到終點的位置差。
    s = steps(x1, y1, x2, y2)

    # 印出座標移動與對應步數。
    print(f"({x1},{y1}) → ({x2},{y2})  步數 = {s}")