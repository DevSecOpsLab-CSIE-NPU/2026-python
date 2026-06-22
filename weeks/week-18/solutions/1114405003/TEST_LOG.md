# TEST_LOG - 第一題 資料清理

## 測試環境
- Python 3.12
- unittest 框架
- 測試日期: 2026/06/22

## 測試結果

```
test_all_duplicates (test_data_cleaning.TestDataCleaning.test_all_duplicates)
全部重複，去重後只剩一個 ... ok
test_already_sorted (test_data_cleaning.TestDataCleaning.test_already_sorted)
已排序的輸入 ... ok
test_d_equals_1 (test_data_cleaning.TestDataCleaning.test_d_equals_1)
D=1 時所有數都保留 ... ok
test_d_equals_2 (test_data_cleaning.TestDataCleaning.test_d_equals_2)
D=2 只保留偶數 ... ok
test_empty_after_filter (test_data_cleaning.TestDataCleaning.test_empty_after_filter)
全部被過濾掉 ... ok
test_large_numbers (test_data_cleaning.TestDataCleaning.test_large_numbers)
大數 ... ok
test_negative_numbers (test_data_cleaning.TestDataCleaning.test_negative_numbers)
含負數 ... ok
test_preserve_first_occurrence (test_data_cleaning.TestDataCleaning.test_preserve_first_occurrence)
去重時保留第一次出現的順序 ... ok
test_reverse_sorted (test_data_cleaning.TestDataCleaning.test_reverse_sorted)
反向排序的輸入 ... ok
test_sample_1 (test_data_cleaning.TestDataCleaning.test_sample_1)
範例測資1: 去重+篩選+排序 -> NONE ... ok
test_sample_2 (test_data_cleaning.TestDataCleaning.test_sample_2)
範例測資2: 去重+篩選+排序 -> [5] ... ok
test_single_element (test_data_cleaning.TestDataCleaning.test_single_element)
n=1 單一元素 ... ok
test_single_element_filtered (test_data_cleaning.TestDataCleaning.test_single_element_filtered)
n=1 單一元素被過濾 ... ok
test_zero (test_data_cleaning.TestDataCleaning.test_zero)
含0，0能被任何數整除 ... ok

----------------------------------------------------------------------
Ran 14 tests in 0.003s

OK
```

## 主程式測試

輸入:
```
8
4 7 4 2 9 2 6 7
3
1 3 5
0
```

輸出:
```
NONE
5
```

符合預期！
