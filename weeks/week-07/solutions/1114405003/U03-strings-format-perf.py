# U03. 字串格式化效能與陷阱（2.14–2.20）
#
# 這個檔案示範三個常見重點：
# 1. 大量字串串接時，join() 通常比反覆使用 + 更有效率。
# 2. format_map() 可以搭配自訂 dict，讓缺失欄位不要直接報錯。
# 3. str 與 bytes 的索引結果不同，字串回傳字元，bytes 回傳整數。

import timeit

# ── join 效能優於 + （2.14）──────────────────────────
# 在迴圈裡面用 + 反覆串接字串，Python 需要一直建立新物件、複製舊內容，
# 因此資料量愈大，成本愈高；這種方式在理論上接近 O(n²)。
# join() 則是先決定總長度，再一次把所有片段接起來，通常更快也更省記憶體。
parts = [f"item{i}" for i in range(1000)]


def bad_concat():
    s = ""
    for p in parts:
        # 每次加一段都可能產生新的字串物件，舊內容會被重新複製。
        s += p  # 每次建立新字串，O(n²)
    return s


def good_join():
    # join() 讓 Python 以較有效率的方式把所有片段一次接起來。
    return "".join(parts)  # 一次分配，O(n)


# 用 timeit 比較兩種寫法的差異。資料越多，join() 的優勢通常越明顯。
t1 = timeit.timeit(bad_concat, number=500)
t2 = timeit.timeit(good_join, number=500)
print(f"+串接: {t1:.3f}s  join: {t2:.3f}s")


# ── format_map 處理缺失鍵（2.15）─────────────────────
# format_map() 會拿 mapping 去填入格式字串。
# 預設若 key 不存在，會直接 KeyError；這裡透過 __missing__ 改寫行為，
# 讓缺失欄位保留成 {key}，方便除錯或做部分渲染。
class SafeSub(dict):
    def __missing__(self, key: str) -> str:
        # 當格式字串引用到不存在的欄位時，回傳原樣佔位符，不直接丟錯。
        return "{" + key + "}"  # 缺失時保留佔位符


name = "Guido"
s = "{name} has {n} messages."
# vars() 會把目前區域變數包成 dict，這裡只有 name，沒有 n。
# SafeSub 讓 n 缺失時仍能輸出 {n}，而不是整個格式化失敗。
print(s.format_map(SafeSub(vars())))  # 'Guido has {n} messages.'（n 不存在也不報錯）

# ── bytes 索引回傳整數（2.20）────────────────────────
# 字串是以「字元」為單位；bytes 是以「位元組」為單位。
# 因此 str[0] 會得到字元，bytes[0] 會得到對應位元組的整數值。
a = "Hello"
b = b"Hello"
print(a[0])  # 'H'（字元）
print(b[0])  # 72（整數 = ord('H')）

# bytes 本身不是格式化字串；通常做法是先用 str.format() 完成排版，
# 再把結果 encode 成 bytes，交給需要二進位資料的 API。
print("{:10s} {:5d}".format("ACME", 100).encode("ascii"))
# b'ACME            100'
