# U01. 計時裝飾器實作與資料格式速度比較（6.1 / 6.2 / 6.3）
# 這份範例先示範：如果每個函式都自己寫計時碼，會出現大量重複。
# 接著改用裝飾器把計時邏輯集中管理，最後再比較 CSV / JSON / XML 的解析速度。

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
    # csv.DictReader 會把第一列欄位名稱當成 key，將每列資料轉成字典。
    return list(csv.DictReader(io.StringIO(data)))

def read_json_raw(data: str) -> list:
    # JSON 直接交給標準函式庫解析即可，回傳 Python list / dict 結構。
    return json.loads(data)

def read_xml_raw(data: str) -> list:
    # XML 先轉成 ElementTree，再把 <row> 節點的屬性取出來。
    root = ET.fromstring(data)
    return [r.attrib for r in root.findall("row")]

# 沒有裝飾器：每次都要複製貼上計時程式碼 ↓
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
    """基礎版計時裝飾器。

    這個版本的工作方式是：
    1. 接收一個函式 func
    2. 回傳一個 wrapper
    3. wrapper 在真正呼叫 func 前後記錄時間
    4. 把執行時間印出來

    注意：這裡只示範裝飾器的核心概念，還沒有保留原函式的 metadata。
    """
    def wrapper(*args, **kwargs):
        # perf_counter 是適合做短時間量測的高精度計時器。
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        # func.__name__ 讓輸出顯示目前被包裝的是哪個函式。
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")
        return result
    return wrapper

# 問題：wrapper 蓋掉了原函式的 __name__ / __doc__
def demo():
    """這是 demo 的說明文字。

    這個函式本身沒有做任何事情，主要是拿來示範：
    如果直接用 wrapper 取代原函式，help()、除錯訊息、函式名稱都會被蓋掉。
    """
    pass

# timeit(demo) 會回傳一個新的 wrapper 函式，並用 wrapper 取代原本呼叫方式。
wrapped = timeit(demo)
# 這裡印出的名稱會是 wrapper，因為我們還沒用 functools.wraps 保留原始資訊。
print("未加 wraps 前：", wrapped.__name__)   # wrapper（錯誤！）

# ── Part 3｜functools.wraps：保留原函式的 metadata ──────────

def timeit(func):
    # wraps 會把 func 的 __name__、__doc__、__module__ 等資訊複製到 wrapper 上。
    @functools.wraps(func)          # 保留 __name__ / __doc__ / __module__
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")
        return result
    return wrapper

# 重新把 demo 丟進新版 timeit，這次 wrapper 的外觀就會維持成 demo。
wrapped = timeit(demo)
# 這裡會印出 demo，證明 wraps 已經成功保留原函式名稱。
print("加 wraps 後：  ", wrapped.__name__)   # demo（正確）
print()

# ═══════════════════════════════════════════════════════════
# Part 4｜實驗：相同資料，CSV vs JSON vs XML 速度比較
# ═══════════════════════════════════════════════════════════

# ── 產生測試資料（1000 筆學生記錄）────────────────────────
# 這裡不用讀外部檔案，而是直接在記憶體中組出三種格式的測試資料。
N = 1000

# CSV 格式
# StringIO 讓我們可以把字串當成檔案使用，配合 DictWriter 直接輸出 CSV 文字。
csv_buf = io.StringIO()
writer = csv.DictWriter(csv_buf, fieldnames=["id", "name", "score"])
writer.writeheader()
for i in range(N):
    # 每筆資料都有固定欄位，score 則用餘數讓它在 60~99 間循環。
    writer.writerow({"id": i, "name": f"Student{i:04d}", "score": 60 + i % 40})
CSV_DATA = csv_buf.getvalue()

# JSON 格式
# json.dumps 會把 Python 的 list / dict 結構轉成 JSON 字串。
JSON_DATA = json.dumps([
    {"id": i, "name": f"Student{i:04d}", "score": 60 + i % 40}
    for i in range(N)
])

# XML 格式
# 這裡用字串拼接方式組出簡單 XML，每一列都做成 <row ... /> 的自閉合標籤。
xml_rows = "".join(
    f'<row id="{i}" name="Student{i:04d}" score="{60 + i % 40}"/>'
    for i in range(N)
)
XML_DATA = f"<data>{xml_rows}</data>"

# ── 帶回傳耗時的計時包裝 ─────────────────────────────────

def timeit_silent(func):
    # 這個版本不印出耗時，而是把「結果 + 耗時」一起回傳，方便後面做統計。
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        return result, time.perf_counter() - start
    return wrapper

# 把三個讀取函式各自包上一層 silent timer，之後就能在迴圈中重複量測。
_csv  = timeit_silent(read_csv_raw)
_json = timeit_silent(read_json_raw)
_xml  = timeit_silent(read_xml_raw)

# ── 執行比較（重複 5 次取平均，排除冷啟動影響）────────────

# 重複測幾次可以降低單次執行的雜訊，例如第一次載入模組、快取建立等成本。
RUNS = 5
times = {"CSV": 0.0, "JSON": 0.0, "XML": 0.0}

# 每一輪都各跑一次 CSV / JSON / XML，最後累積總時間。
for _ in range(RUNS):
    _, t = _csv(CSV_DATA);   times["CSV"]  += t
    _, t = _json(JSON_DATA); times["JSON"] += t
    _, t = _xml(XML_DATA);   times["XML"]  += t

# 輸出格式化表格，讓結果一眼就能比較。
print(f"=== 讀取 {N} 筆資料，重複 {RUNS} 次平均 ===\n")
print(f"{'格式':<6} {'平均耗時':>12}  {'相對 JSON':>10}")
# 先拿 JSON 當基準，觀察其他格式相對於 JSON 慢或快多少。
base = times["JSON"] / RUNS
for fmt, total in times.items():
    avg = total / RUNS
    print(f"  {fmt:<6} {avg:.6f}s   {avg/base:>8.2f}x")

# ═══════════════════════════════════════════════════════════
# 觀察重點
# ═══════════════════════════════════════════════════════════
# 1. JSON 通常最快，因為標準函式庫的解析器多半有較佳的底層實作。
# 2. XML 通常最慢，因為標籤與屬性解析的成本較高，結構也比較冗長。
# 3. CSV 通常介於中間，格式簡單，但每欄位還需要自行後處理與轉型。
#
# 裝飾器帶來的好處：
# - 計時邏輯只寫一次，不會在每個函式裡重複貼相同程式碼。
# - 想暫時關掉計時，只要移除 @timeit，原函式不用跟著改。
# - functools.wraps 可以保留 debug / help() 會用到的原始函式名稱與說明文字。
