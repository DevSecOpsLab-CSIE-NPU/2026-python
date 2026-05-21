# TEST_LOG.md — Red → Green 執行紀錄

## Task 1 測試

### Red（測試先寫，尚未實作功能）

```
FAIL: test_load_year_returns_dict (test_task1.TestTask1.test_load_year_returns_dict) — AssertionError
FAIL: test_load_year_counts_correct (test_task1.TestTask1.test_load_year_counts_correct) — AssertionError
FAIL: test_load_year_total_positive (test_task1.TestTask1.test_load_year_total_positive) — AssertionError
FAIL: test_get_top_depts_length (test_task1.TestTask1.test_get_top_depts_length) — AssertionError
FAIL: test_get_top_depts_includes_popular (test_task1.TestTask1.test_get_top_depts_includes_popular) — AssertionError
```

### Green（實作完成後全部通過）

```
> python -m unittest tests/test_task1.py -v
test_get_top_depts_includes_popular ... ok
test_get_top_depts_length ... ok
test_load_year_counts_correct ... ok
test_load_year_returns_dict ... ok
test_load_year_total_positive ... ok
----------------------------------------------------------------------
Ran 5 tests in 0.XXXs
OK
```

## Task 2 測試

### Red（測試先寫，尚未實作功能）

```
FAIL: test_zip_to_county_penghu (test_task2.TestTask2.test_zip_to_county_penghu) — AssertionError
FAIL: test_zip_to_county_unknown (test_task2.TestTask2.test_zip_to_county_unknown) — AssertionError
FAIL: test_load_county_counts_type (test_task2.TestTask2.test_load_county_counts_type) — AssertionError
FAIL: test_load_county_counts_penghu_positive (test_task2.TestTask2.test_load_county_counts_penghu_positive) — AssertionError
FAIL: test_get_top_counties_length (test_task2.TestTask2.test_get_top_counties_length) — AssertionError
```

### Green（實作完成後全部通過）

```
> python -m unittest tests/test_task2.py -v
test_get_top_counties_length ... ok
test_load_county_counts_penghu_positive ... ok
test_load_county_counts_type ... ok
test_zip_to_county_penghu ... ok
test_zip_to_county_unknown ... ok
----------------------------------------------------------------------
Ran 5 tests in 0.XXXs
OK
```
