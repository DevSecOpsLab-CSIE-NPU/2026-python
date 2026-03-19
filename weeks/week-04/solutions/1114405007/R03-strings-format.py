# R03. 字串清理、對齊、拼接與格式化（2.11–2.16）
# 這份範例涵蓋文字處理中最常遇到的整理工作：
# 1. 去除不要的空白或符號
# 2. 把文字排成固定寬度
# 3. 把多段資料組成一個字串
# 4. 把變數插入文字模板
# 5. 將長文字自動換行

import textwrap

# ── 2.11 清理字元 ─────────────────────────────────────
# 原字串前後帶有空白與換行，這是讀取輸入資料時很常見的情況。
s = "  hello world \n"

# strip() 會去掉左右兩邊的空白字元，包含空白、tab、換行等。
# repr() 的用途是把不可見字元顯示出來，方便觀察清理前後差異。
print(repr(s.strip()))  # 'hello world'

# lstrip() 只去掉左邊。
# 所以右邊的換行仍然會保留下來。
print(repr(s.lstrip()))  # 'hello world \n'

# strip('-=') 不是去掉整個字串 "-="，
# 而是把左右兩邊所有屬於 '-' 或 '=' 的字元都移除。
print("-----hello=====".strip("-="))  # 'hello'

# ── 2.13 字串對齊 ─────────────────────────────────────
# 在輸出表格、報表、終端機內容時，常需要固定欄寬。
text = "Hello World"

# ljust(20) 表示文字靠左，總寬度補到 20。
print(text.ljust(20))  # 'Hello World         '

# rjust(20) 表示文字靠右。
print(text.rjust(20))  # '         Hello World'

# center(20, '*') 表示置中，不足的部分用 * 補滿。
print(text.center(20, "*"))  # '****Hello World*****'

# format() 也能做對齊。
# ^20 表示在寬度 20 中置中。
print(format(text, "^20"))  # '    Hello World     '

# >10.2f 表示：靠右、總寬 10、浮點數保留 2 位小數。
print(format(1.2345, ">10.2f"))  # '      1.23'

# ── 2.14 合併拼接 ─────────────────────────────────────
# join() 是把多個字串用指定分隔符串接起來。
# 這比用 + 一段段相加更有效率，也更清楚。
parts = ["Is", "Chicago", "Not", "Chicago?"]
print(" ".join(parts))  # 'Is Chicago Not Chicago?'
print(",".join(parts))  # 'Is,Chicago,Not,Chicago?'

# join() 要求序列中的每個元素都必須是字串。
# 因此當資料中有數字時，通常要先用 str() 轉型。
data = ["ACME", 50, 91.1]
print(",".join(str(d) for d in data))  # 'ACME,50,91.1'

# ── 2.15 插入變量 ─────────────────────────────────────
# 這是字串模板，裡面預留了 name 與 n 兩個欄位。
name, n = "Guido", 37
s = "{name} has {n} messages."

# format() 以關鍵字參數方式把值塞進模板中。
print(s.format(name=name, n=n))  # 'Guido has 37 messages.'

# vars() 會取得目前作用域中的變數字典。
# format_map() 可以直接用這個字典做欄位對應。
print(s.format_map(vars()))  # 'Guido has 37 messages.'

# f-string 是現代 Python 最常見、也最直觀的寫法。
print(f"{name} has {n} messages.")  # f-string（最簡潔）

# ── 2.16 指定列寬 ─────────────────────────────────────
# 這是一段很長的文字，如果直接輸出，閱讀上不容易掌握。
# textwrap.fill() 可以自動依指定寬度進行換行。
long_s = (
    "Look into my eyes, look into my eyes, the eyes, "
    "not around the eyes, look into my eyes, you're under."
)

# 每行最多 40 個字元。
print(textwrap.fill(long_s, 40))

# initial_indent 只會影響第一行縮排。
# 這常用在段落首行縮排或輸出說明文字。
print(textwrap.fill(long_s, 40, initial_indent="    "))
