# U01. 字串分割與匹配的陷阱（2.1–2.11）
# 本範例說明常見字串處理誤區，以及更安全的用法。
# 包含：re.split 捕獲分組如何保留分隔符、startswith 參數必須是 tuple，
# 以及 strip 只會清除頭尾空白、不會改變中間空白。

import re

# ── 捕獲分組保留分隔符（2.1）─────────────────────────
line = "asdf fjdk; afed, fjek,asdf, foo"
# 使用捕獲分組時，re.split 會把分隔符也當成結果的一部分回傳
fields = re.split(r"(;|,|\s)\s*", line)
# 偶數索引儲存實際內容，奇數索引儲存分隔符
values = fields[::2]
delimiters = fields[1::2] + [""]  # 最後沒有分隔符時補空字串
rebuilt = "".join(v + d for v, d in zip(values, delimiters))
print(rebuilt)  # 'asdf fjdk;afed,fjek,asdf,foo'

# ── startswith 必須傳 tuple（2.2）────────────────────
url = "http://www.python.org"
choices = ["http:", "ftp:"]
# startswith() 不支援 list，必須改成 tuple 才能一次比對多個前綴
try:
    url.startswith(choices)  # type: ignore[arg-type]
except TypeError as e:
    print(f"TypeError: {e}")  # 不能傳 list！
print(url.startswith(tuple(choices)))  # True（轉成 tuple 才行）

# ── strip 只處理頭尾，不處理中間（2.11）──────────────
s = "  hello     world  "
print(repr(s.strip()))  # 'hello     world'（中間多餘空白還在）
print(repr(s.replace(" ", "")))  # 'helloworld'（過頭，連詞間空白也消）
# 正確做法：先 strip，再把連續空白壓成一個
print(repr(re.sub(r"\s+", " ", s.strip())))  # 'hello world'（正確）

# 生成器逐行清理（高效，不預先載入整個資料）
lines = ["  apple  \n", "  banana  \n"]
for line in (l.strip() for l in lines):
    # 這裡用的是生成器表達式，依序產生每一行的 strip 結果
    print(line)
