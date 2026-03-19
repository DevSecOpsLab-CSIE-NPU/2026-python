# ============================================================================
# R02. 正則表達式：搜尋、替換、旗標（2.4–2.8）
# ============================================================================
# 本題展示五個重要的正規表達式操作：
# 1. re.compile() - 編譯正規表達式以提升效能
# 2. findall() / match() / finditer() - 搜尋字串中的匹配項
# 3. sub() / subn() - 搜尋並替換字串
# 4. re.IGNORECASE - 忽略大小寫的標誌
# 5. 非貪婪匹配 (?...) 與 DOTALL 旗標
# ============================================================================

import re


# ── 2.4 匹配和搜尋（Pattern Matching and Searching） ───────────────────────
print("【2.4 匹配和搜尋】")
print("-" * 50)

# 原始文本：包含兩個日期
text = "Today is 11/27/2012. PyCon starts 3/13/2013."
print(f"原始文本: {text}\n")

# 【編譯正規表達式】
# 模式說明：r"(\d+)/(\d+)/(\d+)"
#   (\d+)  捕獲群組 1：一個或多個數字（月份）
#   /      字面上的斜線符號
#   (\d+)  捕獲群組 2：一個或多個數字（日期）
#   /      字面上的斜線符號
#   (\d+)  捕獲群組 3：一個或多個數字（年份）
# 
# 為什麼使用 re.compile()？
# - 如果同一個正規表達式需要多次使用，編譯後會提高效能
# - 編譯後的正規表達式物件可重複使用
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")

# 【方法 1】findall() - 找出所有匹配項，返回一個列表
# 返回值：[捕獲群組組成的 tuple]
print("【方法 1】findall() - 返回所有匹配的捕獲群組:")
matches = datepat.findall(text)
print(f"結果: {matches}")
# 預期: [('11', '27', '2012'), ('3', '13', '2013')]
print()

# 【方法 2】match() - 從字串開頭開始匹配一次
# 返回值：Match 物件（如果匹配）或 None（如果不匹配）
print("【方法 2】match() - 從字串開頭匹配:")
m = datepat.match("11/27/2012")
assert m is not None
print(f"m.group(0) = {m.group(0)}")      # 完整匹配：'11/27/2012'
print(f"m.groups() = {m.groups()}")      # 所有捕獲群組：('11', '27', '2012')
# 注意：group(0) 是完整的匹配，group(1), group(2), group(3) 各自代表第 1、2、3 個捕獲群組
print()

# 【方法 3】finditer() - 返回一個迭代器，產生每一個匹配的 Match 物件
# 優點：適合大文本，不需要一次性載入所有匹配項到記憶體
print("【方法 3】finditer() - 返回匹配的迭代器，可逐一處理:")
for m in datepat.finditer(text):
    month, day, year = m.groups()
    print(f"  找到日期: {year}-{month}-{day}")  # 轉換為 YYYY-MM-DD 格式
# 預期輸出：
#   找到日期: 2012-11-27
#   找到日期: 2013-3-13
print()


# ── 2.5 搜尋和替換（Search and Replace） ──────────────────────────────────
print("【2.5 搜尋和替換】")
print("-" * 50)

# 【方法 1】re.sub() - 用替換字串取代所有匹配項
print("【方法 1】re.sub() - 替換所有匹配項:")
print(f"原始: {text}")

# 替換模式說明：r"\3-\1-\2"
#   \1  第一個捕獲群組（月份）
#   \2  第二個捕獲群組（日期）
#   \3  第三個捕獲群組（年份）
# 轉換：MM/DD/YYYY → YYYY-MM-DD
result1 = re.sub(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text)
print(f"替換後: {result1}")
# 預期: 'Today is 2012-11-27. PyCon starts 2013-3-13.'
print()

# 【方法 2】使用命名捕獲群組（Named Capture Groups）
# 語法：(?P<name>pattern)
# 優點：可讀性更高，不容易出錯
print("【方法 2】使用命名捕獲群組 - 更易讀:")

# 命名群組說明：
#   (?P<month>\d+)  命名為 "month" 的捕獲群組
#   (?P<day>\d+)    命名為 "day" 的捕獲群組
#   (?P<year>\d+)   命名為 "year" 的捕獲群組
# 
# 在替換字串中使用：\g<name> 來引用命名群組
result2 = re.sub(
    r"(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)",
    r"\g<year>-\g<month>-\g<day>",
    text,
)
print(f"替換後: {result2}")
# 預期結果與方法 1 相同，但程式碼更明確
print()

