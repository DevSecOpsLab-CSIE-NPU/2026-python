# R02. 正則表達式：搜尋、替換、旗標（2.4–2.8）
# re.compile / findall / sub / IGNORECASE / 非貪婪 / DOTALL

import re

# ── 2.4 匹配和搜尋 ────────────────────────────────────
text = "Today is 11/27/2012. PyCon starts 3/13/2013."

# re.compile()：預編譯正規表示式，提高重複使用的效率
# (\d+) 使用小括號建立「捕獲群組」(Groups)，分別代表 月/日/年
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")

# findall()：搜尋字串中所有匹配項，並以「列表」形式回傳群組內容
print(datepat.findall(text))
# 輸出：[('11', '27', '2012'), ('3', '13', '2013')]

# match()：從字串的「開頭」進行匹配。如果開頭不符，則回傳 None
m = datepat.match("11/27/2012")
assert m is not None
# group(0) 為完整匹配內容，groups() 為所有小括號內的群組元組
print(m.group(0), m.groups())  # '11/27/2012' ('11', '27', '2012')

# finditer()：以「迭代器」形式回傳匹配對象，適合處理大型字串，節省記憶體
for m in datepat.finditer(text):
    month, day, year = m.groups()
    print(f"{year}-{month}-{day}")

# ── 2.5 搜尋和替換 ───────────────────────────────────
# re.sub()：進行字串替換，\3-\1-\2 代表引用原匹配中的第 3, 1, 2 個群組
print(re.sub(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text))
# 輸出：'Today is 2012-11-27. PyCon starts 2013-3-13.'

# 命名群組 (?P<name>...)：
# 為群組命名以便後續維護，替換時使用 \g<name> 來引用
print(
    re.sub(
        r"(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)",
        r"\g<year>-\g<month>-\g<day>",
        text,
    )
)

# re.subn()：功能與 sub() 相同，但額外回傳一個整數，代表「替換成功的次數」
newtext, n = re.subn(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text)
print(f"替換了 {n} 次")  # 替換了 2 次

# ── 2.6 忽略大小寫 ───────────────────────────────────
s = "UPPER PYTHON, lower python, Mixed Python"
# 使用 re.IGNORECASE 旗標，使匹配不區分大小寫
print(re.findall("python", s, flags=re.IGNORECASE))
# 輸出：['PYTHON', 'python', 'Python']

# ── 2.7 非貪婪（最短匹配）────────────────────────────
text2 = 'Computer says "no." Phone says "yes."'

# 貪婪匹配 (Greedy)：.* 會盡可能匹配最長的字串（直到最後一個引號）
print(re.compile(r'"(.*)"').findall(text2))  # 輸出：['no." Phone says "yes.']

# 非貪婪匹配 (Non-greedy)：.*? 遇到第一個匹配結尾就會停止
print(re.compile(r'"(.*?)"').findall(text2))  # 輸出：['no.', 'yes.']

# ── 2.8 多行匹配（DOTALL）────────────────────────────
code = "/* this is a\nmultiline comment */"

# 預設情況下，點號 (.) 不會匹配換行符號 \n
# re.DOTALL：讓點號 (.) 也能匹配換行符號，常用於抓取跨行註解或 HTML
print(re.compile(r"/\*(.*?)\*/", re.DOTALL).findall(code))
# 輸出：[' this is a\nmultiline comment ']