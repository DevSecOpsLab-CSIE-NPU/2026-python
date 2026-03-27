"""
R05: 數值處理基礎。

示範重點：
1. `round()` 的行為。
2. `Decimal` 避免浮點數誤差。
3. 數字格式化與不同進位表示。
"""

from decimal import Decimal, localcontext
import math

# `round()` 的第二個參數代表保留到哪一位。
print(round(1.27, 1))  # 1.3
print(round(1.25361, 3))  # 1.254

# Python 的 `round()` 採用銀行家捨入，
# .5 會往最近的偶數靠攏。
print(round(0.5))  # 0
print(round(2.5))  # 2

# 傳入負數位數時，代表往十位、百位、千位做四捨五入。
a = 1627731
print(round(a, -2))  # 1627700

# 浮點數採二進位表示，因此有些十進位小數無法精準表達。
print(4.2 + 2.1)  # 6.300000000000001

# `Decimal` 用字串建立時，可以保留十進位精度。
da, db = Decimal("4.2"), Decimal("2.1")
print(da + db)  # 6.3

# `localcontext()` 可在區塊內暫時調整計算精度。
with localcontext() as ctx:
    ctx.prec = 3
    print(Decimal("1.3") / Decimal("1.7"))  # 0.765

# `math.fsum()` 在累加大數與小數混合資料時，誤差通常較小。
print(math.fsum([1.23e18, 1, -1.23e18]))  # 1.0

x = 1234.56789
print(format(x, "0.2f"))  # '1234.57'
print(format(x, ">10.1f"))  # '    1234.6'
print(format(x, ","))  # '1,234.56789'
print(format(x, "0,.2f"))  # '1,234.57'
print(format(x, "e"))  # '1.234568e+03'

# 進位轉換常見於位元操作、序列化或除錯輸出。
n = 1234
print(bin(n), oct(n), hex(n))  # 0b10011010010 0o2322 0x4d2
print(format(n, "b"), format(n, "x"))  # 10011010010 4d2
print(int("4d2", 16), int("2322", 8))  # 1234 1234
