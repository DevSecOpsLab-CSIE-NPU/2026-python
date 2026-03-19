# R02. 正則表達式：搜尋、替換、旗標（2.4–2.8）
# 核心功能：re.compile / findall / sub / IGNORECASE / 非貪婪 / DOTALL
#
# 本檔案演示正則表達式的四大核心操作：
#   1. 編譯與搜尋（compile + findall/match/finditer）
#   2. 進行字串替換與「backreference」技巧
#   3. 使用旗標進行忽略大小寫匹配
#   4. 貪婪與非貪婪匹配的差異

import re

# ═══════════════════════════════════════════════════════════════════════════
# 2.4 編譯及搜尋：re.compile + findall/match/finditer
# ═══════════════════════════════════════════════════════════════════════════
# 問題：想在字串中搜尋日期模式（MM/DD/YYYY）
# 解決：使用 re.compile() 編譯為正則物件，再用 findall/match/finditer

text = "Today is 11/27/2012. PyCon starts 3/13/2013."

# 🔧 編譯正則表達式
# 語法分解：(\d+)/(\d+)/(\d+)
#   (\d+) = 捕獲一個或多個數字到分組1（月份）
#   /     = 字面上的斜杠
#   (\d+) = 捕獲一個或多個數字到分組2（日期）
#   /     = 字面上的斜杠
#   (\d+) = 捕獲一個或多個數字到分組3（年份）
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")

# 方法1：findall() 回傳所有符合的「分組元組」
# 不符合就回傳空，符合就回傳元組清單
print(datepat.findall(text))
# 輸出：[('11', '27', '2012'), ('3', '13', '2013')]
# 説明：找到兩個日期，每個日期的三個分組分別打包成元組

# 方法2：match() 只檢查字串起始位置（從第一字元開始匹配）
# 返回 Match 物件或 None
m = datepat.match("11/27/2012")
assert m is not None  # 確實符合
# m.group(0) = 整個匹配 = '11/27/2012'
# m.groups() = 所有分組 = ('11', '27', '2012')
print(m.group(0), m.groups())  # '11/27/2012' ('11', '27', '2012')

# 方法3：finditer() 回傳指標物件，逐個遍歷匹配
# 適合需要存取 Match 物件的詳細資訊時
for m in datepat.finditer(text):
    # 從 Match 物件的分組中解包
    month, day, year = m.groups()
    # 重組成 YYYY-MM-DD 格式
    print(f"{year}-{month}-{day}")
# 輸出：
# 2012-11-27
# 2013-3-13


# ═══════════════════════════════════════════════════════════════════════════
# 2.5 搜尋與替換：re.sub() 及 Backreference（\1, \2, \3 等）
# ═══════════════════════════════════════════════════════════════════════════
# 問題：想將日期格式從 MM/DD/YYYY 改為 YYYY-MM-DD
# 解決：使用 re.sub() 搭配 backreference（\N 表示第 N 個分組）

# 方法1：使用數字 backreference（\1, \2, \3...）
# 用法：re.sub(pattern, replacement, string)
#   \3 = 第3分組（年份）
#   \1 = 第1分組（月份）
#   \2 = 第2分組（日期）
print(re.sub(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text))
# 輸出：'Today is 2012-11-27. PyCon starts 2013-3-13.'
# 説明：11/27/2012 變 2012-11-27，3/13/2013 變 2013-3-13

# 方法2：使用命名分組（更可讀）
# 語法：(?P<name>...) 將分組命名為 name
# 在替換中用 \g<name> 引用
print(
    re.sub(
        r"(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)",
        r"\g<year>-\g<month>-\g<day>",
        text,
    )
)
# 輸出：'Today is 2012-11-27. PyCon starts 2013-3-13.'
# 説明：使用 (?P<name>...) 給分組命名，\g<name> 引用分組
#      可讀性高，適合複雜模式

# 如果需要知道替換了幾次，使用 re.subn()（返回元組：(新字串, 計數)）
newtext, n = re.subn(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text)
print(f"替換了 {n} 次")  # 替換了 2 次
# 説明：subn = substitute + count


# ═══════════════════════════════════════════════════════════════════════════
# 2.6 忽略大小寫：re.IGNORECASE 旗標
# ═══════════════════════════════════════════════════════════════════════════
# 問題：想搜尋 "python" 但原文中有 PYTHON、python、Python 各種大小寫
# 解決：使用 flags=re.IGNORECASE（或 re.I）

s = "UPPER PYTHON, lower python, Mixed Python"

# 不使用旗標時，只找到小寫 "python"，找不到 PYTHON 或 Python
print(re.findall("python", s))  # ['python']

# 使用 re.IGNORECASE 旗標，找到所有大小寫變體
print(re.findall("python", s, flags=re.IGNORECASE))
# 輸出：['PYTHON', 'python', 'Python']
# 説明：旗標讓正則引擎在匹配時忽略大小寫差異


# ═══════════════════════════════════════════════════════════════════════════
# 2.7 貪婪 vs 非貪婪：* 和 *? 的差異
# ═══════════════════════════════════════════════════════════════════════════
# 問題：想從 'say "no." Phone says "yes."' 中提取報價內容
# 陷阱：不小心選擇會貪心匹配，導致結果不對

text2 = 'Computer says "no." Phone says "yes."'

# ❌ 貪婪匹配 (.*) - 匹配越多越好
# 結果：只提取一個元組，從第一個引號到最後一個引號
greedy_result = re.compile(r'"(.*)"').findall(text2)
print(greedy_result)  # ['no." Phone says "yes.']\（誤）
# 説明：.* 貪心地匹配到最後可能的引號，導致捕獲了中間的 Phone says

# ✅ 非貪婪匹配 (.*?) - 盡快停止（在 ? 後加 ?）
# 在遇到下一個引號時立即停止
nongreedy_result = re.compile(r'"(.*?)"').findall(text2)
print(nongreedy_result)  # ['no.', 'yes.']\（正確）
# 説明：.*? 遇到第一個引號立即停止，然後繼續搜尋下一個配對


# ═══════════════════════════════════════════════════════════════════════════
# 2.8 多行匹配：re.DOTALL 旗標（讓 . 匹配換行符）
# ═══════════════════════════════════════════════════════════════════════════
# 問題：. 在正則中只匹配「除換行外的任何字元」，多行文本匹配困難
# 解決：使用 re.DOTALL（或 re.S）讓 . 也匹配 \n

code = "/* this is a\nmultiline comment */"

# 不使用 DOTALL：. 無法跨越 \n，匹配失敗
no_dotall = re.compile(r"/\*(.*?)\*/").findall(code)
print(no_dotall)  # []\（找不到）
# 説明：.* 無法匹配中間的換行符，所以無法完整提取註解

# 使用 DOTALL：. 可以匹配 \n，成功提取多行內容
with_dotall = re.compile(r"/\*(.*?)\*/", re.DOTALL).findall(code)
print(with_dotall)  # [' this is a\nmultiline comment ']\（正確）
# 説明：re.DOTALL 讓 .* 能跨越換行符，完整捕獲多行註解
