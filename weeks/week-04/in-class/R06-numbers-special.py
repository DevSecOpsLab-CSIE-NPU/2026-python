# R06. 特殊數值：無窮大、NaN、分數、隨機（3.7–3.11）
# float inf/nan / fractions.Fraction / random
# 本檔重點是：
# 1) 特殊浮點值（inf、nan）的語意
# 2) 分數 Fraction 的精確有理數運算
# 3) random 常見抽樣與可重現實驗

import math
import random
from fractions import Fraction

# ── 3.7 無窮大與 NaN ──────────────────────────────────
# inf/-inf/nan 都是 float 的特殊值，可用字串轉型建立。
a = float("inf")
b = float("-inf")
c = float("nan")
print(a, b, c)  # inf -inf nan
# 檢測特殊值請用 math.isinf / math.isnan。
print(math.isinf(a))  # True
print(math.isnan(c))  # True
# inf 參與運算通常仍可得到合理極限結果。
print(a + 45, 10 / a)  # inf 0.0
# 但未定義型態（如 inf - inf、inf / inf）會得到 nan。
print(a / a, a + b)  # nan nan（未定義）
# nan 的核心陷阱：它和任何值比較（包含自己）都不相等。
print(c == c)  # False（NaN 不等於自己！）

# ── 3.8 分數運算 ──────────────────────────────────────
# Fraction 以「分子/分母」精確表示，不會有浮點誤差。
p = Fraction(5, 4)
q = Fraction(7, 16)
r = p * q
print(p + q)  # 27/16
# numerator / denominator 可直接取出分子分母。
print(r.numerator, r.denominator)  # 35 64
# 需要與其他函式互動時，可轉 float。
print(float(r))  # 0.546875
# limit_denominator 可找出分母上限內最接近的分數近似。
print(r.limit_denominator(8))  # 4/7
# 將 float 轉成精確分數表示（依該 float 的實際二進位值）。
print(Fraction(*(3.75).as_integer_ratio()))  # 15/4

# ── 3.11 隨機選擇 ─────────────────────────────────────
values = [1, 2, 3, 4, 5, 6]
# choice：隨機取一個元素。
print(random.choice(values))  # 隨機一個
# sample：不重複抽樣，常用於抽籤/切資料集。
print(random.sample(values, 3))  # 3 個不重複樣本
# shuffle：原地打亂（in-place），會直接改變原 list。
random.shuffle(values)
print(values)  # 打亂後的序列
# randint(a, b) 為閉區間 [a, b]。
print(random.randint(0, 10))  # 0~10 整數
# 設定種子後可重現結果，便於除錯與實驗比對。
random.seed(42)
print(random.random())  # 固定種子：可重現
