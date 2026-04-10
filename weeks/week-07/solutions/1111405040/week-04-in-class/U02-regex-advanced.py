"""
U02. 正則表達式進階技巧。

這份範例示範：
1. 預編譯正則表達式的效能差異。
2. `re.sub()` 使用回呼函式做動態替換。
3. 替換時如何保留原字串的大小寫風格。
"""

import re
import timeit
from calendar import month_abbr


text = "Today is 11/27/2012. PyCon starts 3/13/2013."

# 把樣式先編譯好，之後可重複使用。
date_pattern = re.compile(r"(\d+)/(\d+)/(\d+)")


def using_module():
    """每次都把樣式字串交給 re 模組處理。"""
    return re.findall(r"(\d+)/(\d+)/(\d+)", text)


def using_compiled():
    """重複使用已編譯好的 pattern。"""
    return date_pattern.findall(text)


# 若同一個樣式要反覆使用很多次，預編譯通常較省時間。
module_time = timeit.timeit(using_module, number=50_000)
compiled_time = timeit.timeit(using_compiled, number=50_000)
print(f"直接呼叫: {module_time:.3f}s  預編譯: {compiled_time:.3f}s")


def change_date(match: re.Match) -> str:
    """
    把 `11/27/2012` 轉成 `27 Nov 2012`。

    `match.group(1)` 是月份，
    `match.group(2)` 是日期，
    `match.group(3)` 是年份。
    """

    month_name = month_abbr[int(match.group(1))]
    return f"{match.group(2)} {month_name} {match.group(3)}"


# `re.sub()` 可以不是只換固定字串，而是根據 match 動態決定新內容。
print(date_pattern.sub(change_date, text))


def matchcase(word: str):
    """
    建立一個替換函式，讓新字詞盡量保留原字詞的大小寫形式。

    例如：
    - `PYTHON` -> `SNAKE`
    - `python` -> `snake`
    - `Python` -> `Snake`
    """

    def replace(match: re.Match) -> str:
        target = match.group()
        if target.isupper():
            return word.upper()
        if target.islower():
            return word.lower()
        if target[0].isupper():
            return word.capitalize()
        return word

    return replace


s = "UPPER PYTHON, lower python, Mixed Python"
print(re.sub("python", matchcase("snake"), s, flags=re.IGNORECASE))