# 【方法 3】re.subn() - 替換所有匹配項，並返回 (替換後文本, 替換次數)
print("【方法 3】re.subn() - 返回替換後的文本和替換次數:")
newtext, n = re.subn(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text)
print(f"替換後文本: {newtext}")
print(f"替換次數: {n}")
# 預期: 替換了 2 次（因為文本中有 2 個日期）
print()


# ── 2.6 忽略大小寫（Case-Insensitive Matching） ────────────────────────────
print("【2.6 忽略大小寫】")
print("-" * 50)

# 原始字符串：包含不同大小寫變化的「python」
s = "UPPER PYTHON, lower python, Mixed Python"
print(f"原始字符串: {s}\n")

# 【使用 re.IGNORECASE 旗標】
# 旗標 re.IGNORECASE（別名 re.I）使正規表達式不區分大小寫
# 注意：這只影響圖案匹配本身，不影響替換結果
print("【使用 re.IGNORECASE 旗標】")
results = re.findall("python", s, flags=re.IGNORECASE)
print(f"findall('python', s, flags=re.IGNORECASE)")
print(f"結果: {results}")
# 預期: ['PYTHON', 'python', 'Python']
# 說明：找到所有「python」的變體，並保留原始大小寫
print()


# ── 2.7 非貪婪匹配（Non-greedy Matching） ──────────────────────────────────
print("【2.7 非貪婪匹配 vs 貪婪匹配】")
print("-" * 50)

# 原始文本：包含多個用雙引號括起來的字符串
text2 = 'Computer says "no." Phone says "yes."'
print(f"原始文本: {text2}\n")

# 【貪婪匹配】.*
# 解釋：(.*) 表示「匹配任意字符（除換行外），盡可能多」
# 結果：從第一個 " 開始，一直匹配到最後一個 "
print("【貪婪匹配】(.*)")
greedy = re.compile(r'"(.*)"').findall(text2)
print(f"結果: {greedy}")
# 預期: ['no." Phone says "yes.']
# 問題：一個大的匹配，而非兩個獨立的字符串！
print()

# 【非貪婪匹配】.*?
# 解釋：(.*?) 表示「匹配任意字符，盡可能少」
# 結果：從第一個 " 開始，匹配到第一個 "，然後停止（再從下一個 " 開始新的匹配）
print("【非貪婪匹配】(.*?)")
non_greedy = re.compile(r'"(.*?)"').findall(text2)
print(f"結果: {non_greedy}")
# 預期: ['no.', 'yes.']
# 優點：捕獲到兩個獨立的字符串
print()

# 【何時使用非貪婪】
# - 提取成對的符號內容（如 HTML 標籤、引號）
# - 避免誤匹配過多的內容
# - 提高匹配效率（較少的回溯）
print()


# ── 2.8 多行匹配（DOTALL Flag） ───────────────────────────────────────────
print("【2.8 多行匹配（DOTALL）】")
print("-" * 50)

# 原始文本：包含換行符的 C 風格多行註解
code = "/* this is a\nmultiline comment */"
print(f"原始程式碼:\n{code}\n")

# 【問題】默認情況下，. 不匹配換行符
# (.*?) 只能匹配單行的字符

# 【解決方案】使用 re.DOTALL 旗標
# re.DOTALL（別名 re.S）使 . 可以匹配包括換行符的任意字符
print("【使用 re.DOTALL 旗標】")

# 模式說明：r"/\*(.*?)\*/"
#   /\*    字面上的 /*（開始註解）
#   (.*?)  非貪婪匹配任意字符（包括換行，因為有 re.DOTALL）
#   \*/    字面上的 */（結束註解）
result = re.compile(r"/\*(.*?)\*/", re.DOTALL).findall(code)
print(f"findall(r'/\\*(.*?)\\*/', code, re.DOTALL)")
print(f"結果: {result}")
# 預期: [' this is a\nmultiline comment ']
# 說明：成功捕獲跨越多行的註解內容

print("\n【對比】不使用 re.DOTALL:")
result_no_flag = re.compile(r"/\*(.*?)\*/").findall(code)
print(f"結果: {result_no_flag}")
# 預期: [] （空列表，因為 . 無法匹配 \n）
print()
