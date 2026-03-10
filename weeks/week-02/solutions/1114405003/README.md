# Week 02 - 1114405003

## 完成題目清單
- Task 1: Sequence Clean
- Task 2: Student Ranking
- Task 3: Log Summary

## 執行方式
- Python 版本：3.12（與作業說明相容）

## 程式執行指令
Task 1:
- 直接呼叫 `sequence_clean()` 與 `format_sequence_clean()`

Task 2:
- 呼叫 `student_ranking(lines)`，第一行是 `n k`，後面是 `name score age`

Task 3:
- 呼叫 `log_summary(lines)`，第一行是 `m`，後面是 `user action`

## 測試執行指令
- `python -m unittest discover -s tests -p test_*.py -v`

## 資料結構選擇理由
- Task 1: 使用 `set` + list 追蹤去重順序，`sorted()` 做排序，list 直接保留順序。
- Task 2: 用 `sorted(..., key=...)` 做複合排序，避免手寫交換排序。
- Task 3: 用 `collections.Counter` 做計數，加 `sorted()` 生成穩定輸出。

## 遇到的錯誤與修正方式
- `unittest` 失敗：`test_tie_break_age_name` 預期排序錯誤，調整為 `c` 在 `x` 前。

## Red → Green → Refactor 摘要
Task 1:
- Red: 測試先寫（空輸入、重複值、普通），一開始函式不存在導致 ImportError。
- Green: 實作 `sequence_clean` + `format_sequence_clean`，所有 case 通過。
- Refactor: 分離輸出格式函式，補註解與口訣。

Task 2:
- Red: 測試先寫（基本排序、同分 tiebreak、空輸入），初始邏輯完成後錯誤期待值。
- Green: 實作 `student_ranking`，再調整 testcase 預期，通過。
- Refactor: 用 `key=lambda s: (-s[1], s[2], s[0])` 保持簡潔。

Task 3:
- Red: 測試先寫（基本輸出、0 筆、action tie），初始邏輯未處理 m=0。
- Green: 加 Counter + 讀 m，返回對應格式。
- Refactor: 針對行內空白進行健壯處理，保留 m=0 支援。
