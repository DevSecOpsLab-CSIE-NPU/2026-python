# TEST_CASES

## Case 1: Task 1 一般情況

- 對應測試函式: tests/test_task1.py::test_normal_case
- 輸入:

```text
5 3 5 2 9 2 8 3 1
```

- 預期輸出:

```text
dedupe: 5 3 2 9 8 1
asc: 1 2 2 3 3 5 5 8 9
desc: 9 8 5 5 3 3 2 2 1
evens: 2 2 8
```

- 實際輸出: 與預期一致
- 是否通過: PASS
- 關鍵修改點: 補上 dedupe_preserve_order，避免用 set 直接輸出造成順序錯誤。

## Case 2: Task 1 邊界（空輸入）

- 對應測試函式: tests/test_task1.py::test_empty_input
- 輸入:

```text

```

- 預期輸出:

```text
dedupe:
asc:
desc:
evens:
```

- 實際輸出: 四行皆為空序列
- 是否通過: PASS
- 關鍵修改點: parse_numbers 先判斷空字串，回傳空 list。

## Case 3: Task 2 同分排序情況

- 對應測試函式: tests/test_task2.py::test_tie_break_by_age_then_name
- 輸入:

```text
3 3
d 90 20
a 90 20
b 90 19
```

- 預期輸出:

```text
b 90 19
a 90 20
d 90 20
```

- 實際輸出: 與預期一致
- 是否通過: PASS
- 關鍵修改點: key 改為 (-score, age, name)。

## Case 4: Task 3 反例（action 次數同分）

- 對應測試函式: tests/test_task3.py::test_action_tie_uses_name_asc
- 輸入:

```text
2
u1 b
u2 a
```

- 預期輸出:

```text
u1 1
u2 1
top_action: a 1
```

- 實際輸出: 與預期一致
- 是否通過: PASS
- 關鍵修改點: top action 先按次數降序、再按 action 名稱升序。

## Case 5: Task 3 最能測錯（空紀錄）

- 對應測試函式: tests/test_task3.py::test_empty_records
- 輸入:

```text
0
```

- 預期輸出:

```text
top_action: None 0
```

- 實際輸出: 無使用者統計行，最後一行為 top_action: None 0
- 是否通過: PASS
- 關鍵修改點: summarize_logs 對空 action_counter 回傳 None，solve 再統一格式化輸出。
