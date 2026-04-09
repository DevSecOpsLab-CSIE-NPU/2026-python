# U02. 正則表達式進階技巧（2.4–2.6）
# 這份範例示範三個實務上很常用的正則技巧：
# 1. 先把正則預編譯成物件，避免重複建立模式的成本。
# 2. 使用 sub() 搭配回呼函數，讓替換結果可以依比對內容動態生成。
# 3. 以自訂替換函數保留原文字的大小寫風格，讓批次替換看起來更自然。

import re
import timeit
from calendar import month_abbr

# ── 預編譯效能（2.4）──────────────────────────────────
# re.compile() 會先把正則模式編成可重複使用的物件。
# 當同一個模式要大量執行時，預編譯通常比每次都重新解析字串模式更有效率。
text = "Today is 11/27/2012. PyCon starts 3/13/2013."
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")


def using_module():
    # 每次呼叫都直接把正則字串交給 re.findall()，等於每次都要重新處理模式。
    return re.findall(r"(\d+)/(\d+)/(\d+)", text)


def using_compiled():
    # 這裡直接使用已編譯好的 datepat 物件，重複執行時通常會更快。
    return datepat.findall(text)


# timeit.timeit() 用來做簡單效能比較；這裡執行很多次，是為了讓差異更明顯。
t1 = timeit.timeit(using_module, number=50_000)
t2 = timeit.timeit(using_compiled, number=50_000)
# 你會看到預編譯版本通常較快，但實際差距會依 Python 版本與機器而變動。
print(f"直接呼叫: {t1:.3f}s  預編譯: {t2:.3f}s")


# ── sub 回呼函數（2.5）────────────────────────────────
# re.sub() 除了可以直接用字串替換，也可以傳入函數。
# 當替換內容需要根據每次匹配到的資料動態組裝時，回呼函數會比固定字串更有彈性。
def change_date(m: re.Match) -> str:
    # month_abbr 是月份縮寫表，例如 month_abbr[1] = 'Jan'。
    # m.group(1)、m.group(2)、m.group(3) 分別代表正則中的三個捕獲群組。
    mon_name = month_abbr[int(m.group(1))]
    return f"{m.group(2)} {mon_name} {m.group(3)}"


# 這裡把 11/27/2012 轉成 27 Nov 2012。
# 回呼函數會對每一個符合模式的日期各自執行一次，所以可同時處理多筆資料。
print(datepat.sub(change_date, text))
# 'Today is 27 Nov 2012. PyCon starts 13 Mar 2013.'


# ── 保持大小寫一致的替換（2.6）───────────────────────
# 有時候我們想把所有出現的關鍵字換成新字，但又不想破壞原本的大小寫風格。
# 例如：UPPER 仍然維持全大寫，lower 仍然維持全小寫，Mixed 則保留首字大寫。
def matchcase(word: str):
    # 這個內層函數會真正拿去給 re.sub() 使用。
    # 它會先讀取原本被匹配到的文字，再依其大小寫樣式決定如何產生替換字串。
    def replace(m: re.Match) -> str:
        t = m.group()
        if t.isupper():
            # 若原文字全大寫，替換字也轉成全大寫。
            return word.upper()
        if t.islower():
            # 若原文字全小寫，替換字也轉成全小寫。
            return word.lower()
        if t[0].isupper():
            # 若第一個字母大寫，通常視為標題式大小寫，替換字也跟著首字大寫。
            return word.capitalize()
        # 其他情況就直接回傳原本的替換字，避免過度猜測格式。
        return word

    # 回傳函數本身，而不是直接做替換。
    # 這樣 re.sub() 在每次匹配時都能呼叫同一個規則去產生結果。
    return replace


s = "UPPER PYTHON, lower python, Mixed Python"
# IGNORECASE 讓 python / Python / PYTHON 都能被匹配到。
# 因為替換函數會依原字樣的大小寫再做調整，所以結果看起來比較自然。
print(re.sub("python", matchcase("snake"), s, flags=re.IGNORECASE))
# 'UPPER SNAKE, lower snake, Mixed Snake'
