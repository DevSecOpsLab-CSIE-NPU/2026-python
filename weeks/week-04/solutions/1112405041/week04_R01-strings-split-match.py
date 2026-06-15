# 【Bloom 階段：R - 記憶與基本操作】
# R01. 字串分割與匹配
# August 的惡意提醒：在 Week 03 處理複雜的輸入行（包含逗號、分號與空格）時，
# 單純的 .split() 會讓你寫出極其醜陋的代碼。
# 使用 re.split() 展現你對正規表達式的初步掌握。

import re
from fnmatch import fnmatch, fnmatchcase

# 1. 多重分隔符分割
line = "asdf fjdk; afed, fjek,asdf, foo"
# 語法：[;,\\s] 代表匹配分號、逗號或任何空白
# \\s* 代表後面可能跟隨的任意數量空格
print(f"Split results: {re.split(r'[;,\\s]\\s*', line)}")

# 2. 字串頭尾匹配 (endswith/startswith)
# 指紋點：你知道 endswith() 可以傳入一個 Tuple 來同時檢查多種後綴嗎？
filenames = ["Makefile", "foo.c", "bar.py", "spam.h"]
# 同時過濾 .c 與 .h 檔案
source_files = [name for name in filenames if name.endswith(('.c', '.h'))]
print(f"Source files: {source_files}")

# 3. Shell 風格的通配符匹配 (fnmatch)
# 在處理大批量檔案路徑時比 Regex 更簡直
print(f"Is log file? {fnmatch('data.log', '*.log')}")
# fnmatchcase 則會嚴格區分大小寫
print(f"Case sensitive match: {fnmatchcase('foo.txt', '*.TXT')}")
