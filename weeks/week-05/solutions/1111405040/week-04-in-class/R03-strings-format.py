"""
R03: 常見字串整理與格式化技巧。

示範重點：
1. 去除前後多餘字元。
2. 調整對齊方式與欄位寬度。
3. 串接字串、插值與長文字換行。
"""

import textwrap

# `strip()` 預設會移除前後空白與換行。
# `lstrip()` 只處理左邊，`strip("-=")` 則是指定要移除的字元集合。
s = "  hello world \n"
print(repr(s.strip()))  # 'hello world'
print(repr(s.lstrip()))  # 'hello world \n'
print("-----hello=====".strip("-="))  # 'hello'

text = "Hello World"

# `ljust()`、`rjust()`、`center()` 用來控制字串對齊。
print(text.ljust(20))  # 'Hello World         '
print(text.rjust(20))  # '         Hello World'
print(text.center(20, "*"))  # '****Hello World*****'

# `format()` 提供與 `ljust()` 類似但更統一的格式控制方式。
print(format(text, "^20"))  # '    Hello World     '
print(format(1.2345, ">10.2f"))  # '      1.23'

# `join()` 適合把多個字串高效率地串起來。
parts = ["Is", "Chicago", "Not", "Chicago?"]
print(" ".join(parts))  # 'Is Chicago Not Chicago?'
print(",".join(parts))  # 'Is,Chicago,Not,Chicago?'

# 若串列中不是全字串，先轉成字串再 `join()`。
data = ["ACME", 50, 91.1]
print(",".join(str(item) for item in data))  # 'ACME,50,91.1'

name, n = "Guido", 37
template = "{name} has {n} messages."

# `format()` 以明確指定欄位值的方式完成字串插值。
print(template.format(name=name, n=n))  # 'Guido has 37 messages.'

# `format_map(vars())` 會直接使用目前作用域中的變數名稱。
print(template.format_map(vars()))  # 'Guido has 37 messages.'

# f-string 在簡短情境下通常最直觀。
print(f"{name} has {n} messages.")

long_text = (
    "Look into my eyes, look into my eyes, the eyes, "
    "not around the eyes, look into my eyes, you're under."
)

# `textwrap.fill()` 會依指定寬度自動換行。
print(textwrap.fill(long_text, 40))

# `initial_indent` 可讓第一行帶有固定縮排。
print(textwrap.fill(long_text, 40, initial_indent="    "))
