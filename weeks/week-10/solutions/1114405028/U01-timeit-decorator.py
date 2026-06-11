# U01-timeit-decorator.py
# 完整繁體中文註釋版：示範裝飾器計時與 CSV/JSON/XML 解析速度比較

import csv
import json
import time
import io
import xml.etree.ElementTree as ET
import functools

# ═══════════════════════════════════════════════════════════════════
# Part 1｜問題：每個函式都要手動計時，程式碼重複
# ═══════════════════════════════════════════════════════════════════

def read_csv_raw(data: str) -> list:
    return list(csv.DictReader(io.StringIO(data)))


def read_json_raw(data: str) -> list:
    return json.loads(data)


def read_xml_raw(data: str) -> list:
    root = ET.fromstring(data)
    return [r.attrib for r in root.findall("row")]

# 如果沒有裝飾器，就需要在每個函式呼叫前後手動加上計時程式碼。
# 這樣不但程式碼重複，也容易漏掉或寫錯。

# ═══════════════════════════════════════════════════════════════════
# Part 2｜解法：用裝飾器把計時邏輯包起來
# ═══════════════════════════════════════════════════════════════════

def timeit(func):
    """基礎版裝飾器：在函式執行前後計時並印出耗時。"""
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")
        return result
    return wrapper


def demo():
    """示範函式，用來驗證 wrapper 的 __name__。"""
    pass

wrapped = timeit(demo)
print("未加 wraps 前：", wrapped.__name__)   # wrapper（因為 wrapper 蓋掉原函式名）

# ═══════════════════════════════════════════════════════════════════
# Part 3｜functools.wraps：保留原函式 metadata
# ═══════════════════════════════════════════════════════════════════

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")
        return result
    return wrapper

wrapped = timeit(demo)
print("加 wraps 後：  ", wrapped.__name__)
print()

# ═══════════════════════════════════════════════════════════════════
# Part 4｜實驗：比較 CSV / JSON / XML 解析速度
# ═══════════════════════════════════════════════════════════════════

# 產生測試資料：1000 筆學生資料
N = 1000

csv_buf = io.StringIO()
writer = csv.DictWriter(csv_buf, fieldnames=["id", "name", "score"])
writer.writeheader()
for i in range(N):
    writer.writerow({"id": i, "name": f"Student{i:04d}", "score": 60 + i % 40})
CSV_DATA = csv_buf.getvalue()

JSON_DATA = json.dumps([
    {"id": i, "name": f"Student{i:04d}", "score": 60 + i % 40}
    for i in range(N)
])

xml_rows = "".join(
    f'<row id="{i}" name="Student{i:04d}" score="{60 + i % 40}"/>'
    for i in range(N)
)
XML_DATA = f"<data>{xml_rows}</data>"


# ═══════════════════════════════════════════════════════════════════
# 帶回傳耗時值的 timeit 版本
# ═══════════════════════════════════════════════════════════════════

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
# 1. JSON 解析通常最快，因為內建解析器多為 C 實作。
# 2. XML 解析通常最慢，因為要處理元素、屬性與文字節點。
# 3. CSV 介於中間，格式簡單但欄位都會當成字串處理。
#
# 裝飾器好處：
# - 計時邏輯只寫一次，不需要在每個函式呼叫前後重複寫三行。
# - 如果要移除計時功能，只要拿掉 @timeit 或改成不同包裝器。
# - functools.wraps 可以保留原函式名稱與文件字串，方便除錯與 help()
