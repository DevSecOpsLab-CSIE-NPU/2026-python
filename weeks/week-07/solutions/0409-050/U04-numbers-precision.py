# U04. 數字精度的陷阱與選擇（3.1–3.7）
# 銀行家捨入 / NaN 比較陷阱 / float vs Decimal 選擇

# 導入 math 模組，用於處理特殊的數學運算，如檢查 NaN。
import math
# 導入 timeit 模組，用於測量程式碼的執行時間，比較不同實現的效能。
import timeit
# 從 decimal 模組導入 Decimal 類別（用於精確的十進制浮點數運算）和 ROUND_HALF_UP 常數（用於傳統的四捨五入）。
from decimal import Decimal, ROUND_HALF_UP

# ── 銀行家捨入（3.1）─────────────────────────────────
# 說明：Python 內建的 round() 函數預設採用「銀行家捨入法」（四捨六入五成雙 / Round half to even）。
# 當小數部分剛好是 0.5 時，它會捨入到最接近的「偶數」整數。
# 這種做法在處理大量數據時，可以減少累積誤差，因為捨入方向平均分佈。

# Python round() 用「四捨六入五取偶」，不是日常四捨五入
print(round(0.5))  # 0（最接近的偶數是 0，不是 1！）
print(round(2.5))  # 2（最接近的偶數是 2，不是 3！）
print(round(3.5))  # 4（最接近的偶數是 4）


# 若需傳統四捨五入，用 Decimal + ROUND_HALF_UP
# 定義一個函數來實現傳統我們所認知的「四捨五入」。
def trad_round(x: float, n: int = 0) -> Decimal:
    # 先將浮點數轉換為字串，再轉換為 Decimal 物件，以避免浮點數本身的精度問題。
    d = Decimal(str(x))
    # 設定捨入的精度格式。如果 n=0，代表捨入到整數，格式為 "1"；如果 n>0，格式為 "0.0...0"。
    fmt = Decimal("1") if n == 0 else Decimal("0." + "0" * n)
    # 使用 quantize 方法進行捨入，並明確指定捨入模式為 ROUND_HALF_UP（四捨五入）。
    return d.quantize(fmt, rounding=ROUND_HALF_UP)


# 測試傳統四捨五入函數。
print(trad_round(0.5))  # 1（正常進位）
print(trad_round(2.5))  # 3（正常進位）

# ── NaN 無法用 == 比較（3.7）─────────────────────────
# 說明：NaN (Not a Number) 是浮點數標準 (IEEE 754) 中一個特殊的值。
# 根據標準，NaN 不等於任何值，包含它自己本身。

# 建立一個 NaN 浮點數。
c = float("nan")
# 嘗試將 NaN 與自己比較。
print(c == c)  # False（自己不等於自己！）
# 嘗試將 NaN 與另一個新建立的 NaN 比較。
print(c == float("nan"))  # False
# 正確的做法是使用 math.isnan() 來檢查一個數值是否為 NaN。
print(math.isnan(c))  # True（唯一正確的檢測方式）

# 範例：清理列表中的 NaN 值。
data = [1.0, float("nan"), 3.0, float("nan"), 5.0]
# 使用列表推導式過濾掉所有的 NaN。
clean = [x for x in data if not math.isnan(x)]
print(clean)  # [1.0, 3.0, 5.0]

# ── float vs Decimal 選擇（3.2）──────────────────────
# 說明：浮點數 (float) 在電腦底層是用二進制分數表示的，有些十進制小數（如 0.1）無法精確表示為二進制，
# 這會導致微小的精度誤差。
# Decimal 模組則是基於十進制運算，可以精確表示小數，但運算速度較慢。

# float：快但有誤差（科學/工程適用）
# 0.1 和 0.2 在二進制中是無限循環小數，相加後會產生誤差。
print(0.1 + 0.2)  # 0.30000000000000004
# 由於誤差的存在，直接比較浮點數是否相等通常是危險的（應使用 math.isclose()）。
print(0.1 + 0.2 == 0.3)  # False

# Decimal：精確但慢（金融/會計適用）
# 將字串傳入 Decimal 可以創建精確的十進制表示（不要直接傳浮點數進去，不然又會帶入浮點數誤差）。
print(Decimal("0.1") + Decimal("0.2"))  # 0.3
# Decimal 運算結果是精確的，可以直接進行等於 (==) 比較。
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))  # True

# 使用 timeit 測量 float 的運算效能。
t1 = timeit.timeit(lambda: 0.1 * 999, number=100_000) 
# 使用 timeit 測量 Decimal 的運算效能。
t2 = timeit.timeit(lambda: Decimal("0.1") * 999, number=100_000)
# 輸出比較結果，通常 Decimal 會比 float 慢非常多（可能慢幾十倍）。因此，除非需要絕對精度（如貨幣計算），否則預設還是建議用 float。
print(f"float: {t1:.3f}s  Decimal: {t2:.3f}s（Decimal 約慢 {t2 / t1:.0f} 倍）")
