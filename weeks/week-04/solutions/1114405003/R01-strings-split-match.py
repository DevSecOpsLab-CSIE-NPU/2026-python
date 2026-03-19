# R01. 字串分割與匹配（2.1–2.3）
# 核心功能：re.split() 多分隔符 / startswith / endswith / fnmatch
# 
# 本檔案演示 Python Cookbook 第2章的字串基本操作
# 涵蓋三大常見場景：
#   1. 使用多個分隔符分割字串
#   2. 檢查字串開頭/結尾
#   3. 使用 Shell 通配符進行模式匹配

import re
from fnmatch import fnmatch, fnmatchcase

# ═══════════════════════════════════════════════════════════════════════════
# 2.1 多界定符分割（使用正則表達式）
# ═══════════════════════════════════════════════════════════════════════════
# 問題：想要用多個分隔符（分號、逗號、空白）分割字串
# 解決：使用 re.split() 搭配字元類 [...] 表示「任何一個分隔符」

line = "asdf fjdk; afed, fjek,asdf, foo"

# 方法1：使用字元類 [;,\s] 表示「分號、逗號或任何空白字元」
#        後面加 \s* 表示「分隔符後可能有多個空白」
#        結果將字串完全分割，分隔符被移除
print(re.split(r"[;,\s]\s*", line))
# 輸出：['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
# 説明：
#   - 「,」前的「fjek」和「asdf」中間有逗號被移除
#   - 連續的空白＋逗號被當作一個分隔點

# 方法2：使用非捕獲分組 (?:...) 明確列舉分隔符
#        非捕獲分組 = 參與匹配但不保留分隔符的內容
print(re.split(r"(?:,|;|\s)\s*", line))
# 輸出：['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
# 説明：(?:,|;|\s) 表示「逗號或分號或空白」，效果與方法1相同


# ═══════════════════════════════════════════════════════════════════════════
# 2.2 檢查字串開頭與結尾（最簡單的字串前後綴匹配）
# ═══════════════════════════════════════════════════════════════════════════
# 問題：想判斷文件名是否以特定副檔名結尾，或是否為特定協議開頭
# 解決：使用 endswith() 和 startswith() 方法

filename = "spam.txt"

# endswith：檢查字串是否以指定子串結尾
print(filename.endswith(".txt"))  # True，因為「spam.txt」確實以「.txt」結尾
print(filename.startswith("file:"))  # False，因為「spam.txt」不以「file:」開頭

# ⭐ 重要：同時檢查多種結尾時，必須傳入 tuple，不能傳 list
filenames = ["Makefile", "foo.c", "bar.py", "spam.c", "spam.h"]

# ✅ 正確：傳入元組 (...c", ".h")
print([name for name in filenames if name.endswith((".c", ".h"))])
# 輸出：['foo.c', 'spam.c', 'spam.h']
# 説明：
#   - Makefile：不以 .c 或 .h 結尾，被過濾掉
#   - foo.c, spam.c, spam.h：符合條件，保留
#   - bar.py：以 .py 結尾，不符合，被過濾掉

# ❌ 錯誤示例（不執行）：
# filenames.endswith([".c", ".h"])  # TypeError：此方法只接受 tuple!


# ═══════════════════════════════════════════════════════════════════════════
# 2.3 Shell 通配符匹配（fnmatch：用於檔案名稱的模式匹配）
# ═══════════════════════════════════════════════════════════════════════════
# 問題：想用 Shell 通配符（如 *.txt 或 [0-9]*）進行模式匹配
# 解決：使用 fnmatch 或 fnmatchcase 模組

# 基本通配符語法：
#   *      = 匹配任意個字元
#   ?      = 匹配單個字元
#   [seq]  = 匹配括號內任一字元
#   [!seq] = 匹配括號外的字元

# 範例1：*.txt 匹配所有 txt 檔案
print(fnmatch("foo.txt", "*.txt"))  # True
# 説明：「foo.txt」符合「*.txt」的模式，* 代表「foo」

# 範例2：Dat[0-9]* 匹配「Dat」開頭以數字接續的檔案
print(fnmatch("Dat45.csv", "Dat[0-9]*"))  # True
# 説明：
#   - 「Dat45.csv」以「Dat」開頭 ✓
#   - 跟著數字「4」和「5」，符合 [0-9]+ ✓
#   - 後面可以是任意（.csv），符合 * ✓

# 重點：fnmatch 預設不區分大小寫（取決於作業系統）
# 如果想強制區分大小寫，使用 fnmatchcase

# 範例3：區分大小寫的匹配
print(fnmatchcase("foo.txt", "*.TXT"))  # False
# 説明：「foo.txt」的副檔名是 .txt（小寫），不符合 *.TXT（大寫）

# 實務應用：篩選特定模式的檔案名稱
addresses = ["5412 N CLARK ST", "1060 W ADDISON ST", "1039 W GRANVILLE AVE"]

# 篩選：所有以「 ST」結尾的地址（使用 * 代表任意前綴）
print([a for a in addresses if fnmatchcase(a, "* ST")])
# 輸出：['5412 N CLARK ST', '1060 W ADDISON ST']
# 説明：
#   - 「5412 N CLARK ST」以「 ST」結尾，符合 * ST ✓
#   - 「1060 W ADDISON ST」以「 ST」結尾，符合 * ST ✓
#   - 「1039 W GRANVILLE AVE」以「AVE」結尾，不符合 ✗
