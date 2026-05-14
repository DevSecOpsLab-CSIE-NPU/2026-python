# U01. 計時裝飾器實作與資料格式速度比較（6.1 / 6.2 / 6.3）
# 學習目標 (Bloom: Understand)：從「重複的計時程式碼」痛點出發，理解為什麼需要裝飾器 (Decorator)，
# 接著利用裝飾器來實作不同資料格式 (CSV, JSON, XML) 的解析速度實驗。

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
    # 必須先用 io.StringIO 把字串包裝成「類似檔案」的物件，才能交給 csv.DictReader 解析
    return list(csv.DictReader(io.StringIO(data)))

def read_json_raw(data: str) -> list:
    # JSON 是內建支援最好的格式，直接用 json.loads 反序列化為 Python 字典或列表
    return json.loads(data)

def read_xml_raw(data: str) -> list:
    # 將 XML 字串解析為 ElementTree 的根節點
    root = ET.fromstring(data)
    # 尋找所有 <row> 標籤，並將其屬性 (attrib) 轉為字典放進列表中
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
    """基礎版裝飾器：在呼叫目標函式前後進行計時，並印出耗時"""
    # *args 和 **kwargs 可以接收任何數量的位置參數與關鍵字參數，確保能包裝任何函式
    def wrapper(*args, **kwargs):
        start = time.perf_counter()            # 記錄開始時間 (高精度時鐘)
        result = func(*args, **kwargs)         # 實際執行被包裝的原函式
        elapsed = time.perf_counter() - start  # 計算經過的時間
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")
        return result                          # 將原函式的結果回傳
    return wrapper

# 問題：wrapper 雖然成功計時，但它會把原函式的 metadata（如函式名稱、說明文件）蓋掉。
# 當我們呼叫 help(demo) 或檢查 demo.__name__ 時，會看到 wrapper 而不是 demo。
def demo():
    """這是 demo 的說明文字"""
    pass

# 手動使用裝飾器的方式（等同於在 def demo() 上面加上 @timeit）
wrapped = timeit(demo)
print("未加 wraps 前：", wrapped.__name__)   # wrapper（錯誤！）

# ── Part 3｜functools.wraps：保留原函式的 metadata ──────────

def timeit(func):
    # 解決方案：使用 @functools.wraps
    # 它可以把原函式 (func) 的 metadata (名稱、說明文件等) 安全地複製到 wrapper 上
    @functools.wraps(func)          # 保留 __name__ / __doc__ / __module__
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
N = 1000

# 1. 產生 CSV 格式的測試字串 (利用 StringIO 寫入記憶體)
csv_buf = io.StringIO()
writer = csv.DictWriter(csv_buf, fieldnames=["id", "name", "score"])
writer.writeheader()
for i in range(N):
    writer.writerow({"id": i, "name": f"Student{i:04d}", "score": 60 + i % 40})
CSV_DATA = csv_buf.getvalue()

# 2. 產生 JSON 格式的測試字串 (使用 list comprehension 一次產生字典列表再 dumps)
JSON_DATA = json.dumps([
    {"id": i, "name": f"Student{i:04d}", "score": 60 + i % 40}
    for i in range(N)
])

# 3. 產生 XML 格式的測試字串 (先組裝所有 <row> 標籤，再包上 <data> 根標籤)
xml_rows = "".join(
    f'<row id="{i}" name="Student{i:04d}" score="{60 + i % 40}"/>'
    for i in range(N)
)
XML_DATA = f"<data>{xml_rows}</data>"

# ── 帶回傳耗時的計時包裝 ─────────────────────────────────

def timeit_silent(func):
    """進階版裝飾器：不印出訊息，改為將「執行結果」和「耗時」打包成 Tuple 雙雙回傳，方便做後續統計"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        return result, time.perf_counter() - start
    return wrapper

# 使用 timeit_silent 包裝我們先前定義好的三個解析函式
_csv  = timeit_silent(read_csv_raw)
_json = timeit_silent(read_json_raw)
_xml  = timeit_silent(read_xml_raw)

# ── 執行比較（重複 5 次取平均，排除電腦當下負載不穩定的影響）────────────

RUNS = 5
times = {"CSV": 0.0, "JSON": 0.0, "XML": 0.0}

# 跑迴圈累加每一次解析的耗時 (變數 t 代表耗時)
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
# 1. JSON 通常最快：因為其底層是高度優化的原生 C 實作解析器。
# 2. XML  通常最慢：XML 的文字解析開銷非常大，包含許多冗餘標籤，且屬性皆需做字串轉換。
# 3. CSV  介於中間：格式簡單，但解析時每一欄預設都會變成字串，往往還需自行轉型為 int/float。
#
# 裝飾器帶來的好處：
# - 分離關注點 (Separation of Concerns)：計時邏輯只寫一次，不汙染原函式的商業邏輯。
# - 高度可插拔：要移除計時只需拿掉上方 @timeit 一行字，函式內部完全不需要修改。
# - functools.wraps：開發者友善，確保 debug、印出 log 或使用 help() 時能看到正確的函式名稱。
