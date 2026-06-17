# TEST_LOG — 0617 測試紀錄

## 任務一 timing.py

```
$ python -m unittest test_timing.py -v
test_preserves_exception ... ok
test_preserves_function_metadata ... ok
test_records_each_repeat_and_average ... ok
test_rejects_invalid_repeat ... ok
test_returns_original_result ... ok
----------------------------------------------------------------------
Ran 5 tests in 0.000s
OK
```

## 任務二 search.py

```
$ python -m unittest test_search.py -v
test_empty_list_returns_minus_one ... ok
test_finds_target_in_sorted ... ok
test_rejects_none_data ... ok
test_returns_minus_one_when_not_found ... ok
test_empty_list_returns_minus_one ... ok
test_finds_target_at_beginning ... ok
test_finds_target_at_end ... ok
test_finds_target_in_middle ... ok
test_rejects_none_data ... ok
test_returns_minus_one_when_not_found ... ok
----------------------------------------------------------------------
Ran 10 tests in 0.000s
OK
```

## 效能評估

```
       n   linear (s)   binary (s)      ratio
--------------------------------------------
    1000   0.00000229   0.00000077       2.97x
    5000   0.00003940   0.00000105      37.60x
   10000   0.00024349   0.00000105     230.79x
   50000   0.00062580   0.00000101     619.60x
```
