# R03. 字串清理、對齊、拼接與格式化（2.11–2.16）
# strip / ljust / join / format / format_map / textwrap

import textwrap

# ── 2.11 清理字元 ─────────────────────────────────────
s = "  hello world \n"
# strip()：移除字串前後的空白字元（包含空格、換行 \n、跳格 \t）
print(repr(s.strip()))  # 輸出：'hello world'

# lstrip()：僅移除左側（開頭）的空白字元
print(repr(s.lstrip()))  # 輸出：'hello world \n'

# 也可以指定要移除的特定字元集
print("-----hello=====".strip("-="))  # 輸出：'hello'

# ── 2.13 字串對齊 ─────────────────────────────────────
text = "Hello World"
# ljust(n)：向左對齊，總長度為 n，不足處補空格
print(text.ljust(20))  # 'Hello World         '

# rjust(n)：向右對齊
print(text.rjust(20))  # '         Hello World'

# center(n, char)：居中對齊，可指定填充字元（如 "*"）
print(text.center(20, "*"))  # '****Hello World*****'

# 使用 format() 進行對齊：^ 代表居中，> 代表右對齊，< 代表左對齊
print(format(text, "^20"))  # '    Hello World     '

# 格式化數字：>10.2f 代表總寬度 10，保留兩位小數，且向右對齊
print(format(1.2345, ">10.2f"))  # '      1.23'

# ── 2.14 合併拼接 ─────────────────────────────────────
parts = ["Is", "Chicago", "Not", "Chicago?"]
# join()：將列表中的字串合併，效率遠高於使用 "+" 號加總
print(" ".join(parts))  # 'Is Chicago Not Chicago?'
print(",".join(parts))  # 'Is,Chicago,Not,Chicago?'

# 如果列表中包含非字串型別（如數字），必須先轉成字串
data = ["ACME", 50, 91.1]
print(",".join(str(d) for d in data))  # 'ACME,50,91.1'

# ── 2.15 插入變量 ─────────────────────────────────────
name, n = "Guido", 37
s = "{name} has {n} messages."
# format()：傳統的關鍵字格式化
print(s.format(name=name, n=n))  # 'Guido has 37 messages.'

# format_map(vars())：直接從當前作用域的變數字典中抓取數值
print(s.format_map(vars()))  # 'Guido has 37 messages.'

# f-string：Python 3.6+ 最推薦的寫法，直接在字串內嵌入變數
print(f"{name} has {n} messages.")  # 'Guido has 37 messages.'

# ── 2.16 指定列寬 ─────────────────────────────────────
long_s = (
    "Look into my eyes, look into my eyes, the eyes, "
    "not around the eyes, look into my eyes, you're under."
)
# textwrap.fill()：自動折行，將長字串依照指定寬度（如 40）斷行
print(textwrap.fill(long_s, 40))

# initial_indent：可為第一行加上縮排（如段落開頭的空格）
print(textwrap.fill(long_s, 40, initial_indent="    "))