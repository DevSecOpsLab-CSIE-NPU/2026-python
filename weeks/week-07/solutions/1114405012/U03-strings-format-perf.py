"""U03 字串格式化效能與陷阱（2.14–2.20）。"""

# 核心提醒：大量串接優先用 join；format_map 可處理缺鍵；bytes 索引回傳整數

import timeit

# ── join 效能優於 + （2.14）──────────────────────────
parts = [f"item{i}" for i in range(1000)]


def bad_concat():
    # 反覆 s += p 會產生大量中間字串，成本較高
    s = ""
    for p in parts:
        s += p  # 每次建立新字串，O(n²)
    return s


def good_join():
    return "".join(parts)  # 一次分配，O(n)


t1 = timeit.timeit(bad_concat, number=500)
t2 = timeit.timeit(good_join, number=500)
print(f"+串接: {t1:.3f}s  join: {t2:.3f}s")


# ── format_map 處理缺失鍵（2.15）─────────────────────
class SafeSub(dict):
    # 缺少變數時不丟例外，改回傳原佔位符
    def __missing__(self, key: str) -> str:
        return "{" + key + "}"  # 缺失時保留佔位符


name = "Guido"
s = "{name} has {n} messages."
print(s.format_map(SafeSub(vars())))  # 'Guido has {n} messages.'（n 不存在也不報錯）

# ── bytes 索引回傳整數（2.20）────────────────────────
a = "Hello"
b = b"Hello"
print(a[0])  # 'H'（字元）
print(b[0])  # 72（整數 = ord('H')）

# bytes 通常流程是：先做字串格式化，再 encode
print("{:10s} {:5d}".format("ACME", 100).encode("ascii"))
# b'ACME            100'
