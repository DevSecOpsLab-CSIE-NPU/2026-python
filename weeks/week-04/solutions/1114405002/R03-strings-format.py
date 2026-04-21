# R03 字串修整、對齊、拼接與格式化
# 主題：strip、ljust/rjust/center、join、format、f-string、textwrap

import textwrap

# 1) strip 系列：去除字串頭尾空白或指定字元。
s = "  hello world \n"
print(repr(s.strip()))
print(repr(s.lstrip()))
print("-----hello=====".strip("-="))

# 2) 文字對齊與欄位寬度控制。
text = "Hello World"
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20, "*"))
print(format(text, "^20"))
print(format(1.2345, ">10.2f"))

# 3) join 高效拼接字串；若元素非字串，先轉型。
parts = ["Is", "Chicago", "Not", "Chicago?"]
print(" ".join(parts))
print(",".join(parts))

data = ["ACME", 50, 91.1]
print(",".join(str(d) for d in data))

# 4) format 與 format_map 常見於模板字串。
name, n = "Guido", 37
template = "{name} has {n} messages."
print(template.format(name=name, n=n))
print(template.format_map(vars()))

# 5) f-string 語法最簡潔，推薦日常使用。
print(f"{name} has {n} messages.")

# 6) textwrap.fill 依指定寬度自動換行。
long_s = (
    "Look into my eyes, look into my eyes, the eyes, "
    "not around the eyes, look into my eyes, you're under."
)
print(textwrap.fill(long_s, 40))
print(textwrap.fill(long_s, 40, initial_indent="    "))
