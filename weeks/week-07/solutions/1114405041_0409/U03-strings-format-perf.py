# U03. 字串格式化效能與陷阱（2.14–2.20）
# join vs + / format_map 缺失鍵 / bytes 索引差異
# 本檔重點：
# - 字串組裝方式會直接影響時間複雜度
# - format_map 可提升模板替換容錯性
# - bytes 與 str 行為差異不可混用
# 這類觀念常出現在資料處理、模板組字串、網路封包與編碼問題中。

import timeit

# ── join 效能優於 + （2.14）──────────────────────────
# 準備一批要被串起來的字串片段。
# 這裡刻意用 1000 個元素，好讓 += 與 join 的差異比較容易觀察。
parts = [f"item{i}" for i in range(1000)]


def bad_concat():
    # 這是很多初學者最直覺的寫法。
    # 問題是字串在 Python 是 immutable，不可原地修改。
    # 每次 s += p，本質上都可能建立新的字串物件，並複製舊內容。
    s = ""
    for p in parts:
        s += p  # 長度越長，重複複製的成本越大，容易形成 O(n^2)
    return s


def good_join():
    # join 的想法是：先知道所有片段有哪些，再一次建立結果字串。
    # 因此通常只需要一次主要分配，效能會明顯比較好。
    return "".join(parts)


# 用 timeit 做簡單比較。
# 實際秒數會依電腦不同而改變，但通常 join 都會比較快。
t1 = timeit.timeit(bad_concat, number=500)
t2 = timeit.timeit(good_join, number=500)
print(f"+串接: {t1:.3f}s  join: {t2:.3f}s")


# ── format_map 處理缺失鍵（2.15）─────────────────────
# dict 的 __missing__ 可以攔截「查不到鍵」時的行為。
# 這裡把它做成保留原始佔位符，而不是直接丟 KeyError。
class SafeSub(dict):
    def __missing__(self, key: str) -> str:
        # 若模板中出現不存在的鍵，例如 {n}，
        # 就回傳字面上的 {n}，表示保留它，不讓程式爆掉。
        return "{" + key + "}"


name = "Guido"
s = "{name} has {n} messages."

# vars() 會回傳目前區域變數表，例如這裡至少會有 name。
# 透過 SafeSub 包裝後，缺失鍵也能被安全處理。
print(s.format_map(SafeSub(vars())))  # 'Guido has {n} messages.'

# ── bytes 索引回傳整數（2.20）────────────────────────
# 這裡故意把內容相同的資料用 str 與 bytes 各存一次。
a = "Hello"
b = b"Hello"

# str 索引得到的是「單字元字串」。
print(a[0])  # 'H'

# bytes 索引得到的是「該位元組的整數值」。
# 72 就是 ASCII 中 H 的數值。
print(b[0])  # 72

# bytes 不能像一般字串那樣直接做 format。
# 正確流程通常是：
# 1. 先在 str 世界裡完成格式化
# 2. 再用 encode() 轉成 bytes
print("{:10s} {:5d}".format("ACME", 100).encode("ascii"))
# b'ACME            100'
