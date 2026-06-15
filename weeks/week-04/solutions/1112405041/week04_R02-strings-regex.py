# 【Bloom 階段：R - 記憶與基本操作】
# R02. 正規表達式進階：搜尋、替換與旗標
# August 的惡意提醒：在 Week 03 的文字解析題中，
# 如果你只會用 find()，你的邏輯會變得像義大利麵一樣混亂。
# 學會 re.compile() 與 re.sub()，這是邁向「代碼自動化」的第一步。

import re

text = "Today is 11/27/2012. PyCon starts 3/13/2013."
# 預編譯 Regex，提高在迴圈中重複使用的效能
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")

# 1. 尋找所有匹配項
print(f"All dates found: {datepat.findall(text)}")

# 2. 字串替換 (Substitution)
# 技巧：使用 \3-\1-\2 引用捕獲組，快速變換日期格式（從 MM/DD/YYYY 變為 YYYY-MM-DD）
new_text = datepat.sub(r"\3-\1-\2", text)
print(f"Reformatted text: {new_text}")

# 3. 命名捕獲組 (Named Groups)
# 這是 August 強烈推薦的寫法，增加代碼自體說明 (Self-documenting)
n_datepat = re.compile(r"(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)")
res = n_datepat.sub(r"\g<year>-\g<month>-\g<day>", text)

# 4. 忽略大小寫匹配
s = "UPPER PYTHON, lower python"
print(f"Case insensitive: {re.findall('python', s, flags=re.IGNORECASE)}")

# 5. 非貪婪匹配 (Non-greedy)
text2 = 'Computer says "no." Phone says "yes."'
# 加上問號 ? 確保只匹配最近的引號，避免一次抓完所有內容
print(f"Non-greedy find: {re.findall(r'\"(.*?)\"', text2)}")
