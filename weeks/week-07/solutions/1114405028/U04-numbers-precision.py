# U04. 數字精度的陷阱與選擇（3.1–3.7）
# 本程式示範數字處理中的精確度問題和選擇策略：
# 3.1 銀行家捨入 - Python round() 的捨入規則
# 3.7 NaN 比較陷阱 - NaN 值無法用 == 比較
# 3.2 float vs Decimal 選擇 - 根據使用場景選擇適當的數值型別

import math
import timeit
from decimal import Decimal, ROUND_HALF_UP

# ── 銀行家捨入（3.1）─────────────────────────────────
# 問題：Python 的 round() 使用「銀行家捨入」（四捨六入五取偶）
# 不是我們習慣的「四捨五入」
# 規則：當小數部分恰好為 0.5 時，向最接近的偶數捨入

print(round(0.5))  # 0（不是 1！）
print(round(2.5))  # 2（不是 3！）
print(round(3.5))  # 4（向偶數 4 捨入）
print(round(4.5))  # 4（向偶數 4 捨入）


# 若需傳統四捨五入，使用 Decimal + ROUND_HALF_UP
def trad_round(x: float, n: int = 0) -> Decimal:
    """
    傳統四捨五入函數

    Args:
        x: 要捨入的浮點數
        n: 小數位數（預設 0）

    Returns:
        Decimal 物件，已捨入到指定小數位數
    """
    d = Decimal(str(x))  # 轉為 Decimal 避免浮點誤差
    fmt = Decimal("1") if n == 0 else Decimal("0." + "0" * n)
    return d.quantize(fmt, rounding=ROUND_HALF_UP)


print(trad_round(0.5))  # 1（傳統四捨五入）
print(trad_round(2.5))  # 3（傳統四捨五入）

# ── NaN 無法用 == 比較（3.7）─────────────────────────
# 問題：NaN (Not a Number) 無法用 == 運算子比較
# 原因：根據 IEEE 754 標準，NaN != NaN

c = float("nan")
print(c == c)  # False（自己不等於自己！）
print(c == float("nan"))  # False
print(math.isnan(c))  # True（唯一正確的檢測方式）

# 清理含有 NaN 的資料
data = [1.0, float("nan"), 3.0, float("nan"), 5.0]
clean = [x for x in data if not math.isnan(x)]
print(clean)  # [1.0, 3.0, 5.0]

# ── float vs Decimal 選擇（3.2）──────────────────────
# float：快速但有精確度問題，適合科學計算、遊戲、圖形
# Decimal：精確但慢，適合金融、會計、貨幣計算

# float 的精確度問題
print(0.1 + 0.2)  # 0.30000000000000004（浮點誤差）
print(0.1 + 0.2 == 0.3)  # False

# Decimal 的精確度
print(Decimal("0.1") + Decimal("0.2"))  # 0.3（精確）
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))  # True

# 效能比較：Decimal 約慢 8-10 倍
t1 = timeit.timeit(lambda: 0.1 * 999, number=100_000)
t2 = timeit.timeit(lambda: Decimal("0.1") * 999, number=100_000)
print(f"float: {t1:.3f}s  Decimal: {t2:.3f}s（Decimal 約慢 {t2 / t1:.0f} 倍）")
