## Task 1

### Red（失敗紀錄）
執行指令：python -m unittest tests/test_task1.py -v
結果：
  ERROR test_load_year_returns_dict
  ImportError: cannot import name 'load_year'
  Ran 1 test in 0.001s — FAILED

失敗原因：load_year 尚未實作

### Green（通過紀錄）
執行指令：python -m unittest tests/test_task1.py -v
結果：
  test_get_top_depts_includes_popular ... ok
  test_get_top_depts_length ... ok
  test_load_year_counts_correct ... ok
  test_load_year_returns_dict ... ok
  test_load_year_total_positive ... ok
  Ran 5 tests in 0.050s — OK

讓測試通過的關鍵修改：實作 load_year（讀取 CSV 並統計各系人數）與 get_top_depts（找出任一年前 8 名的系所）

## Task 2

### Red（失敗紀錄）
執行指令：python -m unittest tests/test_task2.py -v
結果：
  ERROR test_zip_to_county_penghu
  ImportError: cannot import name 'zip_to_county'
  Ran 1 test in 0.001s — FAILED

失敗原因：zip_to_county 尚未實作

### Green（通過紀錄）
執行指令：python -m unittest tests/test_task2.py -v
結果：
  test_get_top_counties_length ... ok
  test_load_county_counts_penghu_positive ... ok
  test_load_county_counts_type ... ok
  test_zip_to_county_penghu ... ok
  test_zip_to_county_unknown ... ok
  Ran 5 tests in 0.062s — OK

讓測試通過的關鍵修改：實作 zip_to_county、load_county_counts、get_top_counties 三個函式
