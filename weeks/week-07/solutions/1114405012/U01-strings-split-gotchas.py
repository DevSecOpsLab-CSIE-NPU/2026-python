"""U01 字串分割與匹配的陷阱（2.1–2.11）。"""

# 核心提醒：捕獲群組會保留分隔符、startswith 參數型別要正確、strip 只修頭尾

import re

# ── 捕獲分組保留分隔符（2.1）─────────────────────────
line = "asdf fjdk; afed, fjek,asdf, foo"
fields = re.split(r"(;|,|\s)\s*", line)
# 使用捕獲群組分割時，分隔符也會留在結果中
values = fields[::2]  # 偶數索引 = 實際值
delimiters = fields[1::2] + [""]
rebuilt = "".join(v + d for v, d in zip(values, delimiters))
print(rebuilt)  # 'asdf fjdk;afed,fjek,asdf,foo'

# ── startswith 必須傳 tuple（2.2）────────────────────
url = "http://www.python.org"
choices = ["http:", "ftp:"]
try:
    url.startswith(choices)  # type: ignore[arg-type]
except TypeError as e:
    print(f"TypeError: {e}")  # 不能傳 list！
print(url.startswith(tuple(choices)))  # True（轉成 tuple 才行）

# ── strip 只處理頭尾，不處理中間（2.11）──────────────
s = "  hello     world  "
print(repr(s.strip()))  # 'hello     world'（中間多餘空白還在）
print(repr(s.replace(" ", "")))  # 'helloworld'（過頭，連詞間空白也消）
print(repr(re.sub(r"\s+", " ", s.strip())))  # 'hello world'（正確）

# 生成器逐行清理（高效，不預載入記憶體）
lines = ["  apple  \n", "  banana  \n"]
for line in (l.strip() for l in lines):
    print(line)
