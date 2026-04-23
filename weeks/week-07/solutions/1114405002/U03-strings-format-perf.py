# U03. 字串格式化效能與陷阱（2.14–2.20）
# 本範例說明字串串接效能、format_map 處理缺失鍵，以及 bytes 的索引差異。

import timeit

# ── join 效能優於 + （2.14）──────────────────────────
parts = [f"item{i}" for i in range(1000)]


def bad_concat():
    s = ""
    for p in parts:
        # 每次 s += p 都會建立新的字串物件，導致記憶體重新配置
        # 並使執行時間成長為 O(n²)
        s += p  # 每次建立新字串，O(n²)
    return s


def good_join():
    return "".join(parts)  # 一次分配，O(n)


t1 = timeit.timeit(bad_concat, number=500)
t2 = timeit.timeit(good_join, number=500)
print(f"+串接: {t1:.3f}s  join: {t2:.3f}s")


# ── format_map 處理缺失鍵（2.15）─────────────────────
# 當 format_map 的鍵不存在時，dict 會呼叫 __missing__
# 我們在這裡保留原始佔位符，避免拋出 KeyError
class SafeSub(dict):
    def __missing__(self, key: str) -> str:
        return "{" + key + "}"  # 缺失時保留佔位符


name = "Guido"
s = "{name} has {n} messages."
print(s.format_map(SafeSub(vars())))  # 'Guido has {n} messages.'（n 不存在也不報錯）

# ── bytes 索引回傳整數（2.20）────────────────────────
# bytes 和 str 都是序列，但 bytes 的索引結果會是整數
# 這點和字元串非常不同，必須特別留意
a = "Hello"
b = b"Hello"
print(a[0])  # 'H'（字元）
print(b[0])  # 72（整數 = ord('H')）

# bytes 不能直接 format，需先格式化再 encode
print("{:10s} {:5d}".format("ACME", 100).encode("ascii"))
# b'ACME            100'
