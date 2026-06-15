# q_task2_easy.py
# [AI 教學版] 任務二：安全建立報告檔
# 核心：理解 Python 的 'x' 檔案模式與異常處理

import csv
import os
from collections import Counter

def safe_report(year):
    curr_dir = os.path.dirname(__file__)
    src = os.path.join(curr_dir, f"../../../../assets/stu-data/{year}年新生資料庫.csv")
    dst = os.path.join(curr_dir, f"output/{year}_report.txt")

    # 1. 讀取並使用 Counter 進行高效統計
    with open(src, 'r', encoding='utf-8-sig') as f:
        data = list(csv.DictReader(f))
        counts = Counter(row['入學方式'] for row in data)

    # 2. 'x' 模式：這是 Professor August 用來測試你有沒有看 5.5 節的標準
    try:
        with open(dst, 'x', encoding='utf-8') as f:
            f.write(f"{year} 學年度統計\n")
            for mode, n in counts.most_common():
                f.write(f"{mode}: {n} 人\n")
        print(f"{year} 年報告已建立")
    except FileExistsError:
        # 如果檔案已經在那裡，'x' 會報錯，我們在這裡優雅地捕捉它
        print(f"⚠️  {dst} 已存在，略過。")

def solve():
    # 測試流程
    for y in [109, 110, 114, 109]:
        safe_report(y)

if __name__ == "__main__":
    solve()
