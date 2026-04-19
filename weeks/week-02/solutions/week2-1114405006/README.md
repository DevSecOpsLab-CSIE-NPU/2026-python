# Week 02 Solutions - week2-1114405006

完成題目：Task 1、Task 2、Task 3。

## 執行方式

- Python 版本：Python 3.x
- 程式執行：`python task1_sequence_clean.py` / `python task2_student_ranking.py` / `python task3_log_summary.py`
- 測試執行：`python -m unittest discover -s tests -p "test_*.py" -v`

## 資料結構選擇理由

- Task 1：用 `set` 記錄已見元素，搭配原序列掃描，才能保留第一次出現順序；排序直接交給 `sorted()`。
- Task 2：學生資料用 `dataclass` 表示，排序 key 可以清楚表達多條件規則。
- Task 3：使用 `Counter` 統計 action、用 `defaultdict(int)` 累計每位使用者事件數，讀起來直接且可維護。

## 錯誤與修正

- 一開始在 Task 3 沒有特別處理 `m = 0`，導致空輸入時無法產生合理輸出；後來加入空資料分支，讓 `top_action` 回傳 `none 0`。

## Red → Green → Refactor

### Task 1

先用測試鎖定去重保序、升降冪排序與偶數篩選三個規則。實作時先完成最小功能，再把輸出格式與處理流程拆成小函式，讓 `solve()` 只負責串接。

### Task 2

測試先覆蓋分數、年齡、姓名三層排序，以及只取前 `k` 名。綠燈後把解析、排序與格式化拆開，避免主流程混在一起。

### Task 3

測試先確認使用者總數排序與全域最常見 action 的結果。重構時把解析、統計、格式化分離，並明確處理空輸入與並列情況。