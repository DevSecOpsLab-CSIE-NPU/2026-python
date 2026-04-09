# U04. 數字精度的陷阱與選擇（3.1–3.7）
# 銀行家捨入 / NaN 比較陷阱 / float vs Decimal 選擇
# 本檔目的：釐清「結果看起來不直覺」其實多半來自規則差異，而不是 Python 壞掉。
# 這些觀念在金融、資料清理、科學計算都很常踩雷。

import math
import timeit
from decimal import Decimal, ROUND_HALF_UP

# ── 銀行家捨入（3.1）─────────────────────────────────
# Python 內建 round() 預設採用的是「四捨六入五取偶」，
# 英文常稱為 banker's rounding。
# 它的目的不是符合一般人從小學到的四捨五入直覺，
# 而是希望在大量統計時減少系統性偏差。
print(round(0.5))  # 0：0.5 會往最近的偶數靠
print(round(2.5))  # 2：2 和 3 距離同樣近，選偶數 2
print(round(3.5))  # 4：3 和 4 距離同樣近，選偶數 4


# 若需求是傳統四捨五入，就不能直接依賴 round()。
# 比較穩的作法是使用 Decimal，並明確指定 ROUND_HALF_UP。
def trad_round(x: float, n: int = 0) -> Decimal:
    # 先用 str(x) 而不是直接 Decimal(x)，
    # 是為了避免把 binary float 原本的近似誤差直接帶進 Decimal。
    d = Decimal(str(x))

    # quantize() 需要一個「量化模板」：
    # - n = 0 時，代表四捨五入到整數位，所以用 Decimal('1')
    # - n > 0 時，代表保留對應小數位數，例如 2 位就是 Decimal('0.00')
    fmt = Decimal("1") if n == 0 else Decimal("0." + "0" * n)
    return d.quantize(fmt, rounding=ROUND_HALF_UP)


print(trad_round(0.5))  # 1
print(trad_round(2.5))  # 3

# ── NaN 無法用 == 比較（3.7）─────────────────────────
# NaN = Not a Number，常用來表示未定義或非法數值結果。
# 根據 IEEE 754 規範，NaN 和任何東西比較都不相等，連自己也一樣。
c = float("nan")
print(c == c)  # False：NaN 自己不等於自己
print(c == float("nan"))  # False：兩個 NaN 也不相等
print(math.isnan(c))  # True：檢測 NaN 的正確方式

# 實務上若資料中含 NaN，通常要先清掉再做後續計算。
data = [1.0, float("nan"), 3.0, float("nan"), 5.0]

# 這裡用串列推導式配合 math.isnan() 把 NaN 過濾掉。
clean = [x for x in data if not math.isnan(x)]
print(clean)  # [1.0, 3.0, 5.0]

# ── float vs Decimal 選擇（3.2）──────────────────────
# float 使用二進位浮點數表示十進位小數，
# 所以某些十進位數字（例如 0.1）無法被完全精準表示。
print(0.1 + 0.2)  # 0.30000000000000004
print(0.1 + 0.2 == 0.3)  # False

# Decimal 則是十進位精確表示，適合金額、稅務、報表等要求精準的情境。
print(Decimal("0.1") + Decimal("0.2"))  # 0.3
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))  # True

# 但精準的代價通常是速度較慢。
# 因此在工程上要依需求選擇，而不是一律使用某一種型別。
t1 = timeit.timeit(lambda: 0.1 * 999, number=100_000)
t2 = timeit.timeit(lambda: Decimal("0.1") * 999, number=100_000)
print(f"float: {t1:.3f}s  Decimal: {t2:.3f}s（Decimal 約慢 {t2 / t1:.0f} 倍）")
