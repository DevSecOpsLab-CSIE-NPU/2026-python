import csv
import functools
import json
import time
from collections import Counter
from pathlib import Path


SOLUTION_DIR = Path(__file__).resolve().parent
REPO_ROOT = SOLUTION_DIR.parents[3]
SOURCE_NAME = "113年新生資料庫"
ADMISSION_METHOD = "聯合登記分發"
OUTPUT_FIELDS = ("學號", "系所名稱", "畢業學校", "郵遞區號")
CSV_PATH = REPO_ROOT / "assets/stu-data/113年新生資料庫.csv"


def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[timeit] {func.__name__} 耗時 {elapsed:.6f}s")
        return result

    return wrapper


def find_csv_path() -> Path:
    if CSV_PATH.exists():
        return CSV_PATH
    raise FileNotFoundError(f"找不到 113 年新生資料庫 CSV：{CSV_PATH}")


@timeit
def read_csv(filepath: str | Path) -> list[dict]:
    with open(filepath, "r", encoding="utf-8-sig", newline="") as csv_file:
        return list(csv.DictReader(csv_file))


@timeit
def write_json(data: dict, filepath: str | Path) -> None:
    output_path = Path(filepath)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)


def filter_by_admission(rows: list[dict], method: str) -> list[dict]:
    return [row for row in rows if row.get("入學方式") == method]


def count_by_dept(rows: list[dict]) -> dict:
    counts = Counter(row.get("系所名稱", "") for row in rows if row.get("系所名稱"))
    return dict(sorted(counts.items()))


def build_student_record(row: dict) -> dict:
    return {field: row.get(field, "") for field in OUTPUT_FIELDS}


def build_output(rows: list[dict], method: str = ADMISSION_METHOD) -> dict:
    filtered_rows = filter_by_admission(rows, method)
    student_list = [build_student_record(row) for row in filtered_rows]
    return {
        "來源": SOURCE_NAME,
        "入學方式篩選": method,
        "總人數": len(student_list),
        "系所統計": count_by_dept(filtered_rows),
        "學生清單": student_list,
    }


def main() -> None:
    csv_path = find_csv_path()
    output_path = SOLUTION_DIR / "output" / "students.json"
    rows = read_csv(csv_path)
    data = build_output(rows)
    write_json(data, output_path)
    print(f"JSON 已儲存：{output_path.relative_to(SOLUTION_DIR)}")


if __name__ == "__main__":
    main()
