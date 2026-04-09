import timeit

# ── 1. 字串串接效能：join 遠優於 + (Python 效能優化建議 2.14) ──
# 準備 1000 個字串元素作為測試資料
parts = [f"item{i}" for i in range(1000)]

def bad_concat():
    """
    不建議的寫法：使用迴圈與 + 號串接。
    原因：字串在 Python 中是「不可變」(Immutable) 的。
    每次執行 s += p，Python 都必須重新分配記憶體空間，
    並將舊字串與新內容複製進去。當資料量大時，複雜度會飆升至 O(n²)。
    """
    s = ""
    for p in parts:
        s += p  
    return s

def good_join():
    """
    建議的寫法：使用 join() 方法。
    原因：join() 會先計算所有字串的總長度，一次性分配足夠的記憶體空間，
    然後進行複製。這使得操作的時間複雜度維持在線性的 O(n)。
    """
    return "".join(parts)

# 測試兩種方式執行 500 次的耗時差異
t1 = timeit.timeit(bad_concat, number=500)
t2 = timeit.timeit(good_join, number=500)
print(f"「+」號串接耗時: {t1:.3f}s | 「join」串接耗時: {t2:.3f}s")


# ── 2. 處理 format_map 的缺失鍵 (靈活的模板填充 2.15) ──
class SafeSub(dict):
    """
    自定義字典類別，繼承自 dict。
    透過覆寫 __missing__ 方法，定義當字典找不到某個 Key 時該如何反應。
    """
    def __missing__(self, key: str) -> str:
        # 當 Key 不存在時，不拋出 KeyError，而是回傳原始的佔位符名稱
        return "{" + key + "}"

name = "Guido"
s = "{name} has {n} messages."

# 使用 format_map 配合 SafeSub 進行格式化
# vars() 會抓取當前範圍的變數（包含 name），但裡面沒有 n
# 結果：'Guido' 被填充了，而 '{n}' 因為找不到對應值而被保留下來
print(s.format_map(SafeSub(vars())))  


# ── 3. bytes 與 str 的索引行為差異 (底層資料處理 2.20) ──
a = "Hello"    # 一般字串 (Unicode)
b = b"Hello"   # 字節字串 (Bytes)

# str 索引：回傳的是長度為 1 的「字串」
print(f"字串索引 a[0]: {a[0]} (型別: {type(a[0])})")  

# bytes 索引：回傳的是該位置字節的「整數數值」(0-255)
# 72 即為大寫字母 'H' 的 ASCII 碼
print(f"字節索引 b[0]: {b[0]} (型別: {type(b[0])})")


# ── 4. bytes 的格式化陷阱 ──
# 注意：bytes 物件並不直接支援 .format() 方法。
# 正確做法：先對 str 進行格式化，完成後再使用 .encode() 轉換為 bytes。
formatted_bytes = "{:10s} {:5d}".format("ACME", 100).encode("ascii")
print(f"格式化後的 bytes: {formatted_bytes}")
# 輸出結果為：b'ACME            100'