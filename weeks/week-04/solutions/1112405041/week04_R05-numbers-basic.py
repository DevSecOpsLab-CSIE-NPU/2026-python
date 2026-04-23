# 【Bloom 階段：R - 記憶與基本操作】
# R05. 數字進位與精準度基礎
# August 的惡意提醒：這是本週最「陰險」的陷阱。
# Python 的 round() 行為與你想像的不同：round(2.5) 得到的是 2 (向偶數捨入)。
# 而 4.2 + 2.1 不等於 6.3 的問題，是 Week 05 題目 10056 的核心死因。

from decimal import Decimal, localcontext
import math

# 1. 捨入地雷 (The Rounding Trap)
print(f"round(1.27, 1): {round(1.27, 1)}") # 1.3
print(f"round(2.5):    {round(2.5)}")    # 2 (注意！不是 3)

# 2. 浮點數精度與 Decimal
# 對於需要高精度的計算，不要直接使用 float
print(f"Bad float math: {4.2 + 2.1}") # 6.300000000000001
da, db = Decimal("4.2"), Decimal("2.1")
print(f"Decimal math:   {da + db}")   # 6.3

# 3. 數字格式化
x = 1234.56789
print(f"2 decimal places: {x:0.2f}")
print(f"Thousands comma:  {x:0,.2f}")

# 4. 進位轉換
n = 1234
print(f"Binary: {bin(n)}")
print(f"Hex:    {hex(n)}")
