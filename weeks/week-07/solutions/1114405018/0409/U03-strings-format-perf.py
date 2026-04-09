# U03. 字串格式化效能與陷阱（2.14–2.20）
# 這份範例主要示範三個常見主題：
# 1. 大量字串串接時，join() 通常比用 + 反覆相加更有效率。
# 2. format_map() 可以搭配自訂字典，在欄位缺失時避免直接報錯。
# 3. bytes 和 str 的索引結果不同，這是處理文字與位元組資料時很容易混淆的地方。

import timeit

# ── join 效能優於 + （2.14）──────────────────────────
# 字串在 Python 中是不可變物件，所以每次用 + 串接，都會建立新的字串物件。
# 如果在迴圈中重複做這件事，成本會快速累積，形成類似 O(n²) 的行為。
parts = [f"item{i}" for i in range(1000)]


def bad_concat():
    # 這種寫法每次都把舊字串與新片段重新合成新字串，適合小量資料，不適合大量累積。
    s = ""
    for p in parts:
        s += p  # 每次建立新字串，因為重複複製內容，所以效率較差
    return s


def good_join():
    # join() 會先知道所有片段，再一次完成配置與串接，所以通常更快也更省資源。
    return "".join(parts)  # 一次分配，O(n)


# 這裡用 timeit 做簡單基準測試，讓兩種寫法的差異比較明顯。
# number 設大一點，是為了降低單次測試的雜訊。
t1 = timeit.timeit(bad_concat, number=500)
t2 = timeit.timeit(good_join, number=500)
# 實際結果會受硬體、Python 版本與執行環境影響，但 join() 幾乎都會比較快。
print(f"+串接: {t1:.3f}s  join: {t2:.3f}s")


# ── format_map 處理缺失鍵（2.15）─────────────────────
# format_map() 會從傳入的 mapping 物件取值。
# 如果欄位名稱找不到，預設會拋出 KeyError；因此可以自訂字典的 __missing__ 來控制行為。
class SafeSub(dict):
    def __missing__(self, key: str) -> str:
        # 當欄位缺失時，不直接報錯，而是保留原本的大括號標記，方便後續補值或除錯。
        return "{" + key + "}"


name = "Guido"
s = "{name} has {n} messages."
# vars() 會把目前區域變數轉成字典，提供給 format_map() 當作查找來源。
# 因為 n 不存在，所以會觸發 __missing__，並保留成 {n} 而不是直接失敗。
print(s.format_map(SafeSub(vars())))  # 'Guido has {n} messages.'（n 不存在也不報錯）

# ── bytes 索引回傳整數（2.20）────────────────────────
# str 和 bytes 雖然都可以用索引取值，但回傳型別不同：
# str[0] 取到的是單一字元字串；bytes[0] 取到的是對應的整數位元組值。
a = "Hello"
b = b"Hello"
print(a[0])  # 'H'（字元）
print(b[0])  # 72（整數 = ord('H')）

# bytes 不能直接 format，需先格式化再 encode
# 如果最後要輸出成 bytes，常見流程是先用字串格式化完成排版，再 encode 成 ASCII 或 UTF-8。
print("{:10s} {:5d}".format("ACME", 100).encode("ascii"))
# b'ACME            100'
