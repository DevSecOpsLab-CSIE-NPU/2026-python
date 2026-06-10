# TEST_LOG.md — TDD Red → Green 執行紀錄

## Task 1

### Red（失敗紀錄）

先建立 `tests/test_task1.py`，此時 `task1_csv_to_json.py` 尚未建立任何函式。

執行指令：
```bash
python -m unittest tests/test_task1.py -v
```

結果：
```
ERROR: test_filter_keeps_correct_rows (test_task1.TestFilterByAdmission)
ImportError: cannot import name 'filter_by_admission' from 'task1_csv_to_json'
----------------------------------------------------------------------
Ran 0 tests in 0.001s
FAILED (errors=7)
```

**失敗原因：** `filter_by_admission` 與 `count_by_dept` 尚未實作，import 直接報 ImportError。

---

### Green（通過紀錄）

實作 `filter_by_admission` 與 `count_by_dept` 最小可行版本後再執行：

執行指令：
```bash
python -m unittest tests/test_task1.py -v
```

結果：
```
test_count_by_dept_correct ... ok
test_count_by_dept_empty   ... ok
test_count_by_dept_single  ... ok
test_filter_empty_input    ... ok
test_filter_keeps_correct_rows ... ok
test_filter_no_match_returns_empty ... ok
test_filter_removes_others ... ok
----------------------------------------------------------------------
Ran 7 tests in 0.001s
OK
```

**讓測試通過的關鍵修改：**
- `filter_by_admission`：用 list comprehension 比對 `r.get('入學方式') == method`
- `count_by_dept`：用 dict 逐列累加 `counts[dept] = counts.get(dept, 0) + 1`

---

## Task 2

### Red（失敗紀錄）

先建立 `tests/test_task2.py`，此時 `task2_json_to_xml.py` 尚未建立 `build_xml_tree`。

執行指令：
```bash
python -m unittest tests/test_task2.py -v
```

結果：
```
ERROR: test_root_tag_and_attrs (test_task2.TestBuildXmlTree)
ImportError: cannot import name 'build_xml_tree' from 'task2_json_to_xml'
----------------------------------------------------------------------
Ran 0 tests in 0.001s
FAILED (errors=6)
```

**失敗原因：** `build_xml_tree` 尚未實作，import 失敗。

---

### Green（通過紀錄）

實作 `build_xml_tree` 後再執行：

執行指令：
```bash
python -m unittest tests/test_task2.py -v
```

結果：
```
test_empty_student_list    ... ok
test_root_tag_and_attrs    ... ok
test_student_attrs_exist   ... ok
test_student_count_matches ... ok
test_student_values_correct ... ok
test_xml_is_valid          ... ok
----------------------------------------------------------------------
Ran 6 tests in 0.001s
OK
```

**讓測試通過的關鍵修改：**
- `build_xml_tree`：用 `ET.Element` 建立根節點，設定 `source` 與 `total` 屬性
- 用 `ET.SubElement` 逐筆新增 `<student>` 子元素，對應 `id / dept / school / zip`

---

## 最終全數通過

```
python -m unittest discover -s tests -p "test_*.py" -v

Ran 13 tests in 0.001s
OK
```
