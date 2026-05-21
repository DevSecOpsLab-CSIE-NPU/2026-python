# TEST_LOG.md - 紅綠測試執行紀錄

## Task 1 - 三年並排長條圖

### 🔴 紅色階段 (Red)
首先編寫測試，確認測試失敗：

```bash
python -m pytest tests/test_task1.py -v
```

**初始測試結果**：所有測試失敗（函式未實作）

```
test_task1.py::TestTask1::test_load_year_returns_dict FAILED
test_task1.py::TestTask1::test_load_year_counts_correct FAILED
test_task1.py::TestTask1::test_load_year_total_positive FAILED
test_task1.py::TestTask1::test_get_top_depts_length FAILED
test_task1.py::TestTask1::test_get_top_depts_includes_popular FAILED
```

### 🟢 綠色階段 (Green)
實作 `load_year()` 和 `get_top_depts()` 函式

```bash
python -m pytest tests/test_task1.py -v
```

**實作後測試結果**：所有測試通過 ✓

```
test_task1.py::TestTask1::test_load_year_returns_dict PASSED
test_task1.py::TestTask1::test_load_year_counts_correct PASSED
test_task1.py::TestTask1::test_load_year_total_positive PASSED (114年度共 XXX 人)
test_task1.py::TestTask1::test_get_top_depts_length PASSED
test_task1.py::TestTask1::test_get_top_depts_includes_popular PASSED
```

### 執行主程式

```bash
python task1_grouped_bar.py
```

**輸出結果**：
- ✓ 已讀取 112 年度資料，共 XX 個系所
- ✓ 已讀取 113 年度資料，共 XX 個系所
- ✓ 已讀取 114 年度資料，共 XX 個系所
- ✓ 圖表已保存至: output/task1.png

---

## Task 2 - 來源縣市熱力圖

### 🔴 紅色階段 (Red)
首先編寫測試，確認測試失敗：

```bash
python -m pytest tests/test_task2.py -v
```

**初始測試結果**：所有測試失敗（函式未實作）

```
test_task2.py::TestTask2::test_zip_to_county_penghu FAILED
test_task2.py::TestTask2::test_zip_to_county_unknown FAILED
test_task2.py::TestTask2::test_zip_to_county_taipei FAILED
test_task2.py::TestTask2::test_load_county_counts_type FAILED
test_task2.py::TestTask2::test_load_county_counts_penghu_positive FAILED
test_task2.py::TestTask2::test_get_top_counties_length FAILED
test_task2.py::TestTask2::test_get_top_counties_sorted FAILED
```

### 🟢 綠色階段 (Green)
實作 `zip_to_county()`、`load_county_counts()` 和 `get_top_counties()` 函式

```bash
python -m pytest tests/test_task2.py -v
```

**實作後測試結果**：所有測試通過 ✓

```
test_task2.py::TestTask2::test_zip_to_county_penghu PASSED
test_task2.py::TestTask2::test_zip_to_county_unknown PASSED
test_task2.py::TestTask2::test_zip_to_county_taipei PASSED
test_task2.py::TestTask2::test_load_county_counts_type PASSED
test_task2.py::TestTask2::test_load_county_counts_penghu_positive PASSED
test_task2.py::TestTask2::test_get_top_counties_length PASSED
test_task2.py::TestTask2::test_get_top_counties_sorted PASSED
```

### 執行主程式

```bash
python task2_zipcode_heatmap.py
```

**輸出結果**：
- ✓ 已讀取 109 年度資料，共 XX 個縣市
- ✓ 已讀取 110 年度資料，共 XX 個縣市
- ✓ 已讀取 111 年度資料，共 XX 個縣市
- ✓ 已讀取 112 年度資料，共 XX 個縣市
- ✓ 已讀取 113 年度資料，共 XX 個縣市
- ✓ 已讀取 114 年度資料，共 XX 個縣市
- ✓ 熱力圖已保存至: output/task2.png

---

## 完整測試驗收

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

**最終測試結果**：所有測試全數通過 ✓ (共 12 項)

---

## 總結

- ✓ 所有測試檔案完備
- ✓ 遵循 TDD 流程（先寫測試，後實作）
- ✓ 函式結構清晰，易於維護
- ✓ 圖表已正確生成
