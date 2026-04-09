import re
import timeit
from calendar import month_abbr

# ── 2.4 預編譯效能 (Precompiling Performance) ───────────────────────
# 當你需要重複使用同一個正規表達式時，先用 re.compile() 將其編譯成 Pattern 物件
# 這樣可以省去每次呼叫時重新解析字串的時間。

text = "Today is 11/27/2012. PyCon starts 3/13/2013."
# 預先編譯正則表達式，定義三個數字群組（月/日/年）
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")

def using_module():
    """直接使用 re 模組函式（內部會有快取機制，但在極高頻率下仍略慢）"""
    return re.findall(r"(\d+)/(\d+)/(\d+)", text)

def using_compiled():
    """使用預編譯好的物件（效能最優）"""
    return datepat.findall(text)

# 測試執行 50,000 次的耗時差異
t1 = timeit.timeit(using_module, number=50_000)
t2 = timeit.timeit(using_compiled, number=50_000)
print(f"直接呼叫: {t1:.3f}s  預編譯: {t2:.3f}s")


# ── 2.5 sub 回呼函數 (Callback Functions in sub) ───────────────────
# re.sub() 除了可以用固定字串替換，還可以傳入一個「函式」
# 這個函式會接收一個 Match 物件，並回傳要替換進去的字串。

def change_date(m: re.Match) -> str:
    """
    將匹配到的 Match 物件轉換為格式化的日期。
    例如：'11/27/2012' -> '27 Nov 2012'
    """
    # m.group(1) 是月份，轉成整數後去 month_abbr 找縮寫（如 11 -> Nov）
    mon_name = month_abbr[int(m.group(1))]
    # 重新排列順序：日 (group 2)、月縮寫、年 (group 3)
    return f"{m.group(2)} {mon_name} {m.group(3)}"

# 使用 sub 時傳入 change_date 函式作為替換邏輯
print(datepat.sub(change_date, text))
# 輸出: 'Today is 27 Nov 2012. PyCon starts 13 Mar 2013.'


# ── 2.6 保持大小寫一致的替換 (Case-Insensitive Replacement) ────────
# 有時候我們想忽略大小寫搜尋（IGNORECASE），但在替換時，
# 希望「替換後的字串」能自動模仿「原字串」的大小寫格式。

def matchcase(word: str):
    """
    閉包 (Closure) 函數：記錄目標單字（如 'snake'），
    並回傳一個能根據匹配內容調整大小寫的替換函式。
    """
    def replace(m: re.Match) -> str:
        t = m.group()  # 取得原本在字串中被匹配到的內容
        if t.isupper():
            return word.upper()       # 原本全大寫，則替換後全大寫
        if t.islower():
            return word.lower()       # 原本全小寫，則替換後全小寫
        if t[0].isupper():
            return word.capitalize()  # 原本首字母大寫，則替換後首字母大寫
        return word                   # 其他情況則回傳原始目標單字

    return replace

s = "UPPER PYTHON, lower python, Mixed Python"

# 這裡 re.sub 的第二個參數是 matchcase("snake") 回傳的 replace 函式
# flags=re.IGNORECASE 確保能找到不論大小寫的 'python'
result = re.sub("python", matchcase("snake"), s, flags=re.IGNORECASE)
print(result)
# 輸出: 'UPPER SNAKE, lower snake, Mixed Snake'