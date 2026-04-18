import math
import random
from fractions import Fraction

# ── 特殊浮點值：inf 與 nan ────────────────────────────────
# float("inf") 代表正無窮大，float("-inf") 代表負無窮大
# float("nan") 代表「非數值」(Not a Number)
a = float("inf")
b = float("-inf")
c = float("nan")
print(a, b, c)          # inf -inf nan

# 判斷是否為無窮大 / NaN 必須用 math 函式，不能用 ==
print(math.isinf(a))    # True
print(math.isnan(c))    # True

# inf 的算術：加法有限值仍是 inf；除以 inf 得 0.0
print(a + 45, 10 / a)   # inf  0.0

# inf/inf = nan；inf + (-inf) = nan（不定式）
print(a / a, a + b)     # nan  nan

# nan 與任何值比較（包含自身）皆為 False → 不能用 == 偵測 nan
print(c == c)           # False

# ── 分數（有理數）精確計算 ───────────────────────────────
# Fraction 以分子/分母儲存，不受浮點誤差影響
p = Fraction(5, 4)   # 5/4
q = Fraction(7, 16)  # 7/16
r = p * q            # 35/64

print(p + q)                      # 27/16（自動化簡）
print(r.numerator, r.denominator) # 35  64
print(float(r))                   # 0.546875
print(r.limit_denominator(8))     # 4/7（近似分數，分母 ≤ 8）

# 從浮點數轉分數：as_integer_ratio() 回傳 (分子, 分母)
print(Fraction(*(3.75).as_integer_ratio()))  # 15/4

# ── 隨機數產生 ────────────────────────────────────────────
values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))       # 從序列隨機取一個元素
print(random.sample(values, 3))    # 不重複隨機取 3 個（不修改原序列）
random.shuffle(values)             # 原地隨機打亂序列
print(values)
print(random.randint(0, 10))       # 回傳 [0, 10] 的隨機整數（含兩端）

# seed：固定種子讓隨機序列可重現（測試/除錯時使用）
random.seed(42)
print(random.random())             # [0.0, 1.0) 均勻分布浮點數
