# ===================================================================
# A01. functools.partial：固定參數，減少重複
# 學生：賴俋勳 1114405041
# 日期：2026-05-21
# 主題：functools.partial — 固定函數的某些參數，產生新函數
# ===================================================================
# 【學習心得】
#   partial 讓我們把一個「多參數函數」縮減成「少參數函數」。
#   當一個函數的某個參數在很多地方都是一樣的值，用 partial 就不用
#   一直重複寫那個值，也讓程式碼更好讀。
#   和 lambda 相比，partial 更能清楚表達「我在固定哪個參數」。
# ===================================================================

from functools import partial

# ── 基本概念：固定部分參數，產生新函數 ────────────────────
# power(base, exp) 計算 base 的 exp 次方。
# 如果 exp 永遠是 2（平方），用 partial 固定 exp=2，
# 就不用每次都寫 power(x, 2)，直接呼叫 square(x) 即可。

def power(base, exp):
    """計算 base 的 exp 次方"""
    return base ** exp

# partial(power, exp=2) 的意思：
#   - 第一個參數是「原始函數」power
#   - 之後是要固定的參數（用關鍵字參數指定 exp=2）
#   - 回傳值是一個新的函數物件，呼叫它時只需要填 base
square = partial(power, exp=2)   # 固定 exp=2，只剩 base 要填
cube   = partial(power, exp=3)   # 固定 exp=3，只剩 base 要填

print("=== partial 基本用法 ===")
print(square(5))    # 輸出 25，等同於 power(5, 2)
print(cube(3))      # 輸出 27，等同於 power(3, 3)
print([square(n) for n in range(1, 6)])  # [1, 4, 9, 16, 25]

# ── 搭配 sorted：固定排序的 key ──────────────────────────
# sorted() 的 key= 參數需要一個「只接受一個參數」的函數。
# 但 get_score 需要兩個參數（student 和 subject）。
# 用 partial 固定 subject，就能滿足 sorted 的需求。

students = [
    {"name": "王小明", "math": 80, "english": 70},
    {"name": "李大華", "math": 65, "english": 90},
    {"name": "張三",   "math": 95, "english": 55},
]

def get_score(student, subject):
    """從學生字典取得指定科目的分數"""
    return student[subject]

# 固定 subject，產生只需要 student 的新函數
# sorted() 用 by_math 當 key 時，每次只需傳入一個 student
by_math    = partial(get_score, subject="math")
by_english = partial(get_score, subject="english")

print("\n=== partial 搭配 sorted ===")
# reverse=True 表示由高到低排列
print("數學排名：", [s["name"] for s in sorted(students, key=by_math,    reverse=True)])
print("英文排名：", [s["name"] for s in sorted(students, key=by_english, reverse=True)])

# ── CPE 應用：UVA 11005 進位制成本 ────────────────────────
# 題目概念：數字 n 在不同進位制表示時，每個「位數字元」有不同印刷成本。
# 找最低總成本的進位制。
# 用 partial 固定 costs（成本表），讓計算函數只剩 (n, base) 兩個變數。

DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cost_in_base(n, base, costs):
    """
    計算正整數 n 在 base 進位制下，每一位數字的成本總和。
    例如 n=10, base=2 → 二進位是 1010 → 成本 = costs[1]+costs[0]+costs[1]+costs[0]
    """
    if n == 0:
        return costs[0]   # 0 本身就是一個「0」字元
    total = 0
    while n > 0:
        total += costs[n % base]   # 取最低位的數字（0~base-1），查成本表
        n //= base                 # 右移一位（去掉最低位）
    return total

# 假設每個字元成本都是 1（示範用，實際題目會讀入不同成本）
uniform_costs = [1] * 36

# partial 固定 costs，之後只要給 (n, base) 即可
# 這樣在 min() 和 list comprehension 裡用起來很簡潔
calc = partial(cost_in_base, costs=uniform_costs)

print("\n=== UVA 11005：各進位下的成本 ===")
n = 255
# 檢查所有進位（2 到 36）取最小成本
best_cost = min(calc(n, b) for b in range(2, 37))
best_bases = [b for b in range(2, 37) if calc(n, b) == best_cost]
print(f"數字 {n}，最低成本 {best_cost}，最佳進位：{best_bases}")

# ── 固定 print 的格式 ──────────────────────────────────────
# print() 預設 end="\n"（換行），固定成 end=" " 就能同行輸出。
print_same_line = partial(print, end=" ")
print("\n=== 同行輸出 ===")
for i in range(1, 6):
    print_same_line(i)    # 1 2 3 4 5（全部在同一行）
print()                   # 最後手動換行

# ── partial vs lambda 比較 ─────────────────────────────────
# 兩者效果相同，但用途有差：
#   partial → 語意清晰，表達「固定了哪個參數」
#   lambda  → 更靈活，可以做複雜的表達式
double_lambda  = lambda x: power(x, 2)        # lambda 寫法
double_partial = partial(power, exp=2)         # partial 寫法（語意更清楚）

print("\n=== lambda vs partial ===")
print([double_lambda(n)  for n in range(1, 6)])   # [1, 4, 9, 16, 25]
print([double_partial(n) for n in range(1, 6)])   # [1, 4, 9, 16, 25]

# ─── 記憶重點 ──────────────────────────────────────────────
# partial(函數, 固定的參數) → 回傳新函數，只剩剩餘的參數要填
# 常用場景：sorted key、min/max key、print 格式、重複呼叫某個函數
# 和 lambda 效果類似，但 partial 更清楚表達「固定哪個參數」
