# U02. 正則表達式進階技巧（2.4–2.6）
# 預編譯效能 / sub 回呼函數 / 大小寫一致替換
# 本檔示範如何把 regex 從「能用」提升到「可維護、可擴充」。
# 重點不是背 API，而是理解什麼時候該把 regex 寫得更有結構。

import re
import timeit
from calendar import month_abbr

# ── 預編譯效能（2.4）──────────────────────────────────
# 測試用字串包含兩個日期，格式都是 month/day/year。
text = "Today is 11/27/2012. PyCon starts 3/13/2013."

# re.compile() 會先把正規表達式編譯成可重複使用的 Pattern 物件。
# 當同一個 pattern 要用很多次時，這樣通常會比每次從字串重新開始更有效率。
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")


def using_module():
    # 這種寫法簡短，但每次呼叫都要從 pattern 字串重新處理。
    # 在少量使用時差異不大；大量迴圈時才比較明顯。
    return re.findall(r"(\d+)/(\d+)/(\d+)", text)


def using_compiled():
    # 這種寫法把 pattern 先準備好，之後直接重複使用即可。
    return datepat.findall(text)


# timeit 用來做簡單的效能比較。
# 這裡不是要追求絕對精準的 benchmark，而是觀察「預編譯通常較省成本」。
t1 = timeit.timeit(using_module, number=50_000)
t2 = timeit.timeit(using_compiled, number=50_000)
print(f"直接呼叫: {t1:.3f}s  預編譯: {t2:.3f}s")


# ── sub 回呼函數（2.5）────────────────────────────────
# re.sub() 不只可以放固定字串，還可以放函式。
# 當替換結果需要依照「每次匹配到的內容」動態決定時，callback 非常好用。
def change_date(m: re.Match) -> str:
    # m.group(1) = 月, m.group(2) = 日, m.group(3) = 年
    # month_abbr 會把 1 轉成 Jan、11 轉成 Nov 這種英文縮寫。
    mon_name = month_abbr[int(m.group(1))]
    return f"{m.group(2)} {mon_name} {m.group(3)}"


print(datepat.sub(change_date, text))
# 'Today is 27 Nov 2012. PyCon starts 13 Mar 2013.'


# ── 保持大小寫一致的替換（2.6）───────────────────────
# 如果直接把 python 換成 snake，
# 那麼 PYTHON、Python、python 全都會變成同一種大小寫，閱讀體驗不好。
# matchcase() 的目標，就是根據原本匹配到的字做對應調整。
def matchcase(word: str):
    # 外層先收下要替換成的新字。
    # 內層 replace() 才是真正給 re.sub() 呼叫的函式。
    def replace(m: re.Match) -> str:
        t = m.group()

        # 原字全大寫，就把新字也轉成全大寫。
        if t.isupper():
            return word.upper()

        # 原字全小寫，就維持全小寫。
        if t.islower():
            return word.lower()

        # 若只有第一個字母大寫，像 Python，則用 capitalize。
        if t[0].isupper():
            return word.capitalize()

        # 其他較混雜的情況，直接回傳原本輸入的新字。
        return word

    return replace


s = "UPPER PYTHON, lower python, Mixed Python"
print(re.sub("python", matchcase("snake"), s, flags=re.IGNORECASE))
# 'UPPER SNAKE, lower snake, Mixed Snake'
