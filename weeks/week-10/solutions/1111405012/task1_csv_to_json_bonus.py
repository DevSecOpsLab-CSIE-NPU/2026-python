from collections import Counter
from pathlib import Path

from task1_csv_to_json import (
    ADMISSION_METHOD,
    SOLUTION_DIR,
    build_output,
    find_csv_path,
    read_csv,
    timeit,
    write_json,
)


BONUS_JSON_PATH = SOLUTION_DIR / "output" / "students_bonus.json"


def rank_departments(dept_counts: dict[str, int]) -> list[dict]:
    sorted_items = sorted(dept_counts.items(), key=lambda item: (-item[1], item[0]))
    return [
        {"名次": index, "系所名稱": dept, "人數": count}
        for index, (dept, count) in enumerate(sorted_items, start=1)
    ]


def count_admission_methods(rows: list[dict]) -> dict:
    counts = Counter(row.get("入學方式", "未填寫") or "未填寫" for row in rows)
    return dict(sorted(counts.items(), key=lambda item: (-item[1], item[0])))


def build_bonus_output(rows: list[dict], method: str = ADMISSION_METHOD) -> dict:
    data = build_output(rows, method)
    total_rows = len(rows)
    selected_count = data["總人數"]
    dept_ranking = rank_departments(data["系所統計"])
    top_dept = dept_ranking[0] if dept_ranking else {"系所名稱": "無", "人數": 0}
    selected_ratio = selected_count / total_rows if total_rows else 0

    data["加分摘要"] = {
        "全部資料筆數": total_rows,
        "篩選後筆數": selected_count,
        "篩選比例": f"{selected_ratio:.2%}",
        "系所數量": len(data["系所統計"]),
        "最多學生系所": top_dept["系所名稱"],
        "最多學生系所人數": top_dept["人數"],
    }
    data["系所排名"] = dept_ranking
    data["全部入學方式統計"] = count_admission_methods(rows)
    return data


@timeit
def write_bonus_json(data: dict, filepath: str | Path = BONUS_JSON_PATH) -> None:
    write_json(data, filepath)


def main() -> None:
    rows = read_csv(find_csv_path())
    data = build_bonus_output(rows)
    write_bonus_json(data)
    print(f"加分 JSON 已儲存：{BONUS_JSON_PATH.relative_to(SOLUTION_DIR)}")


if __name__ == "__main__":
    main()
