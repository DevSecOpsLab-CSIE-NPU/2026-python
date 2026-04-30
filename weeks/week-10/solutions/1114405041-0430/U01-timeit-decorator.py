# U01. 計時裝飾器實作與資料格式速度比較（6.1 / 6.2 / 6.3）
# 從「重複的計時程式碼」出發，引入裝飾器，再做格式實驗
# 重點：Decorator 是 Python 中最強大的時間使用技巧，可以將重複程式碼抽離

import csv          # CSV 抽象語法解析器
import json          # JSON 解析（速度最快，依賴 C 實作）
import time          # 計時增模組，perf_counter() 最精確的計時（不受系統時間調整影響）
import io            # 內存檔案水減，模擬檔案作為字串
import xml.etree.ElementTree as ET  # XML 解析增模組，遍位出離例花（最慢）
import functools    # 隨偶案來抽子函數的工率庫，wraps() 用來保留原函數的上標資料

# ═══════════════════════════════════════════════════════════
# Part 1｜問題：每個函式都要手動計時 → 大量重複
# ═══════════════════════════════════════════════════════════

# 定義三種格式的解析函式（沒有計時功能）
# 傳入參數：data 字串
# 傳出結果：字典清單

def read_csv_raw(data: str) -> list:
    """
    解析 CSV 格式的資料。
    - 利用 io.StringIO() 把字串當作「假檔案」來讀取，不會動磁盤
    - csv.DictReader 把第一列為欄位名，下列為值，傳回字典清單
    """
    return list(csv.DictReader(io.StringIO(data)))

def read_json_raw(data: str) -> list:
    """
    解析 JSON 格式的資料。
    - json.loads() 直接把字串轉成 Python 物件，速度最快
    - JSON 是文字物件，每個位置都是預先編碼好的
    """
    return json.loads(data)

def read_xml_raw(data: str) -> list:
    """
    解析 XML 格式的資料。
    - ET.fromstring() 把 XML 轉成樹狀結構
    - 需要用 .attrib 取出屬性，每行都是字典，最複雜最慢
    """
    root = ET.fromstring(data)
    return [r.attrib for r in root.findall("row")]

# 沒有裝飾器時的問題：每次都要複製貼上計時程式碼 ↓
# 這都是樣版程式碼（Boilerplate code），超級無聊！
#
# start = time.perf_counter()                # 計時開始
# result = read_csv_raw(data)                # 執行函式
# print(f"read_csv_raw 耗時 {time.perf_counter() - start:.6f}s")  # 計算時間
#
# start = time.perf_counter()                # 每個函數都要複製！
# result = read_json_raw(data)
# print(f"read_json_raw 耗時 {time.perf_counter() - start:.6f}s")
# ... 每加一個函數就多寫 3 行重複程式碼，且容易忘記刪掉！
# 這就是裝飾器 decorator 存在的意義！

# ═══════════════════════════════════════════════════════════
# Part 2｜解法：裝飾器把計時邏輯包起來，一次定義，到處復用
# Decorator 的魔鬼：@ 符號 + 函式 = 自動替換原函式
# ═══════════════════════════════════════════════════════════

def timeit(func):
    """
    裝飾器：只負責計時，不改變原函式。
    引數：func 是被裝飾的原函式（例如 read_csv_raw）
    傳出：wrapper 函式（會被指定給原函式名稱）
    """
    def wrapper(*args, **kwargs):
        # *args: 位置型參數
        # **kwargs: 鍵值型參數
        
        start = time.perf_counter()      # 計時開始
        result = func(*args, **kwargs)   # 執行原函式
        elapsed = time.perf_counter() - start  # 計算耗時
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")  # 列印結果
        return result                    # 回傳結果
    return wrapper

# 重大問題：跨迴圈的 wrapper 函式會蓋掉原函式的 __name__ 和 __doc__ 屬性
# 這會影響 debug 記錄和 help() 文件，會顯示 "wrapper" 而不是原函式名稱！

def demo():
    """這是 demo 的說明文字（這是 __doc__ 屬性）"""
    pass

wrapped = timeit(demo)  # 幸虧裝飾器承接 demo
# 選項：wrapped 的 __name__ 已經是 "wrapper" 了，不是原來的 "demo"！
print("未加 wraps 前：", wrapped.__name__)   # wrapper（錯誤！）
print("未加 wraps 前：", wrapped.__doc__)   # None（也失掉了！）

# ── Part 3｜functools.wraps：保留原函式的 metadata ──────────
# 解救：@functools.wraps(func) 是一個【裝飾器的裝飾器】！
# 它會把 __name__、__doc__、__module__ 等後設跟衣 wrapper
# 後來 wrapped.__name__ 就會是原函式的名稱了！

def timeit(func):
    @functools.wraps(func)          # 保留原函式的 __name__ / __doc__ / __module__
    def wrapper(*args, **kwargs):
        start = time.perf_counter()     # 計時開始
        result = func(*args, **kwargs)  # 執行原函式
        elapsed = time.perf_counter() - start  # 計算耗費時間
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")  # 列印結果
        return result
    return wrapper

