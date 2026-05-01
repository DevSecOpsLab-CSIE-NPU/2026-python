import csv
import json
import os
import functools
import time

# ── 裝飾器 ────────────────────────────────────────────────────────────────────

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[timeit] {func.__name__} 耗時 {elapsed:.6f}s")
        return result
    return wrapper

# ── 核心函式 ──────────────────────────────────────────────────────────────────

@timeit
def read_csv(filepath: str) -> list[dict]:
    """讀取 CSV，回傳所有列的 list"""
    with open(filepath, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


def filter_by_admission(rows: list[dict], method: str) -> list[dict]:
    """保留指定入學方式的列"""
    return [r for r in rows if r.get("入學方式") == method]


def count_by_dept(rows: list[dict]) -> dict:
    """統計各系所人數"""
    counts: dict[str, int] = {}
    for r in rows:
        dept = r.get("系所名稱", "")
        counts[dept] = counts.get(dept, 0) + 1
    return counts


@timeit
def write_json(data: dict, filepath: str) -> None:
    """將資料寫出為 JSON 檔案"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# ── 主程式 ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.normpath(
        os.path.join(base_dir, "../../../../assets/stu-data/113年新生資料庫.csv")
    )
    json_path = os.path.join(base_dir, "output", "students.json")

    FILTER_METHOD = "聯合登記分發"

    all_rows = read_csv(csv_path)
    filtered = filter_by_admission(all_rows, FILTER_METHOD)
    dept_stats = count_by_dept(filtered)

    student_list = [
        {
            "學號": r["學號"],
            "系所名稱": r["系所名稱"],
            "畢業學校": r["畢業學校"],
            "郵遞區號": r["郵遞區號"],
        }
        for r in filtered
    ]

    output = {
        "來源": "113年新生資料庫",
        "入學方式篩選": FILTER_METHOD,
        "總人數": len(filtered),
        "系所統計": dept_stats,
        "學生清單": student_list,
    }

    write_json(output, json_path)
    print(f"已寫出 {json_path}，共 {len(filtered)} 筆學生資料")
