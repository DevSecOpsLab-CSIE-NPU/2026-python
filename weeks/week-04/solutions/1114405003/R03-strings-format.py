# R03. 字串清理、對齊、拼接與格式化（2.11–2.16）
# 核心功能：strip/lstrip/rstrip / ljust/rjust/center / join / format/format_map / textwrap
#
# 本檔案演示字串後處理的五大操作：
#   1. 清理空白與特定字元
#   2. 左/右/居中對齊
#   3. 用分隔符拼接多個字串
#   4. 使用 format 或 f-string 插入變量
#   5. 將長文本自動折行到指定寬度

import textwrap

# ═══════════════════════════════════════════════════════════════════════════
# 2.11 清理字元：strip() / lstrip() / rstrip()
# ═══════════════════════════════════════════════════════════════════════════
# 問題：字串前後可能有不想要的空白或特殊字元
# 解決：使用 strip 家族函數

s = "  hello world \n"  # 前有空白，後有換行

# strip()：移除字串兩端指定的字元（預設為空白）
print(repr(s.strip()))  # 'hello world'
# 説明：移除了前面的 2 個空格和後面的換行符

# lstrip()：只從左側移除
print(repr(s.lstrip()))  # 'hello world \n'
# 説明：移除了左側空格，但保留了右側的換行符

# 自定義移除字元：移除 - 和 =
print("-----hello=====".strip("-="))  # 'hello'
# 説明：strip() 可接收字元集，移除字元集中的任一字元直到遇到其他字元

# ═══════════════════════════════════════════════════════════════════════════
# 2.13 對齊與填充：ljust() / rjust() / center() / format()
# ═══════════════════════════════════════════════════════════════════════════
# 問題：想讓文本在固定寬度欄位中對齊（製作表格或輸出格式化）
# 解決：使用對齊函數或 format() 規格字串

text = "Hello World"  # 長度為 11

# ljust(width)：左對齐（欄寬 20）
print(text.ljust(20))  # 'Hello World         '
# 説明：原文左對齐，右側補齊空白至 20 字寬

# rjust(width)：右對齐
print(text.rjust(20))  # '         Hello World'
# 説明：原文右對齐，左側補齊空白至 20 字寬

# center(width, fillchar)：居中對齐
print(text.center(20, "*"))  # '****Hello World*****'
# 説明：文本居中，用 * 作為填充字元（而非空白）

# format() 規格字串：^表示居中，>表示右對齐，<表示左對齐
print(format(text, "^20"))  # '    Hello World     '
# 説明：^20 = 居中在寬度 20，用空白填充

# format() 也可用於數字格式化：>10.2f = 右對齐，寬 10，小數 2 位
print(format(1.2345, ">10.2f"))  # '      1.23'
# 説明：1.23 右對齐在寬度 10 的欄位中

# ═══════════════════════════════════════════════════════════════════════════
# 2.14 拼接字串：join() 是連接多字串的最佳方法
# ═══════════════════════════════════════════════════════════════════════════
# 問題：需要用分隔符連接多個字串
# 解決：使用 str.join()（比 + 迴圈或 % 格式化都快）

parts = ["Is", "Chicago", "Not", "Chicago?"]

# join(iterable)：用 separator 連接 iterable 中的所有項目
print(" ".join(parts))  # 'Is Chicago Not Chicago?'
# 説明：用空格連接 4 個字串

print(",".join(parts))  # 'Is,Chicago,Not,Chicago?'
# 説明：用逗號連接

# ⚠️ 重要：join 要求所有元素都是字串，若有數字需先轉換
data = ["ACME", 50, 91.1]  # 包含整數和浮點數

# ❌ 錯誤：",".join(data)  # TypeError，50 和 91.1 不是字串

# ✅ 正確：先轉換為字串
print(",".join(str(d) for d in data))  # 'ACME,50,91.1'
# 説明：生成器表達式逐項轉換為字串，再傳給 join

# ═══════════════════════════════════════════════════════════════════════════
# 2.15 插入變量：三種格式化方法比較
# ═══════════════════════════════════════════════════════════════════════════
# 問題：想用變数值「填入」範本字串特定位置
# 解決方案：format()、format_map()、f-string（推薦最新的 f-string）

name, n = "Guido", 37

# 方法1：format(name=..., n=...)
s = "{name} has {n} messages."
print(s.format(name=name, n=n))  # 'Guido has 37 messages.'
# 説明：{name} 和 {n} 是佔位符，format() 將其替換為傳入的值

# 方法2：format_map(dict)（從字典讀值）
print(s.format_map(vars()))  # 'Guido has 37 messages.'
# 説明：vars() 回傳當前局變數的字典 {'name': 'Guido', 'n': 37}
#        format_map 直接用這字典填入佔位符

# 方法3：f-string（Python 3.6+，最簡潔直觀）
print(f"{name} has {n} messages.")  # 'Guido has 37 messages.'
# 説明：f"..." 中 {expression} 會自動求值並轉換為字串
#        這是現代 Python 中最推薦的方法

# ═══════════════════════════════════════════════════════════════════════════
# 2.16 自動折行：textwrap.fill() 應付長文本
# ═══════════════════════════════════════════════════════════════════════════
# 問題：長文本會超出螢幕寬度或日誌窗口，需要自動折行
# 解決：使用 textwrap.fill() 將文本折行到指定寬度

long_s = (
    "Look into my eyes, look into my eyes, the eyes, "
    "not around the eyes, look into my eyes, you're under."
)

# fill(text, width)：折行至 width 字符
print(textwrap.fill(long_s, 40))
# 輸出：
# Look into my eyes, look into my eyes,
# the eyes, not around the eyes, look
# into my eyes, you're under.
# 説明：textwrap 在 40 字處自動換行，避免詞語被割裂

# fill(..., initial_indent=prefix)：在第一行前加前綴
print(textwrap.fill(long_s, 40, initial_indent="    "))
# 輸出：
#     Look into my eyes, look into my eyes,
# the eyes, not around the eyes, look
# into my eyes, you're under.
# 説明：第一行縮進 4 個空格（常見於代碼註釋或清單項目）
