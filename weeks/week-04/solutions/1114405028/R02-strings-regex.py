# R02. 正則表達式：搜尋、替換、旗標（2.4–2.8）
# re.compile / findall / sub / IGNORECASE / 非貪婪 / DOTALL

import re

# ── 2.4 匹配和搜尋 ────────────────────────────────────
text = "Today is 11/27/2012. PyCon starts 3/13/2013."
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")

print(datepat.findall(text))  # 找出所有匹配，回傳 list[tuple]（月,日,年）
# [('11', '27', '2012'), ('3', '13', '2013')]

m = datepat.match("11/27/2012")
assert m is not None
print(m.group(0), m.groups())  # group(0) 是完整匹配；groups() 是各捕獲群組

for m in datepat.finditer(text):
    month, day, year = m.groups()
    print(f"{year}-{month}-{day}")  # 逐筆迭代匹配，適合大字串避免一次建整包結果

# ── 2.5 搜尋和替換 ───────────────────────────────────
print(re.sub(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text))  # 以反向參照重排日期格式
# 'Today is 2012-11-27. PyCon starts 2013-3-13.'

# 命名群組
print(
    re.sub(
        r"(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)",
        r"\g<year>-\g<month>-\g<day>",
        text,
    )
)
# 使用命名群組可提升可讀性，尤其規則複雜時較不易寫錯群組編號

# re.subn 回傳替換次數
newtext, n = re.subn(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text)
print(f"替換了 {n} 次")  # 替換了 2 次

# ── 2.6 忽略大小寫 ───────────────────────────────────
s = "UPPER PYTHON, lower python, Mixed Python"
print(re.findall("python", s, flags=re.IGNORECASE))  # IGNORECASE 可同時匹配大小寫變體
# ['PYTHON', 'python', 'Python']

# ── 2.7 非貪婪（最短匹配）────────────────────────────
text2 = 'Computer says "no." Phone says "yes."'
print(re.compile(r'"(.*)"').findall(text2))  # 貪婪：盡可能吃到最後一個引號
print(re.compile(r'"(.*?)"').findall(text2))  # 非貪婪：最短匹配，拿到每段被引號包住內容

# ── 2.8 多行匹配（DOTALL）────────────────────────────
code = "/* this is a\nmultiline comment */"
print(re.compile(r"/\*(.*?)\*/", re.DOTALL).findall(code))  # DOTALL 讓 . 可匹配換行字元
# [' this is a\nmultiline comment ']
