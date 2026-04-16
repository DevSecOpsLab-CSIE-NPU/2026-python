# TEST_CASES.md — Week 02 自訂測資

共 5 組測資，涵蓋一般、邊界、重複值、反例及最能測出錯誤的情境。

---

## 測資 1：一般情況（Task 1）

**對應函式**：`tests/test_task1.py::TestDedupeOrdered::test_normal_case`

| 欄位 | 內容 |
|------|------|
| 輸入 | `5 3 5 2 9 2 8 3 1` |
| 預期 dedupe | `5 3 2 9 8 1` |
| 預期 asc | `1 2 2 3 3 5 5 8 9` |
| 預期 desc | `9 8 5 5 3 3 2 2 1` |
| 預期 evens | `2 2 8` |
| 實際輸出 | 與預期相同 |
| 結果 | PASS |

**失敗→通過的關鍵修改**：去重改用遍歷 + set 而非直接 `list(set(...))`，確保順序固定。

---

## 測資 2：邊界情況（Task 3 空輸入）

**對應函式**：`tests/test_task3.py::TestLogSummaryEdge::test_empty_input`

| 欄位 | 內容 |
|------|------|
| 輸入 | `0`（無後續紀錄） |
| 預期輸出 | `top_action: (none) 0` |
| 實際輸出 | `top_action: (none) 0` |
| 結果 | PASS |

**失敗→通過的關鍵修改**：在函式開頭加 `if m == 0` 早返回，避免對空 `Counter` 呼叫 `.most_common(1)[0]` 導致 `IndexError`。

---

## 測資 3：重複值 / 同分排序（Task 2）

**對應函式**：`tests/test_task2.py::TestRankStudents::test_all_same_score_and_age`

| 欄位 | 內容 |
|------|------|
| 輸入 | `3 3`，學生：`charlie 80 20`、`alice 80 20`、`bob 80 20` |
| 預期輸出 | `alice 80 20` → `bob 80 20` → `charlie 80 20` |
| 實際輸出 | 與預期相同 |
| 結果 | PASS |

**失敗→通過的關鍵修改**：key 第三欄加入 `s[0]`（姓名）升序，三元組排序一次到位。

---

## 測資 4：反例（Task 1 — 容易誤用 set 破壞順序）

**對應函式**：`tests/test_task1.py::TestDedupeOrdered::test_preserves_order`

| 欄位 | 內容 |
|------|------|
| 輸入 | `[3, 1, 2, 1, 3]` |
| 預期輸出 | `[3, 1, 2]` |
| 誤解寫法 | `list(set([3,1,2,1,3]))` 可能輸出 `[1, 2, 3]`（順序不定） |
| 實際輸出 | `[3, 1, 2]` |
| 結果 | PASS |

**失敗→通過的關鍵修改**：用 `seen` set 追蹤是否出現過，遍歷時按原始順序 append。

---

## 測資 5：最能測出錯誤的情況（Task 3 — 同數使用者排序）

**對應函式**：`tests/test_task3.py::TestLogSummaryTieBreak::test_tie_sorted_by_name`

| 欄位 | 內容 |
|------|------|
| 輸入 | `2`、`bob view`、`alice login` |
| 預期輸出 | `alice 1` 在前，`bob 1` 在後，最後為 `top_action: ...` |
| 實際輸出 | 與預期相同 |
| 結果 | PASS |

**理由**：若排序只考慮次數而忽略 `name` 升序作為次要鍵，bob 可能排在 alice 前面，這是最容易漏掉的邊界條件。
