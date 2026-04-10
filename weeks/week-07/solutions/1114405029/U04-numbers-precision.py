# U04. 數字精度的陷阱與選擇（3.1–3.7）
# 銀行家捨入 / NaN 比較陷阱 / float vs Decimal 選擇

import math
import timeit
from decimal import Decimal, ROUND_HALF_UP

# ── 銀行家捨入（3.1）─────────────────────────────────
# Python 的內建 round() 採用「四捨六入五取偶」（Banker's rounding）
# 遇到 .5 時會捨入到最接近的「偶數」，旨在減少大量統計時的累積誤差
print(round(0.5))  # 0（向偶數 0 靠攏）
print(round(2.5))  # 2（向偶數 2 靠攏）
print(round(3.5))  # 4（向偶數 4 靠攏）

# 若金融業務需要傳統的四捨五入（5 一律進位），需用 Decimal 物件配合 ROUND_HALF_UP
def trad_round(x: float, n: int = 0) -> Decimal:
    d = Decimal(str(x))
    fmt = Decimal("1") if n == 0 else Decimal("0." + "0" * n)
    return d.quantize(fmt, rounding=ROUND_HALF_UP)

print(trad_round(0.5))  # 1
print(trad_round(2.5))  # 3

# ── NaN 無法用 == 比較（3.7）─────────────────────────
# NaN (Not a Number) 有一個特殊的特性：它與任何值（包含自己）比較都不相等
c = float("nan")
print(c == c)  # False
print(c == float("nan"))  # False
# 唯一正確檢測 NaN 的方式是使用 math.isnan()
print(math.isnan(c))  # True

data = [1.0, float("nan"), 3.0, float("nan"), 5.0]
clean = [x for x in data if not math.isnan(x)] # 過濾掉 NaN
print(clean)  # [1.0, 3.0, 5.0]

# ── float vs Decimal 選擇（3.2）──────────────────────
# float (二進位浮點數)：執行極快但有精度誤差，因為二進位無法精確表示某些十進位小數（如 0.1）
print(0.1 + 0.2)  # 0.30000000000000004
print(0.1 + 0.2 == 0.3)  # False

# Decimal (十進位浮點數)：計算精確但速度較慢，適合金融計算
print(Decimal("0.1") + Decimal("0.2"))  # 0.3
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))  # True

# 效能測試：float vs Decimal 速度差異顯著（通常相差 10 倍以上）
t1 = timeit.timeit(lambda: 0.1 * 999, number=100_000)
t2 = timeit.timeit(lambda: Decimal("0.1") * 999, number=100_000)
print(f"float: {t1:.3f}s  Decimal: {t2:.3f}s（Decimal 約慢 {t2 / t1:.0f} 倍）")