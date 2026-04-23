# R05. 數字基礎：四捨五入、進制、格式化（3.1–3.4）
# round / Decimal / format / bin / oct / hex

from decimal import Decimal, localcontext
import math

# ── 3.1 四捨五入 ──────────────────────────────────────
# round() 的第二個參數表示要捨入到的小數位數；負值可捨入到整數位
print(round(1.27, 1))  # 1.3
print(round(1.25361, 3))  # 1.254
print(round(0.5))  # 0（銀行家捨入，取最近偶數）
print(round(2.5))  # 2

a = 1627731
print(round(a, -2))  # 1627700（對百位四捨五入）

# ── 3.2 精確浮點數 ────────────────────────────────────
# float 有表示誤差，使用 Decimal 以取得精確十進位運算
print(4.2 + 2.1)  # 6.300000000000001（有誤差）
da, db = Decimal("4.2"), Decimal("2.1")
print(da + db)  # 6.3（精確）

with localcontext() as ctx:
    ctx.prec = 3
    print(Decimal("1.3") / Decimal("1.7"))  # 0.765（設定精度）

# math.fsum 可以減少大量數值相加時的累積誤差
print(math.fsum([1.23e18, 1, -1.23e18]))  # 1.0（正確）

# ── 3.3 數字格式化 ────────────────────────────────────
x = 1234.56789
print(format(x, "0.2f"))  # 固定顯示 2 位小數
print(format(x, ">10.1f"))  # 寬度 10，靠右對齊，顯示 1 位小數
print(format(x, ","))  # 加上千位分隔符
print(format(x, "0,.2f"))  # 千位分隔符 + 2 位小數
print(format(x, "e"))  # 科學記號表示法

# ── 3.4 二八十六進制 ──────────────────────────────────
n = 1234
print(bin(n), oct(n), hex(n))  # 2 進位、8 進位、16 進位表示法
print(format(n, "b"), format(n, "x"))  # 以格式化取得不同進制字串
print(int("4d2", 16), int("2322", 8))  # 解析 16 進制與 8 進制字串
