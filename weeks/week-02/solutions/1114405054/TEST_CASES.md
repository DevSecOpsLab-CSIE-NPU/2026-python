# TEST_CASES

## Case 1: Task 1 一般情況

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
- 結果: PASS
- 對應測試: `tests/test_task1.py::test_sample_case`
- 關鍵修改點: 去重由 `set` 改為 `seen + list`。

## Case 2: Task 1 邊界（空輸入）

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

- 實際輸出: 與預期一致
- 結果: PASS
- 對應測試: `tests/test_task1.py::test_empty_input`
- 關鍵修改點: `parse_numbers()` 對空字串回傳空陣列。

## Case 3: Task 2 同分排序

- 輸入:

```text
6 3
amy 88 20
bob 88 19
zoe 92 21
ian 88 19
leo 75 20
eva 92 20
```

- 預期輸出:

```text
eva 92 20
zoe 92 21
bob 88 19
```

- 實際輸出: 與預期一致
- 結果: PASS
- 對應測試: `tests/test_task2.py::test_sample_case`
- 關鍵修改點: key 改為 `(-score, age, name)`。

## Case 4: Task 3 反例（action 次數同分）

- 輸入:

```text
2
u1 view
u2 login
```

- 預期輸出:

```text
u1 1
u2 1
top_action: login 1
```

- 實際輸出: 與預期一致
- 結果: PASS
- 對應測試: `tests/test_task3.py::test_action_tie_uses_lexicographical_order`
- 關鍵修改點: 對同最高次數 action 做字母序最小選擇。

## Case 5: Task 3 最小輸入（m=0）

- 輸入:

```text
0
```

- 預期輸出:

```text
top_action: none 0
```

- 實際輸出: 與預期一致
- 結果: PASS
- 對應測試: `tests/test_task3.py::test_empty_logs`
- 關鍵修改點: 加入空統計預設輸出。