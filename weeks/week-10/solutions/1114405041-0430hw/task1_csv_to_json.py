from __future__ import annotations

import csv
import functools
import json
import time
from collections import Counter
from pathlib import Path
from typing import Any


ADMISSION_METHOD = "聯合登記分發"


def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[timeit] {func.__name__} 耗時 {elapsed:.6f}s")
        return result

    return wrapper


@timeit
def read_csv(filepath: str) -> list[dict[str, str]]:
    with open(filepath, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return [dict(row) for row in reader]


@timeit
def write_json(data: dict[str, Any], filepath: str) -> None:
    output_path = Path(filepath)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def filter_by_admission(rows: list[dict[str, str]], method: str) -> list[dict[str, str]]:
    return [row for row in rows if row.get("入學方式") == method]


def count_by_dept(rows: list[dict[str, str]]) -> dict[str, int]:
    dept_counter = Counter(row.get("系所名稱", "") for row in rows if row.get("系所名稱"))
    return dict(dept_counter)


def _student_brief(row: dict[str, str]) -> dict[str, str]:
    return {
        "學號": row.get("學號", ""),
        "系所名稱": row.get("系所名稱", ""),
        "畢業學校": row.get("畢業學校", ""),
        "郵遞區號": row.get("郵遞區號", ""),
    }


def build_output(rows: list[dict[str, str]], method: str = ADMISSION_METHOD) -> dict[str, Any]:
    filtered = filter_by_admission(rows, method)
    students = [_student_brief(row) for row in filtered]
    return {
        "來源": "113年新生資料庫",
        "入學方式篩選": method,
        "總人數": len(students),
        "系所統計": count_by_dept(filtered),
        "學生清單": students,
    }


def locate_source_csv() -> Path:
    repo_root = Path(__file__).resolve().parents[4]
    candidates = [
        repo_root / "weeks" / "week-08" / "in-class" / "stu-data" / "113年新生資料庫.csv",
        repo_root / "assets" / "stu-data" / "113年新生資料庫.csv",
        repo_root.parent / "_pr_clean_week10_0430" / "assets" / "stu-data" / "113年新生資料庫.csv",
    ]
    for path in candidates:
        if path.exists():
            return path
    raise FileNotFoundError("找不到 113年新生資料庫.csv，請確認 weeks/week-08/in-class/stu-data/ 路徑是否存在")


def main() -> None:
    source_csv = locate_source_csv()
    output_json = Path(__file__).resolve().parent / "output" / "students.json"
    rows = read_csv(str(source_csv))
    data = build_output(rows, ADMISSION_METHOD)
    write_json(data, str(output_json))
    print(f"已輸出 JSON：{output_json}")


if __name__ == "__main__":
    main()
