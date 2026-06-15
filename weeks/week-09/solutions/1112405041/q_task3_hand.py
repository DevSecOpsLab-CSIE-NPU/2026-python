# q_task3_hand.py
# 題目三：用 StringIO 做資料清洗測試
# 關鍵：利用 Duck Typing 實現類檔案物件的單元測試

import csv
import io
import os

def parse_students(file_obj):
    """
    接受任何類檔案物件（File-like object），回傳學生列表。
    這展現了 Duck Typing 的優勢：函式不關心對象是硬碟檔案還是記憶體字串流。
    """
    reader = csv.DictReader(file_obj)
    return list(reader)

def solve():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    real_file_path = os.path.join(base_dir, "../../../../assets/stu-data/114年新生資料庫.csv")

    # 1. 測試真實檔案
    print("--- 真實檔案測試 (114年) ---")
    with open(real_file_path, mode='r', encoding='utf-8-sig') as f:
        students = parse_students(f)
        for s in students[:3]:
            print(f"學號: {s['學號']}, 系所: {s['系所名稱']}")

    # 2. 測試 StringIO (模擬 AI 幻覺與邊界條件)
    print("\n--- StringIO 記憶體測試 ---")
    test_data = """序,學校名稱,系所名稱,學號,入學方式
1,測試大學,資工系,A001,甄選入學
2,測試大學,電機系,A002,繁星推甄"""

    # 陷阱：StringIO 裡面不需要 encoding='utf-8-sig'，因為它是處理 python str
    string_stream = io.StringIO(test_data)
    mock_students = parse_students(string_stream)
    for s in mock_students:
        print(f"解析成功 -> {s['學號']}: {s['入學方式']}")

    # 思考回答：
    # 接受「類檔案物件」的好處是解耦（Decoupling）。
    # 在單元測試中，我們不需建立暫存檔即可驗證邏輯，速度快且不污染檔案系統。
    # 在雲端部署時，若資料來自 S3 或 API，我們可直接將 ByteStream 轉為字串流處理。

if __name__ == "__main__":
    solve()
