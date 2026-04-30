# U01. 計時裝飾器實作與資料格式速度比較（6.1 / 6.2 / 6.3）
# 從「重複的計時程式碼」出發，引入裝飾器，再做格式實驗

# ══════════════════════════════════════════════════════════════════════════
# 必需的模組導入
# ══════════════════════════════════════════════════════════════════════════
import csv                           # CSV 檔案讀取
import json                          # JSON 序列化與反序列化
import time                          # 計時工具（time.perf_counter()）
import io                            # StringIO：把字串包裝成檔案物件
import xml.etree.ElementTree as ET   # XML 解析（原生 C 實作，速度快）
import functools                     # functools.wraps：保留函式原始元數據

# ══════════════════════════════════════════════════════════════════════════
# Part 1｜問題：每個函式都要手動計時 → 大量重複程式碼
# ══════════════════════════════════════════════════════════════════════════
# 
# 三個讀取函式，各自支援不同的資料格式
# 如果沒有裝飾器，就要在每個函式呼叫前後手動加入計時邏輯
# 這樣會導致大量「樣板程式碼」和維護困難

def read_csv_raw(data: str) -> list:
    """解析 CSV 格式資料。csv.DictReader 返回字典列表"""
    # io.StringIO()：把字串轉成檔案物件，供 csv.reader 使用
    return list(csv.DictReader(io.StringIO(data)))

def read_json_raw(data: str) -> list:
    """解析 JSON 格式資料。json.loads() 原生支援 Python 物件序列化"""
    # json.loads()：JSON 字串 → Python 物件（dict / list 等）
    return json.loads(data)

def read_xml_raw(data: str) -> list:
    """解析 XML 格式資料。提取每個 <row> 標籤的屬性"""
    # ET.fromstring()：把 XML 字串解析成元素樹
    # root.findall("row")：尋找所有 <row> 子元素
    # r.attrib：提取元素的屬性字典
    root = ET.fromstring(data)
    return [r.attrib for r in root.findall("row")]

# ── 沒有裝飾器時的手動計時 ──
# 問題：每個函式都要重複相同的計時邏輯
# start = time.perf_counter()        # 記錄開始時間
# result = read_csv_raw(data)        # 執行目標函式
# print(f"read_csv_raw 耗時 {time.perf_counter() - start:.6f}s")  # 印出耗時
#
# start = time.perf_counter()
# result = read_json_raw(data)
# print(f"read_json_raw 耗時 {time.perf_counter() - start:.6f}s")
# 
# start = time.perf_counter()
# result = read_xml_raw(data)
# print(f"read_xml_raw 耗時 {time.perf_counter() - start:.6f}s")
#
# ⚠️ 問題分析：
# - 每加一個函式就多寫 3 行重複程式碼
# - 計時邏輯與商務邏輯混合，難以維護
# - 要移除計時必須逐個修改每個函式
# - 容易複製貼上時出錯

# ══════════════════════════════════════════════════════════════════════════
# Part 2｜解法：裝飾器把計時邏輯包起來，一次定義，到處復用
# ══════════════════════════════════════════════════════════════════════════
# 
# 裝飾器（Decorator）是一個高階函數，它接受一個函數作為輸入
# 並回傳一個「增強版」的函數
#
# 好處：
# - 計時邏輯集中在一個地方，易於維護
# - 使用時只需加一行 @timeit，非常簡潔
# - 不需修改原函式的程式碼
# - 若要移除計時，只需刪除 @timeit 即可

def timeit(func):
    """基礎版裝飾器：在函式執行前後計時，並印出耗時
    
    參數：
        func：要被裝飾的函式
    
    傳回：
        wrapper：增強後的函式（內部包含計時邏輯）
    """
    def wrapper(*args, **kwargs):
        # 記錄開始時間（time.perf_counter() 用於高精度計時）
        start = time.perf_counter()
        
        # 執行原始函式，保留其傳回值
        result = func(*args, **kwargs)
        
        # 計算耗時（秒）
        elapsed = time.perf_counter() - start
        
        # 打印計時結果
        # func.__name__:<20s：函式名稱，左對齐，佔位 20 字元
        # elapsed:.6f：耗時，小數點後 6 位
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")
        
        # 傳回原始函式的結果
        return result
    
    # 傳回包裝後的函式
    return wrapper

