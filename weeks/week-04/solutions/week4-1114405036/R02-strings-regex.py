# R02. 正則表達式：搜尋與替換（範例 2.4–2.8）
import re

# ── 2.4 匹配和搜尋 ──
text = "Today is 11/27/2012. PyCon starts 3/13/2013."
# 先編譯模式可以提高重複執行的效能
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")

# findall 會找到所有匹配項並以 tuple 列表回傳
print(datepat.findall(text)) 
# [('11', '27', '2012'), ('3', '13', '2013')]

# finditer 則適合處理大量匹配，它會回傳迭代器，節省記憶體
for m in datepat.finditer(text):
    print(m.groups()) # 依序處理每一組日期

# ── 2.5 搜尋和替換 ──
# 使用 \3-\1-\2 引用分組內容，將 MM/DD/YYYY 改為 YYYY-MM-DD
print(re.sub(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text))

# 命名群組：讓正則更具可讀性，替換時使用 \g<name>
print(re.sub(r"(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)", r"\g<year>-\g<month>-\g<day>", text))