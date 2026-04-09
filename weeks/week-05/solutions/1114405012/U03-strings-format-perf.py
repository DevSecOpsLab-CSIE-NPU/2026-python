# U03. 字串格式化效能與陷阱（2.14–2.20）
# join vs + / format_map 缺失鍵 / bytes 索引差異

import timeit

# ── join 效能優於 + （2.14）──────────────────────────
# 在迴圈中反覆用 + 串接字串時，每次都會建立新字串，成本會越來越高。
# 如果要把很多片段合成一個字串，通常用 "".join() 會更快也更省記憶體。
parts = [f"item{i}" for i in range(1000)]


def bad_concat():
    s = ""
    for p in parts:
        s += p  # 每次建立新字串，O(n²)
    return s


def good_join():
    return "".join(parts)  # 一次分配，O(n)


t1 = timeit.timeit(bad_concat, number=500)
t2 = timeit.timeit(good_join, number=500)
print(f"用 + 反覆串接：{t1:.3f}s")
print(f"用 join() 合併：{t2:.3f}s")
print(f"join() 大約快了 {t1 / t2:.2f} 倍")


# ── format_map 處理缺失鍵（2.15）─────────────────────
# format_map() 會直接從 mapping 取值；如果某個鍵不存在，預設會丟 KeyError。
# 透過 __missing__，我們可以讓缺失的鍵保留原本的 {name} 形式，而不是報錯。
class SafeSub(dict):
    def __missing__(self, key: str) -> str:
        return "{" + key + "}"  # 缺失時保留佔位符


name = "Guido"
s = "{name} has {n} messages."
print("安全格式化後：", s.format_map(SafeSub(vars())))  # 'Guido has {n} messages.'

# ── bytes 索引回傳整數（2.20）────────────────────────
# 字串是文字序列，索引後拿到的是字元；bytes 是位元組序列，索引後拿到的是整數。
# 這個差異很常在處理編碼、網路資料或二進位資料時踩雷。
a = "Hello"
b = b"Hello"
print("字串 a[0]：", a[0])  # 'H'
print("位元組 b[0]：", b[0])  # 72

# bytes 不能直接 format，需先格式化再 encode
print("格式化後再 encode：", "{:10s} {:5d}".format("ACME", 100).encode("ascii"))
# b'ACME            100'
