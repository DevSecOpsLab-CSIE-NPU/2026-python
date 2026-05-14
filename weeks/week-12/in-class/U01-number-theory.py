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
    if (s + d) % 2 != 0:
        return None
    high = (s + d) // 2
    low  = (s - d) // 2
    if low < 0:
        return None
    return (high, low)


print("=== Beat the Spread! ===")
tests = [(40, 20), (20, 40), (10, 10), (10, 11)]
for s, d in tests:
    result = beat_the_spread(s, d)
    if result:
        print(f"S={s} D={d}  → {result[0]} {result[1]}")
    else:
        print(f"S={s} D={d}  → impossible")

# ── 應用 2：2 the 9s（UVA 10922）────────────────────────
def nine_degree(n_str: str):
    """
    回傳 (是否為 9 的倍數, 深度) 或 (False, -1)
    n_str：數字字串（大數）
    """
    current = n_str
    degree = 0
    while len(current) > 1 or (degree == 0 and len(current) == 1):
        s = sum(int(c) for c in current)
        current = str(s)
        degree += 1
        if len(current) == 1:
            break
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
# 螺旋座標到步數的映射
# 沿對角線排列，(x,y) 的座標值可以用公式計算

def position(x, y):
    """計算 (x,y) 在螺旋中的位置編號（從 0 開始）"""
    if x >= y:
        return x * x + x + y
    else:
        return y * y + x

def steps(x1, y1, x2, y2):
    """從 (x1,y1) 到 (x2,y2) 的步數"""
    return abs(position(x2, y2) - position(x1, y1))


print("\n=== Can You Solve It? ===")
cases = [(0, 3, 3, 0), (0, 0, 2, 2), (1, 1, 2, 3)]
for x1, y1, x2, y2 in cases:
    s = steps(x1, y1, x2, y2)
    print(f"({x1},{y1}) → ({x2},{y2})  步數 = {s}")
