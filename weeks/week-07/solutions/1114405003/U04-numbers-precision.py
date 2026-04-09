# U04. 數字精度的陷阱與選擇（3.1–3.7）
#
# 這個檔案示範三個數值相關的重點：
# 1. Python 的 round() 採用銀行家捨入，不是傳統四捨五入。
# 2. NaN 有特殊比較規則，不能用 == 直接判斷。
# 3. float 與 Decimal 各有用途，速度與精確度之間要做取捨。

import math
import timeit
from decimal import Decimal, ROUND_HALF_UP

# ── 銀行家捨入（3.1）─────────────────────────────────
# Python 的 round() 使用「四捨六入五取偶」或稱銀行家捨入。
# 也就是說，遇到剛好一半時，不一定往上進位，而是看前一位是奇數還是偶數。
# 這樣做可降低大量運算後的系統性偏差，但和一般人熟悉的四捨五入不同。
print(round(0.5))  # 0（不是 1！）
print(round(2.5))  # 2（不是 3！）
print(round(3.5))  # 4


# 若需要傳統四捨五入，應改用 Decimal 搭配 ROUND_HALF_UP。
# 這在金額計算、帳務系統、報表輸出時很常見，因為結果要符合人的直覺。
def trad_round(x: float, n: int = 0) -> Decimal:
    # 先把 float 轉成字串再轉 Decimal，可以減少二進位浮點誤差直接帶入的問題。
    d = Decimal(str(x))
    # n 代表要保留的小數位數；n=0 時四捨五入到整數。
    fmt = Decimal("1") if n == 0 else Decimal("0." + "0" * n)
    return d.quantize(fmt, rounding=ROUND_HALF_UP)


print(trad_round(0.5))  # 1
print(trad_round(2.5))  # 3

# ── NaN 無法用 == 比較（3.7）─────────────────────────
# NaN 代表「不是一個數字」，它的設計就是不和任何值相等，包含它自己。
# 這個規則常讓人誤判資料清理結果，因此檢查 NaN 必須用 math.isnan()。
c = float("nan")
print(c == c)  # False（自己不等於自己！）
print(c == float("nan"))  # False
print(math.isnan(c))  # True（唯一正確的檢測方式）

# 如果資料中可能混有 NaN，建議先過濾，再做後續計算或統計。
data = [1.0, float("nan"), 3.0, float("nan"), 5.0]
clean = [x for x in data if not math.isnan(x)]
print(clean)  # [1.0, 3.0, 5.0]

# ── float vs Decimal 選擇（3.2）──────────────────────
# float：運算快、記憶體小，適合科學計算、圖形處理、工程模擬等。
# 但 float 是二進位浮點數，很多十進位小數無法完全精確表示。
print(0.1 + 0.2)  # 0.30000000000000004
print(0.1 + 0.2 == 0.3)  # False

# Decimal：以十進位表示，適合需要人類直覺精度的場景，例如金融與會計。
# 它通常比 float 慢，因此不建議在大量純數值運算中隨意使用。
print(Decimal("0.1") + Decimal("0.2"))  # 0.3
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))  # True

# 最後用 timeit 比較速度差異。這裡重點不是絕對數值，而是兩者的量級差距。
t1 = timeit.timeit(lambda: 0.1 * 999, number=100_000)
t2 = timeit.timeit(lambda: Decimal("0.1") * 999, number=100_000)
print(f"float: {t1:.3f}s  Decimal: {t2:.3f}s（Decimal 約慢 {t2 / t1:.0f} 倍）")
