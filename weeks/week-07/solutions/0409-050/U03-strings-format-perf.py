# U03. 字串格式化效能與陷阱（2.14–2.20）
# join vs + / format_map 缺失鍵 / bytes 索引差異

# 導入 timeit 模組，用於測量小段程式碼的執行時間，以比較不同實現的效能。
import timeit

# ── join 效能優於 + （2.14）──────────────────────────
# 說明：在 Python 中，使用 `str.join()` 方法來拼接字串通常比使用 `+` 運算符在迴圈中重複拼接字串更高效。
# 這是因為 `+` 運算符每次拼接都會創建一個新的字串對象，導致大量的內存分配和複製操作，時間複雜度為 O(n²)。
# 而 `join()` 方法會先計算出最終字串的總長度，然後一次性分配足夠的內存，再將所有部分複製進去，時間複雜度為 O(n)。

# 創建一個包含 1000 個字串的列表，用於測試拼接效能。
parts = [f"item{i}" for i in range(1000)]


def bad_concat():
    s = ""
    for p in parts:
        s += p  # 每次迴圈都會創建一個新的字串對象，導致效能較差 (O(n²))。
    return s


def good_join():
    return "".join(parts)  # `join()` 方法高效地一次性拼接所有字串 (O(n))。


# 使用 timeit 模組測量 `bad_concat` 函數執行 500 次所需的時間。
t1 = timeit.timeit(bad_concat, number=500)
# 使用 timeit 模組測量 `good_join` 函數執行 500 次所需的時間。
t2 = timeit.timeit(good_join, number=500)
# 輸出兩種方法的執行時間，通常 `join` 會快得多。
print(f"+串接: {t1:.3f}s  join: {t2:.3f}s")


# ── format_map 處理缺失鍵（2.15）─────────────────────
# 說明：`str.format_map()` 方法與 `str.format()` 類似，但它接受一個字典或字典子類型的對象作為參數。
# 當使用 `format_map()` 時，如果格式字串中引用的鍵在提供的字典中不存在，預設會拋出 `KeyError`。
# 透過繼承 `dict` 並重寫 `__missing__` 方法，可以自定義處理缺失鍵的行為，例如保留佔位符而不報錯。

# 定義一個繼承自 `dict` 的 `SafeSub` 類別。
class SafeSub(dict):
    # `__missing__` 方法會在嘗試訪問字典中不存在的鍵時被調用。
    def __missing__(self, key: str) -> str:
        # 當鍵缺失時，返回原始的佔位符字串，而不是拋出錯誤。
        return "{" + key + "}"  # 缺失時保留佔位符


# 定義一個變數 `name`。
name = "Guido"
# 定義一個格式字串，其中包含 `name` 和 `n` 兩個佔位符。
s = "{name} has {n} messages."
# `vars()` 函數返回當前作用域的字典。在這裡，它包含 `name` 變數，但不包含 `n`。
# `SafeSub(vars())` 創建一個 `SafeSub` 實例，並用 `vars()` 的內容初始化。
# 當 `format_map` 嘗試查找 `n` 時，`SafeSub` 的 `__missing__` 方法會被調用，將 `{n}` 保留下來。
print(s.format_map(SafeSub(vars())))  # 'Guido has {n} messages.'（n 不存在也不報錯）

# ── bytes 索引回傳整數（2.20）────────────────────────
# 說明：Python 中的字串 (`str`) 和位元組字串 (`bytes`) 在索引操作時有重要的區別。
# `str` 對象的索引會返回一個單一字元的字串。
# `bytes` 對象的索引會返回一個整數，代表該位元組的數值（0-255），即其 ASCII 值。

# 定義一個普通字串。
a = "Hello"
# 定義一個位元組字串。
b = b"Hello"
# 索引 `a[0]` 返回字元 'H'。
print(a[0])  # 'H'（字元）
# 索引 `b[0]` 返回整數 72，這是字元 'H' 的 ASCII 值。
print(b[0])  # 72（整數 = ord('H')）

# 說明：位元組字串 (`bytes`) 不能直接用於 `str.format()` 或 f-string 進行格式化。
# 格式化操作是針對字串 (`str`) 設計的。如果需要格式化位元組數據，
# 應該先使用普通字串進行格式化，然後再將結果編碼 (`encode()`) 為位元組。

# 這行代碼首先使用普通字串的 `format()` 方法創建一個格式化的字串。
# `"{:10s}"` 將 "ACME" 左對齊並填充到 10 個字元的寬度。
# `"{:5d}"` 將整數 100 右對齊並填充到 5 個字元的寬度。
# 然後，`.encode("ascii")` 將這個格式化後的字串編碼成 ASCII 位元組序列。
# bytes 不能直接 format，需先格式化再 encode
print("{:10s} {:5d}".format("ACME", 100).encode("ascii"))
# b'ACME            100'
