# U01. 計時裝飾器實作與資料格式速度比較
# Bloom: Understand / Create — 這支程式展示裝飾器如何解決「代碼重複」問題，
# 再進一步用它來比較 CSV、JSON、XML 三種格式的讀取效率。n#
# 核心概念：
#   6.1 函式是物件，可以被當成參數傳入或回傳
#   6.2 裝飾器 = 接收函式、返回函式的函式
#   6.3 functools.wraps 保留原函式的後設資料（名稱、說明等）

import csv
import json
import time
import io
import xml.etree.ElementTree as ET
import functools

# ═══════════════════════════════════════════════════════════
# Part 1｜問題：每個函式都要手動計時 → 大量重複代碼
# ═══════════════════════════════════════════════════════════
# 假設有三個讀檔函式，分別讀 CSV / JSON / XML。
# 若要測量每個函式的執行時間，笨辦法是：
#   - 在每個函式前後呼叫 time.perf_counter()
#   - 計算差值並印出
#   - 日後若要改進計時方式、改輸出格式，就要改三遍
# 這正是裝飾器可以解決的問題。

def read_csv_raw(data: str) -> list:
    # 簡單的 CSV 讀取函式，回傳 list of dicts。
    # csv.DictReader 會自動把第一列當表頭轉成欄名。
    return list(csv.DictReader(io.StringIO(data)))

def read_json_raw(data: str) -> list:
    # 簡單的 JSON 讀取函式。
    # json.loads 直接把 JSON 字串解析成 Python list。
    return json.loads(data)

def read_xml_raw(data: str) -> list:
    # 簡單的 XML 讀取函式。
    # ElementTree 的 findall 找出所有 row 元素，再抽出 attrib（屬性字典）。
    root = ET.fromstring(data)
    return [r.attrib for r in root.findall("row")]

# ── 沒有裝飾器的做法會像這樣 ────────────────────────────────────
# 若要計時 read_csv_raw：
#   start = time.perf_counter()
#   result = read_csv_raw(data)
#   print(f"read_csv_raw 耗時 {time.perf_counter() - start:.6f}s")
#
# 若要計時 read_json_raw，又要再寫一遍：
#   start = time.perf_counter()
#   result = read_json_raw(data)
#   print(f"read_json_raw 耗時 {time.perf_counter() - start:.6f}s")
#
# 每新增一個讀檔函式，計時代碼就重複三次，越來越難維護。
# 這就是「橫切面關注（cross-cutting concerns）」：
# 計時邏輯與業務邏輯（讀檔）根本無關，卻被硬生生混在一起。

# ═══════════════════════════════════════════════════════════
# Part 2｜解法：裝飾器把計時邏輯包起來，一次定義，到處復用
# ═══════════════════════════════════════════════════════════
# 裝飾器（decorator）的本質很簡單：
#   1. 接收一個函式作為參數
#   2. 在呼叫這個函式前後加上額外邏輯（這裡是計時）
#   3. 回傳一個新的函式
# 這樣就能把重複的計時邏輯隔離出來，在任何函式前加 @timeit 就搞定。

def timeit(func):
    """基礎版計時裝飾器。

    原理：
    1. timeit 接收函式 func 作為參數
    2. 定義內層函式 wrapper，負責「計時+呼叫+結果回傳」
    3. wrapper 在呼叫 func 前先記時，呼叫後再記時，計算差值並印出
    4. timeit 最後回傳 wrapper（而不是 func）

    用法：decorated_func = timeit(original_func)
    或用 @timeit 語法糖直接把 timeit 套在函式定義上。
    """
    def wrapper(*args, **kwargs):
        # *args 與 **kwargs 代表接收「任意數量任意名稱」的參數，
        # 讓裝飾器能適用於各種函式簽名。
        start = time.perf_counter()
        # perf_counter() 是高精度計時器，適合測量短時間。
        result = func(*args, **kwargs)
        # 呼叫原函式，傳入所有參數。
        elapsed = time.perf_counter() - start
        # 格式化輸出：函式名稱（20 字寬）+ 耗時（6 位小數）。
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")
        return result
    # 回傳 wrapper，之後對裝飾後的函式的呼叫都會先經過這個 wrapper。
    return wrapper

# ── 問題出現：wrapper 蓋掉了原函式的 metadata ────────────────────
# 當你用 @timeit 裝飾一個函式時，該函式的 __name__、__doc__ 等屬性
# 會被 wrapper 覆蓋，這會造成以下問題：
#   1. help(decorated_func) 看到的是 wrapper 的說明，不是原函式的
#   2. 如果代碼依賴 func.__name__，會拿到 'wrapper' 而不是原函式名稱
#   3. 除錯時很容易迷惑
def demo():
    """這是 demo 函式的說明文字。"""
    pass

wrapped = timeit(demo)
# 如果沒有 functools.wraps，這裡會印出 'wrapper'，而非 'demo'。
print("未加 wraps 前：", wrapped.__name__)   # 輸出：wrapper（錯誤！）

