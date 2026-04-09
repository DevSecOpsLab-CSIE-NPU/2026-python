# U02. 正則表達式進階技巧（2.4–2.6）
# 預編譯效能 / sub 回呼函數 / 大小寫一致替換

import re
import timeit
from calendar import month_abbr

# ── 預編譯效能（2.4）──────────────────────────────────
# 同一個正則如果會重複使用，多次 re.compile() 以外的操作會比較慢。
# 預先編譯成 pattern 物件後，可以重複拿來比對，通常更省時間。
text = "Today is 11/27/2012. PyCon starts 3/13/2013."
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")


def using_module():
    return re.findall(r"(\d+)/(\d+)/(\d+)", text)


def using_compiled():
    return datepat.findall(text)


t1 = timeit.timeit(using_module, number=50_000)
t2 = timeit.timeit(using_compiled, number=50_000)
print(f"直接呼叫 re.findall(): {t1:.3f}s")
print(f"使用預編譯 pattern: {t2:.3f}s")
print(f"預編譯快了約 {t1 / t2:.2f} 倍")


# ── sub 回呼函數（2.5）────────────────────────────────
# re.sub() 的第二個參數不一定要是固定字串，也可以傳入函數。
# 函數會收到每一次匹配到的 Match 物件，讓我們能依照捕獲內容動態產生替換結果。
def change_date(m: re.Match) -> str:
    mon_name = month_abbr[int(m.group(1))]
    return f"{m.group(2)} {mon_name} {m.group(3)}"


print("日期格式轉換後：", datepat.sub(change_date, text))
# 'Today is 27 Nov 2012. PyCon starts 13 Mar 2013.'


# ── 保持大小寫一致的替換（2.6）───────────────────────
# 有時候要把文字替換掉，但希望新文字保留原本的大小寫風格。
# 這裡的 matchcase() 會根據原字串是全大寫、全小寫、首字大寫或混合大小寫，
# 決定替換文字要用哪種大小寫形式。
def matchcase(word: str):
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
print("保留原有大小寫風格的替換：", re.sub("python", matchcase("snake"), s, flags=re.IGNORECASE))
# 'UPPER SNAKE, lower snake, Mixed Snake'
