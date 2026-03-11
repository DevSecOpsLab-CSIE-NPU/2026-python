# Week 02 - 1114405002

## 完成題目清單
- Task 1: Sequence Clean
- Task 2: Student Ranking
- Task 3: Log Summary

## 執行方式
Python 版本: 3.8+

### 程式執行指令
- Task 1: `python task1.py`
- Task 2: `python task2.py`
- Task 3: `python task3.py`

### 測試執行指令
`python -m unittest discover -s tests -p "test_*.py" -v`

## 資料結構選擇理由
- Task 1: 使用 list 處理序列，set 檢查重複以維持順序。
- Task 2: 使用 sorted 與 key 進行多條件排序。
- Task 3: 使用 defaultdict 統計用戶，Counter 統計動作。

## 遇到的錯誤與修正
在 Task 1 去重時，最初使用 set 但破壞順序，改用 list 與 in 檢查。

## Red → Green → Refactor 摘要
- Task 1: 先寫測試失敗，實作去重與排序通過，重構拆分函式。
- Task 2: 測試排序邏輯失敗，實作 sorted key 通過，重構 key 函式。
- Task 3: 測試統計失敗，實作 Counter 通過，重構處理空輸入。