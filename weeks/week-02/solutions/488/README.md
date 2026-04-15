# Week 02 Solutions - 488

## 1. 完成題目清單

- Task 1: Sequence Clean
- Task 2: Student Ranking
- Task 3: Log Summary

## 2. 執行方式

- Python 版本: Python 3.14（亦可使用 3.10+）
- 進入目錄:

```bash
cd weeks/week-02/solutions/488
```

- Task 1:

```bash
python task1_sequence_clean.py
```

- Task 2:

```bash
python task2_student_ranking.py < input_task2.txt
```

- Task 3:

```bash
python task3_log_summary.py < input_task3.txt
```

- 測試執行:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## 3. 資料結構選擇理由

- Task 1: 使用 list 保留原始順序，並用 set 輔助判斷是否已出現，能在不破壞順序下完成去重。
- Task 2: 以 tuple(name, score, age) 表示學生資料，配合 sorted 的 key 一次完成多條件排序。
- Task 3: 使用 Counter 統計使用者事件數與 action 次數，程式簡潔且容易驗證。

## 4. 遇到的錯誤與修正

- 一開始測試無法匯入模組（ModuleNotFoundError），因為先寫了 tests 還沒實作 task 檔案。補上三個任務檔案後，測試即可載入並執行。

## 5. Red -> Green -> Refactor 摘要

- Task 1:
  - Red: 先寫 test_task1.py，執行後因 task1_sequence_clean.py 不存在而失敗。
  - Green: 實作 parse、去重、排序與偶數過濾，測試通過。
  - Refactor: 將輸出組裝拆成 solve 與 format_numbers，降低 main 內重複字串處理。

- Task 2:
  - Red: 先寫 test_task2.py，驗證多條件排序與 tie-break 規則。
  - Green: 實作 rank_students，使用 sorted(key=lambda ...) 完成規格要求。
  - Refactor: 補 parse_header、parse_student、top_k_students，讓主流程更清楚、可重用。

- Task 3:
  - Red: 先寫 test_task3.py，包含空輸入與 action 同次數情況。
  - Green: 實作 Counter 統計與排序邏輯，所有測試通過。
  - Refactor: 抽出 parse_records，讓 I/O 與核心統計函式 summarize_logs 分離。
