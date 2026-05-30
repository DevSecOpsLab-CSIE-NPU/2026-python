# 測試紀錄 (TEST LOG)

## Red 階段紀錄
在完成函式實作前，僅先撰寫了 test_task1.py 與 test_task2.py 測試檔並執行：
```bash
$ python3 -m unittest discover -s tests -p "test_*.py" -v
...
ImportError: cannot import name 'DATA_DIR' from 'task1_grouped_bar'
```
(或回傳 `NotImplementedError` / 找不到函式等錯誤，導致 10 個測試案例出現 Failed 與 Error)

## Green 階段紀錄
在完成 `task1_grouped_bar.py` 及 `task2_zipcode_heatmap.py` 等函式實作與重構後，測試通過：
```bash
$ python3 -m unittest discover -s tests -p "test_*.py" -v
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
Ran 10 tests in 0.021s

OK
```
成功達到 Green 狀態！
