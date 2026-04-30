# U01. 計時裝飾器實作與資料格式速度比較（6.1 / 6.2 / 6.3）
# 從「重複的計時程式碼」出發，引入裝飾器，再做格式實驗

import csv
import json
import time
import io
import xml.etree.ElementTree as ET
import functools

# ═══════════════════════════════════════════════════════════
# Part 1｜問題：每個函式都要手動計時，程式碼會大量重複
# ═══════════════════════════════════════════════════════════

def read_csv_raw(data: str) -> list:
    # 直接把 CSV 文字轉成 DictReader，回傳每列資料。
    return list(csv.DictReader(io.StringIO(data)))

def read_json_raw(data: str) -> list:
    # JSON 可以直接用標準函式解碼成 Python 物件。
    return json.loads(data)

def read_xml_raw(data: str) -> list:
    # XML 先解析成樹狀結構，再把每個 row 的屬性取出來。
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
# Part 2｜解法：用裝飾器把計時邏輯包起來，一次定義，到處復用
# ═══════════════════════════════════════════════════════════

def timeit(func):
    """基礎版計時裝飾器：在函式呼叫前後量測並印出耗時。"""
    def wrapper(*args, **kwargs):
        # 記錄開始時間，呼叫原函式後再計算經過時間。
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")
        return result
    return wrapper

# 問題：wrapper 會蓋掉原函式的 __name__ / __doc__ 等資訊。
def demo():
    """這是 demo 的說明文字"""
    pass

wrapped = timeit(demo)
print("未加 wraps 前：", wrapped.__name__)   # 這裡會顯示 wrapper

# ── Part 3｜functools.wraps：保留原函式的 metadata ──────────

def timeit(func):
    # wraps 會把原函式的名稱、說明與模組資訊保留下來。
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 重新量測一次，這裡同樣保留原本的輸出格式。
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")
        return result
    return wrapper

wrapped = timeit(demo)
print("加 wraps 後：  ", wrapped.__name__)   # 這裡會正確顯示 demo
print()

# ═══════════════════════════════════════════════════════════
# Part 4｜實驗：用相同資料比較 CSV、JSON、XML 的讀取速度
# ═══════════════════════════════════════════════════════════

# ── 產生測試資料（1000 筆學生記錄）────────────────────────
N = 1000

# CSV 格式：先用 DictWriter 寫到記憶體中的字串緩衝區。
csv_buf = io.StringIO()
writer = csv.DictWriter(csv_buf, fieldnames=["id", "name", "score"])
writer.writeheader()
for i in range(N):
    writer.writerow({"id": i, "name": f"Student{i:04d}", "score": 60 + i % 40})
CSV_DATA = csv_buf.getvalue()

# JSON 格式：直接把 Python list 轉成 JSON 字串。
JSON_DATA = json.dumps([
    {"id": i, "name": f"Student{i:04d}", "score": 60 + i % 40}
    for i in range(N)
])

# XML 格式：手動組出一串 row 節點，再包成根節點。
xml_rows = "".join(
    f'<row id="{i}" name="Student{i:04d}" score="{60 + i % 40}"/>'
    for i in range(N)
)
XML_DATA = f"<data>{xml_rows}</data>"

# ── 帶回傳耗時的計時包裝 ─────────────────────────────────

def timeit_silent(func):
    # 這個版本不印出結果，只回傳 (原結果, 耗時)，方便做平均比較。
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        return result, time.perf_counter() - start
    return wrapper

_csv  = timeit_silent(read_csv_raw)
_json = timeit_silent(read_json_raw)
_xml  = timeit_silent(read_xml_raw)

# ── 執行比較（重複 5 次取平均，排除冷啟動影響）────────────

RUNS = 5
times = {"CSV": 0.0, "JSON": 0.0, "XML": 0.0}

for _ in range(RUNS):
    # 每輪都跑一次三種格式，累積耗時後再取平均。
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
# 1. JSON 通常最快，因為解析器是高效率的原生實作。
# 2. XML 通常最慢，因為文字結構較冗長，解析開銷也比較大。
# 3. CSV  通常介於中間，格式簡單，但欄位轉型常要額外處理。
#
# 裝飾器帶來的好處：
# - 計時邏輯只需要寫一次，不會污染原本函式內容。
# - 如果不想計時，只要移除 @timeit，不必改函式本體。
# - functools.wraps 可以保留正確的函式名稱與說明文字，方便除錯與 help() 顯示。
