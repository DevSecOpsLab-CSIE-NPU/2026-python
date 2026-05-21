# U01. 數論整合應用
# 整合 GCD / 線性方程 / 大數整除，對應 Week 12 解題題目

import math
import sys

# ── 應用 1：Beat the Spread!（UVA 10812）────────────────
# 給定兩隊分數之和 S 與差 D，求各自得分
# high = (S+D)/2, low = (S-D)/2，必須是非負整數

def beat_the_spread(s: int, d: int):
    """
    回傳 (高分, 低分) 或 None（無解）
    條件：s+d 為偶數、高分 >= 低分 >= 0
    """
    # 若和 (s) 與差 (d) 的相加不是偶數，則除以 2 會有小數，不符合分數需為整數的條件
    if (s + d) % 2 != 0:
        return None
    
    # 根據聯立方程式 s = high + low, d = high - low，解出兩隊得分
    high = (s + d) // 2
    low  = (s - d) // 2
    
    # 題意要求分數不得為負數，若低分算出來為負，代表題目給的差大於和，不合邏輯
    if low < 0:
        return None
    return (high, low)


print("=== Beat the Spread! ===")
tests = [(40, 20), (20, 40), (10, 10), (10, 11)]
for s, d in tests:
    result = beat_the_spread(s, d)
    if result:
        # 若有解，依序印出高分與低分
        print(f"S={s} D={d}  → {result[0]} {result[1]}")
    else:
        # 若無解，輸出 impossible
        print(f"S={s} D={d}  → impossible")

# ── 應用 2：2 the 9s（UVA 10922）────────────────────────
def nine_degree(n_str: str):
    """
    回傳 (是否為 9 的倍數, 深度) 或 (False, -1)
    n_str：數字字串（大數）
    """
    current = n_str
    degree = 0
    
    # 當數字長度超過 1，或尚未做過任何位數和運算時（degree == 0 且長度為 1），進入迴圈
    while len(current) > 1 or (degree == 0 and len(current) == 1):
        # 將數字字串的每一個字元轉為整數後相加 (即位數和)
        s = sum(int(c) for c in current)
        current = str(s)  # 將計算結果轉回字串，供下次運算使用
        degree += 1       # 記錄疊加計算的層次次數 (加 1)
        
        # 如果相加後的結果已經縮減為個位數，則可提早結束運算
        if len(current) == 1:
            break
            
    # 最後留下來的個位數若是 9，代表原數字字串是 9 的倍數
    if current == "9":
        return True, degree
    # 反之則不是 9 的倍數
    return False, -1


print("\n=== 2 the 9s ===")
cases = ["9", "18", "999", "100", "729"]
for n in cases:
    is_mult, deg = nine_degree(n)
    if is_mult:
        # 是 9 的倍數時，印出轉換成單一數字 9 所需要的層數 (9-degree)
        print(f"9-degree of {n} is {deg}.")
    else:
        # 非 9 的倍數時的輸出格式
        print(f"{n} is not a multiple of 9.")

# ── 應用 3：Can You Solve It?（UVA 10642）────────────────
# 螺旋座標到步數的映射
# 沿對角線排列，(x,y) 的座標值可以用公式計算

def position(x, y):
    """計算 (x,y) 在螺旋中的位置編號（從 0 開始）"""
    # 判斷點座標是落在右下半部（x >= y）還是左上半部（x < y），帶入對應公式
    if x >= y:
        return x * x + x + y
    else:
        return y * y + x

def steps(x1, y1, x2, y2):
    """從 (x1,y1) 到 (x2,y2) 的步數"""
    # 位置編號的差值絕對值，就是兩點之間需要移動的步數
    return abs(position(x2, y2) - position(x1, y1))


print("\n=== Can You Solve It? ===")
cases = [(0, 3, 3, 0), (0, 0, 2, 2), (1, 1, 2, 3)]
for x1, y1, x2, y2 in cases:
    s = steps(x1, y1, x2, y2)
    # 顯示從起點到終點所需走過的總步數
    print(f"({x1},{y1}) → ({x2},{y2})  步數 = {s}")
