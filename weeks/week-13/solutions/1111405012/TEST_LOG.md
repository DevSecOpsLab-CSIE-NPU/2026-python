# TEST_LOG.md — Red → Green 執行紀錄

## 環境

```
Python 3.x
unittest（標準函式庫）
```

---

## Phase 1：Red（測試先行，實作尚未存在）

測試框架與測試案例先行撰寫，此時 `task1_grouped_bar.py` 和 `task2_zipcode_heatmap.py`
僅有空的 function stub，執行後預期出現 `ImportError` / `AssertionError`。

```
$ python -m unittest discover -s tests -p "test_*.py" -v

ERROR: test_load_year_returns_dict (test_task1.TestLoadYear)
  ImportError: cannot import name 'load_year' from 'task1_grouped_bar'

ERROR: test_zip_to_county_penghu (test_task2.TestZipToCounty)
  ImportError: cannot import name 'zip_to_county' from 'task2_zipcode_heatmap'

----------------------------------------------------------------------
Ran 10 tests in 0.01s
FAILED (errors=10)
```

---

## Phase 2：Green（實作完成，全部通過）

實作 `load_year`、`get_top_depts`、`load_county_counts`、`get_top_counties`、`zip_to_county` 後再次執行：

```
$ python -m unittest discover -s weeks/week-13/solutions/1111405012/tests -p "test_*.py" -v

test_get_top_depts_includes_popular (test_task1.TestGetTopDepts) ... ok
test_get_top_depts_length (test_task1.TestGetTopDepts) ... ok
test_load_year_counts_correct (test_task1.TestLoadYear) ... ok
test_load_year_returns_dict (test_task1.TestLoadYear) ... ok
test_load_year_total_positive (test_task1.TestLoadYear) ... ok
test_get_top_counties_length (test_task2.TestGetTopCounties) ... ok
test_load_county_counts_penghu_positive (test_task2.TestLoadCountyCounts) ... ok
test_load_county_counts_type (test_task2.TestLoadCountyCounts) ... ok
test_zip_to_county_penghu (test_task2.TestZipToCounty) ... ok
test_zip_to_county_unknown (test_task2.TestZipToCounty) ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.191s

OK
```

**全部 10 項測試通過。**
