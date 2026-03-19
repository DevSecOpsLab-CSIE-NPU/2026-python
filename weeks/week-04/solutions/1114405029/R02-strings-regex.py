# R02. 正則表達式：搜尋、替換、旗標（2.4–2.8）
# 主題包含：
# 1. re.compile：先編譯正則表達式，方便重複使用
# 2. findall / match / finditer：不同的搜尋方式
# 3. sub / subn：字串替換與替換次數統計
# 4. IGNORECASE：忽略大小寫搜尋
# 5. 非貪婪匹配：只取最短符合內容
# 6. DOTALL：讓 . 可以匹配換行字元

# 匯入 re 模組
# re 是 Python 中用來處理正則表達式（Regular Expression）的模組
import re

# ── 2.4 匹配和搜尋 ────────────────────────────────────

# 建立一段文字 text
# 裡面包含兩個日期字串，格式都是 月/日/年
text = "Today is 11/27/2012. PyCon starts 3/13/2013."

# 使用 re.compile() 建立一個正則表達式物件 datepat
# (\d+) 表示「1 個或多個數字」
# 三組括號代表三個捕獲群組（group）：
# 第 1 組：月份
# 第 2 組：日期
# 第 3 組：年份
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")

# 印出原始文字
print("原始文字 text：")
print(text)

print()  # 空一行，讓輸出更清楚

# 使用 findall() 找出所有符合日期格式的內容
# 因為有使用群組，所以回傳的是由 tuple 組成的串列
# 每個 tuple 中依序是 (month, day, year)
print("datepat.findall(text) 的結果：")
print(datepat.findall(text))
# [('11', '27', '2012'), ('3', '13', '2013')]

print()  # 空一行，讓輸出更清楚

# 使用 match() 從字串「開頭」開始匹配
# 這裡的字串 "11/27/2012" 一開頭就是日期格式，所以會成功
m = datepat.match("11/27/2012")

# 確認 m 不是 None，代表有匹配成功
assert m is not None

# group(0) 代表整個匹配到的字串
# groups() 代表所有捕獲群組的內容
print("datepat.match('11/27/2012') 的結果：")
print("m.group(0) =", m.group(0))
print("m.groups() =", m.groups())
# '11/27/2012' ('11', '27', '2012')

print()  # 空一行，讓輸出更清楚

# 使用 finditer() 逐一走訪所有匹配到的結果
# 每次回傳一個 match 物件，適合逐筆處理
print("使用 finditer() 逐筆取出日期，並轉成 年-月-日 格式：")
for m in datepat.finditer(text):
    # 將三個群組內容依序取出
    month, day, year = m.groups()

    # 使用 f-string 重新組成新的日期格式
    print(f"{year}-{month}-{day}")

print()  # 空一行，讓輸出更清楚

# ── 2.5 搜尋和替換 ───────────────────────────────────

# 使用 re.sub() 進行字串替換
# 將原本的 月/日/年 格式改成 年-月-日 格式
# \1、\2、\3 分別代表第 1、2、3 個群組
sub_result_1 = re.sub(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text)

print("使用 re.sub() 進行日期格式替換後的結果：")
print(sub_result_1)
# 'Today is 2012-11-27. PyCon starts 2013-3-13.'

print()  # 空一行，讓輸出更清楚

# 命名群組（named group）
# 使用 ?P<名稱> 的方式替每個群組命名
# 這樣在替換時，可用更清楚的名稱來表示
sub_result_2 = re.sub(
    r"(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)",
    r"\g<year>-\g<month>-\g<day>",
    text,
)

print("使用命名群組進行替換後的結果：")
print(sub_result_2)

print()  # 空一行，讓輸出更清楚

# re.subn() 和 re.sub() 類似，
# 不同的是它會回傳兩個值：
# 1. 替換後的新字串
# 2. 總共替換了幾次
newtext, n = re.subn(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text)

print("使用 re.subn() 替換後的新字串：")
print(newtext)

print("re.subn() 統計到的替換次數：")
print(f"替換了 {n} 次")  # 替換了 2 次

print()  # 空一行，讓輸出更清楚

# ── 2.6 忽略大小寫 ───────────────────────────────────

# 建立一段包含不同大小寫形式的字串
s = "UPPER PYTHON, lower python, Mixed Python"

# 使用 re.findall() 搜尋 "python"
# flags=re.IGNORECASE 表示忽略大小寫
# 因此無論是 PYTHON、python、Python 都能找到
ignorecase_result = re.findall("python", s, flags=re.IGNORECASE)

print("原始字串 s：")
print(s)

print()  # 空一行，讓輸出更清楚

print("使用 re.findall(..., flags=re.IGNORECASE) 的結果：")
print(ignorecase_result)
# ['PYTHON', 'python', 'Python']

print()  # 空一行，讓輸出更清楚

# ── 2.7 非貪婪（最短匹配）────────────────────────────

# 建立一段包含兩組雙引號內容的字串
text2 = 'Computer says "no." Phone says "yes."'

# 使用貪婪匹配（greedy matching）
# .* 會盡可能匹配最多內容
# 因此它會從第一個 " 一路吃到最後一個 "
greedy_result = re.compile(r'"(.*)"').findall(text2)

# 使用非貪婪匹配（non-greedy matching）
# .*? 會盡可能匹配最少內容
# 因此會各自抓出每一組雙引號中的內容
nongreedy_result = re.compile(r'"(.*?)"').findall(text2)

print("原始字串 text2：")
print(text2)

print()  # 空一行，讓輸出更清楚

print("使用貪婪匹配 r'\"(.*)\"' 的結果：")
print(greedy_result)  # ['no." Phone says "yes.']

print("使用非貪婪匹配 r'\"(.*?)\"' 的結果：")
print(nongreedy_result)  # ['no.', 'yes.']

print()  # 空一行，讓輸出更清楚

# ── 2.8 多行匹配（DOTALL）────────────────────────────

# 建立一段多行字串 code
# 裡面模擬 C 語言風格的多行註解
code = "/* this is a\nmultiline comment */"

# 一般情況下，. 不會匹配換行字元
# 但加上 re.DOTALL 之後，. 就可以匹配包含換行在內的所有字元
# 這樣才能正確抓到跨多行的註解內容
dotall_result = re.compile(r"/\*(.*?)\*/", re.DOTALL).findall(code)

print("原始多行字串 code：")
print(code)

print()  # 空一行，讓輸出更清楚

print("使用 re.DOTALL 進行多行匹配的結果：")
print(dotall_result)
# [' this is a\nmultiline comment ']