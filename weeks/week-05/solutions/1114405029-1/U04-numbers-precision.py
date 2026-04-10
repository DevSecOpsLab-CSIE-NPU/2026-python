# U04. 數字精度的陷阱與選擇（3.1–3.7）
# 說明：銀行家捨入 / NaN 比較陷阱 / float vs Decimal 選擇

import math
import timeit
from decimal import Decimal, ROUND_HALF_UP

# ─────────────────────────────────────────────────────────────────
# 銀行家捨入（3.1）
# 說明：Python 的 round() 使用「銀行家捨入法」（Banker's Rounding）
# 又稱「四捨六入五取偶」，不是傳統的四捨五入
# ─────────────────────────────────────────────────────────────────

# 0.5 捨入為 0（因為 0 是偶數）
print(round(0.5))  # 輸出：0（不是 1！）

# 2.5 捨入為 2（因為 2 是偶數）
print(round(2.5))  # 輸出：2（不是 3！）

# 3.5 捨入為 4（因為 4 是偶數）
print(round(3.5))  # 輸出：4


# ─────────────────────────────────────────────────────────────────
# 若需傳統四捨五入，用 Decimal + ROUND_HALF_UP
# 說明：使用 Decimal 配合 quantize 和 ROUND_HALF_UP 實現傳統四捨五入
# ─────────────────────────────────────────────────────────────────

def trad_round(x: float, n: int = 0) -> Decimal:
    """
    傳統四捨五入函數
    
    參數：
        x：要四捨五入的浮點數
        n：小數位數，預設為 0
    
    回傳：
        四捨五入後的 Decimal 物件
    """
    d = Decimal(str(x))
    fmt = Decimal("1") if n == 0 else Decimal("0." + "0" * n)
    return d.quantize(fmt, rounding=ROUND_HALF_UP)


print(trad_round(0.5))  # 輸出：1
print(trad_round(2.5))  # 輸出：3


# ─────────────────────────────────────────────────────────────────
# NaN 無法用 == 比較（3.7）
# 說明：NaN（Not a Number）遵循 IEEE 754 標準，不等於自己
# ─────────────────────────────────────────────────────────────────

c = float("nan")

# NaN 不等於自己！
print(c == c)  # 輸出：False

# NaN 也不等於另一個 NaN
print(c == float("nan"))  # 輸出：False

# 唯一正確的檢測方式是使用 math.isnan()
print(math.isnan(c))  # 輸出：True

# 過濾掉 NaN 的正確方法
data = [1.0, float("nan"), 3.0, float("nan"), 5.0]
clean = [x for x in data if not math.isnan(x)]
print(clean)  # 輸出：[1.0, 3.0, 5.0]


# ─────────────────────────────────────────────────────────────────
# float vs Decimal 選擇（3.2）
# 說明：根據用途選擇適合的數字類型
# ─────────────────────────────────────────────────────────────────

# float：快但有誤差（適合科學計算、工程應用）
print(0.1 + 0.2)  # 輸出：0.30000000000000004（有誤差）
print(0.1 + 0.2 == 0.3)  # 輸出：False

# Decimal：精確但慢（適合金融、會計 applications）
print(Decimal("0.1") + Decimal("0.2"))  # 輸出：0.3
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))  # 輸出：True

# 效能比較
t1 = timeit.timeit(lambda: 0.1 * 999, number=100_000)
t2 = timeit.timeit(lambda: Decimal("0.1") * 999, number=100_000)
print(f"float: {t1:.3f}s  Decimal: {t2:.3f}s（Decimal 約慢 {t2 / t1:.0f} 倍）")