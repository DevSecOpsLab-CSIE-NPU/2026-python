"""
R01. 字串分割與匹配（2.1–2.3）

功能概述：
  - 2.1: 使用 re.split() 進行多分隔符分割
  - 2.2: 使用 startswith/endswith 進行開頭/結尾匹配
  - 2.3: 使用 fnmatch/fnmatchcase 進行 Shell 通配符匹配

核心模塊：
  - re: 正則表達式模塊
  - fnmatch: Shell 風格通配符匹配
"""

import re
from fnmatch import fnmatch, fnmatchcase


# ════════════════════════════════════════════════════════
# 2.1 多界定符分割 (re.split)
# ════════════════════════════════════════════════════════

line = "asdf fjdk; afed, fjek,asdf, foo"
"""
原始字串：包含多種分隔符
內容分析：
  - 空格（分隔 'asdf' 和 'fjdk'）
  - 分號（分隔 'fjdk' 和 'afed'）
  - 逗號（分隔 'afed' 和 'fjek'）
  - 逗號無空格（分隔 'fjek' 和 'asdf'）
  - 逗號加空格（分隔 'asdf' 和 'foo'）
"""

result1 = re.split(r"[;,\s]\s*", line)
print(result1)
"""
使用 re.split() 進行多分隔符分割

正則表達式分析：r"[;,\s]\s*"
  - [;,\s]: 字符類
    ✓ ; 分號
    ✓ , 逗號
    ✓ \s 任何空白字符（空格、制表符、換行等）
  
  - \s*: 匹配 0 個或多個空白字符（用於移除分隔符後的空白）
  
執行過程：
  1. 'asdf' + (空格) → 分割
  2. 'fjdk' + (分號+空格) → 分割並移除空白
  3. 'afed' + (逗號+空格) → 分割並移除空白
  4. 'fjek' + (逗號無空格) → 分割
  5. 'asdf' + (逗號+空格) → 分割並移除空白
  6. 'foo' 結束

結果：['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

說明：
  - 所有分隔符都被移除
  - 分隔符後的空白也被移除
  - 得到的是純文字元素的列表

正則表達式細節：
  [;,\s] 匹配任何一個分隔符
  \s* 移除尾隨空白（防止結果中有多餘空格）
"""


# 非捕獲分組：分組但不保留分隔符
result2 = re.split(r"(?:,|;|\s)\s*", line)
print(result2)
"""
使用非捕獲分組進行多分隔符分割

正則表達式分析：r"(?:,|;|\s)\s*"
  - (?:...): 非捕獲分組
    → 用於分組但不在結果中保留匹配的部分
  
  - ,|;|\s: 選擇（or）
    ✓ , 逗號
    ✓ ; 分號
    ✓ \s 空白字符
  
  - \s*: 移除分隔符後的空白

執行過程：
  1. 查找 (,|;|\s)，找到分隔符
  2. 再檢查 \s*，移除尾隨空白
  3. 按此模式分割所有文字

結果：['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

vs 字符類 [;,\s] 的區別：
  兩個表達式結果相同，但含義不同：
  
  [;,\s]: 匹配任何一個字符（字符類）
    - 更簡潔
    - 適合簡單的單字符選擇
  
  (?:,|;|\s): 匹配任何一個模式（選擇）
    - 更靈活
    - 可用於複雜模式（如 word1|word2）
  
推薦：簡單分隔符用 [...]，複雜模式用 (?:...)|

捕獲 vs 非捕獲分組的區別：
  
  捕獲分組 (...)：
    re.split(r"(,|;|\s)\s*", line)
    結果會包含分隔符本身
    例：['asdf', ' ', 'fjdk', ';', 'afed', ...]
  
  非捕獲分組 (?:...)：
    re.split(r"(?:,|;|\s)\s*", line)
    結果不包含分隔符
    例：['asdf', 'fjdk', 'afed', ...]（推薦）
"""


# ════════════════════════════════════════════════════════
# 2.2 開頭/結尾匹配 (startswith/endswith)
# ════════════════════════════════════════════════════════

filename = "spam.txt"
"""
測試檔名：spam.txt
"""

