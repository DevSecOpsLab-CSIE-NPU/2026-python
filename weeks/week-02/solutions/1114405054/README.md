# Week 02 Homework - 1114405054

## 完成題目清單

- Task 1: `task1_sequence_clean.py`
- Task 2: `task2_student_ranking.py`
- Task 3: `task3_log_summary.py`

## 執行方式

- Python 版本: 3.11+

### 程式執行指令

```bash
python task1_sequence_clean.py
python task2_student_ranking.py
python task3_log_summary.py
```

### 測試執行指令

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## 資料結構選擇理由

- Task 1: 用 `list` 保留序列順序，用 `set` 只做 membership 檢查，避免破壞去重後原順序。
- Task 2: 用 `dataclass` 描述學生資料，搭配 `sorted(key=...)` 寫出多層排序條件且可讀性高。
- Task 3: 用 `defaultdict(int)` 計使用者次數、`Counter` 計 action 次數，統計邏輯清楚且程式短。

## 1 個錯誤與修正方式

- 錯誤: Task 3 最常見 action 同次數時，最初直接用 `Counter.most_common(1)`，結果 tie 時輸出不穩定。
- 修正: 先取最大次數，再在同次數 action 中用字母序最小值，確保測試穩定可重現。

## Red -> Green -> Refactor 摘要

- Task 1:
  - Red: 先寫 sample 測試，去重邏輯最初誤用了直接 `set` 造成順序錯誤。
  - Green: 改成 `seen + list` 的順序去重後，sample 與空輸入測試通過。
  - Refactor: 拆出 `parse_numbers()` 與 `format_line()`，讓輸出規格更集中。

- Task 2:
  - Red: 先寫同分排序測試，初版只按分數排序導致 tie-break 失敗。
  - Green: 改為 key `(-score, age, name)`，符合規格。
  - Refactor: 加入 `Student` dataclass 與 `rank_students()`，可測試性更好。

- Task 3:
  - Red: 先寫空輸入與 action tie 測試，初版在 `m=0` 會缺少輸出行。
  - Green: 補上空輸入分支與 tie-break 規則，所有測試轉綠。
  - Refactor: 將統計拆成 `summarize()`，`solve()` 只負責 I/O 格式化。