# R01-csv-basic.py
# 涵蓋 csv 模組的 reader/writer 與 DictReader/DictWriter

import csv
import os

def demo_standard_csv():
    filename = "data.csv"
    data = [
        ["Name", "Score", "Grade"],
        ["Alice", 95, "A"],
        ["Bob", 82, "B"],
        ["Charlie", 70, "C"]
    ]

    # 寫入 CSV
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    # 讀取 CSV
    print("--- Standard Reader ---")
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def demo_dict_csv():
    filename = "dict_data.csv"
    fieldnames = ["id", "product", "price"]
    items = [
        {"id": 1, "product": "Apple", "price": 30},
        {"id": 2, "product": "Banana", "price": 15},
    ]

    # 寫入 DictWriter
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(items)

    # 讀取 DictReader
    print("\n--- DictReader ---")
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"ID: {row['id']}, 品名: {row['product']}, 價格: {row['price']}")

if __name__ == "__main__":
    print("=== CSV 模組示範 ===")
    demo_standard_csv()
    demo_dict_csv()
    
    # 清理檔案
    for f in ["data.csv", "dict_data.csv"]:
        if os.path.exists(f): os.remove(f)
