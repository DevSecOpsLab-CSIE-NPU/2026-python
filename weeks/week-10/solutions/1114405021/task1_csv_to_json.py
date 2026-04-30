import csv
import functools
import json
import time
from collections import Counter
from pathlib import Path


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
    """讀取 CSV，回傳所有列的 list"""
    with open(filepath, mode="r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


@timeit
def write_json(data: dict, filepath: str) -> None:
    """將資料寫出為 JSON 檔案"""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def filter_by_admission(rows: list[dict], method: str) -> list[dict]:
    return [row for row in rows if row.get("入學方式") == method]


def count_by_dept(rows: list[dict]) -> dict:
    return dict(Counter(row.get("系所名稱", "") for row in rows if row.get("系所名稱")))


def build_output(rows: list[dict], method: str) -> dict:
    selected = filter_by_admission(rows, method)
    students = [
        {
            "學號": row.get("學號", ""),
            "系所名稱": row.get("系所名稱", ""),
            "畢業學校": row.get("畢業學校", ""),
            "郵遞區號": row.get("郵遞區號", ""),
        }
        for row in selected
    ]

    return {
        "來源": "113年新生資料庫",
        "入學方式篩選": method,
        "總人數": len(selected),
        "系所統計": count_by_dept(selected),
        "學生清單": students,
    }


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    weeks_dir = base_dir.parents[2]
    csv_path = weeks_dir / "week-08" / "in-class" / "stu-data" / "113年新生資料庫.csv"
    if not csv_path.exists():
        csv_path = weeks_dir.parents[0] / "assets" / "stu-data" / "113年新生資料庫.csv"
    output_path = base_dir / "output" / "students.json"

    rows = read_csv(str(csv_path))
    result = build_output(rows, "聯合登記分發")
    write_json(result, str(output_path))
    print(f"JSON 已輸出：{output_path.relative_to(base_dir)}")


if __name__ == "__main__":
    main()
