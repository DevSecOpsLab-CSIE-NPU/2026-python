# TEST_LOG

## 測試環境
- Python 版本: 3.14.0
- 執行指令: `python -m unittest test_gcd.py`

## 測試結果
```text
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

## 測試案例說明
1. `test_n_equals_2`: 驗證 N=2 時 GCD 總和為 1 (符合題目範例)。
2. `test_n_equals_10`: 驗證 N=10 時 GCD 總和為 67 (符合題目範例)。
3. `test_edge_case_n1`: 驗證 N=1 時回傳 0 (邊界條件)。
