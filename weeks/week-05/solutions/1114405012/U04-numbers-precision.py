# U04. 數字精度的陷阱與選擇（3.1–3.7）
# 銀行家捨入 / NaN 比較陷阱 / float vs Decimal 選擇

import math
import timeit
from decimal import Decimal, ROUND_HALF_UP

# ── 銀行家捨入（3.1）─────────────────────────────────
# Python round() 用「四捨六入五取偶」，不是日常四捨五入
print("round(0.5) 的結果：", round(0.5))  # 0
print("round(2.5) 的結果：", round(2.5))  # 2
print("round(3.5) 的結果：", round(3.5))  # 4


# 若需傳統四捨五入，用 Decimal + ROUND_HALF_UP
# Decimal 可以控制捨入方式，適合需要符合一般數學或財務規則的情境。
def trad_round(x: float, n: int = 0) -> Decimal:
    d = Decimal(str(x))
    fmt = Decimal("1") if n == 0 else Decimal("0." + "0" * n)
    return d.quantize(fmt, rounding=ROUND_HALF_UP)


print("傳統四捨五入 0.5：", trad_round(0.5))
print("傳統四捨五入 2.5：", trad_round(2.5))

# ── NaN 無法用 == 比較（3.7）─────────────────────────
# NaN 的特殊規則是：它不等於任何值，連自己也不等於自己。
# 因此不能用 == 來判斷，必須用 math.isnan()。
c = float("nan")
print("NaN 是否等於自己：", c == c)  # False
print("NaN 是否等於另一個 NaN：", c == float("nan"))  # False
print("用 math.isnan() 檢查：", math.isnan(c))  # True

data = [1.0, float("nan"), 3.0, float("nan"), 5.0]
clean = [x for x in data if not math.isnan(x)]
print("移除 NaN 後的資料：", clean)

# ── float vs Decimal 選擇（3.2）──────────────────────
# float：快但有誤差（科學/工程適用）
print("0.1 + 0.2 的 float 結果：", 0.1 + 0.2)
print("float 是否等於 0.3：", 0.1 + 0.2 == 0.3)

# Decimal：精確但慢（金融/會計適用）
print("Decimal 0.1 + 0.2 的結果：", Decimal("0.1") + Decimal("0.2"))
print("Decimal 是否等於 0.3：", Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))

t1 = timeit.timeit(lambda: 0.1 * 999, number=100_000)
t2 = timeit.timeit(lambda: Decimal("0.1") * 999, number=100_000)
print(f"float 計算時間：{t1:.3f}s")
print(f"Decimal 計算時間：{t2:.3f}s")
print(f"Decimal 約慢 {t2 / t1:.0f} 倍")
