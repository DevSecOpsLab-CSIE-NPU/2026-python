# Week 02 - 1114405010

## 完成題目清單
- Task 1: `task1_sequence_clean.py`
- Task 2: `task2_student_ranking.py`
- Task 3: `task3_log_summary.py`

## 執行方式（Python 版本）
- 建議 Python 3.11+（本次以 Python 3.12 測試）

### 程式執行指令
- Task 1: `python task1_sequence_clean.py`
- Task 2: `python task2_student_ranking.py < input_task2.txt`
- Task 3: `python task3_log_summary.py < input_task3.txt`

### 測試執行指令
- `python -m unittest discover -s tests -p "test_*.py" -v`

## 資料結構選擇理由
- Task 1: 以 `set + list` 完成保序去重，避免直接輸出 `set` 造成順序破壞。
- Task 2: 以 `sorted(..., key=lambda r: (-score, age, name))` 一次完成多鍵排序，邏輯簡潔且可重複驗證。
- Task 3: 使用 `defaultdict(int)` 統計使用者事件，並用 `Counter` 計算 action 次數，易於處理空輸入與排序。

## 遇到的 1 個錯誤與修正
- 錯誤：Task 3 的 top action 同次數時，若未定義 tie-break，輸出順序不穩定。
- 修正：改為 `(-count, action)` 排序，固定同次數時依 action 字母序輸出。

## Red -> Green -> Refactor 摘要
### Task 1
- Red：先寫測試驗證「保序去重」與「偶數保留原順序」，初版在 dedupe 輸出順序曾出錯。
- Green：改成逐一遍歷配合 `seen` 集合，確認第一次出現才加入結果，測試通過。
- Refactor：把輸出拆成 `build_report` 與 `format_report`，讓計算與格式化分離，後續維護更容易。

### Task 2
- Red：先寫 tie-break 測試，初版只按分數排序，忽略 age/name 規則。
- Green：補上多鍵排序 key：`(-score, age, name)`，與題目規則一致。
- Refactor：把 I/O 解析抽到 `parse_student_input`，主邏輯保留在 `rank_students`，方便獨立測試。

### Task 3
- Red：先寫空輸入與 action 同次數測試，初版 top action 輸出不穩定。
- Green：加入 deterministic tie-break（同次數取字母序較小者），並定義空輸入輸出 `NONE 0`。
- Refactor：分離 `summarize_logs` 與 `format_summary`，提高可讀性與重用性。
