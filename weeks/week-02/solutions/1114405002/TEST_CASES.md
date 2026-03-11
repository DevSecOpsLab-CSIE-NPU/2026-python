# Test Cases

## 1. 一般情況
輸入: 5 3 5 2 9 2 8 3 1
預期輸出: dedupe: 5 3 2 9 8 1; asc: 1 2 2 3 3 5 5 8 9; desc: 9 8 5 5 3 3 2 2 1; evens: 2 2 8
實際輸出: 同上
PASS

對應測試: tests/test_task1.py::test_normal_case
關鍵修改: 實作去重與排序邏輯

## 2. 邊界情況
輸入: (空)
預期輸出: 所有空列表
實際輸出: 空
PASS

對應測試: tests/test_task1.py::test_empty_sequence
關鍵修改: 處理空輸入

## 3. 重複值情況
輸入: 學生列表同分
預期輸出: 按年齡與名稱排序
實際輸出: 正確
PASS

對應測試: tests/test_task2.py::test_all_same_score
關鍵修改: 使用多 key 排序

## 4. 反例
輸入: 無偶數序列
預期輸出: evens 空
實際輸出: 空
PASS

對應測試: tests/test_task1.py::test_no_duplicates_no_evens
關鍵修改: 正確過濾偶數

## 5. 最能測出錯誤的一組
輸入: 日誌空
預期輸出: 空用戶與 (None, 0)
實際輸出: 正確
PASS

對應測試: tests/test_task3.py::test_empty_logs
關鍵修改: 處理空 Counter