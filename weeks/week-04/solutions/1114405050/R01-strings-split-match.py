# R01. 字串分割與匹配（2.1–2.3）
# re.split() 多分隔符 / startswith / endswith / fnmatch
"""
本範例展示三種常見的字串處理技巧：
 1) 使用 re.split() 支援多種分隔符的字串分割
 2) 用 startswith()/endswith() 進行前綴/後綴比對
 3) 用 fnmatch() 進行類似 shell 通配符的模式匹配

這些技巧在處理檔名、日誌、設定檔、資料清理等情境時非常常用。
"""

import re
from fnmatch import fnmatch, fnmatchcase

# ── 2.1 多界定符分割 ──────────────────────────────────
# 當字串有多種分隔符（例如逗號、分號、空白）時，可以用 re.split() 一次處理。
line = "asdf fjdk; afed, fjek,asdf, foo"

# r"[;,\s]\s*"：
#  - [;,\s]   : 匹配分號、逗號或任意空白（空白、換行、制表符等）
#  - \s*      : 匹配分隔符後可能存在的額外空白
# 這樣可以同時處理 ","、";" 與空格分隔的情況。
print(re.split(r"[;,\s]\s*", line))
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# 如果使用捕獲分組 ( ... )，re.split 會把分隔符也當作結果之一。
# 若不想保留分隔符，可以用「非捕獲分組」(?: ... )
print(re.split(r"(?:,|;|\s)\s*", line))
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# ── 2.2 開頭/結尾匹配 ────────────────────────────────
# str.startswith() / str.endswith() 可以檢查字串是否以指定前綴/後綴開始/結尾。
filename = "spam.txt"
print(filename.endswith(".txt"))  # True
print(filename.startswith("file:"))  # False

# 可以同時檢查多個後綴（參數必須是 tuple，不能是 list）
filenames = ["Makefile", "foo.c", "bar.py", "spam.c", "spam.h"]
print([name for name in filenames if name.endswith((".c", ".h"))])
# ['foo.c', 'spam.c', 'spam.h']

# ── 2.3 Shell 通配符匹配 ─────────────────────────────
# fnmatch 提供類似 shell 的檔名通配符語法：
#   *  : 任意字元序列
#   ?  : 單一任意字元
#   [seq] : 任意在 seq 中的字元
print(fnmatch("foo.txt", "*.txt"))  # True
print(fnmatch("Dat45.csv", "Dat[0-9]*"))  # True

# fnmatch 會根據作業系統決定是否忽略大小寫（Windows 通常忽略），
# 若要強制區分大小寫，請使用 fnmatchcase。
print(fnmatchcase("foo.txt", "*.TXT"))  # False

addresses = ["5412 N CLARK ST", "1060 W ADDISON ST", "1039 W GRANVILLE AVE"]
print([a for a in addresses if fnmatchcase(a, "* ST")])
# ['5412 N CLARK ST', '1060 W ADDISON ST']
