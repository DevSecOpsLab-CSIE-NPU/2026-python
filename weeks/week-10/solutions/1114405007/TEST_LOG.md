# TEST_LOG.md

## Task 1

### Red（失敗紀錄）

執行指令：`python -m unittest tests/test_task1.py -v`

```
ERROR: test_filter_keeps_correct_rows (test_task1.TestFilterByAdmission)
ImportError: cannot import name 'filter_by_admission' from 'task1_csv_to_json'

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)
```

失敗原因：`filter_by_admission` 尚未實作，import 直接噴 `ImportError`。

---

### Green（通過紀錄）

執行指令：`python -m unittest tests/test_task1.py -v`

```
test_filter_keeps_correct_rows (test_task1.TestFilterByAdmission) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```

讓測試通過的關鍵修改：在 `task1_csv_to_json.py` 中實作 `filter_by_admission`，用 list comprehension 過濾 `入學方式` 欄位：

```python
def filter_by_admission(rows: list[dict], method: str) -> list[dict]:
    return [r for r in rows if r.get("入學方式") == method]
```

---

## Task 2

### Red（失敗紀錄）

執行指令：`python -m unittest tests/test_task2.py -v`

```
ERROR: test_root_tag_and_attrs (test_task2.TestBuildXmlTree)
ImportError: cannot import name 'build_xml_tree' from 'task2_json_to_xml'

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)
```

失敗原因：`build_xml_tree` 尚未實作。

---

### Green（通過紀錄）

執行指令：`python -m unittest tests/test_task2.py -v`

```
test_root_tag_and_attrs (test_task2.TestBuildXmlTree) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```

讓測試通過的關鍵修改：在 `task2_json_to_xml.py` 實作 `build_xml_tree`，以 `ET.Element` 建立根節點並正確設定 `source`、`total` 屬性：

```python
def build_xml_tree(data: dict) -> ET.Element:
    root = ET.Element(
        "students",
        attrib={
            "source": data.get("來源", ""),
            "total": str(data.get("總人數", 0)),
        },
    )
    for stu in data.get("學生清單", []):
        ET.SubElement(root, "student", attrib={...})
    return root
```

---

## 最終全數通過紀錄

執行指令：`python -m unittest discover -s tests -p "test_*.py" -v`

```
Ran 17 tests in 0.003s

OK
```
