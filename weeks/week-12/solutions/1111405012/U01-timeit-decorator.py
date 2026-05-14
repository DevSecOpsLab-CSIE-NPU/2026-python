"""U01. 計時裝飾器實作與資料格式速度比較。"""

from __future__ import annotations

import csv
import functools
import io
import json
import time
import xml.etree.ElementTree as ET


def read_csv_raw(data: str) -> list[dict[str, str]]:
    """把 CSV 文字讀成 list[dict]。"""
    return list(csv.DictReader(io.StringIO(data)))


def read_json_raw(data: str) -> list[dict[str, object]]:
    """把 JSON 文字讀成 Python 物件。"""
    return json.loads(data)


def read_xml_raw(data: str) -> list[dict[str, str]]:
    """把 XML 文字讀成屬性字典列表。"""
    root = ET.fromstring(data)
    return [dict(row.attrib) for row in root.findall("row")]


def naive_timeit(func):
    """示範沒用 wraps 時，函式名稱會被 wrapper 蓋掉。"""

    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")
        return result

    return wrapper


def timeit(func):
    """正式版計時裝飾器：保留原函式名稱與說明。"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")
        return result

    return wrapper


def timeit_silent(func):
    """回傳結果與耗時，不直接印出，方便做平均比較。"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        return result, elapsed

    return wrapper


def build_sample_datasets(count: int) -> tuple[str, str, str]:
    """建立相同內容的 CSV / JSON / XML 測試資料。"""
    csv_buffer = io.StringIO(newline="")
    writer = csv.DictWriter(csv_buffer, fieldnames=["id", "name", "score"])
    writer.writeheader()
    for index in range(count):
        writer.writerow(
            {"id": index, "name": f"Student{index:04d}", "score": 60 + index % 40}
        )
    csv_data = csv_buffer.getvalue()

    json_data = json.dumps(
        [
            {"id": index, "name": f"Student{index:04d}", "score": 60 + index % 40}
            for index in range(count)
        ]
    )

    xml_rows = "".join(
        f'<row id="{index}" name="Student{index:04d}" score="{60 + index % 40}"/>'
        for index in range(count)
    )
    xml_data = f"<data>{xml_rows}</data>"
    return csv_data, json_data, xml_data


def benchmark_readers(csv_data: str, json_data: str, xml_data: str, runs: int = 5) -> dict[str, float]:
    """重複執行三種讀取方式，回傳平均耗時。"""
    timed_readers = {
        "CSV": timeit_silent(read_csv_raw),
        "JSON": timeit_silent(read_json_raw),
        "XML": timeit_silent(read_xml_raw),
    }
    payloads = {"CSV": csv_data, "JSON": json_data, "XML": xml_data}
    totals = {"CSV": 0.0, "JSON": 0.0, "XML": 0.0}

    for _ in range(runs):
        for name, reader in timed_readers.items():
            _, elapsed = reader(payloads[name])
            totals[name] += elapsed

    return {name: total / runs for name, total in totals.items()}


def main() -> None:
    """印出課堂上示範的裝飾器與速度比較結果。"""

    def demo():
        """這是 demo 的說明文字。"""

    wrapped = naive_timeit(demo)
    print("未加 wraps 前：", wrapped.__name__)

    wrapped = timeit(demo)
    print("加 wraps 後：  ", wrapped.__name__)
    print()

    sample_count = 1000
    runs = 5
    csv_data, json_data, xml_data = build_sample_datasets(sample_count)
    averages = benchmark_readers(csv_data, json_data, xml_data, runs=runs)

    print(f"=== 讀取 {sample_count} 筆資料，重複 {runs} 次平均 ===\n")
    print(f"{'格式':<6} {'平均耗時':>12}  {'相對 JSON':>10}")

    base = averages["JSON"] if averages["JSON"] > 0 else 1e-12
    for name, average in averages.items():
        print(f"  {name:<6} {average:.6f}s   {average / base:>8.2f}x")

    print("\n# 觀察重點")
    print("# 1. JSON 通常很快，因為標準函式庫有成熟的解析器。")
    print("# 2. XML 結構最重，解析成本通常較高。")
    print("# 3. CSV 結構簡單，但欄位進來時都是字串，常要再轉型。")


if __name__ == "__main__":
    main()
