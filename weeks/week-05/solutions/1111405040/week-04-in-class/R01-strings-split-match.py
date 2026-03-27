"""
R01: 字串切分與樣式比對。

示範重點：
1. 用 `re.split()` 依多種分隔符號切字串。
2. 用 `startswith()` 與 `endswith()` 檢查前後綴。
3. 用 `fnmatch()` 模擬 shell 萬用字元比對。
"""

import re
from fnmatch import fnmatch, fnmatchcase

# 同一行文字中同時出現空白、分號與逗號。
# 這種資料不適合只用 `split(",")`，因為分隔符號不只一種。
line = "asdf fjdk; afed, fjek,asdf, foo"

# `[;,\s]` 代表「分號、逗號或任一空白字元」。
# `\s*` 代表分隔符號後面若還有空白，也一起吃掉。
print(re.split(r"[;,\s]\s*", line))
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# 非捕獲群組 `(?:...)` 也能達到相同目的。
# 這種寫法把不同分隔符號明確列出來，閱讀上更直觀。
print(re.split(r"(?:,|;|\s)\s*", line))
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# `endswith()` 與 `startswith()` 適合拿來做簡單、快速的前後綴判斷。
filename = "spam.txt"
print(filename.endswith(".txt"))  # True
print(filename.startswith("file:"))  # False

# `endswith()` 可以直接接受 tuple，
# 方便一次篩選多種副檔名。
filenames = ["Makefile", "foo.c", "bar.py", "spam.c", "spam.h"]
print([name for name in filenames if name.endswith((".c", ".h"))])
# ['foo.c', 'spam.c', 'spam.h']

# `fnmatch()` 使用 shell 風格萬用字元：
# `*` 代表任意長度字元，`[0-9]` 代表數字範圍。
print(fnmatch("foo.txt", "*.txt"))  # True
print(fnmatch("Dat45.csv", "Dat[0-9]*"))  # True

# `fnmatchcase()` 不會依作業系統自動調整大小寫規則，
# 因此行為比較固定，適合要明確區分大小寫的情境。
print(fnmatchcase("foo.txt", "*.TXT"))  # False

addresses = ["5412 N CLARK ST", "1060 W ADDISON ST", "1039 W GRANVILLE AVE"]
print([address for address in addresses if fnmatchcase(address, "* ST")])
# ['5412 N CLARK ST', '1060 W ADDISON ST']
