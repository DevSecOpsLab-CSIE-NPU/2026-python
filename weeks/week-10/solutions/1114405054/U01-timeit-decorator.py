# U01. 計時裝飾器實作與資料格式速度比較（6.1 / 6.2 / 6.3）
# 這份版本保留原本的示範流程，並補上更完整的繁體中文註解說明。
#
# 主題重點：
# 1. 先看到「每個函式都手動計時」會造成重複程式碼
# 2. 再用裝飾器把計時邏輯抽出來
# 3. 最後比較 CSV / JSON / XML 三種格式的讀取速度

import csv
import functools
import io
import json
import time
import xml.etree.ElementTree as ET

# ═══════════════════════════════════════════════════════════
# Part 1｜問題：每個函式都要手動計時 → 大量重複
# ═══════════════════════════════════════════════════════════


def read_csv_raw(data: str) -> list:
    # csv.DictReader 會把每一列轉成字典，欄名來自第一列標題。
    return list(csv.DictReader(io.StringIO(data)))


def read_json_raw(data: str) -> list:
    # json.loads 直接把 JSON 字串轉成 Python 物件。
    return json.loads(data)


def read_xml_raw(data: str) -> list:
    # 先把 XML 字串解析成樹狀結構，再把每個 row 的屬性取出來。
    root = ET.fromstring(data)
    return [r.attrib for r in root.findall("row")]


# 沒有裝飾器：每次都要複製貼上計時程式碼 ↓
# start = time.perf_counter()
# result = read_csv_raw(data)
# print(f"read_csv_raw 耗時 {time.perf_counter() - start:.6f}s")

# ═══════════════════════════════════════════════════════════
# Part 2｜解法：裝飾器把計時邏輯包起來，一次定義，到處復用
# ═══════════════════════════════════════════════════════════


def timeit(func):
    """基礎版：在呼叫前後計時，印出耗時。"""

    def wrapper(*args, **kwargs):
        # 裝飾器本體不改變原函式的功能，只是在前後加上計時邏輯。
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f" {func.__name__:<20s} {elapsed:.6f}s")
        return result

    return wrapper


# 問題：wrapper 蓋掉了原函式的 __name__ / __doc__。
# 這會讓除錯、help()、日誌輸出時看到的名字不正確。

def demo():
    """這是 demo 的說明文字"""
    pass


wrapped = timeit(demo)
print("未加 wraps 前：", wrapped.__name__) # wrapper（錯誤！）


# ── Part 3｜functools.wraps：保留原函式的 metadata ──────────


def timeit(func):
    # wraps 會把原函式名稱、註解、模組資訊等 metadata 複製到 wrapper。
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f" {func.__name__:<20s} {elapsed:.6f}s")
        return result

    return wrapper


wrapped = timeit(demo)
print("加 wraps 後： ", wrapped.__name__) # demo（正確）
print()


# ═══════════════════════════════════════════════════════════
# Part 4｜實驗：相同資料，CSV vs JSON vs XML 速度比較
# ═══════════════════════════════════════════════════════════


# ── 產生測試資料（1000 筆學生記錄）────────────────────────
N = 1000

# CSV 格式：用 DictWriter 寫出標題與每列資料。
csv_buf = io.StringIO()
writer = csv.DictWriter(csv_buf, fieldnames=["id", "name", "score"])
writer.writeheader()
for i in range(N):
    writer.writerow({"id": i, "name": f"Student{i:04d}", "score": 60 + i % 40})
CSV_DATA = csv_buf.getvalue()

# JSON 格式：直接把 Python list/dict 轉成 JSON 字串。
JSON_DATA = json.dumps(
    [
        {"id": i, "name": f"Student{i:04d}", "score": 60 + i % 40}
        for i in range(N)
    ]
)

# XML 格式：手動組成一串 row 標籤。
xml_rows = "".join(
    f'<row id="{i}" name="Student{i:04d}" score="{60 + i % 40}"/>'
    for i in range(N)
)
XML_DATA = f"<data>{xml_rows}</data>"


# ── 帶回傳耗時的計時包裝 ─────────────────────────────────
# 這個版本的裝飾器會回傳 (result, elapsed)，方便後面做平均統計。

def timeit_silent(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        return result, time.perf_counter() - start

    return wrapper


_csv = timeit_silent(read_csv_raw)
_json = timeit_silent(read_json_raw)
_xml = timeit_silent(read_xml_raw)


# ── 執行比較（重複 5 次取平均，排除冷啟動影響）────────────
RUNS = 5
times = {"CSV": 0.0, "JSON": 0.0, "XML": 0.0}

for _ in range(RUNS):
    _, t = _csv(CSV_DATA)
    times["CSV"] += t

    _, t = _json(JSON_DATA)
    times["JSON"] += t

    _, t = _xml(XML_DATA)
    times["XML"] += t

print(f"=== 讀取 {N} 筆資料，重複 {RUNS} 次平均 ===\n")
print(f"{'格式':<6} {'平均耗時':>12} {'相對 JSON':>10}")
base = times["JSON"] / RUNS
for fmt, total in times.items():
    avg = total / RUNS
    print(f" {fmt:<6} {avg:.6f}s {avg/base:>8.2f}x")


# ═══════════════════════════════════════════════════════════
# 觀察重點
# ═══════════════════════════════════════════════════════════
# 1. JSON 通常最快（原生 C 實作的解析器）
# 2. XML 通常最慢（文字解析開銷大，屬性字串轉換）
# 3. CSV 介於中間（簡單格式，但每欄都是字串需自行轉型）
#
# 裝飾器帶來的好處：
# - 計時邏輯只寫一次，不汙染原函式
# - 要移除計時只需拿掉 @timeit，函式本身不需修改
# - functools.wraps 確保 debug / help() 時能看到正確名稱
