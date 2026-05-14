"""U01. 計時裝飾器實作與資料格式速度比較。

這份版本示範：
1. 為什麼重複計時程式碼不好維護。
2. 如何用裝飾器把計時邏輯抽出來。
3. csv、json、xml 三種格式在讀取上的簡單比較。
"""

import csv
import functools
import io
import json
import time
import xml.etree.ElementTree as ET


# 如果每個函式都要手動寫計時程式碼，會出現大量重複。
def read_csv_raw(data: str) -> list:
    return list(csv.DictReader(io.StringIO(data)))


def read_json_raw(data: str) -> list:
    return json.loads(data)


def read_xml_raw(data: str) -> list:
    root = ET.fromstring(data)
    return [r.attrib for r in root.findall("row")]


# 基礎版 timeit 裝飾器。
def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")
        return result

    return wrapper


# 先示範沒有 wraps 時，函式名稱會被 wrapper 蓋掉。
def demo():
    """這是 demo 的說明文字。"""
    pass


wrapped = timeit(demo)
print("未加 wraps 前：", wrapped.__name__)


# functools.wraps 可以保留原函式名稱與說明文字。
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


# 產生測試資料。
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


# 帶回傳耗時的版本，方便做平均比較。
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
    _, t = _csv(CSV_DATA)
    times["CSV"] += t
    _, t = _json(JSON_DATA)
    times["JSON"] += t
    _, t = _xml(XML_DATA)
    times["XML"] += t

print(f"=== 讀取 {N} 筆資料，重複 {RUNS} 次平均 ===\n")
print(f"{'格式':<6} {'平均耗時':>12}  {'相對 JSON':>10}")
base = times["JSON"] / RUNS
for fmt, total in times.items():
    avg = total / RUNS
    print(f"  {fmt:<6} {avg:.6f}s   {avg / base:>8.2f}x")
