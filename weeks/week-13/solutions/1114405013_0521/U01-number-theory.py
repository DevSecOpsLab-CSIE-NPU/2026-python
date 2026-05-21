# U01. 數論整合應用
# 整合 GCD / 線性方程 / 大數整除，對應 Week 12 解題題目

# 這一個檔案整合 Week 12 數論題目的常見套路：
# - 代數公式（Beat the Spread!）
# - 大數字串運算（2 the 9s）
# - 螺旋座標映射（Can You Solve It?）

# ── 應用 1：Beat the Spread!（UVA 10812）────────────────
# 給定兩隊分數之和 S 與差 D，求兩隊各自得分。
# 由 high+low=S、high-low=D 可得到：
#   high = (S+D)/2
#   low  = (S-D)/2
# 這兩個值必須是整數，且 low >= 0 才有意義。

def beat_the_spread(s: int, d: int):
    """
    回傳 (高分, 低分) 或 None（無解）。

    參數：
      s - 兩隊分數的總和
      d - 兩隊分數的差

    條件：
      1. s + d 必須是偶數，才能整除 2
      2. 低分不能為負數
    """
    # 如果 s+d 是奇數，(s+d)/2 就不是整數
    if (s + d) % 2 != 0:
        return None

    high = (s + d) // 2
    low  = (s - d) // 2

    # 如果 low < 0，代表沒有合法解
    if low < 0:
        return None

    return (high, low)


print("=== Beat the Spread! ===")
tests = [(40, 20), (20, 40), (10, 10), (10, 11)]
for s, d in tests:
    result = beat_the_spread(s, d)
    if result:
        print(f"S={s} D={d}  → high={result[0]}, low={result[1]}")
    else:
        print(f"S={s} D={d}  → impossible")

# ── 應用 2：2 the 9s（UVA 10922）────────────────────────
# 9-degree 定義：把一個數字重複加總各位數，直到變成一位數。
# 如果最後結果是 9，則原數是 9 的倍數；degree 表示加總次數。

def nine_degree(n_str: str):
    """
    回傳 (是否為 9 的倍數, 深度) 或 (False, -1)。

    n_str 是大數字串，可以處理超出 Python int 範圍的長數字。
    """
    current = n_str
    degree = 0

    # 只要目前數字不是單位數，就繼續把各位數字相加一次
    while len(current) > 1:
        s = sum(int(c) for c in current)
        current = str(s)
        degree += 1

    # 最後結果會是 1~9 的單位數
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
# 螺旋座標到步數的映射問題：
# 數字按照對角線方向從 (0,0) 開始展開成螺旋形，屬於一個特殊的編號規則。
# 這個公式是根據 x 與 y 的大小關係直接計算編號，而不必實際建構整個螺旋。

def position(x, y):
    """計算 (x,y) 在螺旋中的位置編號（從 0 開始）。

    公式來源：在螺旋結構中，同一個最大值 max(x,y) 對應到一個平方數環。
    - 如果 x >= y，表示座標在水平或向右的邊上，位置可以用 x*x + x + y 計算。
    - 否則表示座標在垂直或向上的邊上，位置可以用 y*y + x 計算。
    """
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

# 記憶重點 ──────────────────────────────────────────────────
# Beat the Spread：利用 S+D 和 S-D 直接求出 high / low，並檢查是否為非負整數。
# 2 the 9s：重複把各位數字相加，最後若等於 9 就是 9 的倍數；degree 是加總次數。
# Can You Solve It：螺旋座標可用 x 與 y 的大小關係直接映射到平方數環，避免模擬整個螺旋。
