# U02. 正則表達式進階技巧（2.4–2.6）
# 預編譯效能 / sub 回呼函數 / 大小寫一致替換

import re
import timeit
from calendar import month_abbr

# ── 預編譯效能（2.4）──────────────────────────────────
# 若同一個正規表達式需執行多次，預先 compile 可以省去反覆解析模式的開銷
text = "Today is 11/27/2012. PyCon starts 3/13/2013."
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")

def using_module():
    # 直接呼叫 re.findall，內部每次都會重新查找快取或重新編譯
    return re.findall(r"(\d+)/(\d+)/(\d+)", text)

def using_compiled():
    # 使用預編譯好的物件，效率較高
    return datepat.findall(text)

t1 = timeit.timeit(using_module, number=50_000)
t2 = timeit.timeit(using_compiled, number=50_000)
print(f"直接呼叫: {t1:.3f}s  預編譯: {t2:.3f}s")

# ── sub 回呼函數（2.5）────────────────────────────────
# re.sub 的第二個參數可以是一個函數，用來處理複雜的格式轉換
def change_date(m: re.Match) -> str:
    # m.group(1) 為月份數字，透過 month_abbr 轉換為英文縮寫（如 11 -> Nov）
    mon_name = month_abbr[int(m.group(1))]
    return f"{m.group(2)} {mon_name} {m.group(3)}"

print(datepat.sub(change_date, text))
# 'Today is 27 Nov 2012. PyCon starts 13 Mar 2013.'

# ── 保持大小寫一致的替換（2.6）───────────────────────
# 當替換目標有多種大小寫形式時，此函數可確保替換後的單字繼承原始單字的風格
def matchcase(word: str):
    def replace(m: re.Match) -> str:
        t = m.group()
        if t.isupper():       # 原本全是全大寫
            return word.upper()
        if t.islower():       # 原本全小寫
            return word.lower()
        if t[0].isupper():    # 原本是首字母大寫（Capitalize）
            return word.capitalize()
        return word           # 其他情況
    return replace

s = "UPPER PYTHON, lower python, Mixed Python"
# flags=re.IGNORECASE 讓比對忽略大小寫，而 matchcase 確保替換後風格一致
print(re.sub("python", matchcase("snake"), s, flags=re.IGNORECASE))
# 'UPPER SNAKE, lower snake, Mixed Snake'