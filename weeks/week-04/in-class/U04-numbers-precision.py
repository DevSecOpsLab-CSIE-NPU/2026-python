# U04. 數字精度的陷阱與選擇（3.1–3.7）
# 關鍵字：銀行家捨入 / NaN 比較陷阱 / float vs Decimal 選擇

import math
import timeit
from decimal import Decimal, ROUND_HALF_UP

# ── 1. 銀行家捨入法 Banker's Rounding (3.1) ──────────────────────
# Python 內建的 round() 採用 IEEE 754 標準的「四捨六入五取偶」
# 當小數點後為 .5 時，會捨入到最接近的「偶數」，而非一律進位。
# 這樣做是為了在大量數據統計時，抵銷傳統四捨五入造成的向上偏誤。

print(round(0.5))  # 0（向偶數 0 靠攏）
print(round(1.5))  # 2（向偶數 2 靠攏）
print(round(2.5))  # 2（向偶數 2 靠攏，不是 3！）
print(round(3.5))  # 4（向偶數 4 靠攏）

# 若業務邏輯需要「傳統四捨五入」（如發票金額），需使用 Decimal 搭配 ROUND_HALF_UP
def trad_round(x: float, n: int = 0) -> Decimal:
    """
    自定義傳統四捨五入函數
    :param x: 待處理數字
    :param n: 小數點位數
    """
    d = Decimal(str(x))  # 務必先轉成字串，避免 float 的原始精度誤差
    # 設定格式，例如 n=2 時為 "0.01"
    fmt = Decimal("1") if n == 0 else Decimal("0." + "0" * (n - 1) + "1")
    return d.quantize(fmt, rounding=ROUND_HALF_UP)

print(trad_round(0.5))  # 1
print(trad_round(2.5))  # 3

# ── 2. NaN (Not a Number) 的比較陷阱 (3.7) ──────────────────────
# NaN 代表「非數字」，它在 IEEE 754 規範中有個特殊的定義：
# NaN 不等於任何東西，包括它自己。

c = float("nan")
print(c == c)              # False（非常奇特，但在數值運算中是合理的）
print(c == float("nan"))   # False
print(math.isnan(c))       # True（這是唯一且標準的檢測方式）

# 實務應用：過濾列表中的無效數據
data = [1.0, float("nan"), 3.0, float("nan"), 5.0]
clean = [x for x in data if not math.isnan(x)]
print(clean)  # [1.0, 3.0, 5.0]

# ── 3. float vs Decimal 的選擇 (3.2) ───────────────────────────
# float：基於二進制（Binary），無法精確表示某些十進制小數（如 0.1）。
# 優點：執行速度極快，適合科學計算、3D 運算、機器學習。

print(0.1 + 0.2)           # 0.30000000000000004（二進制轉換造成的微小誤差）
print(0.1 + 0.2 == 0.3)    # False（永遠不要直接用 == 比較 float）

# Decimal：基於十進制，模擬人類的手算邏輯。
# 優點：絕對精確。適用場景：金融、會計、稅務。
# 缺點：記憶體佔用較高，且運算速度慢許多。

print(Decimal("0.1") + Decimal("0.2"))                  # 0.3
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3")) # True

# 效能測試：float vs Decimal
# 測試 10 萬次乘法運算的耗時
t1 = timeit.timeit(lambda: 0.1 * 999, number=100_000)
t2 = timeit.timeit(lambda: Decimal("0.1") * 999, number=100_000)

print(f"float 耗時:   {t1:.5f}s")
print(f"Decimal 耗時: {t2:.5f}s")
print(f"結論：Decimal 約比 float 慢 {t2 / t1:.0f} 倍")