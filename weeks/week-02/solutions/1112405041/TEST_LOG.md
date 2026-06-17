# TEST_LOG.md - Week 02 測試執行紀錄

> 本紀錄包含 TDD 過程中關鍵的 Red (失敗) 與 Green (成功) 階段。

---

## 1. 測試環境
- **Python**: 3.14 (v114)
- **指令**: `python -m unittest discover -s tests -p "test_*.py" -v`

---

## 2. 第一次測試 (Red - 邏輯未全齊)
- **時間**: 2026-03-05 10:00
- **結果**: 12 測試, 8 通過, 4 失敗
- **失敗原因**:
    - Task 1 缺少從小到大與偶數篩選邏輯。
    - Task 2 排序時未考慮到 `age` 欄位，導致同分時順序錯誤。
- **關鍵修改**:
    - 在 `task1_sequence_clean.py` 補齊 `sorted` 與列表推導式。
    - 在 `task2_student_ranking.py` 修改 lambda 關鍵字加入 `x['age']`。

---

## 3. 第二次測試 (Green - 全面防禦成功)
- **時間**: 2026-03-05 15:30
- **結果**: ✅ **Ran 12 tests in 0.005s / OK**

```text
test_all_duplicates (test_task1.TestTask1) ... ok
test_empty_input (test_task1.TestTask1) ... ok
test_normal_case (test_task1.TestTask1) ... ok
test_age_tie_break (test_task2.TestTask2) ... ok
test_k_larger_than_n (test_task2.TestTask2) ... ok
test_normal_ranking (test_task2.TestTask2) ... ok
test_count_tie_break (test_task3.TestTask3) ... ok
test_m_zero (test_task3.TestTask3) ... ok
test_normal_logs (test_task3.TestTask3) ... ok
...
```

### 修正復盤
- 成功識破了 August 在 `HOMEWORK.md` 埋下的「age 排序」與「Task 1 四項輸出」地雷。
- 透過 `dict.fromkeys()` 解決了 AI 建議中 `set()` 會破壞順序的致命錯誤。
