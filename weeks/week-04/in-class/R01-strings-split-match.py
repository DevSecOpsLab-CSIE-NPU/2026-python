# ============================================================================
# R01. 字串分割與匹配（2.1–2.3）
# ============================================================================
# 本題展示三個重要的字串處理操作：
# 1. re.split() - 使用正規表達式分割字串（支援多個分隔符）
# 2. startswith() / endswith() - 檢查字串的開頭或結尾
# 3. fnmatch - Shell 風格的通配符匹配
# ============================================================================

import re
from fnmatch import fnmatch, fnmatchcase


# ── 2.1 多界定符分割（Multiple Delimiter Splitting） ───────────────────────
# 【需求】: 使用多個分隔符（分號 ; 、逗號 , 、空白符 \s）來分割字串
print("【2.1 多界定符分割】")
print("-" * 50)

# 原始字串：包含不同分隔符和多個空白
line = "asdf fjdk; afed, fjek,asdf, foo"
print(f"原始字串: {line}\n")

# 【方法 1】使用字符集 [;,\s] 匹配任一分隔符，後跟 0 個或多個空白 \s*
# 字符集解釋：
#   [;,\s] 表示匹配分號、逗號或空白字符中的任意一個
#   \s*    表示分隔符後可能跟著 0 個以上的空白（用於去除多餘空白）
result1 = re.split(r"[;,\s]\s*", line)
print(f"方法 1 - 使用字符集 [;,\\s]\\s*:")
print(f"結果: {result1}")
# 預期: ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
print()

# 【方法 2】使用非捕獲分組 (?:,|;|\s)
# 非捕獲分組解釋：
#   (?:...)  非捕獲分組，分組但不保留該部分在結果中
#   ,|;|\s   表示匹配逗號、分號或空白字符
#   效果與方法 1 相同，但寫法更明確
result2 = re.split(r"(?:,|;|\s)\s*", line)
print(f"方法 2 - 使用非捕獲分組 (?:,|;|\\s)\\s*:")
print(f"結果: {result2}")
# 兩種方法都產生相同結果
print()


# ── 2.2 開頭/結尾匹配（Prefix/Suffix Matching） ───────────────────────────
print("【2.2 開頭/結尾匹配】")
print("-" * 50)

# 【基本用法】檢查單個字串的開頭或結尾
filename = "spam.txt"
print(f"檔案名: {filename}\n")

# endswith(suffix) 檢查字串是否以指定後綴結尾
is_text_file = filename.endswith(".txt")
print(f"filename.endswith('.txt') → {is_text_file}")
# 預期: True（因為 spam.txt 以 .txt 結尾）
print()

# startswith(prefix) 檢查字串是否以指定前綴開頭
is_file_url = filename.startswith("file:")
print(f"filename.startswith('file:') → {is_file_url}")
# 預期: False（因為 spam.txt 不以 file: 開頭）
print()

# 【進階用法】檢查多個後綴
# 關鍵點：必須傳入 tuple，不能傳 list！
print("【進階】檢查多種副檔名:")
filenames = ["Makefile", "foo.c", "bar.py", "spam.c", "spam.h"]
print(f"檔案列表: {filenames}\n")

# 篩選出 C 語言和 header 檔案（副檔名為 .c 或 .h）
# 注意：endswith() 的第二個參數是 tuple，不是 list
c_files = [name for name in filenames if name.endswith((".c", ".h"))]
print(f"篩選 .c 和 .h 檔案:")
print(f"結果: {c_files}")
# 預期: ['foo.c', 'spam.c', 'spam.h']
print()


# ── 2.3 Shell 通配符匹配（fnmatch Pattern Matching） ────────────────────────
print("【2.3 Shell 通配符匹配】")
print("-" * 50)

# fnmatch 模組提供 Unix Shell 風格的通配符匹配
# 常見的通配符規則：
#   *     匹配任意個字符
#   ?     匹配單個字符
#   [abc] 匹配方括號內的任一個字符
#   [!x]  匹配除了 x 以外的任意字符

print("【基本通配符匹配】\n")

# 例子 1：*.txt 匹配所有 .txt 檔案
test1 = fnmatch("foo.txt", "*.txt")
print(f"fnmatch('foo.txt', '*.txt') → {test1}")
# 預期: True（foo.txt 符合 *.txt 的模式）
print()

# 例子 2：Dat[0-9]* 匹配 Dat 開頭、後跟數字、再跟任意字符的字串
test2 = fnmatch("Dat45.csv", "Dat[0-9]*")
print(f"fnmatch('Dat45.csv', 'Dat[0-9]*') → {test2}")
# 預期: True（Dat45.csv 符合 Dat[0-9]* 的模式）
print()

# 【區分大小寫 vs 不區分大小寫】
print("【大小寫敏感性】\n")

# fnmatch() 在某些系統上不區分大小寫（取決於系統 OS）
# fnmatchcase() 強制區分大小寫（跨平台一致）
test3 = fnmatchcase("foo.txt", "*.TXT")
print(f"fnmatchcase('foo.txt', '*.TXT') → {test3}")
# 預期: False（強制區分大小寫，所以 .txt 不符合 *.TXT）
print()

# 【實戰應用】篩選地址列表
print("【實戰應用】篩選地址:\n")
addresses = ["5412 N CLARK ST", "1060 W ADDISON ST", "1039 W GRANVILLE AVE"]
print(f"地址列表:")
for addr in addresses:
    print(f"  - {addr}")
print()

# 篩選出所有以 ST（街道）結尾的地址
st_addresses = [a for a in addresses if fnmatchcase(a, "* ST")]
print(f"篩選條件: fnmatchcase(a, '* ST')")
print(f"結果（所有以 ST 結尾的地址）:")
for addr in st_addresses:
    print(f"  ✓ {addr}")
# 預期: ['5412 N CLARK ST', '1060 W ADDISON ST']
# （'1039 W GRANVILLE AVE' 因為以 AVE 結尾而被排除）
print()
