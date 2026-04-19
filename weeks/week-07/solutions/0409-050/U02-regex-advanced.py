# U02. 正則表達式進階技巧（2.4–2.6）
# 預編譯效能 / sub 回呼函數 / 大小寫一致替換

# 導入正則表達式模組，用於處理字串的模式匹配。
import re
# 導入 timeit 模組，用於測量小段程式碼的執行時間，以比較不同實現的效能。
import timeit
# 從 calendar 模組導入 month_abbr，它是一個包含月份縮寫的列表（例如：['', 'Jan', 'Feb', ...]）。
from calendar import month_abbr

# ── 預編譯效能（2.4）──────────────────────────────────
# 說明：當一個正則表達式會被重複使用多次時，預先編譯它（使用 `re.compile()`) 可以提高效能。
# 編譯後的正則表達式物件會將模式轉換為內部格式，避免每次使用時都重新解析。
text = "Today is 11/27/2012. PyCon starts 3/13/2013."
# 使用 re.compile() 預編譯一個正則表達式模式。
# r"(\d+)/(\d+)/(\d+)"：
#   - \d+：匹配一個或多個數字。
#   - /：匹配斜線字元。
#   - ()：捕獲分組，將匹配到的數字分別捕獲為獨立的組（月、日、年）。
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")

# 定義一個函數，每次調用時都直接使用 `re` 模組的函數，不進行預編譯。
def using_module():
    # `re.findall()` 尋找字串中所有不重疊的匹配項，並以列表形式返回所有捕獲分組。
    return re.findall(r"(\d+)/(\d+)/(\d+)", text)

# 定義一個函數，使用預編譯好的正則表達式物件。
def using_compiled():
    # 直接在編譯後的 `datepat` 物件上調用 `findall()`。
    return datepat.findall(text)

# 使用 timeit 測量 `using_module` 函數執行 50,000 次所需的時間。
t1 = timeit.timeit(using_module, number=50_000)
# 使用 timeit 測量 `using_compiled` 函數執行 50,000 次所需的時間。
t2 = timeit.timeit(using_compiled, number=50_000)
# 輸出兩種方法的執行時間，通常預編譯會更快。
print(f"直接呼叫: {t1:.3f}s  預編譯: {t2:.3f}s")

# ── sub 回呼函數（2.5）────────────────────────────────
# 說明：`re.sub()` 函數除了可以接受替換字串外，還可以接受一個回呼函數 (callback function)。
# 這個回呼函數會在每次匹配成功時被調用，並接收一個匹配物件 (match object) 作為參數。
# 函數的返回值將作為替換字串。這提供了更靈活的替換邏輯。

# 定義一個回呼函數，用於將日期格式從 "月/日/年" 轉換為 "日 月份縮寫 年"。
def change_date(m: re.Match) -> str:
    # `m.group(1)` 獲取第一個捕獲分組（月份），轉換為整數後作為 `month_abbr` 的索引。
    mon_name = month_abbr[int(m.group(1))]
    # 返回格式化後的字串。`m.group(2)` 是日期，`m.group(3)` 是年份。
    return f"{m.group(2)} {mon_name} {m.group(3)}"

# 使用 `datepat.sub()` 進行替換，將 `change_date` 函數作為替換參數。
# 每次 `datepat` 匹配到日期時，都會調用 `change_date` 函數來生成替換字串。
print(datepat.sub(change_date, text))
# 'Today is 27 Nov 2012. PyCon starts 13 Mar 2013.'

# ── 保持大小寫一致的替換（2.6）───────────────────────
# 說明：在進行不區分大小寫的替換時，有時需要保持被替換字串的原始大小寫格式。
# 這個例子展示了如何使用回呼函數來實現這一點。

# 定義一個高階函數 `matchcase`，它接受一個目標單詞 `word`，並返回一個內部函數 `replace`。
# 這樣做是為了讓 `replace` 函數能夠「記住」要替換成的目標單詞。
def matchcase(word: str):
    # 內部函數 `replace` 接收一個匹配物件 `m`。
    def replace(m: re.Match) -> str:
        # `m.group()` 獲取整個匹配到的字串（例如 "PYTHON", "python", "Python"）。
        t = m.group()
        # 檢查原始匹配字串是否全部大寫。
        if t.isupper():
            # 如果是，則將目標單詞轉換為全部大寫。
            return word.upper()
        # 檢查原始匹配字串是否全部小寫。
        if t.islower():
            # 如果是，則將目標單詞轉換為全部小寫。
            return word.lower()
        # 檢查原始匹配字串的首字母是否大寫。
        if t[0].isupper():
            # 如果是，則將目標單詞的首字母大寫。
            return word.capitalize()
        # 如果以上條件都不符合（例如，混合大小寫但首字母不是大寫），則直接返回目標單詞。
        return word

    return replace

# 原始字串，包含不同大小寫形式的 "python"。
s = "UPPER PYTHON, lower python, Mixed Python"
# 使用 `re.sub()` 進行替換。
# "python"：要匹配的模式。
# `matchcase("snake")`：替換函數，它會根據原始匹配的大小寫返回 "snake" 的不同形式。
# `s`：要操作的字串。
# `flags=re.IGNORECASE`：設置旗標，使正則表達式匹配時不區分大小寫。
print(re.sub("python", matchcase("snake"), s, flags=re.IGNORECASE))
# 'UPPER SNAKE, lower snake, Mixed Snake' 
