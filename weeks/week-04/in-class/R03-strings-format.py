# R03. 字串清理、對齊、拼接與格式化（2.11–2.16）
# strip / ljust / join / format / format_map / textwrap

import textwrap

# ── 2.11 清理字元 ─────────────────────────────────────
# 範例字串：前後有空白與尾端換行符號。
s = "  hello world \n"

# strip()：移除字串「左右兩端」的空白字元（空白、tab、換行等）。
# repr(...) 可把不可見字元（如 \n）顯示出來，方便觀察差異。
print(repr(s.strip()))  # 'hello world'

# lstrip()：只移除左側空白，右側保持原樣。
print(repr(s.lstrip()))  # 'hello world \n'

# strip(chars) 不是移除子字串，而是移除「左右兩側出現在 chars 集合中的字元」。
# 例如 '-=' 代表左右邊界若是 '-' 或 '=' 就移除，直到遇到其他字元為止。
print("-----hello=====".strip("-="))  # 'hello'

# ── 2.13 字串對齊 ─────────────────────────────────────
text = "Hello World"

# ljust(width)：左對齊，右邊補空白到指定寬度。
print(text.ljust(20))  # 'Hello World         '

# rjust(width)：右對齊，左邊補空白到指定寬度。
print(text.rjust(20))  # '         Hello World'

# center(width, fillchar)：置中對齊，兩側用 fillchar 補齊。
print(text.center(20, "*"))  # '****Hello World*****'

# format(value, spec) 也可做對齊：^ 表示置中，總寬 20。
print(format(text, "^20"))  # '    Hello World     '

# 數值格式化：>10.2f
# - >   ：右對齊
# - 10  ：總寬至少 10
# - .2f ：浮點數保留 2 位小數
print(format(1.2345, ">10.2f"))  # '      1.23'

# ── 2.14 合併拼接 ─────────────────────────────────────
parts = ["Is", "Chicago", "Not", "Chicago?"]

# join 是字串拼接的高效方式：
# '分隔符'.join(可迭代字串集合)
print(" ".join(parts))  # 'Is Chicago Not Chicago?'
print(",".join(parts))  # 'Is,Chicago,Not,Chicago?'

data = ["ACME", 50, 91.1]

# join 只能處理字串，所以先把每個元素轉成 str。
print(",".join(str(d) for d in data))  # 'ACME,50,91.1'

# ── 2.15 插入變量 ─────────────────────────────────────
name, n = "Guido", 37
s = "{name} has {n} messages."

# format：以關鍵字參數填入模板欄位。
print(s.format(name=name, n=n))  # 'Guido has 37 messages.'

# format_map + vars()：直接把當前區域變數字典餵給模板。
# vars() 在函式外通常等同 locals() 的目前命名空間。
print(s.format_map(vars()))  # 'Guido has 37 messages.'

# f-string：語法最簡潔、可讀性高，現代 Python 常用。
print(f"{name} has {n} messages.")  # f-string（最簡潔）

# ── 2.16 指定列寬 ─────────────────────────────────────
long_s = (
    "Look into my eyes, look into my eyes, the eyes, "
    "not around the eyes, look into my eyes, you're under."
)

# textwrap.fill(text, width)：依指定寬度自動換行。
# 適合終端輸出、報表、CLI 說明文字排版。
print(textwrap.fill(long_s, 40))

# initial_indent：僅第一行的縮排字串。
# （若需要每一行都縮排，可再用 subsequent_indent 參數）
print(textwrap.fill(long_s, 40, initial_indent="    "))
