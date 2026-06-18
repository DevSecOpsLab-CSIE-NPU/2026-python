# TEST_LOG

## 1) 單元測試

執行指令:

```bash
python -m unittest -v
```

結果摘要:

- 共 8 個測試
- 全部通過（OK）

## 2) 搜尋效能量測

執行指令:

```bash
python -c "from timing import timeit; from search import linear_search,binary_search; import random; n=200000; data=list(range(n)); random.shuffle(data); target=n-1; sorted_data=sorted(data); run_linear=timeit(repeat=5)(lambda: linear_search(sorted_data,target)); run_binary_only=timeit(repeat=5)(lambda: binary_search(sorted_data,target)); run_sort_plus_binary=timeit(repeat=5)(lambda: binary_search(sorted(data),target)); run_linear(); run_binary_only(); run_sort_plus_binary(); print('linear avg', run_linear.last_elapsed, 'records', run_linear.records); print('binary avg', run_binary_only.last_elapsed, 'records', run_binary_only.records); print('sort+binary avg', run_sort_plus_binary.last_elapsed, 'records', run_sort_plus_binary.records)"
```

量測結果:

- linear avg: `0.00632875997107476`
- binary avg: `3.520003519952297e-06`
- sort+binary avg: `0.038722000038251284`

備註:

- 初次測試曾因浮點數精度導致 `test_records_each_repeat_and_average` 失敗。
- 已改為 `assertAlmostEqual` 後通過。
