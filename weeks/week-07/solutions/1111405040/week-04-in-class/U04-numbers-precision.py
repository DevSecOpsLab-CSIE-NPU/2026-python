"""
U04. 數字精度的陷阱與選擇。

這份範例整理三個常見觀念：
1. `round()` 預設是銀行家捨入，不一定等於一般人認知的四捨五入。
2. `NaN` 不能用 `==` 判斷。
3. `float` 與 `Decimal` 各有用途，不能混為一談。
"""

import math
import timeit
from decimal import Decimal, ROUND_HALF_UP


# ── 1. round() 使用銀行家捨入 ───────────────────────────────
# Python 的 round() 採用「四捨六入五取偶」。
print(round(0.5))  # 0
print(round(2.5))  # 2
print(round(3.5))  # 4


def trad_round(value: float, digits: int = 0) -> Decimal:
    """
    使用 Decimal 模擬一般人比較熟悉的四捨五入。

    `digits=0` 時，保留整數。
    `digits=2` 時，保留到小數第 2 位。
    """

    decimal_value = Decimal(str(value))
    if digits == 0:
        pattern = Decimal("1")
    else:
        pattern = Decimal("0." + "0" * digits)
    return decimal_value.quantize(pattern, rounding=ROUND_HALF_UP)


print(trad_round(0.5))  # 1
print(trad_round(2.5))  # 3


# ── 2. NaN 不能直接用 == 比較 ──────────────────────────────
not_a_number = float("nan")

# NaN 的特性之一，就是連自己都不相等。
print(not_a_number == not_a_number)  # False
print(not_a_number == float("nan"))  # False

# 正確做法是使用 math.isnan()。
print(math.isnan(not_a_number))  # True

data = [1.0, float("nan"), 3.0, float("nan"), 5.0]
clean = [value for value in data if not math.isnan(value)]
print(clean)  # [1.0, 3.0, 5.0]


# ── 3. float 與 Decimal 的取捨 ─────────────────────────────
# float 速度快，但以二進位近似小數，因此可能出現誤差。
print(0.1 + 0.2)  # 0.30000000000000004
print(0.1 + 0.2 == 0.3)  # False

# Decimal 以十進位字串建立數值，可保留較直觀的小數精度。
print(Decimal("0.1") + Decimal("0.2"))  # 0.3
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))  # True

float_time = timeit.timeit(lambda: 0.1 * 999, number=100_000)
decimal_time = timeit.timeit(lambda: Decimal("0.1") * 999, number=100_000)
print(f"float: {float_time:.3f}s  Decimal: {decimal_time:.3f}s（Decimal 約慢 {decimal_time / float_time:.0f} 倍）")
