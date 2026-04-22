# R02. 正則表達式：搜尋、替換、旗標（2.4–2.8）
# re.compile / findall / sub / IGNORECASE / 非貪婪 / DOTALL

import re


def section(title: str) -> None:
    print(f"\n=== {title} ===")

# ── 2.4 匹配和搜尋 ────────────────────────────────────
text = "Today is 11/27/2012. PyCon starts 3/13/2013."
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")
section("2.4 匹配與搜尋")
print("原始文字:", text)

print("findall 結果:", datepat.findall(text))
# [('11', '27', '2012'), ('3', '13', '2013')]

m = datepat.match("11/27/2012")
assert m is not None
print("match.group(0) 與 groups():", m.group(0), m.groups())

for m in datepat.finditer(text):
    month, day, year = m.groups()
    print(f"改寫成 ISO 風格: {year}-{month}-{day}")

# ── 2.5 搜尋和替換 ───────────────────────────────────
section("2.5 搜尋與替換")
print("sub 替換結果:", re.sub(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text))
# 'Today is 2012-11-27. PyCon starts 2013-3-13.'

# 命名群組
print(
    re.sub(
        r"(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)",
        r"\g<year>-\g<month>-\g<day>",
        text,
    )
)

# re.subn 回傳替換次數
newtext, n = re.subn(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text)
print("subn 的新字串:", newtext)
print(f"替換了 {n} 次")  # 替換了 2 次

# ── 2.6 忽略大小寫 ───────────────────────────────────
s = "UPPER PYTHON, lower python, Mixed Python"
section("2.6 忽略大小寫")
print("IGNORECASE 找到:", re.findall("python", s, flags=re.IGNORECASE))
# ['PYTHON', 'python', 'Python']

# ── 2.7 非貪婪（最短匹配）────────────────────────────
text2 = 'Computer says "no." Phone says "yes."'
section("2.7 貪婪 vs 非貪婪")
print("貪婪 (.*):", re.compile(r'"(.*)"').findall(text2))
print("非貪婪 (.*?):", re.compile(r'"(.*?)"').findall(text2))

# ── 2.8 多行匹配（DOTALL）────────────────────────────
code = "/* this is a\nmultiline comment */"
section("2.8 多行匹配 DOTALL")
print("DOTALL 匹配結果:", re.compile(r"/\*(.*?)\*/", re.DOTALL).findall(code))
# [' this is a\nmultiline comment ']
