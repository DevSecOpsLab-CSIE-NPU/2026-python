"""
R03: 字串整理與格式化

示範 strip、對齊、join、format 與 textwrap。
"""

import textwrap


# 2.11 去掉前後空白
s = "  hello world \n"
print(repr(s.strip()))     # 'hello world'
print(repr(s.lstrip()))    # 'hello world \\n'
print("-----hello=====".strip("-="))  # 'hello'

# 2.13 對齊輸出
text = "Hello World"
print(text.ljust(20))         # 'Hello World         '
print(text.rjust(20))         # '         Hello World'
print(text.center(20, "*"))   # '****Hello World*****'
print(format(text, "^20"))    # '    Hello World     '
print(format(1.2345, ">10.2f"))  # '      1.23'

# 2.14 合併字串
parts = ["Is", "Chicago", "Not", "Chicago?"]
print(" ".join(parts))   # 'Is Chicago Not Chicago?'
print(",".join(parts))   # 'Is,Chicago,Not,Chicago?'

data = ["ACME", 50, 91.1]
print(",".join(str(d) for d in data))  # 'ACME,50,91.1'

# 2.15 插入變數
name, n = "Guido", 37
s = "{name} has {n} messages."
print(s.format(name=name, n=n))  # 'Guido has 37 messages.'
print(s.format_map(vars()))       # 'Guido has 37 messages.'
print(f"{name} has {n} messages.")

# 2.16 長字串換行
long_s = (
    "Look into my eyes, look into my eyes, the eyes, "
    "not around the eyes, look into my eyes, you're under."
)
print(textwrap.fill(long_s, 40))
print(textwrap.fill(long_s, 40, initial_indent="    "))
