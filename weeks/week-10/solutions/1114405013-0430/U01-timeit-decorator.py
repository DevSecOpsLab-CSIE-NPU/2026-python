# U01. 計時裝飾器實作與資料格式速度比較（6.1 / 6.2 / 6.3）
# 從「重複的計時程式碼」出發，引入裝飾器，再做格式實驗

import csv
import json
import time
import io
import xml.etree.ElementTree as ET
import functools

# 這個檔案示範兩個重點：
# 1. 用裝飾器把重複的「計時邏輯」抽出來，讓每個函式只專注於自己的核心工作。
# 2. 比較三種資料格式（CSV、JSON、XML）在讀取時的解析效能差異。

# ═══════════════════════════════════════════════════════════
# Part 1｜問題：每個函式都要手動計時 → 大量重複
# ═══════════════════════════════════════════════════════════

def read_csv_raw(data: str) -> list:
    # csv.DictReader 會把 CSV 第一列當成欄位名稱，剩餘列轉成 dict
    # io.StringIO 讓字串變成 file-like 物件，方便 csv 模組讀取
    return list(csv.DictReader(io.StringIO(data)))

def read_json_raw(data: str) -> list:
    # json.loads 直接把 JSON 字串解析成 Python 資料結構
    return json.loads(data)

def read_xml_raw(data: str) -> list:
    # 解析 XML 字串成 ElementTree，然後找出所有 row 元素
    root = ET.fromstring(data)
    # 每個 row 的屬性在 .attrib，這裡把它們收成 dict 列表
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
    """基礎版裝飾器：在呼叫前後計時，並印出執行時間。"""
    def wrapper(*args, **kwargs):
        # 1. 記錄起始時間
        start = time.perf_counter()
        # 2. 執行原函式
        result = func(*args, **kwargs)
        # 3. 計算耗時並印出
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")
        return result
    return wrapper

# 這裡示範原始裝飾器的問題：wrapper 會覆蓋原函式的 metadata
# 包括 __name__、__doc__、__module__ 等屬性。
def demo():
    """這是 demo 的說明文字"""
    pass

wrapped = timeit(demo)
print("未加 wraps 前：", wrapped.__name__)   # wrapper（錯誤！）

# ── Part 3｜functools.wraps：保留原函式的 metadata ──────────

def timeit(func):
    # functools.wraps 會把原函式的 metadata 複製到 wrapper 上，
    # 使得裝飾後的函式仍保留正確的名稱、說明與模組資訊。
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")
        return result
    return wrapper

wrapped = timeit(demo)
print("加 wraps 後：  ", wrapped.__name__)   # demo（正確）
print()

# ═══════════════════════════════════════════════════════════
# Part 4｜實驗：相同資料，CSV vs JSON vs XML 速度比較
# ═══════════════════════════════════════════════════════════

# ── 產生測試資料（1000 筆學生記錄）────────────────────────
# 這裡用三種格式產生相同資料內容，後面比較它們的解析速度。
N = 1000

# CSV 格式：表格型資料，欄位名稱在第一列
csv_buf = io.StringIO()
writer = csv.DictWriter(csv_buf, fieldnames=["id", "name", "score"])
writer.writeheader()
for i in range(N):
    writer.writerow({"id": i, "name": f"Student{i:04d}", "score": 60 + i % 40})
CSV_DATA = csv_buf.getvalue()

# JSON 格式：物件列表，內建解析器通常效率很高
JSON_DATA = json.dumps([
    {"id": i, "name": f"Student{i:04d}", "score": 60 + i % 40}
    for i in range(N)
])

# XML 格式：巢狀標籤形式，需要解析器把字串轉成元素
xml_rows = "".join(
    f'<row id="{i}" name="Student{i:04d}" score="{60 + i % 40}"/>'
    for i in range(N)
)
XML_DATA = f"<data>{xml_rows}</data>"

# ── 帶回傳耗時的計時包裝 ─────────────────────────────────
# 這個裝飾器會回傳原始結果以及耗時，方便後續做平均比較。

def timeit_silent(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        return result, time.perf_counter() - start
    return wrapper

# 把原始讀取函式包成可回傳耗時的版本
_csv  = timeit_silent(read_csv_raw)
_json = timeit_silent(read_json_raw)
_xml  = timeit_silent(read_xml_raw)

# ── 執行比較（重複 5 次取平均，排除冷啟動影響）────────────
# 透過多輪次跑同一段資料，可減少單次波動造成的誤差。
RUNS = 5
times = {"CSV": 0.0, "JSON": 0.0, "XML": 0.0}

for _ in range(RUNS):
    _, t = _csv(CSV_DATA);   times["CSV"]  += t
    _, t = _json(JSON_DATA); times["JSON"] += t
    _, t = _xml(XML_DATA);   times["XML"]  += t

print(f"=== 讀取 {N} 筆資料，重複 {RUNS} 次平均 ===\n")
print(f"{'格式':<6} {'平均耗時':>12}  {'相對 JSON':>10}")
base = times["JSON"] / RUNS
for fmt, total in times.items():
    avg = total / RUNS
    print(f"  {fmt:<6} {avg:.6f}s   {avg/base:>8.2f}x")

# ═══════════════════════════════════════════════════════════
# 觀察重點
# ═══════════════════════════════════════════════════════════
# 1. JSON 通常最快（原生 C 實作的解析器）
# 2. XML  通常最慢（文字解析開銷大，屬性字串轉換）
# 3. CSV  介於中間（簡單格式，但每欄都是字串需自行轉型）
#
# 裝飾器帶來的好處：
# - 計時邏輯只寫一次，不汙染原函式
# - 要移除計時只需拿掉 @timeit，函式本身不需修改
# - functools.wraps 確保 debug / help() 時能看到正確名稱
