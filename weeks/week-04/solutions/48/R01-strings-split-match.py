# R01. 字串分割與匹配（2.1–2.3）
# re.split() 多分隔符 / startswith / endswith / fnmatch
# 重點：同一份資料可以用「正則」與「檔名通配」兩種思維處理

import re
from fnmatch import fnmatch, fnmatchcase

# ── 2.1 多界定符分割 ──────────────────────────────────
line = "asdf fjdk; afed, fjek,asdf, foo"
# 以分號、逗號、空白任一符號作為切點，\s* 表示可有可無的空白
print(re.split(r"[;,\s]\s*", line))
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# 非捕獲分組：分組但不保留分隔符
# (?:...) 只做分組，不建立可回溯的捕獲群組
print(re.split(r"(?:,|;|\s)\s*", line))
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# ── 2.2 開頭/結尾匹配 ────────────────────────────────
filename = "spam.txt"
# endswith / startswith 適合做快速且可讀性高的前後綴判斷
print(filename.endswith(".txt"))  # True
print(filename.startswith("file:"))  # False

# 同時檢查多種後綴 → 傳入 tuple（不能傳 list）
filenames = ["Makefile", "foo.c", "bar.py", "spam.c", "spam.h"]
# 這裡用 tuple 指定多個副檔名條件
print([name for name in filenames if name.endswith((".c", ".h"))])
# ['foo.c', 'spam.c', 'spam.h']

# ── 2.3 Shell 通配符匹配 ─────────────────────────────
# fnmatch 風格類似 shell：* 任意字元、? 單一字元、[0-9] 範圍
print(fnmatch("foo.txt", "*.txt"))  # True
print(fnmatch("Dat45.csv", "Dat[0-9]*"))  # True

# fnmatchcase 強制區分大小寫
print(fnmatchcase("foo.txt", "*.TXT"))  # False

addresses = ["5412 N CLARK ST", "1060 W ADDISON ST", "1039 W GRANVILLE AVE"]
# 僅挑出結尾為 ST 的地址
print([a for a in addresses if fnmatchcase(a, "* ST")])
# ['5412 N CLARK ST', '1060 W ADDISON ST']
