# U01. 計時裝飾器實作與資料格式速度比較（6.1 / 6.2 / 6.3）
# 從「重複的計時程式碼」出發，引入裝飾器，再做格式實驗
#
# 本程式重點：
# 1. 示範為什麼重複寫計時程式碼很麻煩
# 2. 使用裝飾器 decorator 把計時邏輯包起來
# 3. 說明 functools.wraps 的用途
# 4. 產生 CSV、JSON、XML 三種格式的測試資料
# 5. 比較三種資料格式的讀取速度

# 匯入 csv 模組，用來讀取與產生 CSV 格式資料
import csv

# 匯入 json 模組，用來處理 JSON 格式資料
import json

# 匯入 time 模組，用來取得高精度時間，進行效能計時
import time

# 匯入 io 模組，用來使用 StringIO
# StringIO 可以把字串當成類檔案物件使用
import io

# 匯入 xml.etree.ElementTree，並取別名 ET
# 用來解析 XML 格式資料
import xml.etree.ElementTree as ET

# 匯入 functools 模組
# 後面會使用 functools.wraps 來保留原函式的名稱與說明文字
import functools

# ═══════════════════════════════════════════════════════════
# Part 1｜問題：每個函式都要手動計時 → 大量重複
# ═══════════════════════════════════════════════════════════

# 定義讀取 CSV 的原始函式
# data 是一整段 CSV 文字
# io.StringIO(data) 會把字串包裝成類檔案物件
# csv.DictReader 會把每一列資料讀成字典
def read_csv_raw(data: str) -> list:
    return list(csv.DictReader(io.StringIO(data)))

# 定義讀取 JSON 的原始函式
# json.loads(data) 會把 JSON 字串解析成 Python 物件
# 這裡預期會解析成 list，裡面每筆資料是 dict
def read_json_raw(data: str) -> list:
    return json.loads(data)

# 定義讀取 XML 的原始函式
# ET.fromstring(data) 會把 XML 字串解析成 XML 樹狀結構
def read_xml_raw(data: str) -> list:

    # root 是 XML 的根節點
    root = ET.fromstring(data)

    # root.findall("row") 會找出所有 <row ... /> 節點
    # r.attrib 會取得該 row 節點的屬性字典
    # 最後回傳由多個屬性字典組成的 list
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

# 定義一個裝飾器函式 timeit
# 裝飾器本質上是一個「接收函式，回傳新函式」的函式
# func 代表被包裝的原函式
def timeit(func):
    """基礎版：在呼叫前後計時，印出耗時"""

    # wrapper 是真正取代原函式的新函式
    # *args 可以接收任意數量的位置參數
    # **kwargs 可以接收任意數量的關鍵字參數
    # 這樣 wrapper 才能包住各種不同參數形式的函式
    def wrapper(*args, **kwargs):

        # time.perf_counter() 會回傳高精度時間
        # 適合用來測量程式執行耗時
        start = time.perf_counter()

        # 呼叫原本被包裝的函式
        # 並把原本傳進 wrapper 的參數完整轉交給 func
        result = func(*args, **kwargs)

        # 再次取得時間，並減去開始時間，得到執行耗時
        elapsed = time.perf_counter() - start

        # 印出函式名稱與耗時
        # :<20s 表示函式名稱靠左對齊，寬度 20
        # :.6f 表示小數點後顯示 6 位
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")

        # 回傳原函式的結果
        # 這樣裝飾器不會破壞原函式原本的回傳值
        return result

    # 回傳 wrapper，讓外部呼叫時實際執行 wrapper
    return wrapper

# 問題：wrapper 蓋掉了原函式的 __name__ / __doc__

# 定義一個 demo 函式，用來示範裝飾器會造成 metadata 被覆蓋的問題
def demo():
    """這是 demo 的說明文字"""
    pass

# 用 timeit 手動包裝 demo
# wrapped 會變成 wrapper 函式
wrapped = timeit(demo)

# 因為基礎版 timeit 沒有使用 functools.wraps
# 所以 wrapped.__name__ 會變成 "wrapper"
# 而不是原本的 "demo"
print("未加 wraps 前：", wrapped.__name__)   # wrapper（錯誤！）

# ── Part 3｜functools.wraps：保留原函式的 metadata ──────────

# 重新定義 timeit
# 這次加入 functools.wraps，修正原函式 metadata 被覆蓋的問題
def timeit(func):

    # @functools.wraps(func) 會把 func 的 __name__、__doc__、__module__ 等資訊
    # 複製到 wrapper 身上
    # 這樣 debug、help()、錯誤訊息會比較正確
    @functools.wraps(func)          # 保留 __name__ / __doc__ / __module__
    def wrapper(*args, **kwargs):

        # 記錄函式開始執行的時間
        start = time.perf_counter()

        # 執行原函式，並保存回傳結果
        result = func(*args, **kwargs)

        # 計算耗時
        elapsed = time.perf_counter() - start

        # 印出原函式名稱與耗時
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")

        # 回傳原函式執行結果
        return result

    # 回傳包裝後的 wrapper
    return wrapper

# 再次用新版 timeit 包裝 demo
wrapped = timeit(demo)

