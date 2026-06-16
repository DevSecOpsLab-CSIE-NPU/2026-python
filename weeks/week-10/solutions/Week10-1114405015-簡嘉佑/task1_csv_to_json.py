from __future__ import annotations

import csv
import functools
import json
import time
from collections import Counter
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"

DEFAULT_SOURCE = Path(__file__).resolve().parents[4] / "assets" / "stu-data" / "113年新生資料庫.csv"
TARGET_METHOD = "聯合登記分發"

# The real dataset is mojibake encoded; this alias keeps filtering useful data.
METHOD_ALIASES = {
    "聯合登記分發": ["聯合登記分發", "�p�X�n�O���o"],
}


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
    """讀取 CSV，回傳所有列的 list。"""
    rows: list[dict] = []
    with Path(filepath).open(encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)
        for raw in reader:
            if len(raw) < 11:
                continue
            rows.append(
                {
                    "學號": raw[5].strip(),
                    "系所名稱": raw[2].strip(),
                    "入學方式": raw[6].strip(),
                    "郵遞區號": raw[9].strip(),
                    "畢業學校": raw[10].strip(),
                }
            )
    return rows


@timeit
def write_json(data: dict, filepath: str) -> None:
    """將資料寫出為 JSON 檔案。"""
    output_path = Path(filepath)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def filter_by_admission(rows: list[dict], method: str) -> list[dict]:
    return [row for row in rows if row.get("入學方式") == method]


def count_by_dept(rows: list[dict]) -> dict:
    counts = Counter(row.get("系所名稱", "") for row in rows if row.get("系所名稱"))
    return dict(sorted(counts.items(), key=lambda item: (-item[1], item[0])))


def _resolve_filter_method(rows: list[dict], preferred_method: str) -> str:
    aliases = METHOD_ALIASES.get(preferred_method, [preferred_method])
    for candidate in aliases:
        if filter_by_admission(rows, candidate):
            return candidate
    return preferred_method


def build_output_payload(filtered_rows: list[dict], display_method: str) -> dict:
    slim_rows = [
        {
            "學號": row.get("學號", ""),
            "系所名稱": row.get("系所名稱", ""),
            "畢業學校": row.get("畢業學校", ""),
            "郵遞區號": row.get("郵遞區號", ""),
        }
        for row in filtered_rows
    ]
    return {
        "來源": "113年新生資料庫",
        "入學方式篩選": display_method,
        "總人數": len(filtered_rows),
        "系所統計": count_by_dept(filtered_rows),
        "學生清單": slim_rows,
    }


def main() -> None:
    rows = read_csv(str(DEFAULT_SOURCE))
    method_to_use = _resolve_filter_method(rows, TARGET_METHOD)
    filtered = filter_by_admission(rows, method_to_use)
    payload = build_output_payload(filtered, TARGET_METHOD)
    write_json(payload, str(OUTPUT_DIR / "students.json"))
    print(f"已輸出：{OUTPUT_DIR / 'students.json'}")


if __name__ == "__main__":
    main()