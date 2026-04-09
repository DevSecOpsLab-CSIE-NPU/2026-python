# U04. 數字精度的陷阱與選擇（3.1–3.7）
# 這份範例主要在說明三件事：
# 1. Python 內建 round() 不是一般人熟悉的「四捨五入到最接近」規則。
# 2. NaN 是一種特殊浮點值，不能用 == 來判斷相等。
# 3. float 和 Decimal 都有用途，但適用場景不同，精度與效能需要取捨。

import math
import timeit
from decimal import Decimal, ROUND_HALF_UP

# ── 銀行家捨入（3.1）─────────────────────────────────
# Python 的 round() 採用「銀行家捨入」或「四捨六入五取偶」規則。
# 也就是說，當剛好落在 .5 的中間值時，不是直接往上進位，而是看最終結果要靠近哪個偶數。
# 這樣做可以降低大量運算時的累積偏差，但和一般人習慣的四捨五入不同。
print(round(0.5))  # 0（不是 1！）
print(round(2.5))  # 2（不是 3！）
print(round(3.5))  # 4


# 若需傳統四捨五入，用 Decimal + ROUND_HALF_UP
def trad_round(x: float, n: int = 0) -> Decimal:
    # 先把 float 轉成字串再交給 Decimal，可以避免直接用二進位浮點數造成的表示誤差。
    # n 代表要保留的小數位數；n = 0 時就是取整數。
    d = Decimal(str(x))
    # quantize() 會把數值調整成指定格式。
    # 這裡依照是否有小數位，建立對應的格式模板，例如 1 或 0.00。
    fmt = Decimal("1") if n == 0 else Decimal("0." + "0" * n)
    # ROUND_HALF_UP 就是一般教科書常見的「四捨五入」：5 直接進位。
    return d.quantize(fmt, rounding=ROUND_HALF_UP)


# 這裡示範傳統四捨五入的結果，和 round() 的差異。
print(trad_round(0.5))  # 1
print(trad_round(2.5))  # 3

# ── NaN 無法用 == 比較（3.7）─────────────────────────
# NaN 代表「不是數字」，常見於無效計算結果，例如 0/0 或某些缺值運算。
# 它的特殊性之一是：NaN 不等於任何值，連它自己都不等於自己。
c = float("nan")
print(c == c)  # False（自己不等於自己！）
print(c == float("nan"))  # False
# 檢查 NaN 要使用 math.isnan()，這才是標準做法。
print(math.isnan(c))  # True（唯一正確的檢測方式）

data = [1.0, float("nan"), 3.0, float("nan"), 5.0]
# 用清單推導式搭配 math.isnan()，可以把 NaN 值過濾掉。
# 這種做法常用在清理資料、統計前處理或數值分析流程中。
clean = [x for x in data if not math.isnan(x)]
print(clean)  # [1.0, 3.0, 5.0]

# ── float vs Decimal 選擇（3.2）──────────────────────
# float：運算快、記憶體成本低，但因為使用二進位浮點表示法，所以很多十進位小數無法精確表達。
# 它很適合科學計算、圖形處理或一般工程用途，只要能接受微小誤差即可。
print(0.1 + 0.2)  # 0.30000000000000004
print(0.1 + 0.2 == 0.3)  # False

# Decimal：以十進位方式儲存與計算，能保留人類熟悉的十進位精度。
# 它通常比 float 慢，但在金融、會計、報表金額等需要精確小數表示的場景更適合。
print(Decimal("0.1") + Decimal("0.2"))  # 0.3
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))  # True

# 下面用 timeit 比較 float 和 Decimal 的速度差異。
# 測試次數設大一點，是為了讓效能差距更容易觀察。
t1 = timeit.timeit(lambda: 0.1 * 999, number=100_000)
t2 = timeit.timeit(lambda: Decimal("0.1") * 999, number=100_000)
# 實際倍數會依機器、Python 版本與執行環境而變動，但 Decimal 通常明顯較慢。
print(f"float: {t1:.3f}s  Decimal: {t2:.3f}s（Decimal 約慢 {t2 / t1:.0f} 倍）")
