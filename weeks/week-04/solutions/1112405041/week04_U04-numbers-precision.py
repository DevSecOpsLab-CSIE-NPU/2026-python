# 【Bloom 階段：U - 理解與進階應用】
# U04. 數值精準度與捨入地雷
# August 的惡意提醒：這是 Week 05 題目 10056 的「絕殺點」。
# Python 默認的 round() 是「捨入到最近的偶數」(Banker's Rounding)，
# 如果題目要求的是「四捨五入」，你直接用 round() 必錯無疑。

from decimal import Decimal, ROUND_HALF_UP
import math

# 1. 傳統四捨五入的精確寫法 (Model Student Fingerprint)
def trad_round(x, n=0):
    d = Decimal(str(x))
    # 建立格式化目標，如 "0.00" 代表取兩位
    fmt = Decimal("1") if n == 0 else Decimal("0." + "0" * n)
    return d.quantize(fmt, rounding=ROUND_HALF_UP)

print(f"Standard round(2.5): {round(2.5)}") # 2
print(f"August's round(2.5):  {trad_round(2.5)}") # 3 (及格解)

# 2. 處理浮點數累積誤差
# 在計算數千筆浮點數總和時，使用 math.fsum 避免精度丟失
nums = [0.1] * 10
print(f"Standard sum: {sum(nums)}") # 0.9999999999999999
print(f"math.fsum:    {math.fsum(nums)}") # 1.0 (完美)
