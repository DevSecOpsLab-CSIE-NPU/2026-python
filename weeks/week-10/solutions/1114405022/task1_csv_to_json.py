from __future__ import annotations

import csv
import functools
import json
from collections import Counter
from pathlib import Path
from typing import Any


def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        import time

        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[timeit] {func.__name__} 耗時 {elapsed:.6f}s")
        return result

    return wrapper


@timeit
def read_csv(filepath: str) -> list[dict[str, str]]:
    """讀取 CSV，回傳所有列的 list。"""
    with open(filepath, "r", encoding="utf-8-sig", newline="") as file_object:
        reader = csv.DictReader(file_object)
        return [dict(row) for row in reader]


@timeit
def write_json(data: dict[str, Any], filepath: str) -> None:
    """將資料寫出為 JSON 檔案。"""
    output_path = Path(filepath)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as file_object:
        json.dump(data, file_object, ensure_ascii=False, indent=2)


def filter_by_admission(rows: list[dict[str, str]], method: str) -> list[dict[str, str]]:
    """只保留指定入學方式的學生。"""
    return [row for row in rows if row.get("入學方式") == method]


def count_by_dept(rows: list[dict[str, str]]) -> dict[str, int]:
    """統計各系所人數。"""
    return dict(Counter(row.get("系所名稱", "") for row in rows if row.get("系所名稱")))


def build_summary(rows: list[dict[str, str]], admission_method: str = "聯合登記分發") -> dict[str, Any]:
    """建立 Task 1 的輸出資料結構。"""
    filtered_rows = filter_by_admission(rows, admission_method)
    return {
        "來源": "113年新生資料庫",
        "入學方式篩選": admission_method,
        "總人數": len(filtered_rows),
        "系所統計": count_by_dept(filtered_rows),
        "學生清單": [
            {
                "學號": row.get("學號", ""),
                "系所名稱": row.get("系所名稱", ""),
                "畢業學校": row.get("畢業學校", ""),
                "郵遞區號": row.get("郵遞區號", ""),
            }
            for row in filtered_rows
        ],
    }


def default_input_path() -> Path:
    """回傳課程資料檔的預設路徑。"""
    return Path(__file__).resolve().parents[4] / "week-08" / "in-class" / "stu-data" / "113年新生資料庫.csv"


def default_output_path() -> Path:
    """回傳輸出 JSON 的預設路徑。"""
    return Path(__file__).resolve().parent / "output" / "students.json"


def main() -> None:
    input_path = default_input_path()
    output_path = default_output_path()

    if not input_path.exists():
        raise FileNotFoundError(f"找不到資料檔：{input_path}")

    rows = read_csv(str(input_path))
    summary = build_summary(rows)
    write_json(summary, str(output_path))
    print(f"已輸出：{output_path}")


if __name__ == "__main__":
    main()