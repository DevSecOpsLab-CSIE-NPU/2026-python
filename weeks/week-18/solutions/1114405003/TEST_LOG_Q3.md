# TEST_LOG - 第三題 任意進位的數字根

## 測試環境
- Python 3.12
- unittest 框架
- 測試日期: 2026/06/22
- base = 3

## 測試結果

```
test_base_2 ... ok
test_base_8 ... ok
test_edge_case_1 ... ok
test_edge_case_base_16 ... ok
test_edge_case_exact_single_digit_in_base ... ok
test_large_number ... ok
test_repeated_sum ... ok
test_sample_0 ... ok
test_sample_63 ... ok
test_sample_8 ... ok
test_single_digit ... ok
test_sum_digits ... ok
test_to_base_conversion ... ok

----------------------------------------------------------------------
Ran 13 tests in 0.001s

OK
```

## 主程式測試

輸入:
```
0
8
63
```

輸出:
```
0
2
1
```

符合預期！
