# R01. 字串分割與匹配（2.1–2.3）
#
# 本範例示範三件常用技巧：
# 1) 用 re.split() 以「多種分隔符」切字串。
# 2) 用 startswith()/endswith() 做快速前後綴判斷。
# 3) 用 fnmatch/fnmatchcase 進行 shell 風格萬用字元匹配。

import re
from fnmatch import fnmatch, fnmatchcase

# ── 2.1 多界定符分割 ──────────────────────────────────
line = "asdf fjdk; afed, fjek,asdf, foo"

# [;,\s]\s* 的意思：
# - [;,\s]：先吃掉一個分隔符（分號、逗號或空白）。
# - \s*：再吃掉後面可能出現的 0~多個空白。
# 這樣可把「逗號後有空白」與「分號後無空白」統一處理。
print(re.split(r"[;,\s]\s*", line))
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# (?:,|;|\s) 是非捕獲分組：
# - 功能上把「逗號 / 分號 / 空白」視為同一群分隔符。
# - ?: 代表不建立捕獲群組，可避免 split 結果夾帶分隔符內容。
print(re.split(r"(?:,|;|\s)\s*", line))
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# ── 2.2 開頭/結尾匹配 ────────────────────────────────
filename = "spam.txt"
# endswith/startswith 是字串方法，通常比手寫 slicing 更直觀。
print(filename.endswith(".txt"))  # True
print(filename.startswith("file:"))  # False

# 同時檢查多種後綴：
# - endswith 可直接吃 tuple，代表任一後綴符合即可。
# - 常用在批次篩副檔名。
filenames = ["Makefile", "foo.c", "bar.py", "spam.c", "spam.h"]
print([name for name in filenames if name.endswith((".c", ".h"))])
# ['foo.c', 'spam.c', 'spam.h']

# ── 2.3 Shell 通配符匹配 ─────────────────────────────
# fnmatch 使用 shell 風格萬用字元：
# - *：任意長度任意字元
# - ?：任意單一字元
# - [0-9]：字元集合或範圍
print(fnmatch("foo.txt", "*.txt"))  # True
print(fnmatch("Dat45.csv", "Dat[0-9]*"))  # True

# fnmatchcase：永遠區分大小寫，不受作業系統預設行為影響。
print(fnmatchcase("foo.txt", "*.TXT"))  # False

addresses = ["5412 N CLARK ST", "1060 W ADDISON ST", "1039 W GRANVILLE AVE"]
# 篩選以 " ST" 結尾的地址。
print([a for a in addresses if fnmatchcase(a, "* ST")])
# ['5412 N CLARK ST', '1060 W ADDISON ST']
