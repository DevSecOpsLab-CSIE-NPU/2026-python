from __future__ import annotations
import csv, functools, json, time
from collections import Counter
from pathlib import Path
from typing import Any

TARGET_ADMISSION = "聯合登記分發"
SOURCE_NAME = "113年新生資料庫"
OUTPUT_FIELDS = ("學號", "系所名稱", "畢業學校", "郵遞區號")

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[timeit] {func.__name__} 耗時 {elapsed:.6f}s")
        return result
    return wrapper

def get_repo_root() -> Path:
    here = Path(__file__).resolve()
    for p in here.parents:
        if (p / "weeks").exists():
            return p
    return here.parents[4]

def find_csv_file() -> Path:
    root = get_repo_root()
    candidates = [
        root / "weeks/week-08/in-class/stu-data/113年新生資料庫.csv",
        root / "weeks/week-08/assets/stu-data/113年新生資料庫.csv",
        root / "weeks/week-08/stu-data/113年新生資料庫.csv",
        root / "weeks/week-13/assets/stu-data/113年新生資料庫.csv",
    ]
    for c in candidates:
        if c.exists():
            return c
    matches = list((root / "weeks").rglob("113年新生資料庫.csv")) or list((root / "weeks").rglob("*113*新生*資料*.csv"))
    if matches:
        return sorted(matches, key=lambda p: len(str(p)))[0]
    raise FileNotFoundError("找不到 113年新生資料庫.csv，請先同步 upstream/main。")

@timeit
def read_csv(filepath: str | Path) -> list[dict[str, str]]:
    with Path(filepath).open("r", encoding="utf-8-sig", newline="") as f:
        return [dict(r) for r in csv.DictReader(f)]

@timeit
def write_json(data: dict[str, Any], filepath: str | Path) -> None:
    p = Path(filepath)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def filter_by_admission(rows: list[dict[str, str]], method: str) -> list[dict[str, str]]:
    return [r for r in rows if str(r.get("入學方式", "")).strip() == method]

def count_by_dept(rows: list[dict[str, str]]) -> dict[str, int]:
    return dict(Counter(str(r.get("系所名稱", "")).strip() for r in rows if str(r.get("系所名稱", "")).strip()))

def simplify_student(row: dict[str, str]) -> dict[str, str]:
    return {k: str(row.get(k, "")).strip() for k in OUTPUT_FIELDS}

def build_output_data(rows: list[dict[str, str]], method: str = TARGET_ADMISSION) -> dict[str, Any]:
    selected = filter_by_admission(rows, method)
    students = [simplify_student(r) for r in selected]
    return {"來源": SOURCE_NAME, "入學方式篩選": method, "總人數": len(students), "系所統計": count_by_dept(selected), "學生清單": students}

def main() -> None:
    base = Path(__file__).resolve().parent
    csv_path = find_csv_file()
    rows = read_csv(csv_path)
    data = build_output_data(rows)
    write_json(data, base / "output/students.json")
    print(f"資料來源：{csv_path}")
    print(f"篩選後總人數：{data['總人數']}")
    print("JSON 已儲存：output/students.json")

if __name__ == "__main__":
    main()
