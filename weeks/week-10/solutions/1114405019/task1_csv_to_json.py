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

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.normpath(os.path.join(BASE_DIR, '..', '..', '..', '..', 'assets', 'stu-data', '113年新生資料庫.csv'))
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')
JSON_PATH = os.path.join(OUTPUT_DIR, 'students.json')


@timeit
def read_csv(filepath: str) -> list[dict]:
    """讀取 CSV，回傳所有列的 list"""
    with open(filepath, encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))


@timeit
def write_json(data: dict, filepath: str) -> None:
    """將資料寫出為 JSON 檔案"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def filter_by_admission(rows: list[dict], method: str) -> list[dict]:
    return [r for r in rows if r.get('入學方式') == method]


def count_by_dept(rows: list[dict]) -> dict:
    counts: dict[str, int] = {}
    for r in rows:
        dept = r.get('系所名稱', '')
        counts[dept] = counts.get(dept, 0) + 1
    return counts


if __name__ == '__main__':
    rows = read_csv(CSV_PATH)
    filtered = filter_by_admission(rows, '聯合登記分發')
    dept_counts = count_by_dept(filtered)

    output = {
        '來源': '113年新生資料庫',
        '入學方式篩選': '聯合登記分發',
        '總人數': len(filtered),
        '系所統計': dept_counts,
        '學生清單': [
            {
                '學號': r['學號'],
                '系所名稱': r['系所名稱'],
                '畢業學校': r['畢業學校'],
                '郵遞區號': r['郵遞區號'],
            }
            for r in filtered
        ],
    }

    write_json(output, JSON_PATH)
    print(f'已輸出 {len(filtered)} 筆學生資料至 {JSON_PATH}')
