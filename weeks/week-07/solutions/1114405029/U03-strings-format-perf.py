# U03. 字串格式化效能與陷阱（2.14–2.20）
# join vs + / format_map 缺失鍵 / bytes 索引差異

import timeit

# ── join 效能優於 + （2.14）──────────────────────────
# 字串是不可變物件，使用 += 會導致不斷建立新物件並進行記憶體拷貝，效能為 O(n²)
parts = [f"item{i}" for i in range(1000)]

def bad_concat():
    s = ""
    for p in parts:
        s += p  
    return s

def good_join():
    # .join() 會先計算總長度並一次性分配記憶體，效能為 O(n)
    return "".join(parts)  

t1 = timeit.timeit(bad_concat, number=500)
t2 = timeit.timeit(good_join, number=500)
print(f"+串接: {t1:.3f}s  join: {t2:.3f}s")

# ── format_map 處理缺失鍵（2.15）─────────────────────
# 透過自定義字典類別的 __missing__ 方法，當 key 不存在時不會報錯，而是返回佔位符
class SafeSub(dict):
    def __missing__(self, key: str) -> str:
        return "{" + key + "}"  # 讓缺失的 key 保留在結果字串中

name = "Guido"
s = "{name} has {n} messages."
# vars() 返回當前範圍的變數字典
print(s.format_map(SafeSub(vars())))  # 'Guido has {n} messages.'

# ── bytes 索引回傳整數（2.20）────────────────────────
# bytes 物件的索引運作方式與一般的字串（str）不同
a = "Hello"
b = b"Hello"
print(a[0])  # 'H'（str 的索引回傳長度為 1 的字串）
print(b[0])  # 72（bytes 的索引回傳該字元的 ASCII/整數值）

# bytes 不支援直接使用 .format()，必須先在 str 格式化後再編碼成 bytes
print("{:10s} {:5d}".format("ACME", 100).encode("ascii"))
# b'ACME            100'