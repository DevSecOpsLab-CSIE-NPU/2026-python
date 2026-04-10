# U02. 正則表達式進階技巧（2.4–2.6）
# 說明：預編譯效能 / sub 回呼函數 / 大小寫一致替換

import re
import timeit
from calendar import month_abbr

# ─────────────────────────────────────────────────────────────────
# 預編譯效能（2.4）
# 說明：預先編譯正則表達式可以提升效能，適合重複使用同一個 pattern
# ─────────────────────────────────────────────────────────────────

text = "Today is 11/27/2012. PyCon starts 3/13/2013."

# 預先編譯正則表達式 pattern
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")


def using_module():
    """每次呼叫 re.findall() 時都會重新解析正則表達式"""
    return re.findall(r"(\d+)/(\d+)/(\d+)", text)


def using_compiled():
    """使用預先編譯的 pattern 直接呼叫方法"""
    return datepat.findall(text)


# 執行效能測試：50,000 次
t1 = timeit.timeit(using_module, number=50_000)
t2 = timeit.timeit(using_compiled, number=50_000)
print(f"直接呼叫: {t1:.3f}s  預編譯: {t2:.3f}s")


# ─────────────────────────────────────────────────────────────────
# sub 回呼函數（2.5）
# 說明：re.sub() 的替換參數可以是一個函數，進行更複雜的處理
# ─────────────────────────────────────────────────────────────────

def change_date(m: re.Match) -> str:
    """
    將日期格式從 MM/DD/YYYY 改為 DD Mon YYYY
    
    參數：
        m：正則表達式的匹配物件
    
    回傳：
        格式化後的字串
    """
    # m.group(1) = 月份
    # m.group(2) = 日期
    # m.group(3) = 年份
    mon_name = month_abbr[int(m.group(1))]
    return f"{m.group(2)} {mon_name} {m.group(3)}"


# 使用回呼函數進行自定義替換
print(datepat.sub(change_date, text))
# 輸出：'Today is 27 Nov 2012. PyCon starts 13 Mar 2013.'


# ─────────────────────────────────────────────────────────────────
# 保持大小寫一致的替換（2.6）
# 說明：替換時保留原文的大小寫形式（全部大寫、全部小寫、首字母大寫）
# ─────────────────────────────────────────────────────────────────

def matchcase(word: str):
    """
    建立一個回呼函數，根據匹配文字的大小寫形式調整替換文字
    
    參數：
        word：要替換成的基準字串
    
    回傳：
        回呼函數物件
    """
    
    def replace(m: re.Match) -> str:
        t = m.group()
        # 如果原文全部大寫，替換文字也全部大寫
        if t.isupper():
            return word.upper()
        # 如果原文全部小寫，替換文字也全部小寫
        if t.islower():
            return word.lower()
        # 如果原文首字母大寫，替換文字也首字母大寫
        if t[0].isupper():
            return word.capitalize()
        # 其他情況直接使用原文
        return word
    
    return replace


s = "UPPER PYTHON, lower python, Mixed Python"

# 使用 re.IGNORECASE 忽略大小寫匹配，再用 matchcase 保持大小寫一致
print(re.sub("python", matchcase("snake"), s, flags=re.IGNORECASE))
# 輸出：'UPPER SNAKE, lower snake, Mixed Snake'