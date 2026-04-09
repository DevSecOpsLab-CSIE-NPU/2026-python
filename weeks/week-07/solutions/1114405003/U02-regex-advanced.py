# U02. 正則表達式進階技巧（2.4–2.6）
#
# 這個檔案示範三個實用的正則表達式技巧：
# 1. 把常用的 pattern 預先編譯，可避免重複解析字串樣式。
# 2. re.sub() 可以搭配回呼函數，根據每次比對到的內容動態產生替換字串。
# 3. 替換時若要保留原字串的大小寫風格，可以先判斷原文字的大小寫型態。

import re
import timeit
from calendar import month_abbr

# ── 預編譯效能（2.4）──────────────────────────────────
# re.compile() 會先把正則樣式編譯成可重複使用的物件。
# 當同一個 pattern 會被大量使用時，預編譯可以省下重複解析的成本。
# 這種差異在單次執行時不一定明顯，但在大量迴圈裡通常會比較快。
text = "Today is 11/27/2012. PyCon starts 3/13/2013."
# 預先編譯日期樣式，之後就可以直接重複呼叫 datepat.findall()。
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")


def using_module():
    # 每次都把 pattern 傳給 re.findall()，會重複進行解析與比對準備。
    return re.findall(r"(\d+)/(\d+)/(\d+)", text)


def using_compiled(text=text):
    # 直接使用已編譯好的 pattern，少掉重複處理的開銷。
    return datepat.findall(text)


# 用 timeit 比較「直接呼叫」與「預編譯後使用」的效能差異。
# 數字只是在示範，不同電腦、Python 版本、執行環境都可能不同。
t1 = timeit.timeit(using_module, number=50_000)
t2 = timeit.timeit(lambda: using_compiled(text), number=50_000)
print(f"直接呼叫: {t1:.3f}s  預編譯: {t2:.3f}s")


# ── sub 回呼函數（2.5）────────────────────────────────
# re.sub() 不一定只能把所有比對結果替換成固定字串；
# 如果傳入函數，函數會接收到每一次 match 物件，並回傳該次要替換的結果。
# 這樣可以依照捕獲到的群組內容，動態組合新字串。
def change_date(m: re.Match) -> str:
    # m.group(1)、m.group(2)、m.group(3) 分別是月、日、年。
    # month_abbr 會把月份數字轉成英文月份縮寫，例如 11 -> Nov。
    mon_name = month_abbr[int(m.group(1))]
    return f"{m.group(2)} {mon_name} {m.group(3)}"


# 將 mm/dd/yyyy 轉成 dd Mon yyyy，讓輸出更符合人類閱讀習慣。
print(datepat.sub(change_date, text))
# 'Today is 27 Nov 2012. PyCon starts 13 Mar 2013.'


# ── 保持大小寫一致的替換（2.6）───────────────────────
# 有時候我們想把某個關鍵字換掉，但又希望新字串保留原本的大小寫外觀。
# 例如原文是 UPPER、lower、Mixed，替換後也分別維持大寫、小寫、首字大寫。
def matchcase(word: str):
    # 回傳一個真正執行替換的函數，讓 re.sub() 在每次比對時呼叫。
    def replace(m: re.Match) -> str:
        # m.group() 代表本次匹配到的完整文字。
        t = m.group()
        if t.isupper():
            return word.upper()
        if t.islower():
            return word.lower()
        if t[0].isupper():
            return word.capitalize()
        return word

    return replace


# flags=re.IGNORECASE 讓 python/python/PYTHON 都能被比對到。
# matchcase("snake") 會依照原字的大小寫，輸出 SNAKE / snake / Snake。
s = "UPPER PYTHON, lower python, Mixed Python"
print(re.sub("python", matchcase("snake"), s, flags=re.IGNORECASE))
# 'UPPER SNAKE, lower snake, Mixed Snake'