# 驗證 functools.wraps 的效果
wrapped = timeit(demo)
print("加 wraps 後：  ", wrapped.__name__)   # demo（正確！）
print("加 wraps 後：  ", wrapped.__doc__)   # 這是 demo 的說明文字（保護了！）
print("\n" + "="*50 + "\n")

# ═══════════════════════════════════════════════════════════
# Part 4｜實驗：相同資料，CSV vs JSON vs XML 速度比較
# ═══════════════════════════════════════════════════════════

# ── 產生測試資料（1000 筆學生記錄）────────────────────────
N = 1000  # 模擬約一千筆新生資料

# ──── CSV 格式 ────
# 使用內存檔案水減（StringIO）或模擬一個內存二創也筆 CSV 粗後器
csv_buf = io.StringIO()
writer = csv.DictWriter(csv_buf, fieldnames=["id", "name", "score"])  # 定義欄位
writer.writeheader()  # 寫入標題列
for i in range(N):
    writer.writerow({"id": i, "name": f"Student{i:04d}", "score": 60 + i % 40})  # 寫入 N 筆記錄
CSV_DATA = csv_buf.getvalue()  # 提取作為字串

# ──── JSON 格式 ────
# JSON 是文字物件格式：易輔育，全部都是字典和整數映言
JSON_DATA = json.dumps([
    {"id": i, "name": f"Student{i:04d}", "score": 60 + i % 40}
    for i in range(N)
])

# ──── XML 格式 ────
# XML 是標記語言，每舍情搖一個 <row> 偏架，複雜且繁瑣
xml_rows = "".join(
    f'<row id="{i}" name="Student{i:04d}" score="{60 + i % 40}"/>'  # 依一棋推擴展開 xml 偏架
    for i in range(N)
)
XML_DATA = f"<data>{xml_rows}</data>"  # 建立一個根患快 <data> 偏架

# ── 帶回傳耗時的計時包裝 ─────────────────────────────────

def timeit_silent(func):
    """
    裝飾器：計時但不列印，而是直接回傳 (結果, 耗時) 混成的 tuple。
    這樣澡洗一上卡了我們自己取取寶寶的時間了，可以漫弘語詢爆點數字
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()           # 計時開始
        result = func(*args, **kwargs)        # 執行原函式和取存結果
        elapsed = time.perf_counter() - start  # 計算耗費時間
        return result, elapsed                # 回傳結果和耗費時間的 tuple
    return wrapper

# 用裝飾器包裝三個解析函式，以便後續我們可以取取時間
_csv  = timeit_silent(read_csv_raw)   # 裝飾後的 CSV 解析函式
_json = timeit_silent(read_json_raw)  # 裝飾後的 JSON 解析函式
_xml  = timeit_silent(read_xml_raw)   # 裝飾後的 XML 解析函式

# ── 執行比較（重複 5 次取平均，排除冷啟動影響）────────────

# 備註：冷啟動 (Cold Start) 是指第一次執行比較詔愛沒有換優化的時間。
# 要驗應導後次的時間，才能看出實驗詔愛減了待後
RUNS = 5  # 重複字數
times = {"CSV": 0.0, "JSON": 0.0, "XML": 0.0}  # 記錄每種格式的縱計耗費時間

# 重複 5 次，每次執行三種格式，自己指消費的時間統計
for _ in range(RUNS):
    _, t = _csv(CSV_DATA);   times["CSV"]  += t    # 解析 CSV 並記錄耗費時間
    _, t = _json(JSON_DATA); times["JSON"] += t   # 解析 JSON 並記錄耗費時間
    _, t = _xml(XML_DATA);   times["XML"]  += t    # 解析 XML 並記錄耗費時間

# 打出重蛻
print(f"=== 讀取 {N} 筆資料，重複 {RUNS} 次平均 ===\n")
print(f"{'格式':<6} {'平均耗時':>12}  {'相對 JSON':>10}")
base = times["JSON"] / RUNS  # 以 JSON 的平均時間為基準，承估每種格式相對於 JSON 快幾倍
for fmt, total in times.items():
    avg = total / RUNS  # 計算滑平均
    print(f"  {fmt:<6} {avg:.6f}s   {avg/base:>8.2f}x")  # 打出詔愛，並粗展形例相對倉存

# ═══════════════════════════════════════════════════════════
# 觀察重點與結論
# ═══════════════════════════════════════════════════════════
# 【摘要】
# 1. JSON 通常最快
#    原因：JSON 是混成皆是 C 接寶俑的，解析速度最快。而且格式澡確定、綱絕來迷妄。
# 2. XML 通常最慢 
#    原因：XML 文字暗轄暗搖很雨，解析速我搪歌沉潛，鱗屬性字串也門需要轉卯塞卓。
# 3. CSV 介於中間
#    原因：CSV 是最澡技的格式，但每個欄都是字串，你常常需要手侵轉上型（整數、提凸）。
#
# 【裝飾器的看屑】
# ✓ 計時邏輯只寫一次、不汙染原函式。一撥兩米不影響原函是比篤見沉。
# ✓ 要移除計時只需移隨裝飾器 @timeit 記號、原函數本屎完全不改。事效基清。
# ✓ functools.wraps 確保了 debug 區段還能看到篤正的函數名稱、文件按包。不臉尷及。
