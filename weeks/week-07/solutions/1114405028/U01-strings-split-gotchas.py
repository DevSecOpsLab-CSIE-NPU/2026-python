# U01. 字串分割與匹配的陷阱（2.1–2.11）
# 本程式示範字串處理中的常見陷阱和最佳實踐：
# 2.1 捕獲分組保留分隔符 - 使用正則表達式分割時保留分隔符
# 2.2 startswith 必須傳 tuple - startswith() 方法的正確用法
# 2.11 strip 只處理頭尾 - strip() 方法的行為說明

import re

# ── 捕獲分組保留分隔符（2.1）─────────────────────────
# 問題：re.split() 預設會丟棄分隔符，但有時需要保留它們
# 解決方案：使用捕獲分組 ( ) 將分隔符包含在分割結果中
line = "asdf fjdk; afed, fjek,asdf, foo"

# 使用捕獲分組分割，保留分隔符
# r"(;|,|\s)\s*" 表示匹配分號、逗號或空白字元，後面可選空白
fields = re.split(r"(;|,|\s)\s*", line)

# 分割結果包含：實際值、分隔符、實際值、分隔符...
# fields[::2] 取偶數索引（實際值）
values = fields[::2]  # 偶數索引 = 實際值
# fields[1::2] 取奇數索引（分隔符）
delimiters = fields[1::2] + [""]

# 重建原始字串：值 + 分隔符
rebuilt = "".join(v + d for v, d in zip(values, delimiters))
print(rebuilt)  # 'asdf fjdk;afed,fjek,asdf,foo'

# ── startswith 必須傳 tuple（2.2）────────────────────
# 問題：startswith() 的第一個參數必須是字串或字串元組，不能是列表
url = "http://www.python.org"
choices = ["http:", "ftp:"]

# 錯誤用法：傳入列表會引發 TypeError
try:
    url.startswith(choices)  # type: ignore[arg-type]
except TypeError as e:
    print(f"TypeError: {e}")  # 不能傳 list！

# 正確用法：轉換為元組
print(url.startswith(tuple(choices)))  # True（轉成 tuple 才行）

# ── strip 只處理頭尾，不處理中間（2.11）──────────────
# 問題：strip() 只移除字串頭尾的空白字元，中間的空白不會被處理
s = "  hello     world  "

# strip() 只處理頭尾
print(repr(s.strip()))  # 'hello     world'（中間多餘空白還在）

# replace() 會移除所有空白，過於激進
print(repr(s.replace(" ", "")))  # 'helloworld'（過頭，連詞間空白也消）

# 正確做法：使用正則表達式合併多餘空白
print(repr(re.sub(r"\s+", " ", s.strip())))  # 'hello world'（正確）

# 生成器逐行清理（高效，不預載入記憶體）
# 對於大量資料，使用生成器避免記憶體浪費
lines = ["  apple  \n", "  banana  \n"]

# 生成器表達式：對每一行執行 strip()
for line in (l.strip() for l in lines):
    print(line)
