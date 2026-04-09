# U03. 字串格式化效能與陷阱（2.14–2.20）
# 本程式示範字串格式化的效能問題和常見陷阱：
# 2.14 join vs + 串接效能 - join() 比 + 運算子更高效
# 2.15 format_map 缺失鍵處理 - 優雅處理格式化時的缺失鍵
# 2.20 bytes 索引差異 - bytes 與 str 的索引行為差異

import timeit

# ── join 效能優於 + （2.14）──────────────────────────
# 問題：使用 + 運算子串接大量字串時效能很差（O(n²)）
# 原因：每次 + 都會建立新字串
# 解決方案：使用 "".join() 一次分配足夠記憶體（O(n)）

# 測試資料：1000 個字串
parts = [f"item{i}" for i in range(1000)]


# 低效方法：使用 + 串接
def bad_concat():
    s = ""
    for p in parts:
        s += p  # 每次建立新字串，O(n²)
    return s


# 高效方法：使用 join()
def good_join():
    return "".join(parts)  # 一次分配，O(n)


# 效能測試：執行 500 次
t1 = timeit.timeit(bad_concat, number=500)
t2 = timeit.timeit(good_join, number=500)
print(f"+串接: {t1:.3f}s  join: {t2:.3f}s")


# ── format_map 處理缺失鍵（2.15）─────────────────────
# 問題：str.format_map() 在鍵缺失時會引發 KeyError
# 解決方案：自訂字典類別處理缺失鍵

class SafeSub(dict):
    """
    安全的字典子類，當鍵不存在時返回格式化的鍵名稱
    用於 format_map() 時不會因為缺失鍵而崩潰
    """
    def __missing__(self, key: str) -> str:
        # 返回 {key} 格式，保留原始佔位符
        return "{" + key + "}"


# 測試：name 存在，n 不存在
name = "Guido"
s = "{name} has {n} messages."

# 使用 SafeSub 處理缺失鍵
print(s.format_map(SafeSub(vars())))  # 'Guido has {n} messages.'（n 不存在也不報錯）

# ── bytes 索引回傳整數（2.20）────────────────────────
# 問題：bytes 物件的索引行為與 str 不同
# str 索引返回字元，bytes 索引返回整數（ASCII 值）

a = "Hello"  # str
b = b"Hello"  # bytes

# str 索引返回字元
print(a[0])  # 'H'（字元）

# bytes 索引返回整數（對應 ASCII 值）
print(b[0])  # 72（整數 = ord('H')）

# 注意：bytes 不能直接使用 str.format()
# 需要先格式化字串再編碼為 bytes
print("{:10s} {:5d}".format("ACME", 100).encode("ascii"))
# b'ACME            100'
