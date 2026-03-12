# Week 02 Homework - 1114405012

## 1) 完成題目清單

- [x] Task 1：Sequence Clean
- [x] Task 2：Student Ranking
- [x] Task 3：Log Summary

## 2) 執行方式（Python 版本與指令）

- Python 版本：Python 3.9+

### 程式執行指令

```bash
# Task 1
echo "5 3 5 2 9 2 8 3 1" | python3 task1_sequence_clean.py

# Task 2
cat << 'EOF' | python3 task2_student_ranking.py
6 3
amy 88 20
bob 88 19
zoe 92 21
ian 88 19
leo 75 20
eva 92 20
EOF

# Task 3
cat << 'EOF' | python3 task3_log_summary.py
8
alice login
bob login
alice view
alice logout
bob view
bob view
chris login
bob logout
EOF
```

### 測試執行指令

```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```

## 3) 資料結構選擇理由

- Task 1：使用 `list` 保存輸入順序與輸出序列，搭配 `set` 僅做查重判斷（不直接輸出去重結果），確保「保留第一次出現順序」。
- Task 2：使用 `list[tuple(name, score, age)]` 表示學生資料，並以 `sorted(..., key=...)` 一次完成多條件排序，邏輯清楚且穩定。
- Task 3：使用 `Counter` 計算使用者事件數與 action 次數，再以排序處理 tie-break 規則，程式碼簡潔且容易驗證。

## 4) 遇到的錯誤與修正方式

一開始使用 `python -m unittest ...` 時，環境回報 `python: command not found`，導致無法執行測試。我改成 `python3 -m unittest ...` 後可正常執行，後續全部測試流程都統一使用 `python3`。

## 5) 各題 Red → Green → Refactor 摘要

### Task 1

Red：先寫 `test_task1.py`，此時因 `task1_sequence_clean.py` 尚未建立而失敗。Green：補上 `parse_numbers`、`dedupe_preserve_order`、`solve` 後，正常/邊界案例皆通過。Refactor：將輸出格式抽成 `format_line`，降低重複字串拼接邏輯。

### Task 2

Red：先定義排序 tie-break 測試（分數、年齡、姓名），尚未實作時測試失敗。Green：使用 `sorted(students, key=lambda ...)` 完成規格排序與前 `k` 名切片，測試轉綠。Refactor：將解析、排序、取前 `k`、格式化拆成函式，提升可讀性與可測性。

### Task 3

Red：先寫出統計輸出與空輸入測試，未有模組時失敗。Green：使用 `Counter` 完成 user/action 計數，並依規則排序與輸出 `top_action`。Refactor：把事件解析、使用者排序統計、最常見 action 計算分離成獨立函式，維護更容易。
