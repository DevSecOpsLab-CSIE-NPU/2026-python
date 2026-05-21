# U01. 數論整合應用
# 整合 GCD / 線性方程 / 大數整除，對應 Week 12 解題題目
# 這是一個關於基礎數論與數學公式應用的程式碼，包含了三道 UVA 解題平台的經典題目。

import math
import sys

# ── 應用 1：Beat the Spread!（UVA 10812）────────────────
# 題目說明：美式足球比賽中，我們知道兩隊「分數之和 (S)」與「分數之差 (D)」。
# 我們的任務是算出兩隊各自的得分。
# 數學原理：假設高分為 high，低分為 low
# high + low = S
# high - low = D
# 將兩式相加可得 2 * high = S + D，所以 high = (S + D) / 2
# 將兩式相減可得 2 * low = S - D，所以 low = (S - D) / 2
# 注意條件：因為分數必須是「非負整數」，所以 (S + D) 必須是偶數（才能整除 2），且 low 不能小於 0。

def beat_the_spread(s: int, d: int):
    """
    計算並回傳 (高分, 低分) 的元組，如果條件不符（無解）則回傳 None。
    
    參數：
        s (int): 兩隊分數之總和 (Sum)
        d (int): 兩隊分數之差值 (Difference)
        
    條件：
        1. s + d 必須為偶數（代表能被 2 整除，因為分數不會是小數）
        2. 低分 (low) 必須大於等於 0
    """
    # 檢查總和與差值相加是否為偶數，若不是代表會出現小數，不符合分數定義
    if (s + d) % 2 != 0:
        return None
    
    # 利用公式計算高分與低分，使用 // 確保結果為整數
    high = (s + d) // 2
    low  = (s - d) // 2
    
    # 檢查低分是否為負數，若為負數則代表輸入的差值大於總和，這是不合理的狀況
    if low < 0:
        return None
        
    return (high, low)

# 測試 "Beat the Spread!" 功能
print("=== Beat the Spread! ===")
# 測試資料：格式為 (S, D)
tests = [(40, 20), (20, 40), (10, 10), (10, 11)]
for s, d in tests:
    result = beat_the_spread(s, d)
    if result:
        # 如果有解，印出計算出來的高分與低分
        print(f"S={s} D={d}  → {result[0]} {result[1]}")
    else:
        # 如果無解，印出 impossible (不可能)
        print(f"S={s} D={d}  → impossible")


# ── 應用 2：2 the 9s（UVA 10922）────────────────────────
# 題目說明：判斷一個數字（可能非常巨大）是否為 9 的倍數。
# 數學原理：一個數字如果是 9 的倍數，其「各個位數數字相加的總和」也會是 9 的倍數。
# 所謂的「9-degree (9 的深度)」，是指重複執行「各位數相加」這個動作，直到結果剩下個位數為止的「執行次數」。
# 如果最後結果是 9，則代表原數字為 9 的倍數。

def nine_degree(n_str: str):
    """
    判斷字串表示的數字是否為 9 的倍數，並計算其 9-degree (深度)。
    回傳格式：(是否為 9 的倍數, 深度)，若不是則回傳 (False, -1)。
    
    參數：
        n_str (str): 要判斷的數字字串（因為可能會超過整數上限，所以用字串處理大數）
    """
    current = n_str  # 當前正在處理的數字字串
    degree = 0       # 記錄執行相加的深度（次數）
    
    # 迴圈條件：當數字超過一位數，或者一開始就是只有一位數時進行判斷
    while len(current) > 1 or (degree == 0 and len(current) == 1):
        # 將字串中的每一個字元轉換回整數並加總
        s = sum(int(c) for c in current)
        # 將總和轉回字串，準備進行下一輪判斷
        current = str(s)
        # 每相加一次，深度就加 1
        degree += 1
        
        # 如果相加後的結果已經縮減為一位數，就可以結束迴圈
        if len(current) == 1:
            break
            
    # 判斷最後收斂的一位數字是否為 9
    if current == "9":
        return True, degree
    # 如果不是 9，代表原數字不是 9 的倍數
    return False, -1

# 測試 "2 the 9s" 功能
print("\n=== 2 the 9s ===")
# 測試資料：各種不同的數字字串
cases = ["9", "18", "999", "100", "729"]
for n in cases:
    is_mult, deg = nine_degree(n)
    if is_mult:
        # 如果是 9 的倍數，印出其深度
        print(f"9-degree of {n} is {deg}.")
    else:
        # 如果不是，印出不是 9 的倍數
        print(f"{n} is not a multiple of 9.")


# ── 應用 3：Can You Solve It?（UVA 10642）────────────────
# 題目說明：在一個無限大的二維平面上，座標點按照特定的螺旋或折線路徑進行連續編號。
# 我們需要計算從起點座標 (x1, y1) 移動到終點座標 (x2, y2) 需要走多少步。
# 原理：直接計算目標座標在整個路徑上的絕對「位置編號」，然後將兩個位置編號相減取絕對值。

def position(x, y):
    """
    計算二維座標 (x,y) 在螺旋路徑上的絕對位置編號（從 0 開始計算）。
    這裡依據題目給定的數列規律，推導出公式來直接計算出編號，避免使用迴圈慢慢數。
    
    參數：
        x (int): X 座標
        y (int): Y 座標
    """
    # 根據 X 與 Y 的大小關係決定計算公式（此為螺旋數字方陣推導之公式）
    if x >= y:
        return x * x + x + y
    else:
        return y * y + x

def steps(x1, y1, x2, y2):
    """
    計算兩座標點在路徑上的步數距離。
    
    參數：
        x1, y1: 起點座標
        x2, y2: 終點座標
    """
    # 取得兩點的絕對位置編號，相減後取絕對值 (abs) 即可得到所需步數
    return abs(position(x2, y2) - position(x1, y1))

# 測試 "Can You Solve It?" 功能
print("\n=== Can You Solve It? ===")
# 測試資料：格式為 (x1, y1, x2, y2)
cases = [(0, 3, 3, 0), (0, 0, 2, 2), (1, 1, 2, 3)]
for x1, y1, x2, y2 in cases:
    s = steps(x1, y1, x2, y2)
    print(f"({x1},{y1}) → ({x2},{y2})  步數 = {s}")