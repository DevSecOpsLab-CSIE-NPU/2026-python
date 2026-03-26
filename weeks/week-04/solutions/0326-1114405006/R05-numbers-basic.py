# R05. 數字基礎：四捨五入、進制、格式化（3.1–3.4）
#
# 本檔案示範 Python 常見數值處理主題：
# 1) round() 的四捨五入規則
# 2) Decimal 的高精度十進位計算
# 3) format() 的數字格式化語法
# 4) bin / oct / hex 與進位轉換
#
# 重點觀念：
# - 浮點數（float）是二進位近似值，不保證十進位精確
# - 需要財務或高精度時，優先使用 Decimal

from decimal import Decimal, localcontext
import math

# ── 3.1 四捨五入 ──────────────────────────────────────
# round(number, ndigits)
# - ndigits > 0：保留小數位數
# - ndigits = 0 或省略：四捨五入到整數
# - ndigits < 0：在十位、百位、千位做四捨五入
print(round(1.27, 1))  # 1.3
print(round(1.25361, 3))  # 1.254

# Python 採用銀行家捨入（round half to even）：
# 剛好在 .5 時，會捨入到「最近的偶數」
print(round(0.5))  # 0（銀行家捨入，取最近偶數）
print(round(2.5))  # 2

a = 1627731
# ndigits = -2 表示對百位四捨五入
print(round(a, -2))  # 1627700（對百位四捨五入）

# ── 3.2 精確浮點數 ────────────────────────────────────
# 一般 float 可能出現看似「怪異」的小誤差，因為底層是二進位表示
print(4.2 + 2.1)  # 6.300000000000001（有誤差）

# Decimal 使用十進位表示，適合金額與精準十進位運算
# 建議以字串建立 Decimal，避免把 float 的誤差帶進來
da, db = Decimal("4.2"), Decimal("2.1")
print(da + db)  # 6.3（精確）

# localcontext 可在區塊中暫時調整 Decimal 運算環境（例如有效位數）
with localcontext() as ctx:
    ctx.prec = 3
    print(Decimal("1.3") / Decimal("1.7"))  # 0.765

# math.fsum 修正大數+小數精度
# 在大量或差距很大的浮點加總中，fsum 比 sum 更穩定
print(math.fsum([1.23e18, 1, -1.23e18]))  # 1.0（正確）

# ── 3.3 數字格式化 ────────────────────────────────────
x = 1234.56789

# 常見格式規格：
# - 0.2f   ：固定小數 2 位
# - >10.1f ：總寬度 10、靠右、1 位小數
# - ,      ：千分位逗號
# - 0,.2f  ：千分位 + 小數 2 位
# - e      ：科學記號
print(format(x, "0.2f"))  # '1234.57'
print(format(x, ">10.1f"))  # '    1234.6'
print(format(x, ","))  # '1,234.56789'
print(format(x, "0,.2f"))  # '1,234.57'
print(format(x, "e"))  # '1.234568e+03'

# ── 3.4 二八十六進制 ──────────────────────────────────
n = 1234

# 轉換為字串表示（含前綴）
print(bin(n), oct(n), hex(n))  # 0b10011010010 0o2322 0x4d2

# format 可產生不含前綴的表示
print(format(n, "b"), format(n, "x"))  # 10011010010 4d2

# int(字串, 進位) 可將不同進位字串轉回十進位整數
print(int("4d2", 16), int("2322", 8))  # 1234 1234
