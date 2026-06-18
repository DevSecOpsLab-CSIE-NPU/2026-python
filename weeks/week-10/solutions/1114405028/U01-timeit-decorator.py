# U01. 計時裝飾器實作與資料格式速度比較
# 這個版本加上更完整的繁體中文註解，說明裝飾器與 CSV/JSON/XML 的比較。

import csv
import json
import time
import io
import xml.etree.ElementTree as ET
import functools


def read_csv_raw(data: str) -> list:
    """直接把 CSV 字串讀成 dict 列表。"""
    return list(csv.DictReader(io.StringIO(data)))


def read_json_raw(data: str) -> list:
    """直接把 JSON 字串解析成 Python 物件。"""
    return json.loads(data)


def read_xml_raw(data: str) -> list:
    """把 XML 字串解析成 ET 物件，並取出每個 row 的屬性。"""
    root = ET.fromstring(data)
    return [r.attrib for r in root.findall("row")]


# 這裡展示使用裝飾器之前的問題：每個函式都要複製計時程式碼。
# 下面的 timeit() 把計時邏輯封裝成可重複使用的裝飾器。

def timeit(func):
    """簡單的計時裝飾器，印出呼叫耗時。"""
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")
        return result
    return wrapper


def demo():
    """示範函式，用來檢查 functools.wraps 是否保留 metadata。"""
    pass

wrapped = timeit(demo)
print("未加 wraps 前：", wrapped.__name__)


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

# 產生 1000 筆測試資料，用於比較 CSV、JSON、XML 的讀取速度。
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


def timeit_silent(func):
    """回傳函式結果與耗時，不直接印出。"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        return result, time.perf_counter() - start
    return wrapper

_csv  = timeit_silent(read_csv_raw)
_json = timeit_silent(read_json_raw)
_xml  = timeit_silent(read_xml_raw)

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

# 觀察重點：
# 1) JSON 解析通常最快，因為 Python 內建 C 實作。
# 2) XML 解析較慢，因為字串與節點解析開銷大。
# 3) CSV 速度介於其中，雖然格式簡單但每行要分隔與轉型。
# 4) 裝飾器可以把額外邏輯抽離，不必讓主要函式變得複雜。
