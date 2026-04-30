# U01. 計時裝飾器實作與資料格式速度比較（6.1 / 6.2 / 6.3）
# 這支程式示範兩件事：
# 1) 先解決「每個函式都重複寫計時程式碼」的問題
# 2) 再比較 CSV / JSON / XML 三種資料格式的讀取速度
#
# 核心概念：
# - 裝飾器可以把通用行為（例如計時）抽離出來
# - functools.wraps 可以保留原函式名稱與說明文字
# - time.perf_counter() 適合拿來做高精度效能測量

import csv                   # 讀寫 CSV 格式資料
import json                  # 讀寫 JSON 格式資料
import time                  # 提供高精度計時函式
import io                    # StringIO：把字串包成檔案物件
import xml.etree.ElementTree as ET  # XML 解析器
import functools             # wraps：保留被包裝函式的 metadata

# ═══════════════════════════════════════════════════════════
# Part 1｜問題：每個函式都要手動計時 → 大量重複
# ═══════════════════════════════════════════════════════════
#
# 如果不用裝飾器，每個函式在測試效能時通常都要重複寫：
#   start = time.perf_counter()
#   result = func(...)
#   print(time.perf_counter() - start)
#
# 這樣的問題是：
# - 程式碼重複，難維護
# - 容易忘記某個函式要加計時
# - 真正的業務邏輯會被效能測試碼干擾

def read_csv_raw(data: str) -> list:
    """把 CSV 文字資料解析成字典列表。

    這裡直接回傳 list，是因為示範重點在「讀取解析速度」。
    csv.DictReader 會把第一列當成欄位名稱，後續每列轉成 dict。
    """
    return list(csv.DictReader(io.StringIO(data)))

def read_json_raw(data: str) -> list:
    """把 JSON 文字資料直接轉成 Python 物件。

    JSON 在 Python 中常對應成 list / dict / str / int 這些基本結構。
    """
    return json.loads(data)

def read_xml_raw(data: str) -> list:
    """把 XML 文字資料解析成字典列表。

    這裡假設 XML 格式固定為 <data><row .../></data>。
    每個 <row> 節點的屬性會被轉成一個 dict。
    """
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
#
# timeit(func) 的角色：
# - 接收一個函式 func
# - 回傳另一個函式 wrapper
# - wrapper 內部先計時、再呼叫 func、最後印出耗時
#
# 這就是裝飾器最常見的用途：
# 把「額外功能」包在原函式外層，但不改動原函式內容。

def timeit(func):
    """基礎版：在呼叫前後計時，印出耗時。

    這個版本只負責顯示結果，不回傳耗時數值。
    適合你只想看輸出、但不需要把時間拿去做後續計算的情況。
    """
    def wrapper(*args, **kwargs):
        # perf_counter() 是高解析度計時器，比 time.time() 更適合測效能
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        # {func.__name__:<20s}：函式名稱靠左對齊，欄位寬度 20
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")
        return result
    return wrapper

# 問題：wrapper 蓋掉了原函式的 __name__ / __doc__
def demo():
    """這是 demo 的說明文字"""
    pass

wrapped = timeit(demo)
print("未加 wraps 前：", wrapped.__name__)   # 會看到 wrapper，因為外層函式名稱被蓋掉

# ── Part 3｜functools.wraps：保留原函式的 metadata ──────────

def timeit(func):
    # wraps(func) 會把 func 的名稱、說明文字、模組資訊等複製到 wrapper
    # 這樣 help()、除錯訊息、IDE 提示就不會只看到 wrapper
    @functools.wraps(func)          # 保留 __name__ / __doc__ / __module__
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")
        return result
    return wrapper

wrapped = timeit(demo)
print("加 wraps 後：  ", wrapped.__name__)   # 這次會保留 demo，表示 wraps 生效
print()

# ═══════════════════════════════════════════════════════════
# Part 4｜實驗：相同資料，CSV vs JSON vs XML 速度比較
# ═══════════════════════════════════════════════════════════
#
# 接下來建立三份內容相同、但格式不同的測試資料。
# 這樣可以比較「格式本身」對讀取速度的影響。
#
# 注意：這不是嚴格基準測試，只是課堂示範。
# 真正的 benchmark 還需要：更多次數、冷啟動控制、硬體固定等。

# ── 產生測試資料（1000 筆學生記錄）────────────────────────
N = 1000

# CSV 格式
csv_buf = io.StringIO()
writer = csv.DictWriter(csv_buf, fieldnames=["id", "name", "score"])
writer.writeheader()
for i in range(N):
    # 每筆資料結構一致：id、name、score
    writer.writerow({"id": i, "name": f"Student{i:04d}", "score": 60 + i % 40})
CSV_DATA = csv_buf.getvalue()

# JSON 格式
JSON_DATA = json.dumps([
    {"id": i, "name": f"Student{i:04d}", "score": 60 + i % 40}
    for i in range(N)
])

# XML 格式
# XML 比較冗長，因為每筆資料都需要 <row .../> 標籤與屬性名稱。
xml_rows = "".join(
    f'<row id="{i}" name="Student{i:04d}" score="{60 + i % 40}"/>'
    for i in range(N)
)
XML_DATA = f"<data>{xml_rows}</data>"

# ── 帶回傳耗時的計時包裝 ─────────────────────────────────

def timeit_silent(func):
    """計時版本，但不印出來，只回傳 (result, elapsed)。

    用途：當你想把多次執行的耗時累積起來、再自己算平均值時很方便。
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        return result, time.perf_counter() - start
    return wrapper

# 把原始讀取函式包成「回傳耗時」版本，方便做統計平均
_csv  = timeit_silent(read_csv_raw)
_json = timeit_silent(read_json_raw)
_xml  = timeit_silent(read_xml_raw)

# ── 執行比較（重複 5 次取平均，排除冷啟動影響）────────────

RUNS = 5
# times 先記錄每種格式的總耗時，再除以 RUNS 求平均
times = {"CSV": 0.0, "JSON": 0.0, "XML": 0.0}

for _ in range(RUNS):
    _, t = _csv(CSV_DATA);   times["CSV"]  += t
    _, t = _json(JSON_DATA); times["JSON"] += t
    _, t = _xml(XML_DATA);   times["XML"]  += t

# print 標題列：方便閱讀比較表
print(f"=== 讀取 {N} 筆資料，重複 {RUNS} 次平均 ===\n")
print(f"{'格式':<6} {'平均耗時':>12}  {'相對 JSON':>10}")
# 以 JSON 的平均耗時作為基準，其他格式顯示相對倍數
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
