# q_task3_easy.py
# [AI 教學版] 任務三：用 StringIO 做資料清洗測試
# 重點：學習「介面抽象化」，讓函式不依賴真實硬碟

import csv
import io
import os

def parse_students(file_obj):
    # 這裡接受的是「類檔案物件」，不管是實體檔還是 StringIO 都可以
    return list(csv.DictReader(file_obj))

def solve():
    # 測試字串，模擬不開檔案的測試
    test_csv = "序,學校名稱,系所名稱,學號,入學方式\n1,測試大學,資工系,A001,甄選入學"

    # 使用 io.StringIO 將字串變成流（Stream）
    with io.StringIO(test_csv) as mock_file:
        result = parse_students(mock_file)
        print(f"StringIO 測試結果: {result[0]['學號']}")

if __name__ == "__main__":
    solve()
