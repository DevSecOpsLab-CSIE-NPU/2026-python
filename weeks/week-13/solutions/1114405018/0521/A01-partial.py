# A01. functools.partial：固定參數，減少重複
# =============================================================================
# 什麼是 partial？
#   partial 是 Python 內建模組 functools 提供的一個工具。
#   當你有一個函數需要「固定某些參數」，每次都傳一樣的值很麻煩，
#   partial 可以幫你「鎖住」那些參數，產生一個新的、參數更少的函數。
#
# 生活比喻：
#   想像你去飲料店點餐，每次都說「一杯珍珠奶茶，微糖，去冰」。
#   partial 就像幫你記住「微糖去冰」，下次你只要說「珍珠奶茶」就好。
#
# 對應 Bloom's Taxonomy：應用（Apply）— 能把技巧套到新情境
# =============================================================================

from functools import partial

# ═════════════════════════════════════════════════════════════════════════════
# 基本概念：固定部分參數，產生新函數
# ═════════════════════════════════════════════════════════════════════════════
# 語法：partial(原函數, 要固定的參數...)
# 回傳值：一個新的函數，只需要傳入「沒有被固定」的參數即可
#
# 範例：power(base, exp) 有兩個參數
#   我們固定 exp=2 得到 square，之後只要給 base
#   我們固定 exp=3 得到 cube，之後只要給 base

def power(base, exp):
    """計算 base 的 exp 次方（base^exp）"""
    return base ** exp

# 固定 exp=2，產生 square 函數，只需要傳 base
square = partial(power, exp=2)

# 固定 exp=3，產生 cube 函數，只需要傳 base
cube   = partial(power, exp=3)

print("=== partial 基本用法 ===")
print(square(5))    # 5^2 = 25
print(cube(3))      # 3^3 = 27
# 搭配列表推導式，一次產生 1~5 的平方
print([square(n) for n in range(1, 6)])  # [1, 4, 9, 16, 25]


# ═════════════════════════════════════════════════════════════════════════════
# 搭配 sorted：固定排序的 key 函數
# ═════════════════════════════════════════════════════════════════════════════
# sorted() 的 key 參數需要一個「接收一個參數、回傳比較值」的函數
# 如果我們想比較的是學生的某個科目分數，用 partial 可以固定 subject

students = [
    {"name": "王小明", "math": 80, "english": 70},
    {"name": "李大華", "math": 65, "english": 90},
    {"name": "張三",   "math": 95, "english": 55},
]

def get_score(student, subject):
    """從學生字典中取出指定科目的成績"""
    return student[subject]

# 固定 subject，產生兩個專門的 key 函數
by_math    = partial(get_score, subject="math")
by_english = partial(get_score, subject="english")

print("\n=== partial 搭配 sorted ===")
# reverse=True 表示由高到低排序
print("數學排名：", [s["name"] for s in sorted(students, key=by_math,    reverse=True)])
print("英文排名：", [s["name"] for s in sorted(students, key=by_english, reverse=True)])


# ═════════════════════════════════════════════════════════════════════════════
# CPE 應用：UVA 11005 進位制成本
# ═════════════════════════════════════════════════════════════════════════════
# 題目說明：
#   給定 36 個字元（0-9, A-Z）各自的印刷成本，
#   問某個數字在不同進位（2~36 進位）下，最低成本是多少。
#
# 使用 partial 的好處：
#   cost_in_base 需要三個參數：(n, base, costs)
#   其中 costs（成本表）是固定的，不會改變。
#   用 partial 固定 costs，之後每次只要傳 (n, base) 即可。

DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cost_in_base(n, base, costs):
    """計算 n 在 base 進位下每一位數字的成本總和

    參數：
        n：要計算的數字（十進位）
        base：目標進位（2~36）
        costs：長度 36 的 list，每個位置代表該字元的成本

    原理：
        不斷對 base 取餘數，得到每一位的數字，
        用該數字當作索引去 costs 查成本，加總。
    """
    if n == 0:
        return costs[0]
    total = 0
    while n > 0:
        total += costs[n % base]   # n % base 得到該位數字的索引
        n //= base                 # 去掉已經算過的最低位
    return total

# 假設每個字元成本都是 1（示範用）
uniform_costs = [1] * 36

# 用 partial 固定 costs，之後只要填 (n, base)
calc = partial(cost_in_base, costs=uniform_costs)

print("\n=== UVA 11005：各進位下的成本 ===")
n = 255
# 找出 2~36 進位中的最低成本
best_cost = min(calc(n, b) for b in range(2, 37))
# 找出哪些進位達到這個最低成本
best_bases = [b for b in range(2, 37) if calc(n, b) == best_cost]
print(f"數字 {n}，最低成本 {best_cost}，最佳進位：{best_bases}")


# ═════════════════════════════════════════════════════════════════════════════
# 固定 print 的格式
# ═════════════════════════════════════════════════════════════════════════════
# 競程中經常需要「同行輸出」，每次手寫 end=" " 很麻煩
# 用 partial 固定 end 參數，得到一個「會印在同一行」的 print

print_same_line = partial(print, end=" ")
print("\n=== 同行輸出 ===")
for i in range(1, 6):
    print_same_line(i)
print()   # 最後手動換行


# ═════════════════════════════════════════════════════════════════════════════
# partial vs lambda 比較
# ═════════════════════════════════════════════════════════════════════════════
# 同樣功能，兩種寫法：
#   lambda: 比較簡潔，但參數不明確
#   partial: 明確寫出「固定了哪個參數」，可讀性更好

double_lambda  = lambda x: power(x, 2)        # lambda 寫法
double_partial = partial(power, exp=2)         # partial 寫法

print("\n=== lambda vs partial ===")
print([double_lambda(n)  for n in range(1, 6)])   # [1, 4, 9, 16, 25]
print([double_partial(n) for n in range(1, 6)])   # [1, 4, 9, 16, 25]


# ═════════════════════════════════════════════════════════════════════════════
# 記憶重點
# ═════════════════════════════════════════════════════════════════════════════
# 1. partial(函數, 固定的參數...) → 回傳新函數，只剩未固定的參數要填
# 2. 常用場景：
#    - sorted / min / max 的 key 參數
#    - print 的格式（固定 end, sep）
#    - 重複呼叫某個函數，但參數大部分相同
# 3. 和 lambda 的比較：
#    - 功能類似，但 partial 更清楚表達「固定了哪個參數」
#    - lambda 更靈活，可以做運算；partial 只能固定參數
