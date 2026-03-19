"""
R02: 正規表示式的基本操作

示範 compile、findall、sub、IGNORECASE、非貪婪比對與 DOTALL。
"""

import re


# 2.4 找出日期
text = "Today is 11/27/2012. PyCon starts 3/13/2013."
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")

print(datepat.findall(text))
# [('11', '27', '2012'), ('3', '13', '2013')]

m = datepat.match("11/27/2012")
assert m is not None
print(m.group(0), m.groups())
# 11/27/2012 ('11', '27', '2012')

for m in datepat.finditer(text):
    month, day, year = m.groups()
    print(f"{year}-{month}-{day}")

# 2.5 取代字串
print(re.sub(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text))
# Today is 2012-11-27. PyCon starts 2013-3-13.

# 用具名群組也可以做同樣的事。
print(
    re.sub(
        r"(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)",
        r"\g<year>-\g<month>-\g<day>",
        text,
    )
)

# subn 會同時回傳新字串與替換次數。
newtext, n = re.subn(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text)
print(f"替換次數：{n}")

# 2.6 忽略大小寫搜尋
s = "UPPER PYTHON, lower python, Mixed Python"
print(re.findall("python", s, flags=re.IGNORECASE))
# ['PYTHON', 'python', 'Python']

# 2.7 非貪婪比對
text2 = 'Computer says "no." Phone says "yes."'
print(re.compile(r'"(.*)"').findall(text2))
# ['no." Phone says "yes.']
print(re.compile(r'"(.*?)"').findall(text2))
# ['no.', 'yes.']

# 2.8 跨行比對
code = "/* this is a\nmultiline comment */"
print(re.compile(r"/\*(.*?)\*/", re.DOTALL).findall(code))
# [' this is a\nmultiline comment ']
