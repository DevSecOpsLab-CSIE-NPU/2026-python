import re

# ── bytes 物件基本操作 ────────────────────────────────────
# bytes 是「不可變的位元組序列」，字面值以 b"..." 表示
data = b"Hello World"

# 切片：取前 5 個位元組（與 str 切片語法相同）
print(data[0:5])                          # b'Hello'

# startswith / split / replace 與 str 同名方法，但參數須為 bytes
print(data.startswith(b"Hello"))          # True
print(data.split())                       # [b'Hello', b'World']
print(data.replace(b"Hello", b"Hello Cruel"))  # 替換位元組序列

# ── 用正規表示式分割 bytes ────────────────────────────────
# 在 pattern 前加 rb"..." 表示「原始位元組字串」
raw = b"FOO:BAR,SPAM"
print(re.split(rb"[:,]", raw))            # 以 : 或 , 分割

# ── str 與 bytes 的索引差異 ──────────────────────────────
a = "Hello"     # str（Unicode 字串）
b = b"Hello"    # bytes（位元組序列）

print(a[0])     # 'H'    → str 索引回傳單字元字串
print(b[0])     # 72     → bytes 索引回傳整數（ASCII 碼）

# ── 將格式化字串編碼為 bytes ─────────────────────────────
# .encode("ascii") 把 str 轉成 bytes；ascii 只支援 0–127
formatted = "{:10s} {:10d}".format("ACME", 100).encode("ascii")
print(formatted)   # b'ACME           100'
