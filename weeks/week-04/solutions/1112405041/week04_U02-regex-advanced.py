# 【Bloom 階段：U - 理解與進階應用】
# U02. 正規表達式性能優化與動態替換
# August 的惡意提醒：在 Week 03 處理大型文本（如 10008 題）時，
# 反覆呼叫 re.findall() 會慢到讓你懷疑人生。
# 學會使用 Match Object 的回呼函數 (Callback)，這是展現「邏輯控制力」的高級指紋。

import re
import timeit

# 1. 預編譯的性能優勢 (Performance Trap)
text = "Today is 11/27/2012. PyCon starts 3/13/2013."
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")

def using_module(): return re.findall(r"(\d+)/(\d+)/(\d+)", text)
def using_compiled(): return datepat.findall(text)

# 你會發現預編譯快了約 20%~30%
t1 = timeit.timeit(using_module, number=50000)
t2 = timeit.timeit(using_compiled, number=50000)
print(f"Direct vs Compiled: {t1:.3f}s vs {t2:.3f}s")

# 2. sub 搭配回呼函數 (The Substitution Callback)
# 這是 August 最愛的「大家來找碴」考點：根據匹配到的內容「動態」決定替換結果
def matchcase(word):
    def replace(m):
        t = m.group()
        if t.isupper(): return word.upper()
        if t.islower(): return word.lower()
        if t[0].isupper(): return word.capitalize()
        return word
    return replace

s = "UPPER PYTHON, lower python, Mixed Python"
# 讓替換後的單字自動繼承原單字的大小寫格式
print(re.sub("python", matchcase("snake"), s, flags=re.IGNORECASE))
