# U01. 數論整合應用
# 整合 GCD / 線性方程 / 大數整除，對應 Week 12 解題題目

import math
import sys

# ── 應用 1：Beat the Spread! (UVA 10812) ────────────────
# 給定兩隊分數之和 S 與差 D，求各自得分。
# 假設兩隊得分分別為 a 與 b (a >= b)：
# a + b = S
# a - b = D
# 解聯立方程式可得：
# a = (S + D) / 2
# b = (S - D) / 2
# 條件：S >= D 且 (S + D) 必須是偶數（即 a, b 必須為非負整數）

def beat_the_spread(s: int, d: int):
    """
    根據分數和與分數差計算兩隊得分。
    
    參數:
        s: 兩隊分數之和 (Sum)
        d: 兩隊分數之差 (Difference)
        
    回傳:
        (高分, 低分) 的元組，若無解則回傳 None。
    """
    # 如果和比差小，或者兩者相加不是偶數（無法整除），則不可能有整數解
    if s < d or (s + d) % 2 != 0:
        return None
    
    high = (s + d) // 2
    low  = (s - d) // 2
    
    return (high, low)


print("=== Beat the Spread! ===")
# 測試案例：(和, 差)
tests = [(40, 20), (20, 40), (10, 10), (10, 11)]
for s, d in tests:
    result = beat_the_spread(s, d)
    if result:
        print(f"S={s} D={d}  → 得分：{result[0]} {result[1]}")
    else:
        print(f"S={s} D={d}  → 無法達成 (impossible)")

# ── 應用 2：2 the 9s (UVA 10922) ────────────────────────
# 判斷一個大數是否為 9 的倍數，並計算其「9-degree」。
# 一個數是 9 的倍數，若且為若其各位數字之和也是 9 的倍數。
# 9-degree 定義為：重複執行「求各位數字之和」直到結果只有一位數所需次數。

def nine_degree(n_str: str):
    """
    判斷數字字串是否為 9 的倍數，並計算其 9-degree。
    
    參數:
        n_str: 數字字串（處理大數）
        
    回傳:
        (是否為 9 的倍數, 9-degree 深度)
    """
    # 原始數字如果是 9，其 degree 為 1
    current = n_str
    degree = 0
    
    # 如果數字字串本身就是 "0"，通常題目會有特殊處理，這裡假設為一般正整數
    # 根據 UVA 10922，只要總和是 9 的倍數就是 True
    
    while True:
        # 計算各位數字之和
        s = sum(int(c) for c in current)
        current = str(s)
        degree += 1
        
        # 如果結果已經變成個位數，停止迭代
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
        print(f"數字 {n} 的 9-degree 為 {deg}。")
    else:
        print(f"數字 {n} 不是 9 的倍數。")

# ── 應用 3：Can You Solve It? (UVA 10642) ────────────────
# 座標映射問題：將二維平面上的點 (x, y) 映射到一個序列編號。
# 題目通常是沿著斜線 (x+y = k) 進行編號。

def position(x, y):
    """
    計算 (x, y) 在特定排序規則下的位置編號（從 0 開始）。
    
    註：此處實作採用的是一種基於平方的螺旋或階層映射邏輯。
    若對應 UVA 10642 原始題目，公式通常為：
    n = x + y
    pos = (n * (n + 1)) // 2 + x
    """
    # 目前程式碼中的邏輯：
    if x >= y:
        return x * x + x + y
    else:
        return y * y + x

def steps(x1, y1, x2, y2):
    """
    計算從點 1 到點 2 需要走的步數（位置編號之差）。
    """
    return abs(position(x2, y2) - position(x1, y1))


print("\n=== Can You Solve It? ===")
cases = [(0, 3, 3, 0), (0, 0, 2, 2), (1, 1, 2, 3)]
for x1, y1, x2, y2 in cases:
    s = steps(x1, y1, x2, y2)
    print(f"從 ({x1},{y1}) 到 ({x2},{y2}) 的步數 = {s}")