# ── 問題：装飾器會遺失原函式的元數據 ──
# 當我們使用 @timeit 裝飾函式時，wrapper 函式會覆蓋原函式的元數據
# 特別是 __name__ 和 __doc__ 屬性

def demo():
    """這是 demo 的說明文字"""
    pass

# 手動應用裝飾器
wrapped = timeit(demo)
print("未加 wraps 前：", wrapped.__name__)   # 輸出 wrapper（錯誤！應該是 demo）
print("未加 wraps 前：", wrapped.__doc__)    # 輸出 None（說明文字遺失）

# 這會導致 debug 時看不到函式的真實名稱，help() 也無法顯示說明文字

# ══════════════════════════════════════════════════════════════════════════
# Part 3｜functools.wraps：保留原函式的元數據
# ══════════════════════════════════════════════════════════════════════════
# 
# 解決方案：使用 functools.wraps 裝飾器
# 它會自動複製原函式的 __name__、__doc__、__module__ 等屬性到 wrapper

def timeit(func):
    """改進版裝飾器：使用 functools.wraps 保留原函式的元數據"""
    @functools.wraps(func)          # 這一行很關鍵！將原函式的元數據複製到 wrapper
    def wrapper(*args, **kwargs):
        # 計時邏輯（同前）
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")
        return result
    return wrapper

# 使用改進後的裝飾器
wrapped = timeit(demo)
print("加 wraps 後：  ", wrapped.__name__)   # 輸出 demo（正確！）
print("加 wraps 後：  ", wrapped.__doc__)    # 輸出這是 demo 的說明文字（正確！）
print()

# ══════════════════════════════════════════════════════════════════════════
# Part 4｜實驗：相同資料用不同格式儲存，測速 CSV vs JSON vs XML
# ══════════════════════════════════════════════════════════════════════════
# 
# 目的：比較三種常見資料格式的解析速度
# 實驗變數：資料量固定（1000 筆），改變格式，測量讀取耗時
# 預期結果：
#   - JSON 最快（原生 C 實作的高效解析器）
#   - CSV 中等（簡單格式，但需逐欄轉型）
#   - XML  最慢（文字解析開銷大，屬性提取複雜）

# ── 產生測試資料集（1000 筆學生記錄）────────────────────────
N = 1000  # 資料筆數

# ── CSV 格式 ──
# 結構：id,name,score
#      0,Student0000,60
#      1,Student0001,61
#      ...
csv_buf = io.StringIO()  # 建立字串緩衝區（代替檔案）
writer = csv.DictWriter(csv_buf, fieldnames=["id", "name", "score"])  # 定義欄位
writer.writeheader()  # 寫入表頭
for i in range(N):
    writer.writerow({
        "id": i,                      # 學號：0～999
        "name": f"Student{i:04d}",   # 姓名：Student0000～Student0999
        "score": 60 + i % 40           # 成績：60～99（循環）
    })
CSV_DATA = csv_buf.getvalue()  # 提取字串內容

# ── JSON 格式 ──
# 結構：[{"id": 0, "name": "Student0000", "score": 60}, {...}, ...]
JSON_DATA = json.dumps([
    {
        "id": i,
        "name": f"Student{i:04d}",
        "score": 60 + i % 40
    }
    for i in range(N)
])

# ── XML 格式 ──
# 結構：<data><row id="0" name="Student0000" score="60"/><row .../></data>
xml_rows = "".join(
    f'<row id="{i}" name="Student{i:04d}" score="{60 + i % 40}"/>'
    for i in range(N)
)
XML_DATA = f"<data>{xml_rows}</data>"

# ── 計時裝飾器（改版）：帶回傳耗時值 ──
# 不同於前面的 timeit（只印出結果），這個版本會同時傳回結果和耗時
# 用途：需要進一步處理耗時數據（如累積、平均等）

