# TEST_CASES

以下列出 6 組自行設計測資，涵蓋一般、邊界、同分排序、反例與高鑑別度案例。

---

## Case 1（一般情況）- Task 1 基本序列處理

- 輸入：`5 3 5 2 9 2 8 3 1`
- 預期輸出：

```text
dedupe: 5 3 2 9 8 1
asc: 1 2 2 3 3 5 5 8 9
desc: 9 8 5 5 3 3 2 2 1
evens: 2 2 8
```

- 實際輸出：

```text
dedupe: 5 3 2 9 8 1
asc: 1 2 2 3 3 5 5 8 9
desc: 9 8 5 5 3 3 2 2 1
evens: 2 2 8
```

- 是否通過：PASS
- 對應測試函式：`tests/test_task1.py::test_solve_formats_expected_output`
- 失敗到通過的關鍵修改點：補上 `dedupe_preserve_order()`，避免直接用 `set` 破壞順序。

---

## Case 2（邊界情況）- Task 1 空輸入

- 輸入：`""`（空字串）
- 預期輸出：

```text
dedupe:
asc:
desc:
evens:
```

- 實際輸出：

```text
dedupe:
asc:
desc:
evens:
```

- 是否通過：PASS
- 對應測試函式：`tests/test_task1.py::test_empty_input_returns_empty_sections`
- 失敗到通過的關鍵修改點：在 `parse_numbers()` 先處理 `strip()` 後空字串，回傳空陣列。

---

## Case 3（重複值/同分排序）- Task 2 tie-break 驗證

- 輸入：

```text
6 3
amy 88 20
bob 88 19
zoe 92 21
ian 88 19
leo 75 20
eva 92 20
```

- 預期輸出：

```text
eva 92 20
zoe 92 21
bob 88 19
```

- 實際輸出：

```text
eva 92 20
zoe 92 21
bob 88 19
```

- 是否通過：PASS
- 對應測試函式：`tests/test_task2.py::test_rank_students_with_tie_breakers`
- 失敗到通過的關鍵修改點：排序 key 改為 `(-score, age, name)`，一次符合三層規則。

---

## Case 4（反例）- Task 2 `k=0`

- 輸入：

```text
2 0
ann 90 18
ben 70 19
```

- 預期輸出：空字串
- 實際輸出：空字串
- 是否通過：PASS
- 對應測試函式：`tests/test_task2.py::test_solve_with_zero_k_returns_empty_output`
- 失敗到通過的關鍵修改點：在 `top_k_students()` 增加 `if k <= 0: return []`。

---

## Case 5（一般+分組統計）- Task 3 題目範例

- 輸入：

```text
8
alice login
bob login
alice view
alice logout
bob view
bob view
chris login
bob logout
```

- 預期輸出：

```text
bob 4
alice 3
chris 1
top_action: login 3
```

- 實際輸出：

```text
bob 4
alice 3
chris 1
top_action: login 3
```

- 是否通過：PASS
- 對應測試函式：`tests/test_task3.py::test_summary_matches_example`
- 失敗到通過的關鍵修改點：使用 `Counter` 進行 action 計數，避免手刻計數遺漏。

---

## Case 6（最能測出錯誤）- Task 3 空紀錄 `m=0`

- 輸入：

```text
0
```

- 預期輸出：

```text
top_action: none 0
```

- 實際輸出：

```text
top_action: none 0
```

- 是否通過：PASS
- 對應測試函式：`tests/test_task3.py::test_empty_log_input`
- 失敗到通過的關鍵修改點：在 `most_common_action()` 對空 `Counter` 回傳預設值 `("none", 0)`。
