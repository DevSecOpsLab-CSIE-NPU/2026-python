import re
import timeit
from calendar import month_abbr

# ── 預編譯正規表示式 vs 每次呼叫模組函式 ────────────────
# 若同一個 pattern 要重複使用，預先編譯可節省每次解析 pattern 的時間
text = "Today is 11/27/2012. PyCon starts 3/13/2013."
# re.compile 回傳一個已編譯的 Pattern 物件
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")


def using_module():
    """每次都讓 re 模組重新解析 pattern（較慢）。"""
    return re.findall(r"(\d+)/(\d+)/(\d+)", text)


def using_compiled():
    """使用已編譯的 Pattern 物件（較快）。"""
    return datepat.findall(text)


# timeit：測量函式執行 50,000 次的總秒數
t1 = timeit.timeit(using_module, number=50_000)
t2 = timeit.timeit(using_compiled, number=50_000)
print(f"直接呼叫: {t1:.3f}s 預編譯: {t2:.3f}s")  # 預編譯通常快約 10–20%


# ── 用回呼函式做進階替換 ─────────────────────────────────
# re.sub 的 repl 參數可以是函式；每次匹配都會呼叫該函式
def change_date(m: re.Match) -> str:
    """將 MM/DD/YYYY 格式轉成 DD Mon YYYY 格式。"""
    mon_name = month_abbr[int(m.group(1))]  # group(1)=月份 → 英文縮寫
    return f"{m.group(2)} {mon_name} {m.group(3)}"


print(datepat.sub(change_date, text))  # Today is 27 Nov 2012. ...


# ── 保留大小寫的替換（closure 技巧）──────────────────────
def matchcase(word: str):
    """回傳一個替換函式，讓替換後的詞保持與原匹配相同的大小寫風格。"""
    def replace(m: re.Match) -> str:
        t = m.group()
        if t.isupper():       # 全大寫 → 全大寫替換
            return word.upper()
        if t.islower():       # 全小寫 → 全小寫替換
            return word.lower()
        if t[0].isupper():    # 首字大寫 → 首字大寫替換
            return word.capitalize()
        return word           # 其他情況原樣

    return replace  # 回傳閉包函式


s = "UPPER PYTHON, lower python, Mixed Python"
# re.IGNORECASE：不分大小寫匹配；matchcase 確保替換後樣式一致
print(re.sub("python", matchcase("snake"), s, flags=re.IGNORECASE))
# → UPPER SNAKE, lower snake, Mixed Snake
