# R01. 字串分割與匹配（2.1–2.3）
# re.split() 多分隔符 / startswith / endswith / fnmatch

import re
from fnmatch import fnmatch, fnmatchcase

# ── 2.1 多界定符分割 ──────────────────────────────────
# 問題：一個字串可能有多種分隔符（如逗號、分號、空白），
# 需要用單一操作把它們都分割開。

line = "asdf fjdk; afed, fjek,asdf, foo"

# 方式 1：使用字元集 [;,\s] + \s* 
#        - [;,\s] 匹配「分號、逗號或任何空白字元」
#        - \s* 表示分隔符後可能還有空白（一起消掉）
#        - 結果：以這些分隔符為邊界，分割成單詞列表
#        - 前面加 r"..."（raw string）可避免反斜線跳脫混淆
print(re.split(r"[;,\s]\s*", line))
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# 方式 2：使用非捕獲分組 (?:,|;|\s)
#        - (?:...) 表示「非捕獲分組」：分組但不保留分隔符本身
#        - 功能上完全等同於方式 1，但邏輯更明確
#        - 適合註明「這些是可選的分隔符」
#        - 若改成捕獲分組 (...)，split 結果會把分隔符也放進清單
print(re.split(r"(?:,|;|\s)\s*", line))
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# 補充：若資料可能有連續分隔符（例如 ",," 或 "; ;"），
# split 結果可能出現空字串，可再用 if token 過濾。
# tokens = [token for token in re.split(r"[;,\s]\s*", line) if token]

# ── 2.2 開頭/結尾匹配 ────────────────────────────────
# 快速檢驗字串是否以特定文字開頭或結尾。
# 比 regex 更快，適合簡單的前綴/後綴檢查。

filename = "spam.txt"
print(filename.endswith(".txt"))        # True：以 .txt 結尾
print(filename.startswith("file:"))     # False：不以 file: 開頭

# 檢查多種後綴：傳入 tuple（不能傳 list，會報 TypeError）
# tuple 是必須的，因為 endswith 的第二參數預期是 tuple。
filenames = ["Makefile", "foo.c", "bar.py", "spam.c", "spam.h"]
print([name for name in filenames if name.endswith((".c", ".h"))])
# ['foo.c', 'spam.c', 'spam.h']

# 補充：若不小心傳 list，會失敗：
# filenames_wrong = [name for name in filenames if name.endswith([".c", ".h"])]  # TypeError
# 同理，startswith 也接受 tuple：
# any_url = [s for s in ["http://a", "ftp://b", "file:/c"] if s.startswith(("http:", "https:"))]

# ── 2.3 Shell 通配符匹配 ─────────────────────────────
# fnmatch 與 fnmatchcase 提供簡單的「通配符模式」匹配，
# 類似在終端機用 *.txt 或 *.py 的感覺。
# 相比 regex，通配符語法更簡潔，但功能有限。

# fnmatch 在 Windows 上不區分大小寫，Unix 上區分。
# 支援的通配符：
#   * 匹配任意字元序列
#   ? 匹配單一字元
#   [序列] 字元集，如 [0-9] 表示數字

print(fnmatch("foo.txt", "*.txt"))           # True：foo.txt 符合 *.txt 模式
print(fnmatch("Dat45.csv", "Dat[0-9]*"))     # True：Dat45.csv 符合 Dat[數字]*

# fnmatchcase 強制區分大小寫（regardless of 系統），
# 即使在 Windows 上也會區分 .TXT 和 .txt。
print(fnmatchcase("foo.txt", "*.TXT"))       # False：大小寫不符

# 實務建議：
# - 要跨平台行為一致時，優先使用 fnmatchcase
# - 只做路徑樣式快速匹配時，fnmatch 可讀性通常優於 regex

# 實務應用：搜尋符合模式的地址字串
addresses = ["5412 N CLARK ST", "1060 W ADDISON ST", "1039 W GRANVILLE AVE"]
# 只列出以 " ST"（空白加 ST）結尾的地址
# "* ST" 動作：
#   * 匹配前面任意字元
#   ST 必須精確匹配
result = [a for a in addresses if fnmatchcase(a, "* ST")]
print(result)
# ['5412 N CLARK ST', '1060 W ADDISON ST']