# ═══════════════════════════════════════════════════════════
# Part 3｜functools.wraps：保留原函式的 metadata
# ═══════════════════════════════════════════════════════════
# functools.wraps 是標準庫提供的工具，它會自動把被裝飾的原函式
# 的 __name__、__doc__、__module__ 等屬性複製到 wrapper 上。
# 這樣用戶看到的還是原函式的資訊，不會被 wrapper 矇騙。

def timeit(func):
    # @functools.wraps(func) 這行會在 wrapper 複製 func 的 metadata。
    @functools.wraps(func)          # 保留 __name__ / __doc__ / __module__
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        # 輸出格式：左對齐 20 字寬的函式名稱 + 6 位小數耗時。
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")
        return result
    return wrapper

wrapped = timeit(demo)
# 加上 @functools.wraps 後，wrapped 的 __name__ 會變成 'demo'。
print("加 wraps 後：  ", wrapped.__name__)   # 輸出：demo（正確）
print()

# ═══════════════════════════════════════════════════════════
# Part 4｜實驗：相同資料，CSV vs JSON vs XML 速度比較
# ═══════════════════════════════════════════════════════════
# 現在用裝飾器來做一個有趣的實驗：
# 用相同的 1000 筆學生資料，分別以 CSV、JSON、XML 格式存放，
# 然後測量各自的讀取速度。

# ── 產生測試資料（1000 筆學生記錄）────────────────────────
N = 1000

# CSV 格式
csv_buf = io.StringIO()
writer = csv.DictWriter(csv_buf, fieldnames=["id", "name", "score"])
writer.writeheader()
for i in range(N):
    writer.writerow({"id": i, "name": f"Student{i:04d}", "score": 60 + i % 40})
CSV_DATA = csv_buf.getvalue()

# JSON 格式
JSON_DATA = json.dumps([
    {"id": i, "name": f"Student{i:04d}", "score": 60 + i % 40}
    for i in range(N)
])

# XML 格式
xml_rows = "".join(
    f'<row id="{i}" name="Student{i:04d}" score="{60 + i % 40}"/>'
    for i in range(N)
)
XML_DATA = f"<data>{xml_rows}</data>"

# ── 帶回傳耗時的計時包裝 ──────────────────────────────────────
# 前面的 timeit 會直接把耗時印出來，但這裡我們需要「拿到耗時值」
# 才能彙整計算，所以定義 timeit_silent 版本：
# 回傳 (結果, 耗時)，交給外面的代碼決定怎麼處理耗時。

def timeit_silent(func):
    # 這個版本裝飾器不印出耗時，而是把它當成返回值的一部分。
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        # 回傳 tuple：(原結果, 耗時)。
        return result, time.perf_counter() - start
    return wrapper

# 把三個讀檔函式都包裝上 timeit_silent。
_csv  = timeit_silent(read_csv_raw)
_json = timeit_silent(read_json_raw)
_xml  = timeit_silent(read_xml_raw)

# ── 執行比較（重複 5 次取平均，排除冷啟動影響）─────────────────
# 單次測量的耗時容易受到系統狀況（快取、行程排程等）影響，
# 所以通常重複多次取平均會更穩定。這裡設定 5 次。

RUNS = 5
# times 字典用來累積耗時總數。
times = {"CSV": 0.0, "JSON": 0.0, "XML": 0.0}

# 執行 5 回合，每回合都測量三種格式。
for _ in range(RUNS):
    # _ 捨棄結果（因為只關心耗時），t 拿到耗時值並累加。
    _, t = _csv(CSV_DATA);   times["CSV"]  += t
    _, t = _json(JSON_DATA); times["JSON"] += t
    _, t = _xml(XML_DATA);   times["XML"]  += t

# 印出統計結果。
print(f"=== 讀取 {N} 筆資料，重複 {RUNS} 次平均 ===\n")
print(f"{'格式':<6} {'平均耗時':>12}  {'相對 JSON':>10}")
# JSON 通常是最快的基準，計算其他格式相對 JSON 的倍數。
base = times["JSON"] / RUNS
for fmt, total in times.items():
    # avg 是平均耗時（總耗時 / 重複次數）。
    avg = total / RUNS
    # 相對倍數 = 該格式平均耗時 / JSON 平均耗時。
    print(f"  {fmt:<6} {avg:.6f}s   {avg/base:>8.2f}x")

# ═══════════════════════════════════════════════════════════
# 觀察重點與結論
# ═══════════════════════════════════════════════════════════
# 1. JSON 通常最快
#    原因：Python 的 json 模組用 C 實作，解析器優化程度高。
#
# 2. XML 通常最慢
#    原因：XML 標籤冗長，解析時要處理大量文字結構；
#         元素樹的走訪與屬性轉換也有開銷。
#
# 3. CSV 介於中間
#    原因：格式簡單（純文字，逗號分隔），但每欄預設都是字串，
#         若要用數值就得自己 int() 轉型。
#
#
# 裝飾器設計模式帶來的好處：
# ✓ 計時邏輯只寫一次，不汙染原函式業務邏輯
# ✓ 要移除計時只需拿掉 @timeit，原函式本身完全不用改
# ✓ functools.wraps 確保 debug / help() 時能看到正確名稱
# ✓ 對所有讀檔函式一致應用，無須複製貼上
# ✓ 未來要改進計時方式（改輸出格式、新增日誌等），只需改裝飾器定義
