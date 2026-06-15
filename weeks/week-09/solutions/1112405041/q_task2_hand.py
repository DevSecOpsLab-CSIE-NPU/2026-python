# q_task2_hand.py
# 任務二：安全建立報告檔（不覆蓋既有檔案）
# 關鍵：使用 'x' 模式防止覆蓋並正確捕捉異常

import csv
import os
from collections import Counter

def safe_report(year):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(base_dir, f"../../../../assets/stu-data/{year}年新生資料庫.csv")
    output_file = os.path.join(base_dir, f"output/{year}_report.txt")

    if not os.path.exists(input_file):
        print(f"❌ 錯誤：找不到 {year} 年的原始資料。")
        return

    # 1. 讀取並統計
    admission_counts = Counter()
    with open(input_file, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            admission_counts[row['入學方式']] += 1

    # 2. 嘗試寫入 (使用 'x' 模式)
    try:
        # 陷阱：'x' 模式若檔案已存在會拋出 FileExistsError
        with open(output_file, mode='x', encoding='utf-8') as f:
            f.write(f"{year} 學年度 入學方式統計\n")
            f.write("-" * 30 + "\n")
            for mode, count in admission_counts.most_common():
                f.write(f"{mode}: {count} 人\n")
        print(f"{year} 年報告已建立：output/{year}_report.txt")
    except FileExistsError:
        print(f"⚠️  output/{year}_report.txt 已存在，略過。")

def solve():
    # 依序呼叫
    safe_report(109)
    safe_report(110)
    safe_report(114)
    safe_report(109)   # 第二次呼叫，應觸發警告

if __name__ == "__main__":
    solve()
