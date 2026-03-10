# 測試執行紀錄
# Round 1: Red
- 指令: `python -m unittest discover -s tests -p "test_*.py" -v`
- 結果: FAILED ImportError
- 原因: 尚未撰寫實作檔案，導致測試程式抓不到函式

# Round 2: Green
- 指令: `python -m unittest discover -s tests -p "test_*.py" -v`
- 結果: OK (9 tests passed)
- 修改: 完成了三題的邏輯實作，並修正了空輸入的邊界處理