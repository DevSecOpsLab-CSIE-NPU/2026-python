# A01. functools.partial：固定參數，減少重複
# 當你一直用「幾乎相同」的參數呼叫同一個函數，partial 幫你省掉重複
# 對應 Bloom's Taxonomy：應用（Apply）— 能把技巧套到新情境

from functools import partial

# ── 基本概念：固定部分參數，產生新函數 ───────────────────

def power(base, exp):
    """計算 base 的 exp 次方"""
    return base ** exp

# 使用 partial 固定 exp 參數
# square 函數現在等同於 power(base, exp=2)
square = partial(power, exp=2)   # 固定 exp=2，呼叫時只需提供 base
# cube 函數現在等同於 power(base, exp=3)
cube   = partial(power, exp=3)   # 固定 exp=3

print("=== partial 基本用法 ===")
print(square(5))    # 5 的平方，結果為 25
print(cube(3))      # 3 的三次方，結果為 27
# 結合 List Comprehension (串列生成式) 進行批次計算
print([square(n) for n in range(1, 6)])  # [1, 4, 9, 16, 25]

# ── 搭配 sorted：固定排序的 key ──────────────────────────

# 一份包含學生各科成績的字典列表
students = [
    {"name": "王小明", "math": 80, "english": 70},
    {"name": "李大華", "math": 65, "english": 90},
    {"name": "張三",   "math": 95, "english": 55},
]

def get_score(student, subject):
    """從學生資料字典中取得特定科目的成績"""
    return student[subject]

# 產生只針對特定科目取分數的函數，用於排序
by_math    = partial(get_score, subject="math")    # 等同於取出數學成績
by_english = partial(get_score, subject="english") # 等同於取出英文成績

print("\n=== partial 搭配 sorted ===")
# 根據數學分數降冪排序 (由高到低)
print("數學排名：", [s["name"] for s in sorted(students, key=by_math,    reverse=True)])
# 根據英文分數降冪排序 (由高到低)
print("英文排名：", [s["name"] for s in sorted(students, key=by_english, reverse=True)])

# ── CPE 應用：UVA 11005 進位制成本 ──────────────────────
# 題目需要計算同一個數字在不同進位下的成本
# 用 partial 固定「成本表」，讓程式碼更簡潔

# 定義 36 進位的所有字元
DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cost_in_base(n, base, costs):
    """計算 n 在 base 進位下每一位數字的成本總和"""
    if n == 0:
        return costs[0]
    total = 0
    while n > 0:
        # 取出該進位下的個位數，並累加其對應成本
        total += costs[n % base]
        n //= base # 將數字除以進位底數，處理下一位
    return total

# 假設每個字元成本都是 1（示範用，實際 UVA 11005 的成本由輸入給定）
uniform_costs = [1] * 36

# 用 partial 固定 costs 參數，之後只要填入 (n, base)
calc = partial(cost_in_base, costs=uniform_costs)

print("\n=== UVA 11005：各進位下的成本 ===")
n = 255
# 計算在 2 到 36 進位下的最小成本
best_cost = min(calc(n, b) for b in range(2, 37))
# 找出哪些進位能達成這個最小成本
best_bases = [b for b in range(2, 37) if calc(n, b) == best_cost]
print(f"數字 {n}，最低成本 {best_cost}，最佳進位：{best_bases}")

# ── 固定 print 的格式 ─────────────────────────────────────
# 競程輸出時常用，避免每次都要寫 end=" "

# 產生一個新的 print 函數，預設結尾是空白而非換行
print_same_line = partial(print, end=" ")
print("\n=== 同行輸出 ===")
for i in range(1, 6):
    print_same_line(i)
print()   # 最後補一個換行

# ── partial vs lambda 比較 ────────────────────────────────
# 兩種寫法效果一樣，partial 可讀性更高，意圖更明確

double_lambda  = lambda x: power(x, 2)         # lambda 寫法：建立匿名函數
double_partial = partial(power, exp=2)         # partial 寫法：固定參數

print("\n=== lambda vs partial ===")
print([double_lambda(n)  for n in range(1, 6)])   # [1, 4, 9, 16, 25]
print([double_partial(n) for n in range(1, 6)])   # [1, 4, 9, 16, 25]

# 記憶重點 ──────────────────────────────────────────────────
# partial(函數, 固定的參數) → 回傳新函數，只剩剩餘的參數要填
# 常用場景：sorted key、min/max key、print 格式、重複呼叫某個函數
# 和 lambda 效果類似，但 partial 更清楚表達「固定哪個參數」
