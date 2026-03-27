"""
R02: 正規表達式基本操作。

示範重點：
1. 預先編譯樣式並反覆使用。
2. 擷取、取代與統計匹配次數。
3. `IGNORECASE`、非貪婪匹配與 `DOTALL` 的效果。
"""

import re

# 範例文字中包含兩個日期，格式都是 月/日/年。
text = "Today is 11/27/2012. PyCon starts 3/13/2013."

# 把月份、日期、年份都各自放進捕獲群組，之後可以單獨取出。
date_pattern = re.compile(r"(\d+)/(\d+)/(\d+)")

# `findall()` 會直接回傳所有匹配結果。
print(date_pattern.findall(text))
# [('11', '27', '2012'), ('3', '13', '2013')]

# `match()` 只從字串開頭開始比對。
m = date_pattern.match("11/27/2012")
assert m is not None
print(m.group(0), m.groups())  # '11/27/2012' ('11', '27', '2012')

# `finditer()` 會逐筆回傳 match 物件，
# 適合需要針對每個匹配結果做進一步處理的情況。
for match in date_pattern.finditer(text):
    month, day, year = match.groups()
    print(f"{year}-{month}-{day}")

# 使用反向參照把日期格式改成 年-月-日。
print(re.sub(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text))
# 'Today is 2012-11-27. PyCon starts 2013-3-13.'

# 具名群組可以讓樣式與替換規則更容易讀懂。
print(
    re.sub(
        r"(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)",
        r"\g<year>-\g<month>-\g<day>",
        text,
    )
)

# `subn()` 除了回傳新字串，也會回傳取代次數。
new_text, count = re.subn(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text)
print(new_text)
print(f"替換次數: {count}")

# `IGNORECASE` 可忽略大小寫，讓同一個樣式匹配多種寫法。
s = "UPPER PYTHON, lower python, Mixed Python"
print(re.findall("python", s, flags=re.IGNORECASE))
# ['PYTHON', 'python', 'Python']

text2 = 'Computer says "no." Phone says "yes."'

# `.*` 預設是貪婪匹配，會盡可能吃到最後一個引號。
print(re.compile(r'"(.*)"').findall(text2))
# ['no." Phone says "yes.']

# `.*?` 改成非貪婪匹配後，會在最早可結束的位置停下來。
print(re.compile(r'"(.*?)"').findall(text2))
# ['no.', 'yes.']

# `DOTALL` 讓 `.` 也能匹配換行字元，因此可抓到多行註解內容。
code = "/* this is a\nmultiline comment */"
print(re.compile(r"/\*(.*?)\*/", re.DOTALL).findall(code))
# [' this is a\nmultiline comment ']
