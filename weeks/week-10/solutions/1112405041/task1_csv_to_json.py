import csv
import json
import os
import functools
import time

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
def read_csv(filepath: str) -> list[dict]:
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        return list(reader)

def filter_by_admission(rows: list[dict], method: str) -> list[dict]:
    return [r for r in rows if r.get("入學方式") == method]

def count_by_dept(rows: list[dict]) -> dict:
    if not isinstance(rows, list):
        raise TypeError("rows 必須是 list")
    result = {}
    for r in rows:
        if not isinstance(r, dict):
            raise TypeError("rows 中的每一筆必須是 dict")
        dept = r.get("系所名稱")
        if dept is not None:
            result[dept] = result.get(dept, 0) + 1
    return result

@timeit
def write_json(data: dict, filepath: str) -> None:
    d = os.path.dirname(filepath)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    from pathlib import Path
    DATA_FILE = Path(__file__).parent.parent.parent.parent.parent / "assets" / "stu-data" / "113年新生資料庫.csv"
    rows = read_csv(str(DATA_FILE))
    filtered = filter_by_admission(rows, "聯合登記分發")
    dept_count = count_by_dept(filtered)
    output = {
        "來源": "113年新生資料庫",
        "入學方式篩選": "聯合登記分發",
        "總人數": len(filtered),
        "系所統計": dept_count,
        "學生清單": [
            {"學號": s.get("學號"), "系所名稱": s.get("系所名稱"),
             "畢業學校": s.get("畢業學校"), "郵遞區號": s.get("郵遞區號")}
            for s in filtered
        ]
    }
    write_json(output, "students.json")