def timeit_silent(func):
    """無聲計時裝飾器：執行函式並傳回 (結果, 耗時) 的 tuple"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)  # 執行原函式
        elapsed = time.perf_counter() - start  # 計算耗時
        return result, elapsed  # 同時傳回結果和耗時
    return wrapper

# 用裝飾器包裝三個讀取函式
_csv  = timeit_silent(read_csv_raw)   # 讀取 CSV 的計時版本
_json = timeit_silent(read_json_raw)  # 讀取 JSON 的計時版本
_xml  = timeit_silent(read_xml_raw)   # 讀取 XML 的計時版本

# ── 執行重複測試（排除冷啟動影響，取平均值）────────────
# 計時實驗的最佳實踐：
# 1. 重複多次（減少隨機波動）
# 2. 第一次往往較慢（冷啟動），多次取平均更準確
# 3. 相同順序執行，排除快取效應

RUNS = 5  # 重複次數
times = {"CSV": 0.0, "JSON": 0.0, "XML": 0.0}  # 累積耗時字典

# 執行 RUNS 次重複測試
for run_idx in range(RUNS):
    # 第 run_idx 次：執行三種格式的讀取，累積耗時
    _, t = _csv(CSV_DATA)      # 讀取 CSV，取耗時 t
    times["CSV"]  += t          # 累積到 CSV 總耗時
    
    _, t = _json(JSON_DATA)    # 讀取 JSON，取耗時 t
    times["JSON"] += t          # 累積到 JSON 總耗時
    
    _, t = _xml(XML_DATA)      # 讀取 XML，取耗時 t
    times["XML"]  += t          # 累積到 XML 總耗時

# ── 輸出結果 ──
print(f"=== 讀取 {N} 筆資料，重複 {RUNS} 次平均 ===")
print()
print(f"{'格式':<6} {'平均耗時':>12}  {'相對 JSON':>10}")
print("-" * 35)

# 計算 JSON 的平均耗時，作為基準
base = times["JSON"] / RUNS

# 逐個輸出各格式的平均耗時和相對倍數
for fmt, total in times.items():
    avg = total / RUNS  # 平均耗時 = 總耗時 / 重複次數
    ratio = avg / base  # 相對倍數 = 該格式平均耗時 / JSON 平均耗時
    print(f"  {fmt:<6} {avg:.6f}s   {ratio:>8.2f}x")

# ══════════════════════════════════════════════════════════════════════════
# 觀察與分析
# ══════════════════════════════════════════════════════════════════════════
#
# 📊 預期的速度排序（快到慢）：
# 1. JSON 通常最快（原因：Python 內建 json 模組使用 C 實作，解析效率高）
# 2. CSV  介於中間（原因：簡單的文字格式，但每欄都是字串，需要自行轉型）
# 3. XML  通常最慢（原因：標籤開銷大，文字解析複雜，屬性字串轉換成本高）
#
# 💡 裝飾器（Decorator）的設計優勢：
#
# ✓ 單一職責原則
#   - 計時邏輯獨立在 timeit 函式，與讀取邏輯完全分離
#   - 易於理解、測試、維護
#
# ✓ 代碼復用
#   - 同一個 @timeit 裝飾器可應用於任何函式
#   - 不需為每個函式複製貼上計時程式碼
#
# ✓ 簡易移除
#   - 要移除計時功能，只需刪除 @timeit 這一行
#   - 原函式代碼完全不需修改
#
# ✓ 元數據保留
#   - 透過 functools.wraps，保留原函式的 __name__、__doc__ 等
#   - debug、help()、IDE 跳轉等工具都能正常工作
#
# 🎯 進階應用：
#   - 可改寫 timeit 為參數化版本，支援自訂格式和輸出方式
#   - 可與日誌系統整合，記錄效能數據到檔案
#   - 可加上異常處理，在執行出錯時也記錄耗時
#   - 可支援遞迴函式，累積所有層級的耗時
