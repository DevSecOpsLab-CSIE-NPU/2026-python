# 【Bloom 階段：U - 理解與進階應用】
# U03. 字串拼接性能與安全替換
# August 的惡意提醒：這是 Big-O 陷阱。
# 在迴圈中使用 s += part 是 O(N^2) 的自殺行為。
# 永遠使用 "".join() 這是 O(N) 的工業級標準。

import timeit

parts = [f"item{i}" for i in range(1000)]

def bad_concat():
    s = ""
    for p in parts: s += p # 每次都產生新物件，內存拷貝地獄
    return s

def good_join():
    return "".join(parts) # 預先計算總長度，一次分配

t1 = timeit.timeit(bad_concat, number=500)
t2 = timeit.timeit(good_join, number=500)
print(f"Concat vs Join: {t1:.3f}s vs {t2:.3f}s")

# 2. 安全字串替換 (The Safe Interpolation)
# 指紋點：你知道如何處理格式字串中「缺失」的鍵嗎？
class SafeSub(dict):
    def __missing__(self, key):
        return "{" + key + "}" # 找不到就保留原樣，不報錯

name = "Guido"
s = "{name} has {n} messages."
# 故意不提供 n，看看會發生什麼
print(s.format_map(SafeSub(vars())))
