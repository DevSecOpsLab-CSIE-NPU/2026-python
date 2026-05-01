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
    with open(filepath, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


@timeit
def write_json(data: dict, filepath: str) -> None:
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def filter_by_admission(rows: list[dict], method: str) -> list[dict]:
    return [r for r in rows if r.get("入學方式") == method]


def count_by_dept(rows: list[dict]) -> dict:
    counts: dict[str, int] = {}
    for r in rows:
        dept = r.get("系所名稱", "未知")
        counts[dept] = counts.get(dept, 0) + 1
    return counts


def main():
    csv_path = os.path.join(
        os.path.dirname(__file__),
        "..", "..", "..", "week-08", "in-class", "stu-data", "113年新生資料庫.csv",
    )
    csv_path = os.path.normpath(csv_path)

    rows = read_csv(csv_path)

    filtered = filter_by_admission(rows, "聯合登記分發")
    dept_stats = count_by_dept(filtered)

    student_list = [
        {
            "學號": s["學號"],
            "系所名稱": s["系所名稱"],
            "畢業學校": s["畢業學校"],
            "郵遞區號": s["郵遞區號"],
        }
        for s in filtered
    ]

    output = {
        "來源": "113年新生資料庫",
        "入學方式篩選": "聯合登記分發",
        "總人數": len(student_list),
        "系所統計": dept_stats,
        "學生清單": student_list,
    }

    output_path = os.path.join(os.path.dirname(__file__), "output", "students.json")
    write_json(output, output_path)
    print(f"已寫入 {len(student_list)} 筆學生資料至 {output_path}")


if __name__ == "__main__":
    main()
