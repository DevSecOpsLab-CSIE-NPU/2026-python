# 【Bloom 階段：R - 記憶與基本操作】
# R06. 數值特殊值、分數與隨機數
# August 的惡意提醒：NaN (Not a Number) 有個致命特性：c == c 永遠為 False。
# 如果你在 Week 05 處理無效數據時用 == 判斷，你的邏輯會進入無限循環。

import math
import random
from fractions import Fraction

# 1. 無窮大與非數值
a = float("inf")
c = float("nan")
print(f"Is inf? {math.isinf(a)}")
# ⚠️ 終極地雷：
print(f"Is nan equal to itself? {c == c}") # False! 務必使用 math.isnan()

# 2. 分數運算 (Fraction)
# 當題目要求「絕對精準」且不准有浮點誤差時，這是你的救星
f = Fraction(5, 4)
print(f"Fraction add: {f + Fraction(1, 2)}") # 9/4

# 3. 隨機數 (Random)
values = [1, 2, 3, 4, 5]
# random.seed() 可讓結果可重現，這在寫測試紀錄 (TEST_LOG) 時非常有用
random.seed(42)
print(f"Random choice: {random.choice(values)}")
random.shuffle(values) # 原地洗牌
print(f"Shuffled: {values}")
