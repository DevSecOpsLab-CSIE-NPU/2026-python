import math
import timeit
from decimal import Decimal, ROUND_HALF_UP

# ── Python 的「銀行家捨入」(Banker's Rounding) ────────────
# round() 採 IEEE 754 的「捨入到偶數」規則：
# .5 時捨入到最近的偶數，而非傳統的「四捨五入」
print(round(0.5))   # 0（偶數）
print(round(2.5))   # 2（偶數）
print(round(3.5))   # 4（偶數）


def trad_round(x: float, n: int = 0) -> Decimal:
    """傳統四捨五入：使用 Decimal.quantize + ROUND_HALF_UP 模式。"""
    d = Decimal(str(x))  # 先轉字串再建 Decimal，避免浮點誤差
    # 格式樣板：n=0 → Decimal("1")；n=2 → Decimal("0.00")
    fmt = Decimal("1") if n == 0 else Decimal("0." + "0" * n)
    return d.quantize(fmt, rounding=ROUND_HALF_UP)  # .5 一律進位


print(trad_round(0.5))   # 1（傳統四捨五入）
print(trad_round(2.5))   # 3

# ── NaN 的偵測 ────────────────────────────────────────────
# NaN 與任何值（包含自身）的 == 比較皆為 False
c = float("nan")
print(c == c)             # False
print(c == float("nan")) # False
# 唯一可靠的偵測方式：math.isnan()
print(math.isnan(c))      # True

# 從串列過濾掉 NaN
data = [1.0, float("nan"), 3.0, float("nan"), 5.0]
clean = [x for x in data if not math.isnan(x)]
print(clean)  # [1.0, 3.0, 5.0]

# ── 浮點數精度陷阱 ────────────────────────────────────────
# 0.1 與 0.2 的二進位表示均有誤差，相加後不等於 0.3
print(0.1 + 0.2)            # 0.30000000000000004
print(0.1 + 0.2 == 0.3)     # False

# Decimal 以十進位字串儲存，可精確表示 0.1 和 0.2
print(Decimal("0.1") + Decimal("0.2"))            # 0.3
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))  # True

# ── 效能比較：float vs Decimal ───────────────────────────
# Decimal 精確但速度比原生 float 慢數倍（需純 Python 計算）
t1 = timeit.timeit(lambda: 0.1 * 999, number=100_000)
t2 = timeit.timeit(lambda: Decimal("0.1") * 999, number=100_000)
print(f"float: {t1:.3f}s Decimal: {t2:.3f}s（Decimal 約慢 {t2 / t1:.0f} 倍）")