check_end = filename.endswith(".txt")
print(check_end)
"""
檢查檔名是否以 ".txt" 結尾

方法：str.endswith(suffix)
  - suffix: 要檢查的後綴字符串
  - 返回值：True 如果字符串以該後綴結尾，否則 False

執行：
  filename = "spam.txt"
  filename.endswith(".txt") → True ✓
  
說明：
  - 字符串 "spam.txt" 確實以 ".txt" 結尾
  - 返回 True
  - 這是高效的字符串檢查方式（比正則表達式快）
"""

check_start = filename.startswith("file:")
print(check_start)
"""
檢查檔名是否以 "file:" 開頭

方法：str.startswith(prefix)
  - prefix: 要檢查的前綴字符串
  - 返回值：True 如果字符串以該前綴開頭，否則 False

執行：
  filename = "spam.txt"
  filename.startswith("file:") → False ✗
  
說明：
  - 字符串 "spam.txt" 不以 "file:" 開頭
  - 返回 False
  - "spam" 是開頭，不是 "file:"
"""


# 同時檢查多種後綴 → 傳入 tuple（不能傳 list）
filenames = ["Makefile", "foo.c", "bar.py", "spam.c", "spam.h"]
"""
檔名列表：包含多種副檔名
  - Makefile（無副檔名）
  - foo.c（C 語言源碼文件）
  - bar.py（Python 程式）
  - spam.c（C 語言源碼文件）
  - spam.h（C 語言頭文件）
"""

result_code_files = [name for name in filenames if name.endswith((".c", ".h"))]
print(result_code_files)
"""
篩選出所有 C 語言相關檔案（.c 或 .h）

語法：name.endswith((".c", ".h"))
  - 傳入 tuple，而非 list！
  - (".c", ".h") 是元組
  - 檢查是否以任何一個後綴結尾

重要限制：
  ✗ 錯誤：name.endswith([".c", ".h"])
    → TypeError: endswith() argument must be str or tuple, not list
  
  ✓ 正確：name.endswith((".c", ".h"))
    → 使用 tuple，不能用 list

執行過程：
  1. "Makefile".endswith((".c", ".h"))
     → 不以 .c 或 .h 結尾 → False ✗
  
  2. "foo.c".endswith((".c", ".h"))
     → 以 .c 結尾 → True ✓ 保留
  
  3. "bar.py".endswith((".c", ".h"))
     → 不以 .c 或 .h 結尾 → False ✗
  
  4. "spam.c".endswith((".c", ".h"))
     → 以 .c 結尾 → True ✓ 保留
  
  5. "spam.h".endswith((".c", ".h"))
     → 以 .h 結尾 → True ✓ 保留

結果：['foo.c', 'spam.c', 'spam.h']

為什麼必須用 tuple？
  - endswith() 的 signature 要求第二個參數是 str 或 tuple
  - Python 不允許 list 作為後綴參數
  - 這是設計決定（tuple 是不可變的，更適合作為配置）

等效的替代方式：

方式1：逐個檢查（冗長）
  [name for name in filenames if name.endswith(".c") or name.endswith(".h")]

方式2：字符串方法
  [name for name in filenames if name[-2:] in ('.c', '.h')]
  （不推薦，性能較差）

方式3：正則表達式（過度設計）
  [name for name in filenames if re.search(r'\.(c|h)$', name)]
  （功能強大但性能較低）

推薦：使用 tuple 版本，最優雅、高效、易讀
"""


# ════════════════════════════════════════════════════════
# 2.3 Shell 通配符匹配 (fnmatch)
# ════════════════════════════════════════════════════════

match1 = fnmatch("foo.txt", "*.txt")
print(match1)
"""
Shell 通配符 - 文件類型匹配

函數：fnmatch(name, pattern)
  - name: 要檢查的字符串
  - pattern: Shell 風格通配符模式
  - 返回值：True 如果名稱符合模式

執行：fnmatch("foo.txt", "*.txt")
  
通配符說明：
  - * 代表任意數量的字符（可以是 0 個）
  - *.txt 表示任何以 .txt 結尾的字符串

匹配過程：
  1. 模式 *.txt："任何字符序列" + ".txt"
  2. 檢查 foo.txt：foo + .txt
  3. foo 符合 * 的條件（任意字符序列）
  4. .txt 完全匹配 .txt
  5. 結果：True ✓

結果：True

應用場景：
  - shell 中的 ls *.txt
  - 文件篩選
  - 模式簡單匹配（性能比正則表達式好）
"""

