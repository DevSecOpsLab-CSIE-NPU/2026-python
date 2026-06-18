# TEST_LOG

## 測試環境
- Python 版本: 3.14.0
- 執行指令: `python -m unittest test_square_counter.py`

## 測試結果
```text
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

## 測試案例說明
1. `test_basic_case`: 驗證區間 [1, 10] 有 3 個平方數 (1, 4, 9)。
2. `test_edge_case`: 驗證 [1, 1] 與 [100, 100] 等單點區間。
3. `test_exception`: 驗證當 a > b 時拋出 `ValueError`。