# 因為新版 timeit 使用了 functools.wraps
# 所以 wrapped.__name__ 會正確保留為 "demo"
print("加 wraps 後：  ", wrapped.__name__)   # demo（正確）

# 印出空行，讓後面的速度比較輸出更清楚
print()

# ═══════════════════════════════════════════════════════════
# Part 4｜實驗：相同資料，CSV vs JSON vs XML 速度比較
# ═══════════════════════════════════════════════════════════

# ── 產生測試資料（1000 筆學生記錄）────────────────────────

# N 代表要產生幾筆學生資料
N = 1000

# CSV 格式

# 建立一個 StringIO 物件
# 用來把 CSV 內容先寫在記憶體中，而不是寫到實體檔案
csv_buf = io.StringIO()

# 建立 csv.DictWriter
# fieldnames 指定 CSV 欄位名稱與欄位順序
writer = csv.DictWriter(csv_buf, fieldnames=["id", "name", "score"])

# 寫入 CSV 標題列
# 也就是 id,name,score
writer.writeheader()

# 產生 N 筆學生資料
for i in range(N):

    # writer.writerow 會寫入一列 CSV 資料
    # id 是學生編號
    # name 使用 Student0000、Student0001 這種格式
    # score 使用 60 + i % 40，讓分數落在 60~99 的範圍循環
    writer.writerow({"id": i, "name": f"Student{i:04d}", "score": 60 + i % 40})

# 取得 StringIO 目前累積的全部 CSV 文字
CSV_DATA = csv_buf.getvalue()

# JSON 格式

# 使用 json.dumps 把 Python list/dict 轉成 JSON 字串
# 這裡用 list comprehension 產生 N 筆學生資料
JSON_DATA = json.dumps([
    {"id": i, "name": f"Student{i:04d}", "score": 60 + i % 40}
    for i in range(N)
])

# XML 格式

# 產生多個 <row ... /> XML 節點字串
# 每一筆學生資料會變成一個 row 標籤
# 例如：<row id="0" name="Student0000" score="60"/>
xml_rows = "".join(
    f'<row id="{i}" name="Student{i:04d}" score="{60 + i % 40}"/>'
    for i in range(N)
)

# 在所有 row 外面包一層 <data> 根節點
# XML 必須有單一根節點，才能被正確解析
XML_DATA = f"<data>{xml_rows}</data>"

# ── 帶回傳耗時的計時包裝 ─────────────────────────────────

# 定義另一個計時裝飾器 timeit_silent
# 與前面的 timeit 不同：
# 1. 不直接印出耗時
# 2. 回傳「原函式結果」與「耗時」
# 這樣比較適合做多次實驗並計算平均
def timeit_silent(func):

    # 使用 wraps 保留原函式 metadata
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        # 記錄開始時間
        start = time.perf_counter()

        # 執行原函式
        result = func(*args, **kwargs)

        # 回傳 tuple：
        # 第一個值是原函式結果
        # 第二個值是耗時
        return result, time.perf_counter() - start

    # 回傳包裝後的 wrapper
    return wrapper

# 將三個讀取函式分別包上 timeit_silent
# 之後呼叫 _csv、_json、_xml 時，就會同時取得解析結果與耗時
_csv  = timeit_silent(read_csv_raw)
_json = timeit_silent(read_json_raw)
_xml  = timeit_silent(read_xml_raw)

# ── 執行比較（重複 5 次取平均，排除冷啟動影響）────────────

# 設定每種格式重複測試的次數
RUNS = 5

# 建立 times 字典，用來累加每種格式的總耗時
# 最後再除以 RUNS 得到平均耗時
times = {"CSV": 0.0, "JSON": 0.0, "XML": 0.0}

# 重複測試 RUNS 次
for _ in range(RUNS):

    # 測試 CSV 解析時間
    # _ 代表忽略解析結果，只取耗時 t
    # ; 在同一行中分隔兩個敘述
    _, t = _csv(CSV_DATA);   times["CSV"]  += t

    # 測試 JSON 解析時間，並累加耗時
    _, t = _json(JSON_DATA); times["JSON"] += t

    # 測試 XML 解析時間，並累加耗時
    _, t = _xml(XML_DATA);   times["XML"]  += t

# 印出本次實驗標題
# 會顯示資料筆數 N 與重複次數 RUNS
print(f"=== 讀取 {N} 筆資料，重複 {RUNS} 次平均 ===\n")

# 印出表格標題
# {'格式':<6} 表示「格式」靠左對齊，占 6 格
# {'平均耗時':>12} 表示「平均耗時」靠右對齊，占 12 格
# {'相對 JSON':>10} 表示「相對 JSON」靠右對齊，占 10 格
print(f"{'格式':<6} {'平均耗時':>12}  {'相對 JSON':>10}")

# 以 JSON 的平均耗時當作比較基準
# 後面會用其他格式的平均耗時除以 base
# 得到相對於 JSON 慢或快幾倍
base = times["JSON"] / RUNS

# 逐一輸出 CSV、JSON、XML 的平均耗時與相對倍率
for fmt, total in times.items():

    # 計算平均耗時
    avg = total / RUNS

    # avg/base 表示該格式相對於 JSON 的耗時倍率
    # 例如 2.00x 代表約為 JSON 的 2 倍耗時
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