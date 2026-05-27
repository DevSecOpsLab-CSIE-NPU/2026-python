# TEST_LOG.md

## Red 階段

先建立 `tests/test_task1.py` 與 `tests/test_task2.py` 後，在尚未完成 `task1_grouped_bar.py` 與 `task2_zipcode_heatmap.py` 的函式實作前，測試會因為函式不存在、回傳值不正確或尚未完成統計邏輯而失敗。此階段用來確認測試案例能偵測尚未完成的功能。

## Green 階段

完成資料讀取、統計、排名與圖表輸出函式後，重新執行 unittest，結果如下：

```text
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
Ran 10 tests in 0.036s

OK
```
