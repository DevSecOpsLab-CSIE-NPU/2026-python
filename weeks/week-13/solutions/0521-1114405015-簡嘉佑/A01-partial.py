# A01. functools.partial：固定參數，減少重複
# 當你一直用「幾乎相同」的參數呼叫同一個函數，partial 幫你省掉重複
# 對應 Bloom's Taxonomy：應用（Apply）— 能把技巧套到新情境
#
# partial 的核心概念：你有一個需要多個參數的函數，
# 卻每次呼叫時有幾個參數總是相同的。
# partial 會為你「預先填套」對應參數，產生一個新函數，
# 之後只需填剩下的參數即可。

from functools import partial

# ── 基本概念：固定部分參數，產生新函數 ───────────────────

def power(base, exp):
    # 計算 base 的 exp 次方，示範 partial 的起點
    return base ** exp

# partial(power, exp=2) 表示：「固定 exp=2，只剩 base 要填」
# 回傳的 square 就是一個只需一個參數的新函數
square = partial(power, exp=2)   # 固定 exp=2，只剩 base 要填
cube   = partial(power, exp=3)   # 固定 exp=3

print("=== partial 基本用法 ===")
print(square(5))    # 25  — 等於 power(5, exp=2)
print(cube(3))      # 27  — 等於 power(3, exp=3)
print([square(n) for n in range(1, 6)])  # [1, 4, 9, 16, 25]

# ── 搭配 sorted：固定排序的 key ──────────────────────────
# sorted 的 key 參數需要一個「只收一個參數」的函數
# 但 get_score 需要 student 和 subject 兩個參數
# 用 partial 固定 subject，讓 key 只剩 student 要填

students = [
    {"name": "王小明", "math": 80, "english": 70},
    {"name": "李大華", "math": 65, "english": 90},
    {"name": "張三",   "math": 95, "english": 55},
]

def get_score(student, subject):
    # 從學生字典取出指定科目的分數
    return student[subject]

# 固定 subject 後，by_math 只需傳入一個學生 dict 即可
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
        return costs[0]   # 0 只有一位，直接回傳 '0' 的成本
    total = 0
    while n > 0:
        total += costs[n % base]   # n % base 是最低位的數字索引
        n //= base                 # 去掉最低位
    return total

# 假設每個字元成本都是 1（示範用）
uniform_costs = [1] * 36

# 用 partial 固定 costs，之後只要填 (n, base)
# 這樣 min/list-comprehension 都能簡潔地只傳 (n, base)
calc = partial(cost_in_base, costs=uniform_costs)

print("\n=== UVA 11005：各進位下的成本 ===")
n = 255
# min 與 list comprehension 都可以直接使用 calc
best_cost  = min(calc(n, b) for b in range(2, 37))
best_bases = [b for b in range(2, 37) if calc(n, b) == best_cost]
print(f"數字 {n}，最低成本 {best_cost}，最佳進位：{best_bases}")

# ── 固定 print 的格式 ─────────────────────────────────────
# partial(print, end=" ") 表示固定 end=" "。
# 之後呼叫 print_same_line(x) 等於 print(x, end=" ")
print_same_line = partial(print, end=" ")
print("\n=== 同行輸出 ===")
for i in range(1, 6):
    print_same_line(i)
print()   # 最後手動換行

# ── partial vs lambda 比較 ────────────────────────────────
# 兩種寫法效果一樣，partial 可讀性更高，明確表達「固定哪個參數」

double_lambda  = lambda x: power(x, 2)        # lambda 寫法：意圖不明顯
double_partial = partial(power, exp=2)         # partial 寫法：明確表達固定 exp
double_lambda  = lambda x: power(x, 2)        # lambda 寫法
double_partial = partial(power, exp=2)         # partial 寫法

print("\n=== lambda vs partial ===")
print([double_lambda(n)  for n in range(1, 6)])   # [1, 4, 9, 16, 25]
print([double_partial(n) for n in range(1, 6)])   # [1, 4, 9, 16, 25]

# 記憶重點 ──────────────────────────────────────────────────
# partial(函數, 固定的參數) → 回傳新函數，只剩剩餘的參數要填
# 常用場景：sorted key、min/max key、print 格式、重複呼叫某個函數
# 和 lambda 效果類似，但 partial 更清楚表達「固定哪個參數」
