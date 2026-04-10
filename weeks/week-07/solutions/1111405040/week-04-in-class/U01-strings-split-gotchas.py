"""
U01. 字串分割與匹配的常見陷阱。

這份範例示範三個觀念：
1. `re.split()` 若使用捕獲群組，分隔符本身也會被保留下來。
2. `startswith()` / `endswith()` 若要一次比對多個前綴，必須傳 tuple。
3. `strip()` 只會處理頭尾，不會整理字串中間的空白。
"""

import re


# ── 1. 捕獲群組會把分隔符一起保留下來 ───────────────────────
line = "asdf fjdk; afed, fjek,asdf, foo"

# `(;|,|\s)` 是捕獲群組，所以分隔符會出現在結果中。
# `\s*` 代表分隔符後面如果還有空白，也一起吃掉。
fields = re.split(r"(;|,|\s)\s*", line)

# 保留下來的列表會呈現：
# 值, 分隔符, 值, 分隔符, ...
# 因此偶數索引是值，奇數索引是分隔符。
values = fields[::2]
delimiters = fields[1::2] + [""]

# 重新把值與分隔符組回去，可以驗證拆分過程是否正確。
rebuilt = "".join(value + delimiter for value, delimiter in zip(values, delimiters))
print(rebuilt)  # 'asdf fjdk;afed,fjek,asdf,foo'


# ── 2. startswith 必須傳 tuple，不能直接傳 list ───────────────
url = "http://www.python.org"
choices = ["http:", "ftp:"]

try:
    # 這裡故意示範錯法。
    # `startswith()` 第二個參數接受單一字串或 tuple，不接受 list。
    url.startswith(choices)  # type: ignore[arg-type]
except TypeError as error:
    print(f"TypeError: {error}")

# 轉成 tuple 之後，才可以一次判斷多個候選前綴。
print(url.startswith(tuple(choices)))  # True


# ── 3. strip 只整理頭尾，不會碰中間 ─────────────────────────
s = "  hello     world  "

# 只移除頭尾空白，中間連續空白仍保留。
print(repr(s.strip()))  # 'hello     world'

# `replace(" ", "")` 會把所有空白都拿掉，常常比需求更激進。
print(repr(s.replace(" ", "")))  # 'helloworld'

# 若目標是把中間的多個空白壓成一格，通常用正則會比較準確。
print(repr(re.sub(r"\s+", " ", s.strip())))  # 'hello world'


# ── 4. 生成器可逐行清理資料，不必一次先建立整份新列表 ─────────
lines = ["  apple  \n", "  banana  \n"]

# `(l.strip() for l in lines)` 是生成器運算式。
# 它會在 for 迴圈逐筆產生結果，資料量大時會比較省記憶體。
for cleaned_line in (raw_line.strip() for raw_line in lines):
    print(cleaned_line)
