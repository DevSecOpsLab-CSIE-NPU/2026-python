# TEST_LOG.md

## 0617 預演：timeit + 搜尋效能評估

### Unit Test 結果

執行 `python -m unittest test_timing.py -v`

```
test_preserves_function_metadata (test_timing.TestTimeit.test_preserves_function_metadata) ... ok
test_records_each_repeat_and_average (test_timing.TestTimeit.test_records_each_repeat_and_average) ... ok
test_rejects_invalid_repeat (test_timing.TestTimeit.test_rejects_invalid_repeat) ... ok
test_repeat_one_records_single_value (test_timing.TestTimeit.test_repeat_one_records_single_value) ... ok
test_returns_original_result (test_timing.TestTimeit.test_returns_original_result) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

### Benchmark 結果

執行 `python benchmark.py`

```
Data size: 1000000
Target: 350213

linear_search: avg=0.024886s
  records: [0.02005079999798909, 0.026488400006201118, 0.02369980001822114, 0.028061200049705803, 0.02612799999769777]
binary_search: avg=0.000010s
  records: [2.0700041204690933e-05, 8.500006515532732e-06, 6.999995093792677e-06, 5.800044164061546e-06, 5.999987479299307e-06]
```

### 結論

- binary_search 比 linear_search 快約 2500 倍
- 5 次 repeat 的紀錄顯示 binary 非常穩定（6~20µs），linear 波動較大（20~28ms）
