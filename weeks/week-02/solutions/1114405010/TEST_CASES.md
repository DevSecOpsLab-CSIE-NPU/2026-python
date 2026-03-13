# TEST_CASES

## Case 1 - Task 1 一般情況
- 輸入
```
5 3 5 2 9 2 8 3 1
```
- 預期輸出
```
dedupe: 5 3 2 9 8 1
asc: 1 2 2 3 3 5 5 8 9
desc: 9 8 5 5 3 3 2 2 1
evens: 2 2 8
```
- 實際輸出：與預期一致
- PASS/FAIL：PASS
- 對應測試函式：`tests/test_task1.py::test_build_report_normal_case`
- 關鍵修改點：去重改為「先檢查 seen 再 append」。

## Case 2 - Task 1 邊界情況（空輸入）
- 輸入
```
(空字串)
```
- 預期輸出
```
[]
```
- 實際輸出：`parse_numbers_line` 回傳 `[]`
- PASS/FAIL：PASS
- 對應測試函式：`tests/test_task1.py::test_parse_numbers_line_empty`
- 關鍵修改點：補上 `strip` 後空字串直接回傳空列表。

## Case 3 - Task 2 同分排序情況
- 輸入
```
6 3
amy 88 20
bob 88 19
zoe 92 21
ian 88 19
leo 75 20
eva 92 20
```
- 預期輸出
```
eva 92 20
zoe 92 21
bob 88 19
```
- 實際輸出：與預期一致
- PASS/FAIL：PASS
- 對應測試函式：`tests/test_task2.py::test_tie_break_by_age_then_name`
- 關鍵修改點：排序 key 由單鍵改為三鍵 `(-score, age, name)`。

## Case 4 - Task 3 反例（action 同次數）
- 輸入
```
4
u1 view
u2 login
u3 view
u4 login
```
- 預期輸出
```
top_action: login 2
```
- 實際輸出：`top_action: login 2`
- PASS/FAIL：PASS
- 對應測試函式：`tests/test_task3.py::test_action_tie_break_by_name`
- 關鍵修改點：同次數以 action 字母序排序，避免不穩定輸出。

## Case 5 - Task 3 邊界情況（m=0）
- 輸入
```
0
```
- 預期輸出
```
top_action: NONE 0
```
- 實際輸出：`top_action: NONE 0`
- PASS/FAIL：PASS
- 對應測試函式：`tests/test_task3.py::test_empty_input`
- 關鍵修改點：`Counter` 為空時回傳預設值 `(NONE, 0)`。
