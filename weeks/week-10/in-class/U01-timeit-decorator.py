# U01. 計時裝飾器實作與資料格式速度比較（6.1 / 6.2 / 6.3）
# 從「重複的計時程式碼」出發，引入裝飾器，再做格式實驗
#
# 這個範例分成兩個重點：
# 1. 示範如何用裝飾器把重複的計時程式碼抽離出來。
# 2. 比較 CSV、JSON、XML 在讀取同一批資料時的大致速度差異。

import csv
import json
import time
import io
import xml.etree.ElementTree as ET
import functools

# ═══════════════════════════════════════════════════════════
# Part 1｜問題：每個函式都要手動計時 → 大量重複
# ═══════════════════════════════════════════════════════════

def read_csv_raw(data: str) -> list:
    # csv.DictReader 會把每一列轉成 dict，方便用欄位名稱存取。
    # 這裡搭配 StringIO，讓字串可以像檔案一樣被 csv 模組讀取。
    return list(csv.DictReader(io.StringIO(data)))

def read_json_raw(data: str) -> list:
    # JSON 字串直接交給 json.loads，就會還原成 Python 物件。
    return json.loads(data)

def read_xml_raw(data: str) -> list:
    # 先把 XML 字串解析成樹狀結構，再抓出所有 <row> 節點的屬性。
    root = ET.fromstring(data)
    return [r.attrib for r in root.findall("row")]

# 沒有裝飾器：每次都要複製貼上計時程式碼 ↓
# 這段註解是在說明問題本身：如果每個函式都自己包一段計時邏輯，
# 程式會變得很冗長，而且每新增一個測試函式都要重寫同樣的步驟。
# start = time.perf_counter()
# result = read_csv_raw(data)
# print(f"read_csv_raw 耗時 {time.perf_counter() - start:.6f}s")
#
# start = time.perf_counter()
# result = read_json_raw(data)
# print(f"read_json_raw 耗時 {time.perf_counter() - start:.6f}s")
# ... 每加一個函式就多寫三行，且容易忘記移除

# ═══════════════════════════════════════════════════════════
# Part 2｜解法：裝飾器把計時邏輯包起來，一次定義，到處復用
# ═══════════════════════════════════════════════════════════

def timeit(func):
    """基礎版：在呼叫前後計時，印出耗時"""
    # 這個外層函式接收一個原始函式 func，並回傳一個新的 wrapper。
    # wrapper 會先記錄開始時間，呼叫原函式，再計算總耗時並印出來。
    def wrapper(*args, **kwargs):
        # perf_counter() 提供高解析度的時間點，適合拿來量測短時間操作。
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        # func.__name__ 用來顯示正在被計時的原始函式名稱。
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")
        return result
    # 回傳 wrapper，這樣 @timeit 套上去後，原函式就會被包住。
    return wrapper

# 問題：wrapper 蓋掉了原函式的 __name__ / __doc__
# 裝飾器會回傳新的函式物件，因此原本的函式名稱、說明文字等 metadata
# 如果不額外處理，就會變成 wrapper 的資訊。
def demo():
    """這是 demo 的說明文字"""
    pass

wrapped = timeit(demo)
# 這裡故意示範未使用 wraps 時的結果：wrapped.__name__ 會變成 wrapper。
print("未加 wraps 前：", wrapped.__name__)   # wrapper（錯誤！）

# ── Part 3｜functools.wraps：保留原函式的 metadata ──────────

def timeit(func):
    # wraps 會把原函式的名稱、文件字串、模組名稱等資訊複製到 wrapper 上。
    # 這對除錯、help()、紀錄與測試都很重要。
    @functools.wraps(func)          # 保留 __name__ / __doc__ / __module__
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")
        return result
    return wrapper

wrapped = timeit(demo)
# 使用 wraps 之後，wrapped.__name__ 會回到 demo，而不是 wrapper。
print("加 wraps 後：  ", wrapped.__name__)   # demo（正確）
print()

# ═══════════════════════════════════════════════════════════
# Part 4｜實驗：相同資料，CSV vs JSON vs XML 速度比較
# ═══════════════════════════════════════════════════════════

