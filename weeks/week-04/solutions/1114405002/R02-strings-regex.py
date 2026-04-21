# R02 正規表達式日期擷取與替換
# 主題：re.compile()、findall()、finditer()、sub()、subn()

import re

text = "Today is 11/27/2012. PyCon starts 3/13/2013."

# 1) 先編譯 regex：三個群組分別擷取月、日、年。
#    (\d+) 代表 1 個以上數字。
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")

# 2) findall 直接回傳所有匹配群組的 tuple 清單。
print(datepat.findall(text))

# 3) match 只會從字串開頭嘗試匹配。
m = datepat.match("11/27/2012")
assert m is not None
print(m.group(0), m.groups())

# 4) finditer 回傳迭代器，可逐筆讀取 Match 物件。
for m in datepat.finditer(text):
    month, day, year = m.groups()
    print(f"{year}-{month}-{day}")

# 5) sub 以反向參照 \1、\2、\3 做日期格式轉換。
print(re.sub(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text))

# 6) 也可使用具名群組，可讀性通常較高。
print(
    re.sub(
        r"(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)",
        r"\g<year>-\g<month>-\g<day>",
        text,
    )
)

# 7) subn 會回傳 (替換後字串, 替換次數)。
newtext, n = re.subn(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text)
print(f"替換次數：{n}")

# 8) IGNORECASE 忽略大小寫，適合使用者輸入清理。
s = "UPPER PYTHON, lower python, Mixed Python"
print(re.findall("python", s, flags=re.IGNORECASE))

# 9) 貪婪與非貪婪：.* 會盡可能吃最多，.*? 會盡可能短。
text2 = 'Computer says "no." Phone says "yes."'
print(re.compile(r'"(.*)"').findall(text2))
print(re.compile(r'"(.*?)"').findall(text2))

# 10) DOTALL 讓 . 也能匹配換行，常用於多行區塊擷取。
code = "/* this is a\nmultiline comment */"
print(re.compile(r"/\*(.*?)\*/", re.DOTALL).findall(code))
