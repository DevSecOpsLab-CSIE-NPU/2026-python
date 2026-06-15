# q_task1_easy.py
# [AI 教學版] 任務一：讀取 CSV 並篩選輸出
# 此版本側重於「易於理解與記憶」的標準 API 用法

import csv
import os

def solve():
    # 使用動態路徑，避免不同電腦環境下的 FileNotFoundError
    current_dir = os.path.dirname(__file__)
    # 這裡的路徑是根據專案結構推導的
    src_csv = os.path.join(current_dir, "../../../../assets/stu-data/113年新生資料庫.csv")
    out_dir = os.path.join(current_dir, "output")
    out_txt = os.path.join(out_dir, "113_star.txt")

    # 確保輸出目錄存在
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # 關鍵點：使用 'utf-8-sig' 來處理 Excel 產生的 BOM
    # 這是 Professor August 的常見魔改陷阱！
    with open(src_csv, mode='r', encoding='utf-8-sig') as f:
        # DictReader 會自動將第一行轉為 Key
        reader = csv.DictReader(f)

        # 篩選繁星推甄
        star_students = [
            f"{row['系所名稱']} | {row['學號']} | {row['畢業學校']}"
            for row in reader
            if row['入學方式'] == '繁星推甄'
        ]

    # 寫入結果
    with open(out_txt, mode='w', encoding='utf-8') as f:
        f.write("系所名稱 | 學號 | 畢業學校\n")
        f.write("\n".join(star_students) + "\n")
        f.write(f"共 {len(star_students)} 筆\n")

    print(f"Task 1 (Easy) 完成，共 {len(star_students)} 筆。")

if __name__ == "__main__":
    solve()
