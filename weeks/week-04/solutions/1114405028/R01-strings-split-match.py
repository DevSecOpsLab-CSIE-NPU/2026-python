# R01. 字串分割與匹配（2.1–2.3）
# re.split() 多分隔符 / startswith / endswith / fnmatch

import re
from fnmatch import fnmatch, fnmatchcase

# ── 2.1 多界定符分割 ──────────────────────────────────
line = "asdf fjdk; afed, fjek,asdf, foo"
print(re.split(r"[;,\s]\s*", line))  # 以分號、逗號或空白做切割，\s* 吃掉後續空白
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# 非捕獲分組：分組但不保留分隔符
print(re.split(r"(?:,|;|\s)\s*", line))  # (?:...) 只分組不捕獲，常用於純結構用途
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# ── 2.2 開頭/結尾匹配 ────────────────────────────────
filename = "spam.txt"
print(filename.endswith(".txt"))  # 檢查副檔名是否為 .txt，回傳布林值
print(filename.startswith("file:"))  # 檢查是否為特定前綴（例如 URL scheme）

# 同時檢查多種後綴 → 傳入 tuple（不能傳 list）
filenames = ["Makefile", "foo.c", "bar.py", "spam.c", "spam.h"]
print([name for name in filenames if name.endswith((".c", ".h"))])  # tuple 可一次比對多種後綴
# ['foo.c', 'spam.c', 'spam.h']

# ── 2.3 Shell 通配符匹配 ─────────────────────────────
print(fnmatch("foo.txt", "*.txt"))  # * 代表任意字元序列
print(fnmatch("Dat45.csv", "Dat[0-9]*"))  # [0-9] 代表單一數字字元，後接 * 代表可延伸

# fnmatchcase 強制區分大小寫
print(fnmatchcase("foo.txt", "*.TXT"))  # 在大小寫敏感環境可避免平台差異

addresses = ["5412 N CLARK ST", "1060 W ADDISON ST", "1039 W GRANVILLE AVE"]
print([a for a in addresses if fnmatchcase(a, "* ST")])  # 篩出以空白+ST 結尾的地址
# ['5412 N CLARK ST', '1060 W ADDISON ST']
