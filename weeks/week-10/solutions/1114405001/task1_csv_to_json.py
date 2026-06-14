import csv
import functools
import json
import time
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
DATA_PATH = HERE.parent.parent.parent.parent / "assets" / "stu-data" / "113年新生資料庫.csv"
OUTPUT_DIR = HERE / "output"
OUTPUT_JSON = OUTPUT_DIR / "students.json"
TARGET_METHOD = "聯合登記分發"


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
    with open(filepath, "r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


@timeit
def write_json(data: dict, filepath: str) -> None:
    out_path = Path(filepath)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def filter_by_admission(rows: list[dict], method: str) -> list[dict]:
    return [row for row in rows if row.get("入學方式") == method]


def count_by_dept(rows: list[dict]) -> dict:
    counter = Counter(row.get("系所名稱", "") for row in rows if row.get("系所名稱"))
    return dict(counter)


def select_student_fields(rows: list[dict]) -> list[dict]:
    picked = []
    for row in rows:
        picked.append(
            {
                "學號": row.get("學號", ""),
                "系所名稱": row.get("系所名稱", ""),
                "畢業學校": row.get("畢業學校", ""),
                "郵遞區號": row.get("郵遞區號", ""),
            }
        )
    return picked


def build_output(rows: list[dict], method: str) -> dict:
    filtered = filter_by_admission(rows, method)
    students = select_student_fields(filtered)
    summary = count_by_dept(filtered)
    return {
        "來源": "113年新生資料庫",
        "入學方式篩選": method,
        "總人數": len(filtered),
        "系所統計": summary,
        "學生清單": students,
    }


def main() -> None:
    rows = read_csv(str(DATA_PATH))
    data = build_output(rows, TARGET_METHOD)
    write_json(data, str(OUTPUT_JSON))
    print(f"已輸出：{OUTPUT_JSON}")


if __name__ == "__main__":
    main()
