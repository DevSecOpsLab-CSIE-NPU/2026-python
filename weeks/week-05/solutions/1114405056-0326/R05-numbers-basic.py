from decimal import Decimal, localcontext
import math

# ── 四捨五入（Banker's Rounding）─────────────────────────
# Python 的 round() 採「銀行家捨入」：.5 捨入到最近的偶數
print(round(1.27, 1))      # 1.3
print(round(1.25361, 3))   # 1.254
print(round(0.5))          # 0  ← .5 捨入到偶數 0
print(round(2.5))          # 2  ← .5 捨入到偶數 2

# 負數精度：捨入到百位
a = 1627731
print(round(a, -2))        # 1627700

# ── 浮點數精度問題與 Decimal ──────────────────────────────
# 浮點數的二進位表示會產生誤差
print(4.2 + 2.1)           # 6.300000000000001（浮點誤差）

# Decimal 以十進位字串初始化，可避免二進位轉換誤差
da, db = Decimal("4.2"), Decimal("2.1")
print(da + db)             # 6.3（精確）

# localcontext：暫時改變 Decimal 的精度（有效位數）
with localcontext() as ctx:
    ctx.prec = 3           # 指定 3 位有效數字
    print(Decimal("1.3") / Decimal("1.7"))  # 0.765

# math.fsum：對浮點數串列做精確加總，避免累積誤差
print(math.fsum([1.23e18, 1, -1.23e18]))   # 1.0（一般加法會得 0.0）

# ── 數字格式化輸出 ────────────────────────────────────────
x = 1234.56789
print(format(x, "0.2f"))    # 1234.57      → 固定 2 位小數
print(format(x, ">10.1f"))  #    1234.6    → 右對齊寬度 10
print(format(x, ","))       # 1,234.56789  → 千分位逗號
print(format(x, "0,.2f"))   # 1,234.57     → 千分位 + 2 位小數
print(format(x, "e"))       # 1.234568e+03 → 科學記號

# ── 進位制轉換 ────────────────────────────────────────────
n = 1234
print(bin(n), oct(n), hex(n))          # 0b10011010010  0o2322  0x4d2
print(format(n, "b"), format(n, "x"))  # 10011010010  4d2（不含前綴）

# 字串轉整數：第二個參數指定來源進位基底
print(int("4d2", 16), int("2322", 8))  # 1234  1234
