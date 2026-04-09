# U02. 正則表達式進階技巧（2.4–2.6）
# 本程式示範正則表達式的進階用法和效能優化：
# 2.4 預編譯效能 - 編譯正則表達式以提升重複使用的效能
# 2.5 sub 回呼函數 - 在替換時使用函數進行動態處理
# 2.6 大小寫一致替換 - 保持替換字串的大小寫格式

import re
import timeit
from calendar import month_abbr

# ── 預編譯效能（2.4）──────────────────────────────────
# 問題：重複使用相同正則表達式時，每次呼叫 re.findall() 都會重新編譯
# 解決方案：預先編譯正則表達式，只編譯一次
text = "Today is 11/27/2012. PyCon starts 3/13/2013."

# 日期匹配模式：月/日/年
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")


# 未預編譯版本：每次呼叫都重新編譯
def using_module():
    return re.findall(r"(\d+)/(\d+)/(\d+)", text)


# 預編譯版本：使用已編譯的模式
def using_compiled():
    return datepat.findall(text)


# 效能測試：執行 50,000 次
t1 = timeit.timeit(using_module, number=50_000)
t2 = timeit.timeit(using_compiled, number=50_000)
print(f"直接呼叫: {t1:.3f}s  預編譯: {t2:.3f}s")


# ── sub 回呼函數（2.5）────────────────────────────────
# 問題：re.sub() 的替換字串是固定的
# 解決方案：使用回呼函數根據匹配結果動態產生替換字串

# 日期格式轉換函數：將 MM/DD/YYYY 轉為 DD Mon YYYY
def change_date(m: re.Match) -> str:
    # m.group(1) = 月, m.group(2) = 日, m.group(3) = 年
    mon_name = month_abbr[int(m.group(1))]  # 將月份數字轉為英文縮寫
    return f"{m.group(2)} {mon_name} {m.group(3)}"


print(datepat.sub(change_date, text))
# 'Today is 27 Nov 2012. PyCon starts 13 Mar 2013.'


# ── 保持大小寫一致的替換（2.6）───────────────────────
# 問題：替換時不考慮原始字串的大小寫格式
# 解決方案：根據匹配字串的大小寫動態調整替換字串

def matchcase(word: str):
    """
    建立一個替換函數，根據匹配字串的大小寫格式調整替換字串

    Args:
        word: 要替換成的目標字串

    Returns:
        替換函數，接受 re.Match 物件並返回適當大小寫的字串
    """
    def replace(m: re.Match) -> str:
        t = m.group()  # 匹配的原始字串
        if t.isupper():
            return word.upper()  # 全大寫
        elif t.islower():
            return word.lower()  # 全小寫
        elif t[0].isupper():
            return word.capitalize()  # 首字母大寫
        else:
            return word  # 其他情況保持原樣

    return replace


# 測試大小寫一致替換
s = "UPPER PYTHON, lower python, Mixed Python"
print(re.sub("python", matchcase("snake"), s, flags=re.IGNORECASE))
# 'UPPER SNAKE, lower snake, Mixed Snake'
