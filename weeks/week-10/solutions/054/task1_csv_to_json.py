import csv
import json
import functools
import time
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "..", "..", "..", "assets", "stu-data", "113年新生資料庫.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "output", "students.json")
FILTER_METHOD = "聯合登記分發"


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
    with open(filepath, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def filter_by_admission(rows: list[dict], method: str) -> list[dict]:
    return [r for r in rows if r.get("入學方式") == method]


def count_by_dept(rows: list[dict]) -> dict:
    result = {}
    for r in rows:
        dept = r.get("系所名稱", "未知")
        result[dept] = result.get(dept, 0) + 1
    return result


@timeit
def write_json(data: dict, filepath: str) -> None:
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def build_output(rows: list[dict], method: str) -> dict:
    dept_count = count_by_dept(rows)
    student_list = []
    for r in rows:
        student_list.append({
            "學號": r.get("學號", ""),
            "系所名稱": r.get("系所名稱", ""),
            "畢業學校": r.get("畢業學校", ""),
            "郵遞區號": r.get("郵遞區號", ""),
        })
    return {
        "來源": "113年新生資料庫",
        "入學方式篩選": method,
        "總人數": len(rows),
        "系所統計": dept_count,
        "學生清單": student_list,
    }


def main():
    all_rows = read_csv(DATA_PATH)
    filtered = filter_by_admission(all_rows, FILTER_METHOD)
    output_data = build_output(filtered, FILTER_METHOD)
    write_json(output_data, OUTPUT_PATH)
    print(f"完成！共 {len(filtered)} 位學生資料寫入 {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
