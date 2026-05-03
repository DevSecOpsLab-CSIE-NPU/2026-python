"""Task 1：CSV 轉 JSON。

讀取 Week 08 的學生 CSV，篩選出「聯合登記分發」的資料，
再依系所名稱統計人數並輸出為 JSON。
"""

from __future__ import annotations

import csv
import functools
import json
import time
from collections import Counter
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = Path(__file__).resolve().parents[4]
SOURCE_CSV = PROJECT_ROOT / "assets/stu-data/113年新生資料庫.csv"
OUTPUT_JSON = SCRIPT_DIR / "output/students.json"
ADMISSION_METHOD = "聯合登記分發"


def timeit(func):
    """計算函式執行時間並印出結果。"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[timeit] {func.__name__} 耗時 {elapsed:.6f}s")
        return result

    return wrapper


@timeit
def read_csv(filepath: str) -> list[dict]:
    """讀取 CSV，回傳所有列的 list。"""

    with open(filepath, encoding="utf-8-sig", newline="") as file_handle:
        return list(csv.DictReader(file_handle))


def filter_by_admission(rows: list[dict], method: str) -> list[dict]:
    """保留入學方式符合指定條件的資料列。"""

    return [row for row in rows if row.get("入學方式") == method]


def count_by_dept(rows: list[dict]) -> dict:
    """統計每個系所的學生人數。"""

    counter = Counter()
    for row in rows:
        dept = row.get("系所名稱", "")
        if dept:
            counter[dept] += 1
    return dict(counter)


@timeit
def write_json(data: dict, filepath: str) -> None:
    """將資料寫出為 JSON 檔案。"""

    output_path = Path(filepath)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as file_handle:
        json.dump(data, file_handle, ensure_ascii=False, indent=2)


def build_json_data(rows: list[dict]) -> dict:
    """將篩選結果整理為作業要求的 JSON 結構。"""

    filtered_rows = filter_by_admission(rows, ADMISSION_METHOD)
    students = [
        {
            "學號": row.get("學號", ""),
            "系所名稱": row.get("系所名稱", ""),
            "畢業學校": row.get("畢業學校", ""),
            "郵遞區號": row.get("郵遞區號", ""),
        }
        for row in filtered_rows
    ]
    return {
        "來源": SOURCE_CSV.stem,
        "入學方式篩選": ADMISSION_METHOD,
        "總人數": len(students),
        "系所統計": count_by_dept(filtered_rows),
        "學生清單": students,
    }


def main() -> None:
    """執行 Task 1 的完整轉換流程。"""

    rows = read_csv(str(SOURCE_CSV))
    data = build_json_data(rows)
    write_json(data, str(OUTPUT_JSON))
    print(f"JSON 已儲存：{OUTPUT_JSON.relative_to(SCRIPT_DIR)}")


if __name__ == "__main__":
    main()