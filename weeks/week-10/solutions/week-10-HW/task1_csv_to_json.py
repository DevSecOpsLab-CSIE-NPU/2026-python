import csv
import json
import functools
import time
import os

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
    with open(filepath, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        return list(reader)

def filter_by_admission(rows: list[dict], method: str) -> list[dict]:
    """只保留指定的入學方式"""
    return [r for r in rows if r.get("入學方式") == method]

def count_by_dept(rows: list[dict]) -> dict:
    """計算各系所的人數"""
    stats = {}
    for r in rows:
        dept = r.get("系所名稱")
        stats[dept] = stats.get(dept, 0) + 1
    return stats

@timeit
def write_json(data: dict, filepath: str) -> None:
    """將資料寫出為 JSON 檔案"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, mode='w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    filepath = "../../../../assets/stu-data/113年新生資料庫.csv"
    method = "聯合登記分發"
    
    # 1. 讀取並過濾
    rows = read_csv(filepath)
    filtered_rows = filter_by_admission(rows, method)
    
    # 2. 統計
    dept_stats = count_by_dept(filtered_rows)
    
    # 確保輸出的 key 是對應的
    student_list = []
    for r in filtered_rows:
        student_list.append({
            "學號": r.get("學號"),
            "系所名稱": r.get("系所名稱"),
            "畢業學校": r.get("畢業學校"),
            "郵遞區號": r.get("郵遞區號")
        })
        
    data = {
        "來源": "113年新生資料庫",
        "入學方式篩選": method,
        "總人數": len(filtered_rows),
        "系所統計": dept_stats,
        "學生清單": student_list
    }
    
    # 3. 輸出 JSON
    write_json(data, "output/students.json")

if __name__ == '__main__':
    main()
