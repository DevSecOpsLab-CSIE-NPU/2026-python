# TEST_LOG

## Task 1

### Red（失敗紀錄）

執行指令：`python -m unittest tests/test_task1.py -v`

結果：

```text
ImportError: cannot import name 'filter_by_admission'
```

失敗原因：核心過濾函式尚未實作。

### Green（通過紀錄）

執行指令：`python -m unittest tests/test_task1.py -v`

結果：

```text
Ran 7 tests in 0.001s
OK
```

讓測試通過的關鍵修改：實作 `filter_by_admission()`、`count_by_dept()`、`build_summary()` 與 `read_csv()` / `write_json()`。

## Task 2

### Red（失敗紀錄）

執行指令：`python -m unittest tests/test_task2.py -v`

結果：

```text
ImportError: cannot import name 'build_xml_tree'
```

失敗原因：XML 結構建立函式尚未實作。

### Green（通過紀錄）

執行指令：`python -m unittest tests/test_task2.py -v`

結果：

```text
Ran 6 tests in 0.001s
OK
```

讓測試通過的關鍵修改：實作 `build_xml_tree()`、`read_json()`、`write_xml()`，並正確輸出 `students` 根節點與屬性。