# A01. functools.partial：固定參數，減少重複
# 當你一直用「幾乎相同」的參數呼叫同一個函數，partial 幫你省掉重複
# 對應 Bloom's Taxonomy：應用（Apply）— 能把技巧套到新情境

from functools import partial

# ── 基本概念：固定部分參數，產生新函數 ───────────────────

def power(base, exp):
    """回傳 base 的 exp 次方"""
    return base ** exp

# partial 可以把函數的一部分參數先固定
# 之後呼叫 new_func 時，就只要補足剩下的參數
square = partial(power, exp=2)        # 固定 exp=2，只要填 base
cube   = partial(power, exp=3)        # 固定 exp=3，只要填 base
power_of_three = partial(power, 3)    # 固定 base=3，只要填 exp

print("=== partial 基本用法 ===")
print(square(5))    # 25
print(cube(3))      # 27
print(power_of_three(4))  # 3^4 = 81
print([square(n) for n in range(1, 6)])  # [1, 4, 9, 16, 25]

# ── 搭配 sorted：固定排序的 key ──────────────────────────

students = [
    {"name": "王小明", "math": 80, "english": 70},
    {"name": "李大華", "math": 65, "english": 90},
    {"name": "張三",   "math": 95, "english": 55},
]

def get_score(student, subject):
    """回傳 student 在指定 subject 的分數"""
    return student[subject]

# 用 partial 固定 subject，得到只要 student 的函數
# 這樣搭配 sorted 時就能直接當成 key 函數使用
by_math    = partial(get_score, subject="math")
by_english = partial(get_score, subject="english")

print("\n=== partial 搭配 sorted ===")
print("數學排名：", [s["name"] for s in sorted(students, key=by_math,    reverse=True)])
print("英文排名：", [s["name"] for s in sorted(students, key=by_english, reverse=True)])

# ── CPE 應用：UVA 11005 進位制成本 ──────────────────────
# 題目需要計算同一個數字在不同進位下的成本
# 用 partial 固定「成本表」，讓程式碼更簡潔

DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cost_in_base(n, base, costs):
    """計算 n 在 base 進位下每一位數字的成本總和

    costs 參數是一個列表，對應數值 0~35 的成本。
    例如 costs[10] 代表進位數字 'A' 的成本。
    """
    if n == 0:
        return costs[0]
    total = 0
    while n > 0:
        total += costs[n % base]
        n //= base
    return total

# 假設每個字元成本都是 1（示範用）
# 這裡預先準備 36 個成本，對應 0~35 的數字/字元
uniform_costs = [1] * 36

# 用 partial 固定 costs，之後只要填 (n, base)
# 等價於 lambda n, base: cost_in_base(n, base, uniform_costs)
calc = partial(cost_in_base, costs=uniform_costs)

print("\n=== UVA 11005：各進位下的成本 ===")
n = 255
best_cost = min(calc(n, b) for b in range(2, 37))
best_bases = [b for b in range(2, 37) if calc(n, b) == best_cost]
print(f"數字 {n}，最低成本 {best_cost}，最佳進位：{best_bases}")

# ── 固定 print 的格式 ─────────────────────────────────────
# 競程輸出時常用：固定 end、sep、file 等參數

print_same_line = partial(print, end=" ")
print("\n=== 同行輸出 ===")
for i in range(1, 6):
    print_same_line(i)
print()   # 換行

# ── partial vs lambda 比較 ────────────────────────────────
# 兩種寫法效果一樣，但 partial 更清楚表達「固定哪個參數」

# lambda 直接把函數呼叫包裝起來
double_lambda  = lambda x: power(x, 2)
# partial 則是直接指定 exp=2，意圖更明確
double_partial = partial(power, exp=2)

print("\n=== lambda vs partial ===")
print([double_lambda(n)  for n in range(1, 6)])   # [1, 4, 9, 16, 25]
print([double_partial(n) for n in range(1, 6)])   # [1, 4, 9, 16, 25]

# 記憶重點 ──────────────────────────────────────────────────
# partial(函數, 固定的參數) → 回傳新函數，只剩剩餘的參數要填
# 常用場景：sorted key、min/max key、print 格式、重複呼叫某個函數
# 和 lambda 效果類似，但 partial 更清楚表達「固定哪個參數」
