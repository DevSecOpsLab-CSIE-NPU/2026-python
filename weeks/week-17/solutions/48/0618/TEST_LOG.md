# 測試執行紀錄 (TEST_LOG.md)

## 執行指令

```
python -m unittest discover -p "test_*.py" -v
```

## 測試結果 (全部 18 項)

```
test_png_exists_and_nonempty (test_plot.TestRadarPlot) ... ok
test_binary_search_exact_index (test_search.TestSearchFunctions) ... ok
test_found_cases (test_search.TestSearchFunctions) ... ok
test_input_not_mutated (test_search.TestSearchFunctions) ... ok
test_linear_search_exact_index (test_search.TestSearchFunctions) ... ok
test_none_input_raises_typeerror (test_search.TestSearchFunctions) ... ok
test_not_found_cases (test_search.TestSearchFunctions) ... ok
test_plot_closes_figure (test_security.TestSecurity) ... ok
test_search_rejects_non_list_data (test_security.TestSecurity) ... ok
test_timeit_rejects_bool_repeat (test_security.TestSecurity) ... ok
test_default_repeat_is_three (test_timing.TestTimeit) ... ok
test_exception_pass_through (test_timing.TestTimeit) ... ok
test_non_integer_repeat_type_error (test_timing.TestTimeit) ... ok
test_preserves_function_metadata (test_timing.TestTimeit) ... ok
test_repeat_below_one_raises_valueerror (test_timing.TestTimeit) ... ok
test_repeat_records_and_average (test_timing.TestTimeit) ... ok
test_returns_original_result (test_timing.TestTimeit) ... ok
test_timing_records_positive (test_timing.TestTimeit) ... ok
----------------------------------------------------------------------
Ran 18 tests in 0.607s
OK
```

## 各階段測試涵蓋

| Stage | 測試檔案 | 測試數 |
|:-----|:---------|:------:|
| 1 — `@timeit` 裝飾器 | `test_timing.py` | 8 |
| 2 — 三種搜尋 | `test_search.py` | 6 |
| 3 — 加速實驗 | (無測試) | — |
| 4 — 雷達圖 | `test_plot.py` | 1 |
| 5 — 安全性 | `test_security.py` | 3 |
| **總計** | | **18** |
