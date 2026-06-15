# q_task1_hand.py
# 任務一：讀取 CSV 並篩選輸出（手打版）
# 關鍵：處理 UTF-8-BOM 編碼與 DictReader 欄位匹配

import csv
import os

def solve():
    # 修正路徑陷阱：動態推導 assets 目錄位置
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(base_dir, "../../../../assets/stu-data/113年新生資料庫.csv")
    output_dir = os.path.join(base_dir, "output")
    output_file = os.path.join(output_dir, "113_star.txt")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    count = 0
    results = []

    # 陷阱一：必須使用 utf-8-sig 處理 BOM，否則第一個欄位名稱會包含不可見字元
    with open(input_file, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # 陷阱二：注意欄位名稱必須與 CSV 標題完全一致
            if row['入學方式'] == '繁星推甄':
                results.append(f"{row['系所名稱']} | {row['學號']} | {row['畢業學校']}")
                count += 1

    with open(output_file, mode='w', encoding='utf-8') as f:
        f.write("系所名稱 | 學號 | 畢業學校\n")
        for line in results:
            f.write(line + "\n")
        f.write(f"共 {count} 筆\n")

    print(f"Task 1 完成，共 {count} 筆學生資料。")

if __name__ == "__main__":
    solve()
