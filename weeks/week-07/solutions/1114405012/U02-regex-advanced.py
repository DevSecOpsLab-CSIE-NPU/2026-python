"""U02 正則表達式進階技巧（2.4–2.6）。"""

# 核心提醒：重複使用的 pattern 可預編譯；sub 可用函式做客製化替換

import re
import timeit
from calendar import month_abbr

# ── 預編譯效能（2.4）──────────────────────────────────
text = "Today is 11/27/2012. PyCon starts 3/13/2013."
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")


def using_module():
    return re.findall(r"(\d+)/(\d+)/(\d+)", text)


def using_compiled():
    # 預編譯後可重複使用，通常比每次重新解析 pattern 更快
    return datepat.findall(text)


t1 = timeit.timeit(using_module, number=50_000)
t2 = timeit.timeit(using_compiled, number=50_000)
print(f"直接呼叫: {t1:.3f}s  預編譯: {t2:.3f}s")


# ── sub 回呼函數（2.5）────────────────────────────────
def change_date(m: re.Match) -> str:
    # m.group(1/2/3) 分別對應月、日、年
    mon_name = month_abbr[int(m.group(1))]
    return f"{m.group(2)} {mon_name} {m.group(3)}"


print(datepat.sub(change_date, text))
# 'Today is 27 Nov 2012. PyCon starts 13 Mar 2013.'


# ── 保持大小寫一致的替換（2.6）───────────────────────
def matchcase(word: str):
    # 回傳一個替換函式：依照匹配到的原字串大小寫輸出對應結果
    def replace(m: re.Match) -> str:
        t = m.group()
        if t.isupper():
            return word.upper()
        if t.islower():
            return word.lower()
        if t[0].isupper():
            return word.capitalize()
        return word

    return replace


s = "UPPER PYTHON, lower python, Mixed Python"
print(re.sub("python", matchcase("snake"), s, flags=re.IGNORECASE))
# 'UPPER SNAKE, lower snake, Mixed Snake'
