# R05. 數字基礎：四捨五入、進制、格式化（3.1–3.4）
# round / Decimal / format / bin / oct / hex
# 本檔目標：建立「數值顯示」與「數值計算精度」是兩件事的觀念。
# - 顯示：可用 format/round 控制輸出外觀
# - 計算：若要求精確（例如金額），請優先使用 Decimal

from decimal import Decimal, localcontext
import math

# ── 3.1 四捨五入 ──────────────────────────────────────
# round(x, n) 的 n 表示「保留到小數點後 n 位」。
print(round(1.27, 1))  # 1.3
print(round(1.25361, 3))  # 1.254
# Python 採銀行家捨入（ties to even）：剛好 .5 時取最近偶數。
print(round(0.5))  # 0（銀行家捨入，取最近偶數）
print(round(2.5))  # 2

a = 1627731
# n 為負數時，代表往十位、百位、千位做四捨五入。
print(round(a, -2))  # 1627700（對百位四捨五入）

# ── 3.2 精確浮點數 ────────────────────────────────────
# 浮點數以二進位表示，很多十進位小數無法被精確表示。
print(4.2 + 2.1)  # 6.300000000000001（有誤差）
# Decimal 用字串建立，可避免把 float 誤差帶入。
da, db = Decimal("4.2"), Decimal("2.1")
print(da + db)  # 6.3（精確）

with localcontext() as ctx:
    # localcontext 可在區塊內暫時調整精度，不影響全域設定。
    ctx.prec = 3
    print(Decimal("1.3") / Decimal("1.7"))  # 0.765

# math.fsum 修正大數+小數精度
# sum 在極端數值混合時容易累積誤差；fsum 採補償演算法更穩定。
print(math.fsum([1.23e18, 1, -1.23e18]))  # 1.0（正確）

# ── 3.3 數字格式化 ────────────────────────────────────
x = 1234.56789
# 0.2f：固定小數格式，四捨五入至小數 2 位。
print(format(x, "0.2f"))  # '1234.57'
# >10.1f：右對齊、總寬 10、小數 1 位。
print(format(x, ">10.1f"))  # '    1234.6'
# ,：加千分位分隔符，便於閱讀大量數字。
print(format(x, ","))  # '1,234.56789'
print(format(x, "0,.2f"))  # '1,234.57'
# e：科學記號表示法。
print(format(x, "e"))  # '1.234568e+03'

# ── 3.4 二八十六進制 ──────────────────────────────────
n = 1234
# bin/oct/hex 會帶前綴 0b/0o/0x，表示基底。
print(bin(n), oct(n), hex(n))  # 0b10011010010 0o2322 0x4d2
# format 不帶前綴，常用於純輸出。
print(format(n, "b"), format(n, "x"))  # 10011010010 4d2
# int(字串, 基底) 可以把不同進制字串轉回十進位整數。
print(int("4d2", 16), int("2322", 8))  # 1234 1234