match2 = fnmatch("Dat45.csv", "Dat[0-9]*")
print(match2)
"""
Shell 通配符 - 混合字符類與星號

通配符說明：
  - [0-9] 字符類，表示 0 到 9 之間的任何一個數字
  - * 任意數量的字符
  - Dat[0-9]* 表示 "Dat" + "任何一個數字" + "任意字符"

匹配過程：
  1. 模式 Dat[0-9]*
  2. 檢查 Dat45.csv：
     - Dat → 匹配 Dat ✓
     - 4 → 匹配 [0-9]（是數字）✓
     - 5.csv → 匹配 * ✓
  3. 所有部分都匹配
  4. 結果：True ✓

結果：True

通配符語法參考：
  - * 匹配任意數量字符（包括 0 個）
  - ? 匹配恰好 1 個字符
  - [seq] 匹配序列中的任何一個字符
  - [!seq] 匹配不在序列中的任何字符

例子：
  - *.txt 匹配 file.txt, a.txt 但不匹配 file.doc
  - file?.txt 匹配 file1.txt, fileA.txt 但不匹配 file10.txt
  - file[0-9].txt 匹配 file5.txt 但不匹配 fileA.txt
"""


# fnmatchcase 強制區分大小寫
sensitive_result = fnmatchcase("foo.txt", "*.TXT")
print(sensitive_result)
"""
區分大小寫的 Shell 通配符匹配

函數：fnmatchcase(name, pattern)
  - 與 fnmatch() 類似，但強制區分大小寫
  - fnmatch() 在某些系統上不區分大小寫
  - fnmatchcase() 在所有系統上都區分大小寫

執行：fnmatchcase("foo.txt", "*.TXT")

匹配分析：
  1. 模式 *.TXT（全大寫）
  2. 檢查 foo.txt（小寫）
  3. foo 符合 *
  4. 但 .txt ≠ .TXT（大小寫不符）
  5. 結果：False ✗

結果：False

對比：fnmatch vs fnmatchcase

fnmatch("foo.txt", "*.TXT")
  → Windows/macOS：True（不區分大小寫）
  → Linux：False（區分大小寫）
  → 行為依賴操作系統

fnmatchcase("foo.txt", "*.TXT")
  → 所有系統：False（強制區分大小寫）
  → 行為一致、可預測

推薦：需要可靠的跨平台行為時用 fnmatchcase()
"""

addresses = ["5412 N CLARK ST", "1060 W ADDISON ST", "1039 W GRANVILLE AVE"]
"""
地址列表：美國城市地址
  - "5412 N CLARK ST"（以 ST 結尾）
  - "1060 W ADDISON ST"（以 ST 結尾）
  - "1039 W GRANVILLE AVE"（以 AVE 結尾）
"""

result_st_addresses = [a for a in addresses if fnmatchcase(a, "* ST")]
print(result_st_addresses)
"""
篩選出所有以 " ST"（街道）結尾的地址

模式：fnmatchcase(a, "* ST")
  - * 任意字符序列（包括空格和錯號）
  - 空格 分隔符
  - ST 街道代碼

模式説明：
  - "* ST" 匹配任何以空格+ST 結尾的字符串
  - 使用 fnmatchcase() 確保大小寫敏感

執行過程：
  1. "5412 N CLARK ST"
     → 符合模式 "* ST"（以 ST 結尾）✓ 保留
  
  2. "1060 W ADDISON ST"
     → 符合模式 "* ST"（以 ST 結尾）✓ 保留
  
  3. "1039 W GRANVILLE AVE"
     → 不符合（以 AVE 結尾，不是 ST）✗ 丟棄

結果：['5412 N CLARK ST', '1060 W ADDISON ST']

應用場景：
  - 地址分類
  - 文件擴展名過濾
  - 簡單模式匹配

vs 正則表達式的區別：
  fnmatchcase：簡單、快速、直觀
  正則表達式：功能豐富、功能複雜、性能較低

選擇建議：
  - 簡單 Shell 通配符 → 用 fnmatch/fnmatchcase ✓
  - 複雜模式 → 用 re.match/re.search
"""
