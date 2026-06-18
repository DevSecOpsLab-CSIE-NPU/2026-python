# TEST_LOG.md — 0618 搜尋效能五階段專題

## Stage 1: timeit 裝飾器

```
test_preserves_function_metadata ... ok
test_repeat_below_one_raises_valueerror ... ok
test_repeat_records_and_average ... ok
test_returns_original_result ... ok
```

## Stage 2: 搜尋正確性

```
test_duplicate_values ... ok
test_empty_list ... ok
test_found_cases ... ok
test_input_not_mutated ... ok
test_not_found_cases ... ok
```

## Stage 3: Benchmark

```
    size     linear     binary        set         in     bisect
    1000   0.000027   0.000002   0.000020   0.000007   0.000001
    5000   0.000115   0.000002   0.000493   0.000028   0.000001
   20000   0.000080   0.000004   0.003786   0.000038   0.000001
   80000   0.000207   0.000003   0.009091   0.000098   0.000001
```

## Stage 4: 雷達圖

```
assets/radar.png saved
```

## Stage 5: 安全性

```
test_load_uses_json_not_pickle ... ok
test_make_data_rejects_negative ... ok
test_results_file_closed ... ok
```

## 全部測試總覽

```
$ python -m unittest discover -p "test_*.py" -v
...
Ran 14 tests in 0.007s
OK
```
