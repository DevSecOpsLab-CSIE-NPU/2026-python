# R06. 特殊數值：無窮大、NaN、分數、隨機（3.7–3.11）
# 說明：float inf/nan / fractions.Fraction / random 的用法

import math
import random
from fractions import Fraction

# ─────────────────────────────────────────────────────────────────
# 3.7 無窮大與 NaN
# 說明：浮點數支援無窮大（inf）和非數（NaN）
# ─────────────────────────────────────────────────────────────────

# 建立正無窮大
a = float("inf")

# 建立負無窮大
b = float("-inf")

# 建立 NaN（非數，通常用於表示未定義或無法表示的結果）
c = float("nan")

print(a, b, c)  # 輸出：inf -inf nan

# 檢查是否為無窮大
print(math.isinf(a))  # 輸出：True

# 檢查是否為 NaN
print(math.isnan(c))  # 輸出：True

# 無窮大的運算規則
print(a + 45, 10 / a)  # 輸出：inf 0.0

# NaN 的運算規則：任何涉及 NaN 的運算都會回傳 NaN
# 無窮大減無窮大會得到 NaN
print(a / a, a + b)  # 輸出：nan nan

# 重要：NaN 不等於自己！（這是 IEEE 754 標準規定的）
print(c == c)  # 輸出：False

# ─────────────────────────────────────────────────────────────────
# 3.8 分數運算
# 說明：Fraction 類別可以精確表示分數，避免浮點數誤差
# ─────────────────────────────────────────────────────────────────

# 建立分數：5/4
p = Fraction(5, 4)

# 建立分數：7/16
q = Fraction(7, 16)

# 分數乘法：p * q
r = p * q

# 分數加法
print(p + q)  # 輸出：27/16

# 取得分子和分母
print(r.numerator, r.denominator)  # 輸出：35 64

# 轉換為浮點數
print(float(r))  # 輸出：0.546875

# 限制分母最大值，找出最接近的分數
# 找出分母不超過 8 的最接近分數
print(r.limit_denominator(8))  # 輸出：4/7

# 從浮點數建立分數（注意：浮點數會有精度問題）
print(Fraction(*(3.75).as_integer_ratio()))  # 輸出：15/4

# ─────────────────────────────────────────────────────────────────
# 3.11 隨機選擇
# 說明：random 模組提供多種隨機選擇功能
# ─────────────────────────────────────────────────────────────────

# 建立一個列表
values = [1, 2, 3, 4, 5, 6]

# 隨機選擇清單中的一個元素
print(random.choice(values))  # 輸出：隨機選擇一個元素

# 隨機選擇 k 個不重複的元素
print(random.sample(values, 3))  # 輸出：3 個不重複的隨機樣本

# 隨機打亂清單順序（會直接修改原清單）
random.shuffle(values)
print(values)  # 輸出：打亂後的序列

# 隨機產生指定範圍內的整數（包含兩端）
print(random.randint(0, 10))  # 輸出：0 到 10 之間的隨機整數

# 設定隨機種子，讓隨機結果可重現
# 相同種子會產生相同的隨機序列
random.seed(42)
print(random.random())  # 輸出：固定值（由种子決定）