# ── 產生測試資料（1000 筆學生記錄）────────────────────────
# 為了公平比較不同格式的解析速度，這裡先建立相同內容的三種資料格式。
# N 設成 1000，代表每種格式都會有 1000 筆紀錄。
N = 1000

# CSV 格式
# 使用 StringIO 當作記憶體中的檔案，讓 DictWriter 把資料寫成 CSV 字串。
csv_buf = io.StringIO()
writer = csv.DictWriter(csv_buf, fieldnames=["id", "name", "score"])
# 先寫標頭列，這樣 CSV 才知道每一欄的名稱。
writer.writeheader()
# 每一列都寫入 id、name、score 三個欄位。
for i in range(N):
    writer.writerow({"id": i, "name": f"Student{i:04d}", "score": 60 + i % 40})
# getvalue() 會把記憶體中的整份 CSV 文字抓出來。
CSV_DATA = csv_buf.getvalue()

# JSON 格式
# JSON 直接把一個 list of dict 轉成字串即可。
JSON_DATA = json.dumps([
    {"id": i, "name": f"Student{i:04d}", "score": 60 + i % 40}
    for i in range(N)
])

# XML 格式
# XML 需要自己拼出每個 <row /> 節點的字串，再包成一個 <data> 根節點。
# 這裡使用屬性而不是子標籤，讓範例更簡潔，也方便和其他格式對照。
xml_rows = "".join(
    f'<row id="{i}" name="Student{i:04d}" score="{60 + i % 40}"/>'
    for i in range(N)
)
XML_DATA = f"<data>{xml_rows}</data>"

# ── 帶回傳耗時的計時包裝 ─────────────────────────────────

def timeit_silent(func):
    # 這個版本和前面的 timeit 類似，但不負責印出訊息，
    # 而是把「結果」與「耗時」一起回傳，方便外層做統計計算。
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        # 回傳一個二元組：第一個元素是函式結果，第二個元素是執行秒數。
        return result, time.perf_counter() - start
    return wrapper

# 把三個讀取函式包成可量測版本，之後迴圈只要呼叫包裝後的版本即可。
_csv  = timeit_silent(read_csv_raw)
_json = timeit_silent(read_json_raw)
_xml  = timeit_silent(read_xml_raw)

# ── 執行比較（重複 5 次取平均，排除冷啟動影響）────────────

# 多跑幾次再取平均，可以減少偶發抖動對結果的影響。
# RUNS 越大通常越穩定，但也會讓測試時間變長。
RUNS = 5
# times 用來累加每一種格式的總耗時，最後再除以 RUNS 取得平均。
times = {"CSV": 0.0, "JSON": 0.0, "XML": 0.0}

for _ in range(RUNS):
    # 依序測試 CSV、JSON、XML，並把每次耗時累加起來。
    _, t = _csv(CSV_DATA);   times["CSV"]  += t
    _, t = _json(JSON_DATA); times["JSON"] += t
    _, t = _xml(XML_DATA);   times["XML"]  += t

# 印出總體比較表。
print(f"=== 讀取 {N} 筆資料，重複 {RUNS} 次平均 ===\n")
print(f"{'格式':<6} {'平均耗時':>12}  {'相對 JSON':>10}")
# 先把 JSON 的平均耗時當作基準，後面其他格式都和它做相對比較。
base = times["JSON"] / RUNS
for fmt, total in times.items():
    avg = total / RUNS
    # avg/base 會顯示某格式相對於 JSON 慢了幾倍或快了幾倍。
    print(f"  {fmt:<6} {avg:.6f}s   {avg/base:>8.2f}x")

# ═══════════════════════════════════════════════════════════
# 觀察重點
# ═══════════════════════════════════════════════════════════
# 1. JSON 通常最快：Python 的 JSON 解析器在很多情況下都有不錯的效能，
#    而且資料結構和 Python 原生型別對應很直接。
# 2. XML 通常最慢：因為標籤結構較複雜，解析成本也較高，還要處理屬性與節點。
# 3. CSV 介於中間：格式簡單，但每一欄通常都是字串，後續若要做數值運算還要轉型。
#
# 裝飾器帶來的好處：
# - 計時邏輯只寫一次，不汙染原函式本身。
# - 要移除計時只需拿掉 @timeit，函式本體不需要修改。
# - functools.wraps 確保 debug / help() 時能看到正確名稱與說明文字。
