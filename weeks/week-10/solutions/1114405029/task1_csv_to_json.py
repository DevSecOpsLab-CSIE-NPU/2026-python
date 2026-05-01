import csv
import json
import time
import functools
from pathlib import Path


ADMISSION_METHOD = "聯合登記分發"


def timeit(func):
    """自訂計時裝飾器，用來量測函式執行時間。"""
    @functools.wraps(func)
    def inner(*args, **kwargs):
        begin = time.perf_counter()
        value = func(*args, **kwargs)
        cost = time.perf_counter() - begin
        print(f"[timeit] {func.__name__} 耗時 {cost:.6f}s")
        return value
    return inner


def get_csv_path() -> Path:
    """取得 CSV 檔案路徑。"""

    project_root = Path(__file__).resolve().parents[4]

    return (
        project_root
        / "assets"
        / "stu-data"
        / "113年新生資料庫.csv"
    )


@timeit
def read_csv(filepath: str) -> list[dict]:
    """讀取 CSV，回傳所有資料列。"""

    with open(filepath, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


@timeit
def write_json(data: dict, filepath: str) -> None:
    """將資料寫出成 JSON 檔案。"""

    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def filter_by_admission(rows: list[dict], method: str) -> list[dict]:
    """依照入學方式篩選學生資料。"""

    return [
        row
        for row in rows
        if row.get("入學方式") == method
    ]


def count_by_dept(rows: list[dict]) -> dict:
    """統計各系所的人數。"""

    result = {}

    for row in rows:
        dept = row.get("系所名稱", "")

        if dept:
            result[dept] = result.get(dept, 0) + 1

    return result


def simplify_students(rows: list[dict]) -> list[dict]:
    """只保留 JSON 需要的欄位。"""

    students = []

    for row in rows:
        students.append({
            "學號": row.get("學號", ""),
            "系所名稱": row.get("系所名稱", ""),
            "畢業學校": row.get("畢業學校", ""),
            "郵遞區號": row.get("郵遞區號", ""),
        })

    return students


def build_output(rows: list[dict]) -> dict:
    """建立輸出的 JSON 結構。"""

    filtered_rows = filter_by_admission(
        rows,
        ADMISSION_METHOD
    )

    return {
        "來源": "113年新生資料庫",
        "入學方式篩選": ADMISSION_METHOD,
        "總人數": len(filtered_rows),
        "系所統計": count_by_dept(filtered_rows),
        "學生清單": simplify_students(filtered_rows),
    }


def main() -> None:
    """主程式。"""

    csv_path = get_csv_path()

    rows = read_csv(str(csv_path))

    data = build_output(rows)

    write_json(
        data,
        "output/students.json"
    )


if __name__ == "__main__":
    main()