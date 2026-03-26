# R05. 數字基礎：四捨五入、進制、格式化（3.1–3.4）
# round / Decimal / format / bin / oct / hex

from decimal import Decimal, localcontext
import math

# ── 3.1 四捨五入 ──────────────────────────────────────
# round(數值, 小數位數)
print(round(1.27, 1))  # 1.3
print(round(1.25361, 3))  # 1.254
# Python 的 round 採「銀行家捨入」（ties to even）
# 當剛好在 0.5 中間值時，會捨入到最近的偶數
print(round(0.5))  # 0（銀行家捨入，取最近偶數）
print(round(2.5))  # 2

a = 1627731
# 位數可給負數：-2 代表以百位為單位四捨五入
print(round(a, -2))  # 1627700（對百位四捨五入）

# ── 3.2 精確浮點數 ────────────────────────────────────
# 一般 float 使用二進位近似表示，可能出現微小誤差
print(4.2 + 2.1)  # 6.300000000000001（有誤差）
# Decimal 以十進位字串建立，可保留精確十進位運算
da, db = Decimal("4.2"), Decimal("2.1")
print(da + db)  # 6.3（精確）

# localcontext() 可暫時調整 Decimal 計算精度
with localcontext() as ctx:
    ctx.prec = 3
    print(Decimal("1.3") / Decimal("1.7"))  # 0.765

# math.fsum 修正大數+小數精度
# fsum 以更穩定的演算法做總和，降低累積誤差
print(math.fsum([1.23e18, 1, -1.23e18]))  # 1.0（正確）

# ── 3.3 數字格式化 ────────────────────────────────────
x = 1234.56789
# 固定小數 2 位
print(format(x, "0.2f"))  # '1234.57'
# 右對齊，欄寬 10，保留 1 位小數
print(format(x, ">10.1f"))  # '    1234.6'
# 加入千分位逗號
print(format(x, ","))  # '1,234.56789'
# 同時指定千分位與小數位
print(format(x, "0,.2f"))  # '1,234.57'
# 科學記號表示法
print(format(x, "e"))  # '1.234568e+03'

# ── 3.4 二八十六進制 ──────────────────────────────────
n = 1234
# 內建函式會帶前綴：0b / 0o / 0x
print(bin(n), oct(n), hex(n))  # 0b10011010010 0o2322 0x4d2
# format 可輸出不含前綴的進位字串
print(format(n, "b"), format(n, "x"))  # 10011010010 4d2
# int(字串, 基底) 可把不同進位字串轉回十進位整數
print(int("4d2", 16), int("2322", 8))  # 1234 1234
