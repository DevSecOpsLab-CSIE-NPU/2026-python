# Week 02 Homework - 1114405011

## 完成題目清單
- [x] Task 1: Sequence Clean
- [x] Task 2: Student Ranking
- [x] Task 3: Log Summary

## 執行方式
- Python version: 3.14.2 (venv)
- 執行 Task 1:
  - `python task1_sequence_clean.py`
- 執行 Task 2:
  - `python task2_student_ranking.py`
- 執行 Task 3:
  - `python task3_log_summary.py`
- 執行全部測試:
  - `python -m unittest discover -s tests -p "test_*.py" -v`

## 資料結構選擇理由
- Task 1: 使用 `list` 保存原始順序，搭配 `set` 記錄是否看過，完成「保序去重」。
- Task 2: 使用 `list[tuple]` 儲存學生資料，透過 `sorted(..., key=(-score, age, name))` 一次完成多條件排序。
- Task 3: 使用 `defaultdict(int)` 統計每位使用者事件數，搭配 `Counter` 取得全域 action 次數。

## 錯誤與修正
- Task 1 一開始只改了編輯器內容但檔案未同步到終端機，測試仍跑到舊版 `test_todo_red`。修正方式是重新覆寫實體檔案後再執行測試。
- Task 2 一開始排序只用 `score`，沒有把 `age` 和 `name` 放進 tie-break，導致同分時順序錯誤。修正方式是改成 `key=(-score, age, name)`。
- Task 3 一開始用 `Counter.most_common(1)` 取 top action，遇到同次數時結果不穩定。修正方式是加上同分時字母序規則，固定輸出一致。

## Red -> Green -> Refactor 摘要
- Task 1: 我先寫 `test_basic/test_empty/test_with_zero/test_format` 後執行，因為函式尚未實作而失敗（Red）。之後依序完成 `parse_input`、`process_numbers`、`format_output`、`main` 讓四個測試通過（Green）。最後把檔案整理成較簡潔寫法並再跑一次測試，確認沒有回歸（Refactor）。
- Task 2: 我先寫樣例、同分排序、`k > n` 的測試，確認一開始會失敗（Red）。接著完成 `parse_input/rank_students/format_output/main`，並把排序 key 修正為 `(-score, age, name)` 後全綠（Green）。最後把測試命名與變數簡化，確保程式與測試都可讀（Refactor）。
- Task 3: 我先寫樣例、`m=0` 邊界、top action 同分案例做驗證（Red）。再完成 `parse_input/summarize/format_output/main`，加入空輸入與同分規則後通過測試（Green）。最後固定輸出格式並重跑全測試，確認結果穩定（Refactor）。
