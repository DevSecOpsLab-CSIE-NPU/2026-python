# U01. 計時裝飾器實作與資料格式速度比較（6.1 / 6.2 / 6.3）
# 從「重複的計時程式碼」出發，引入裝飾器，再做格式實驗

# 匯入必要的模組
import csv      # 用於處理CSV資料
import json     # 用於處理JSON資料
import time     # 用於計時功能
import io       # 用於處理字串輸入輸出
import xml.etree.ElementTree as ET  # 用於解析XML資料
import functools  # 用於裝飾器工具

# ═══════════════════════════════════════════════════════════
# Part 1｜問題：每個函式都要手動計時 → 大量重複
# ═══════════════════════════════════════════════════════════

# 定義三個讀取不同格式資料的函式
def read_csv_raw(data: str) -> list:
    """從CSV字串讀取資料並返回字典列表"""
    return list(csv.DictReader(io.StringIO(data)))

def read_json_raw(data: str) -> list:
    """從JSON字串讀取資料並返回列表"""
    return json.loads(data)

def read_xml_raw(data: str) -> list:
    """從XML字串讀取資料並返回屬性字典列表"""
    root = ET.fromstring(data)
    return [r.attrib for r in root.findall("row")]

# 沒有裝飾器：每次都要複製貼上計時程式碼 ↓
# 以下是手動計時的範例程式碼（已註解）：
# start = time.perf_counter()  # 開始計時
# result = read_csv_raw(data)  # 執行函式
# print(f"read_csv_raw 耗時 {time.perf_counter() - start:.6f}s")  # 輸出耗時
#
# 同樣的計時程式碼需要為每個函式重複撰寫，容易出錯且難以維護

# ═══════════════════════════════════════════════════════════
# Part 2｜解法：裝飾器把計時邏輯包起來，一次定義，到處復用
# ═══════════════════════════════════════════════════════════

def timeit(func):
    """基礎版：在呼叫前後計時，印出耗時"""
    def wrapper(*args, **kwargs):
        start = time.perf_counter()  # 記錄開始時間
        result = func(*args, **kwargs)  # 執行原始函式
        elapsed = time.perf_counter() - start  # 計算耗時
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")  # 格式化輸出耗時
        return result  # 返回原始函式的結果
    return wrapper

# 問題：wrapper 蓋掉了原函式的 __name__ / __doc__
def demo():
    """這是 demo 的說明文字"""
    pass

wrapped = timeit(demo)
print("未加 wraps 前：", wrapped.__name__)   # 輸出：wrapper（錯誤！）

# ── Part 3｜functools.wraps：保留原函式的 metadata ──────────

def timeit(func):
    @functools.wraps(func)          # 使用wraps保留原函式的__name__、__doc__等屬性
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")
        return result
    return wrapper

wrapped = timeit(demo)
print("加 wraps 後：  ", wrapped.__name__)   # 輸出：demo（正確）
print()

# ═══════════════════════════════════════════════════════════
# Part 4｜實驗：相同資料，CSV vs JSON vs XML 速度比較
# ═══════════════════════════════════════════════════════════

# ═══════════════════════════════════════════════════════════
# Part 4｜實驗：相同資料，CSV vs JSON vs XML 速度比較
# ═══════════════════════════════════════════════════════════

# ── 產生測試資料（1000 筆學生記錄）────────────────────────
N = 1000  # 設定測試資料筆數

# CSV 格式：產生CSV格式的字串資料
csv_buf = io.StringIO()  # 建立字串緩衝區
writer = csv.DictWriter(csv_buf, fieldnames=["id", "name", "score"])  # 建立CSV寫入器
writer.writeheader()  # 寫入標頭
for i in range(N):  # 產生N筆測試資料
    writer.writerow({"id": i, "name": f"Student{i:04d}", "score": 60 + i % 40})  # 寫入每一列
CSV_DATA = csv_buf.getvalue()  # 取得完整的CSV字串

# JSON 格式：產生JSON格式的列表資料
JSON_DATA = json.dumps([  # 將列表序列化為JSON字串
    {"id": i, "name": f"Student{i:04d}", "score": 60 + i % 40}
    for i in range(N)  # 產生N筆字典資料
])

# XML 格式：產生XML格式的字串資料
xml_rows = "".join(  # 將所有列組合成單一字串
    f'<row id="{i}" name="Student{i:04d}" score="{60 + i % 40}"/>'  # 產生每一列的XML標籤
    for i in range(N)
)
XML_DATA = f"<data>{xml_rows}</data>"  # 包裝在根元素中

# ── 帶回傳耗時的計時包裝 ─────────────────────────────────

def timeit_silent(func):
    """靜默計時裝飾器：執行函式並返回結果與耗時，不印出訊息"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()  # 開始計時
        result = func(*args, **kwargs)  # 執行函式
        return result, time.perf_counter() - start  # 返回結果和耗時
    return wrapper

# 將三個讀取函式包裝為靜默計時版本
_csv  = timeit_silent(read_csv_raw)
_json = timeit_silent(read_json_raw)
_xml  = timeit_silent(read_xml_raw)

# ── 執行比較（重複 5 次取平均，排除冷啟動影響）────────────

RUNS = 5  # 設定重複執行次數
times = {"CSV": 0.0, "JSON": 0.0, "XML": 0.0}  # 初始化計時字典

for _ in range(RUNS):  # 重複執行多次
    _, t = _csv(CSV_DATA);   times["CSV"]  += t  # 執行CSV讀取並累加耗時
    _, t = _json(JSON_DATA); times["JSON"] += t  # 執行JSON讀取並累加耗時
    _, t = _xml(XML_DATA);   times["XML"]  += t  # 執行XML讀取並累加耗時

print(f"=== 讀取 {N} 筆資料，重複 {RUNS} 次平均 ===\n")
print(f"{'格式':<6} {'平均耗時':>12}  {'相對 JSON':>10}")
base = times["JSON"] / RUNS  # 以JSON的平均耗時作為基準
for fmt, total in times.items():
    avg = total / RUNS  # 計算平均耗時
    print(f"  {fmt:<6} {avg:.6f}s   {avg/base:>8.2f}x")  # 輸出格式化結果

# ═══════════════════════════════════════════════════════════
# 觀察重點
# ═══════════════════════════════════════════════════════════
# 1. JSON 通常最快（原生 C 實作的解析器）
#    - JSON格式具有高效能的C語言解析器，處理速度最快
#
# 2. XML 通常最慢（文字解析開銷大，屬性字串轉換）
#    - XML需要解析標籤結構和屬性，處理複雜度較高
#
# 3. CSV 介於中間（簡單格式，但每欄都是字串需自行轉型）
#    - CSV格式簡單，但欄位都是字串，應用時可能需要額外轉換型別
#
# 裝飾器帶來的好處：
# - 計時邏輯只寫一次，不汙染原函式
#   - 將計時功能封裝在裝飾器中，避免重複程式碼
#
# - 要移除計時只需拿掉 @timeit，函式本身不需修改
#   - 透過裝飾器語法，可以輕鬆開關功能而不改動原函式
#
# - functools.wraps 確保 debug / help() 時能看到正確名稱
#   - 保留原函式的元資料（名稱、說明文件等），有助於除錯和說明文件
