# R06. 特殊數值：無窮大、NaN、分數、隨機（3.7–3.11）
#
# 本檔案整理 Python 中幾種「不是一般整數/小數」的常見主題：
# 1) 無窮大（inf, -inf）與 NaN（不是數字）
# 2) Fraction（有理數）做精確分數運算
# 3) random 模組的基本隨機抽樣與亂數生成
#
# 學習重點：
# - NaN 有特殊比較行為（連自己都不相等）
# - Fraction 可避免浮點誤差，適合精確比例運算
# - 設定 random.seed() 可讓結果可重現（利於測試）

import math
import random
from fractions import Fraction

# ── 3.7 無窮大與 NaN ──────────────────────────────────
# 透過 float() 建立特殊浮點值
a = float("inf")
b = float("-inf")
c = float("nan")
print(a, b, c)  # inf -inf nan

# 使用 math.isinf / math.isnan 檢查特殊值
print(math.isinf(a))  # True
print(math.isnan(c))  # True

# 與無窮大運算時，部分結果可定義（例如 inf + 常數 = inf）
print(a + 45, 10 / a)  # inf 0.0

# 某些運算屬於未定義，結果會是 nan
print(a / a, a + b)  # nan nan（未定義）

# NaN 的重要特性：任何相等比較都為 False（包含自己）
print(c == c)  # False（NaN 不等於自己！）

# ── 3.8 分數運算 ──────────────────────────────────────
# Fraction(分子, 分母) 以最簡分數形式保存，運算精確
p = Fraction(5, 4)
q = Fraction(7, 16)
r = p * q

# 分數加法結果仍保持分數
print(p + q)  # 27/16

# 可直接取得分子與分母
print(r.numerator, r.denominator)  # 35 64

# 需要輸出小數時可轉為 float
print(float(r))  # 0.546875

# limit_denominator(max_den) 用較小分母近似分數
print(r.limit_denominator(8))  # 4/7

# float.as_integer_ratio() 可取出精確比例，再轉成 Fraction
print(Fraction(*(3.75).as_integer_ratio()))  # 15/4

# ── 3.11 隨機選擇 ─────────────────────────────────────
values = [1, 2, 3, 4, 5, 6]

# choice：從序列中隨機取 1 個元素
print(random.choice(values))  # 隨機一個

# sample：不重複抽樣 k 個，原序列不會被改動
print(random.sample(values, 3))  # 3 個不重複樣本

# shuffle：原地打亂（in-place），會直接修改原 list
random.shuffle(values)
print(values)  # 打亂後的序列

# randint(a, b)：回傳 [a, b]（含端點）的整數
print(random.randint(0, 10))  # 0~10 整數

# seed 固定亂數起點，之後 random() 的結果可重現
random.seed(42)
print(random.random())  # 固定種子：可重現
