import csv
import json
import time
import functools
import os

def timeit(func):
    """計時裝飾器，記錄函式執行時間"""
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
    """讀取 CSV 檔案並回傳字典串列"""
    # 依作業要求使用 utf-8-sig 處理 BOM
    with open(filepath, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        return list(reader)

@timeit
def write_json(data: dict, filepath: str) -> None:
    """將字典資料寫入 JSON 檔案"""
    # 確保輸出目錄存在
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, mode='w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def filter_by_admission(rows: list[dict], method: str) -> list[dict]:
    """根據入學方式過濾資料"""
    return [r for r in rows if r.get("入學方式") == method]

def count_by_dept(rows: list[dict]) -> dict:
    """統計各系所人數"""
    stats = {}
    for r in rows:
        dept = r.get("系所名稱")
        if dept:
            stats[dept] = stats.get(dept, 0) + 1
    return stats

def main():
    # 資料來源路徑
    csv_path = "../../../../assets/stu-data/113年新生資料庫.csv"
    output_path = "output/students.json"

    # 1. 讀取
    print(f"正在讀取資料: {csv_path}")
    all_rows = read_csv(csv_path)

    # 2. 過濾
    target_method = "聯合登記分發"
    filtered_rows = filter_by_admission(all_rows, target_method)
    print(f"篩選條件: {target_method}, 篩選後筆數: {len(filtered_rows)}")

    # 3. 統計
    dept_stats = count_by_dept(filtered_rows)

    # 4. 準備輸出格式
    output_data = {
        "來源": "113年新生資料庫",
        "入學方式篩選": target_method,
        "總人數": len(filtered_rows),
        "系所統計": dept_stats,
        "學生清單": [
            {
                "學號": r.get("學號"),
                "系所名稱": r.get("系所名稱"),
                "畢業學校": r.get("畢業學校"),
                "郵遞區號": r.get("郵遞區號")
            } for r in filtered_rows
        ]
    }

    # 5. 寫出
    write_json(output_data, output_path)
    print(f"資料已成功寫出至: {output_path}")

if __name__ == "__main__":
    main()
