# A01. functools.partial：固定參數，減少重複
# 當你一直用「幾乎相同」的參數呼叫同一個函數時，
# partial 可以先把某些參數綁定起來，之後只要補剩下的參數就好。
# 這樣可以降低重複、提升可讀性，也很適合拿來做重複使用的工具函數。
# 對應 Bloom's Taxonomy：應用（Apply）— 能把技巧套到新情境

from functools import partial

# ── 基本概念：固定部分參數，產生新函數 ───────────────────

def power(base, exp):
    # 一個最單純的冪次函數：回傳 base 的 exp 次方
    return base ** exp

# 先把 exp 固定成 2 / 3，得到新的「單參數函數」
# 之後呼叫 square(5) 時，其實等同於 power(5, exp=2)
square = partial(power, exp=2)
cube   = partial(power, exp=3)

print("=== partial 基本用法 ===")
print(square(5))    # 25
print(cube(3))      # 27
print([square(n) for n in range(1, 6)])  # [1, 4, 9, 16, 25]

# ── 搭配 sorted：固定排序的 key ──────────────────────────

students = [
    {"name": "王小明", "math": 80, "english": 70},
    {"name": "李大華", "math": 65, "english": 90},
    {"name": "張三",   "math": 95, "english": 55},
]

def get_score(student, subject):
    # 依照 subject 取出對應分數，方便給 sorted 的 key 使用
    return student[subject]

# 這裡把 subject 先固定住，sorted 只要拿到學生資料就能直接比大小
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
    """計算 n 在 base 進位下每一位數字的成本總和"""
    if n == 0:
        # 特別處理 0：因為迴圈不會進入，所以要直接回傳 0 的成本
        return costs[0]
    total = 0
    while n > 0:
        # n % base 代表目前最低位的數字索引，對應到 costs 裡的成本
        total += costs[n % base]
        # 把最低位移除，繼續處理下一位
        n //= base
    return total

# 假設每個字元成本都是 1（示範用）；實際題目會換成輸入的成本表
uniform_costs = [1] * 36

# 用 partial 固定 costs，之後只要填 n 和 base 就能重複計算
calc = partial(cost_in_base, costs=uniform_costs)

print("\n=== UVA 11005：各進位下的成本 ===")
n = 255
best_cost = min(calc(n, b) for b in range(2, 37))
best_bases = [b for b in range(2, 37) if calc(n, b) == best_cost]
print(f"數字 {n}，最低成本 {best_cost}，最佳進位：{best_bases}")

# ── 固定 print 的格式 ─────────────────────────────────────
# 競程輸出時常用

# 把 print 的 end 先固定成空白，之後每次呼叫都會接在同一行
print_same_line = partial(print, end=" ")
print("\n=== 同行輸出 ===")
for i in range(1, 6):
    print_same_line(i)
print()   # 換行

# ── partial vs lambda 比較 ────────────────────────────────
# 兩種寫法效果一樣，partial 可讀性更高

# lambda 直接寫出匿名函數；partial 則是把參數名稱與固定值說清楚
double_lambda  = lambda x: power(x, 2)
double_partial = partial(power, exp=2)

print("\n=== lambda vs partial ===")
print([double_lambda(n)  for n in range(1, 6)])   # [1, 4, 9, 16, 25]
print([double_partial(n) for n in range(1, 6)])   # [1, 4, 9, 16, 25]

# 記憶重點 ──────────────────────────────────────────────────
# partial(函數, 固定的參數) → 回傳新函數，只剩剩餘的參數要填
# 常用場景：sorted key、min/max key、print 格式、重複呼叫某個函數
# 和 lambda 效果類似，但 partial 更清楚表達「固定哪個參數」，
# 對閱讀大型程式或調整參數預設值時通常更直觀。
