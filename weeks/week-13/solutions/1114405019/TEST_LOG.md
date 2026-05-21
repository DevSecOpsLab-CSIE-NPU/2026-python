# TEST_LOG.md — TDD Red → Green 執行紀錄

## Red Phase（測試先行，尚未實作）

執行時間：2026-05-21

```
python -m unittest discover -s tests -v

test_get_top_depts_includes_popular (test_task1.TestTask1.test_get_top_depts_includes_popular) ... ERROR
test_get_top_depts_length (test_task1.TestTask1.test_get_top_depts_length) ... ERROR
test_load_year_counts_correct (test_task1.TestTask1.test_load_year_counts_correct) ... ERROR
test_load_year_returns_dict (test_task1.TestTask1.test_load_year_returns_dict) ... ERROR
test_load_year_total_positive (test_task1.TestTask1.test_load_year_total_positive) ... ERROR
test_get_top_counties_length (test_task2.TestTask2.test_get_top_counties_length) ... ERROR
test_load_county_counts_penghu_positive (test_task2.TestTask2.test_load_county_counts_penghu_positive) ... ERROR
test_load_county_counts_type (test_task2.TestTask2.test_load_county_counts_type) ... ERROR
test_zip_to_county_penghu (test_task2.TestTask2.test_zip_to_county_penghu) ... ERROR
test_zip_to_county_unknown (test_task2.TestTask2.test_zip_to_county_unknown) ... ERROR

----------------------------------------------------------------------
Ran 10 tests in 0.007s

FAILED (errors=10)
```

**失敗原因：** `task1_grouped_bar` 與 `task2_zipcode_heatmap` 模組尚未建立，所有測試在 `setUp` 即拋出 `ModuleNotFoundError`。

---

## Green Phase（實作完成後）

執行時間：2026-05-21

```
python -m unittest discover -s tests -v

test_get_top_depts_includes_popular (test_task1.TestTask1.test_get_top_depts_includes_popular) ... ok
test_get_top_depts_length (test_task1.TestTask1.test_get_top_depts_length) ... ok
test_load_year_counts_correct (test_task1.TestTask1.test_load_year_counts_correct) ... ok
test_load_year_returns_dict (test_task1.TestTask1.test_load_year_returns_dict) ... ok
test_load_year_total_positive (test_task1.TestTask1.test_load_year_total_positive) ... ok
test_get_top_counties_length (test_task2.TestTask2.test_get_top_counties_length) ... ok
test_load_county_counts_penghu_positive (test_task2.TestTask2.test_load_county_counts_penghu_positive) ... ok
test_load_county_counts_type (test_task2.TestTask2.test_load_county_counts_type) ... ok
test_zip_to_county_penghu (test_task2.TestTask2.test_zip_to_county_penghu) ... ok
test_zip_to_county_unknown (test_task2.TestTask2.test_zip_to_county_unknown) ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.509s

OK
```

**10/10 通過。**

### 修復過程摘要

1. **Red → 初步 Green（部分）**：建立 `task1_grouped_bar.py` 與 `task2_zipcode_heatmap.py`，`test_zip_to_county_*` 兩測試立即通過，其餘因路徑計算失誤（`parent` 層數少一層）仍失敗。
2. **路徑修正**：將 `DATA_DIR` 的 `Path(__file__).parent` 層數從 4 層修正為 5 層（實作檔），測試檔從 5 層修正為 6 層，所有 FileNotFoundError 消失。
3. **邏輯修正 `get_top_depts`**：函式原先回傳三年聯集（最多可達 24 項），違反 `assertLessEqual(len(top), top_n)` 約束，改為先取聯集後以六年合計排序，再截取 top_n 項。
