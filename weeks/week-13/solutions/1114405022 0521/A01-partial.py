# A01. functools.partial：固定參數，減少重複
# 當你一直用「幾乎相同」的參數呼叫同一個函數，partial 幫你省掉重複
# 對應 Bloom's Taxonomy：應用（Apply）— 能把技巧套到新情境

from functools import partial  # 從 functools 模組匯入 partial 工具

# ── 基本概念：固定部分參數，產生新函數 ───────────────────

def power(base, exp):
    """計算 base 的 exp 次方（冪運算）"""
    return base ** exp  # 回傳 base 的 exp 次方

# partial(power, exp=2) 的意思是：建立一個新函數，已經固定 exp=2
square = partial(power, exp=2)   # 固定 exp=2，只剩 base 要填
# partial(power, exp=3) 固定指數為 3
cube   = partial(power, exp=3)   # 固定 exp=3

# 呼叫 square(5) 相當於呼叫 power(5, exp=2)
print("=== partial 基本用法 ===")
print(square(5))    # 輸出 25，即 5 的平方
print(cube(3))      # 輸出 27，即 3 的立方
# 列表推導式搭配 partial：對 1~5 每個數計算平方
print([square(n) for n in range(1, 6)])  # [1, 4, 9, 16, 25]

# ── 搭配 sorted：固定排序的 key ──────────────────────────

# 學生資料列表，每個元素是一個字典
students = [
    {"name": "王小明", "math": 80, "english": 70},  # 第一位學生
    {"name": "李大華", "math": 65, "english": 90},  # 第二位學生
    {"name": "張三",   "math": 95, "english": 55},  # 第三位學生
]

def get_score(student, subject):
    """從學生字典中取出指定科目的成績"""
    return student[subject]  # 根據 subject 鍵取出對應值

# 固定 subject="math"，產生一個「取數學成績」的函數
by_math    = partial(get_score, subject="math")
# 固定 subject="english"，產生一個「取英文成績」的函數
by_english = partial(get_score, subject="english")

print("\n=== partial 搭配 sorted ===")
# 按數學成績遞減排序（reverse=True），取出姓名
print("數學排名：", [s["name"] for s in sorted(students, key=by_math,    reverse=True)])
# 按英文成績遞減排序，取出姓名
print("英文排名：", [s["name"] for s in sorted(students, key=by_english, reverse=True)])

# ── CPE 應用：UVA 11005 進位制成本 ──────────────────────
# 題目需要計算同一個數字在不同進位下的成本
# 用 partial 固定「成本表」，讓程式碼更簡潔

# 定義 0~9、A~Z 共 36 個字元的字串，對應進位制的每一位
DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cost_in_base(n, base, costs):
    """計算 n 在 base 進位下每一位數字的成本總和"""
    if n == 0:          # 如果 n 是 0
        return costs[0]  # 直接回傳第 0 個字元的成本
    total = 0           # 初始化成本總和為 0
    while n > 0:         # 當 n 大於 0 時持續迴圈
        total += costs[n % base]  # 取餘數取得最低位數字的成本，加入總和
        n //= base       # 整數除法去掉最低位，繼續處理下一位
    return total        # 回傳總成本

# 假設每個字元成本都是 1（示範用）
uniform_costs = [1] * 36  # 產生長度 36 的列表，每個元素都是 1

# 用 partial 固定 costs，之後只要填 (n, base)
calc = partial(cost_in_base, costs=uniform_costs)

print("\n=== UVA 11005：各進位下的成本 ===")
n = 255              # 測試用的數字
# 用生成器表達式計算 n 在 2~36 進位下的所有成本，取最小值
best_cost = min(calc(n, b) for b in range(2, 37))
# 找出所有能達到最小成本的進位
best_bases = [b for b in range(2, 37) if calc(n, b) == best_cost]
print(f"數字 {n}，最低成本 {best_cost}，最佳進位：{best_bases}")

# ── 固定 print 的格式 ─────────────────────────────────────
# 競程輸出時常用

# 固定 print 的 end 參數為 " "（空白），取代預設的換行
print_same_line = partial(print, end=" ")
print("\n=== 同行輸出 ===")
for i in range(1, 6):   # 迴圈 i 從 1 到 5
    print_same_line(i)   # 印出 i 並在結尾加空白而非換行
print()   # 換行

# ── partial vs lambda 比較 ────────────────────────────────
# 兩種寫法效果一樣，partial 可讀性更高

# lambda 寫法：用匿名函數包裝 power(x, 2)
double_lambda  = lambda x: power(x, 2)        # lambda 寫法
# partial 寫法：直接固定 exp=2，語意更清楚
double_partial = partial(power, exp=2)         # partial 寫法

print("\n=== lambda vs partial ===")
# 兩種寫法對 1~5 計算平方的結果完全一樣
print([double_lambda(n)  for n in range(1, 6)])   # [1, 4, 9, 16, 25]
print([double_partial(n) for n in range(1, 6)])   # [1, 4, 9, 16, 25]

# 記憶重點 ──────────────────────────────────────────────────
# partial(函數, 固定的參數) → 回傳新函數，只剩剩餘的參數要填
# 常用場景：sorted key、min/max key、print 格式、重複呼叫某個函數
# 和 lambda 效果類似，但 partial 更清楚表達「固定哪個參數」
