# R01. 字串分割與匹配（2.1–2.3）
# re.split() 多分隔符 / startswith / endswith / fnmatch

import re
from fnmatch import fnmatch, fnmatchcase

# ── 2.1 多界定符分割 ──────────────────────────────────
# 處理含有多種不同分隔符（空格、分號、逗號）的字串
line = "asdf fjdk; afed, fjek,asdf, foo"

# 使用正規表示式 re.split()
# [;,\s] 表示匹配分號、逗號或空白字元
# \s* 表示匹配 0 個或多個後續的空白，確保能處理像 ", " 這種組合
print(re.split(r"[;,\s]\s*", line))
# 輸出：['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# 非捕獲分組 (?:...)：
# 在正規表示式中使用分組時，如果不希望分割出的結果包含分隔符本身，
# 應使用 (?:...) 非捕獲分組。
print(re.split(r"(?:,|;|\s)\s*", line))
# 輸出：['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# ── 2.2 開頭/結尾匹配 ────────────────────────────────
filename = "spam.txt"
# endswith：檢查字串是否以特定字串結尾
print(filename.endswith(".txt"))  # True
# startswith：檢查字串是否以特定字串開頭
print(filename.startswith("file:"))  # False

# 同時檢查多種後綴：
# 注意：當需要匹配多個可能性時，必須封裝成 tuple ()，
# 若使用 list [] 會觸發 TypeError。
filenames = ["Makefile", "foo.c", "bar.py", "spam.c", "spam.h"]
# 篩選出所有以 .c 或 .h 結尾的檔案名稱
print([name for name in filenames if name.endswith((".c", ".h"))])
# 輸出：['foo.c', 'spam.c', 'spam.h']

# ── 2.3 Shell 通配符匹配 ─────────────────────────────
# fnmatch 提供類似 Unix Shell 的萬用字元匹配功能

# * 代表匹配任意長度的字元
print(fnmatch("foo.txt", "*.txt"))  # True

# [0-9] 代表匹配任何一個數字
print(fnmatch("Dat45.csv", "Dat[0-9]*"))  # True

# fnmatchcase：強制區分大小寫
# fnmatch 在 Windows 系統下可能不區分大小寫（隨系統特性），
# 若要確保在所有平台都能精確區分大小寫，應使用 fnmatchcase。
print(fnmatchcase("foo.txt", "*.TXT"))  # False

addresses = ["5412 N CLARK ST", "1060 W ADDISON ST", "1039 W GRANVILLE AVE"]
# 使用列表推導式篩選出以 " ST" 結尾的地址
print([a for a in addresses if fnmatchcase(a, "* ST")])
# 輸出：['5412 N CLARK ST', '1060 W ADDISON ST']