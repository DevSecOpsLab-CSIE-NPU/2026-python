# A01. functools.partial：固定參數，減少重複
# 範例與說明（繁體中文）：
# 本檔展示如何使用 functools.partial 將某些參數「預先綁定」，
# 產生更簡潔的呼叫介面（新函數），避免在程式中重複傳入相同參數。
# 常見應用場景包括：
# - 當作 sorted/min/max 的 key 函數（減少重複設定同一個 key）
# - 固定輸出格式的 print（例如固定 end 或 sep）
# - 將不常變動的設定（如成本表）綁定到演算法上，提升可讀性

from functools import partial

# ── 基本概念：固定部分參數，產生新函數 ───────────────────

def power(base, exp):
    # base: 底數（int 或 float）
    # exp: 指數（int）
    # 回傳 base 的 exp 次方
    return base ** exp

square = partial(power, exp=2)   # 固定 exp=2，只剩 base 要填
cube   = partial(power, exp=3)   # 固定 exp=3

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
    # student: 字典，例如 {"name": ..., "math": 80, "english": 70}
    # subject: 欄位名稱字串，例如 "math" 或 "english"
    # 此函數從 student 取出指定科目的分數並回傳
    return student[subject]

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
    """
    計算整數 n 在指定進位 base（2..36）下，每一位數字的成本總和。

    參數：
      n (int): 非負整數，要轉換為指定進位的表示法
      base (int): 進位，範圍通常為 2..36
      costs (Sequence[int]): 每個數字對應的成本，索引 0..(base-1)

    回傳：
      int: n 在該進位下各位數字成本的加總

    範例說明：若 costs 全部為 1，函數會回傳該表示法中所有位元（含 0 位）的成本加總；
    若只對非零位計數，則可修改邏輯以跳過成本為 0 的情況。
    """
    if n == 0:
        return costs[0]
    total = 0
    while n > 0:
        total += costs[n % base]
        n //= base
    return total

# 假設每個字元成本都是 1（示範用）
uniform_costs = [1] * 36

# 用 partial 固定 costs，之後只要填 (n, base)
calc = partial(cost_in_base, costs=uniform_costs)

print("\n=== UVA 11005：各進位下的成本 ===")
n = 255
best_cost = min(calc(n, b) for b in range(2, 37))
best_bases = [b for b in range(2, 37) if calc(n, b) == best_cost]
print(f"數字 {n}，最低成本 {best_cost}，最佳進位：{best_bases}")

# ── 固定 print 的格式 ─────────────────────────────────────
# 競程輸出時常用：使用 partial 將常用參數（如 end/sep）綁定，讓呼叫更簡潔

print_same_line = partial(print, end=" ")
print("\n=== 同行輸出 ===")
for i in range(1, 6):
    print_same_line(i)
print()   # 換行

# ── partial vs lambda 比較 ────────────────────────────────
# 兩種寫法效果相同，但在不同情境各有優勢：
# - partial: 明確綁定命名參數、可讀性佳、易於與高階函數搭配
# - lambda: 彈性高，可執行簡單轉換或在綁定位置參數時更直覺

double_lambda  = lambda x: power(x, 2)        # lambda 寫法
double_partial = partial(power, exp=2)         # partial 寫法

print("\n=== lambda vs partial ===")
print([double_lambda(n)  for n in range(1, 6)])   # [1, 4, 9, 16, 25]
print([double_partial(n) for n in range(1, 6)])   # [1, 4, 9, 16, 25]

# 記憶重點 ──────────────────────────────────────────────────
# - partial(函數, **固定的參數) → 回傳新函數，只需傳入未綁定的參數即可
# - 好處：提高可讀性、減少重複參數、清楚表達哪些參數為設定值
# - 常見用法：sorted/min/max 的 key、固定 print 的格式、將設定（如成本表）注入演算法
# - 與 lambda 比較：lambda 更適合做 inline 的小轉換；partial 更適合表達「綁定設定值」的語意
