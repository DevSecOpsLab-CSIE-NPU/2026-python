# TEST_LOG - search & timing

## 執行指令
```
python -m unittest discover -s tests -p "test_*.py" -v
```

## 測試輸出
```
(已省略先前其他測試，只列新新增測試部分)
test_binary_search_found ... ok
test_binary_search_not_found ... ok
test_linear_search_found ... ok
test_linear_search_not_found ... ok
test_set_search ... ok
test_timeit_decorator_records ... ok
test_timeit_repeat_validation ... ok

Ran 19 tests in 0.002s

OK
```

## 說明
- 新增 `search.py`、`timing.py`、`plot.py` 與對應測試。
- `timing.timeit` 裝飾器已實作，支援 `repeat` 參數並記錄 `records` 與 `last_elapsed`。
- `plot.draw_radar` 可產生 `assets/radar.png`（在無視窗環境使用 `Agg`）。
