# R01. 字串分割與匹配（2.1–2.3）
# 主題包含：
# 1. re.split()：使用多種分隔符來分割字串
# 2. startswith() / endswith()：判斷字串開頭或結尾是否符合條件
# 3. fnmatch / fnmatchcase：使用 Shell 通配符進行字串匹配

# 匯入 re 模組
# re 是 Python 的正規表達式（regular expression）模組
import re

# 從 fnmatch 模組匯入 fnmatch 與 fnmatchcase
# fnmatch：使用類似 Shell 的萬用字元進行比對
# fnmatchcase：與 fnmatch 類似，但會強制區分大小寫
from fnmatch import fnmatch, fnmatchcase

# ── 2.1 多界定符分割 ──────────────────────────────────

# 建立一個字串 line
# 這個字串中混合了空白、分號、逗號等不同分隔符號
line = "asdf fjdk; afed, fjek,asdf, foo"

# 印出原始字串，方便和分割結果對照
print("原始字串 line：")
print(line)

print()  # 空一行，讓輸出更清楚

# 使用 re.split() 進行字串分割
# 正規表達式 r"[;,\s]\s*" 的意思如下：
# [;,\s] ：表示分隔符可以是分號 ;、逗號 ,、或空白字元 \s
# \s*    ：表示分隔符後面可以接 0 個或多個空白
#
# 也就是說：遇到分號、逗號、空白時，就把字串切開
split_result_1 = re.split(r"[;,\s]\s*", line)

# 印出第一種 split 結果
print("使用 re.split(r\"[;,\\s]\\s*\", line) 的結果：")
print(split_result_1)

# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

print()  # 空一行，讓輸出更清楚

# 使用非捕獲分組（non-capturing group）
# 正規表達式 r"(?:,|;|\s)\s*" 的意思如下：
# (?:,|;|\s) ：表示分隔符可以是逗號、分號或空白
# ?:         ：代表這是一個「非捕獲分組」
#              也就是只拿來分組比對，不把分隔符保留到結果中
# \s*        ：表示分隔符後面可以接 0 個或多個空白
split_result_2 = re.split(r"(?:,|;|\s)\s*", line)

# 印出第二種 split 結果
print("使用 re.split(r\"(?:,|;|\\s)\\s*\", line) 的結果：")
print(split_result_2)

# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

print()  # 空一行，讓輸出更清楚

# ── 2.2 開頭/結尾匹配 ────────────────────────────────

# 建立一個檔名字串 filename
filename = "spam.txt"

# 印出目前檔名
print("檔名 filename：")
print(filename)

print()  # 空一行，讓輸出更清楚

# 使用 endswith() 判斷字串是否以 .txt 結尾
# 若是，回傳 True；否則回傳 False
print("filename.endswith('.txt') 的結果：")
print(filename.endswith(".txt"))  # True

# 使用 startswith() 判斷字串是否以 file: 開頭
print("filename.startswith('file:') 的結果：")
print(filename.startswith("file:"))  # False

print()  # 空一行，讓輸出更清楚

# 建立一個檔名串列 filenames
filenames = ["Makefile", "foo.c", "bar.py", "spam.c", "spam.h"]

# 印出原始檔名串列
print("原始檔名串列 filenames：")
print(filenames)

print()  # 空一行，讓輸出更清楚

# 使用串列推導式搭配 endswith()
# 篩選出所有以 .c 或 .h 結尾的檔名
#
# 注意：
# endswith() 可以接 tuple，表示同時檢查多種可能的結尾
# 但不能傳入 list
c_h_files = [name for name in filenames if name.endswith((".c", ".h"))]

# 印出篩選結果
print("篩選出副檔名為 .c 或 .h 的檔案：")
print(c_h_files)

# ['foo.c', 'spam.c', 'spam.h']

print()  # 空一行，讓輸出更清楚

# ── 2.3 Shell 通配符匹配 ─────────────────────────────

# 使用 fnmatch() 判斷 foo.txt 是否符合 *.txt 這個樣式
# * 代表任意長度的任意字元
print("fnmatch('foo.txt', '*.txt') 的結果：")
print(fnmatch("foo.txt", "*.txt"))  # True

print()  # 空一行，讓輸出更清楚

# 使用 fnmatch() 判斷 Dat45.csv 是否符合 Dat[0-9]* 這個樣式
# [0-9] 代表一個數字字元
# * 代表後面可以接任意數量的字元
print("fnmatch('Dat45.csv', 'Dat[0-9]*') 的結果：")
print(fnmatch("Dat45.csv", "Dat[0-9]*"))  # True

print()  # 空一行，讓輸出更清楚

# 使用 fnmatchcase() 強制區分大小寫
# 這裡 foo.txt 與 *.TXT 比對時，因為大小寫不同，所以結果是 False
print("fnmatchcase('foo.txt', '*.TXT') 的結果：")
print(fnmatchcase("foo.txt", "*.TXT"))  # False

print()  # 空一行，讓輸出更清楚

# 建立地址串列 addresses
addresses = ["5412 N CLARK ST", "1060 W ADDISON ST", "1039 W GRANVILLE AVE"]

# 印出原始地址資料
print("原始地址串列 addresses：")
print(addresses)

print()  # 空一行，讓輸出更清楚

# 使用串列推導式搭配 fnmatchcase()
# 篩選出所有以 " ST" 結尾的地址
# * ST 表示：前面可以是任意內容，但最後必須是空白加上 ST
street_addresses = [a for a in addresses if fnmatchcase(a, "* ST")]

# 印出篩選結果
print("篩選出以 ' ST' 結尾的地址：")
print(street_addresses)

# ['5412 N CLARK ST', '1060 W ADDISON ST']