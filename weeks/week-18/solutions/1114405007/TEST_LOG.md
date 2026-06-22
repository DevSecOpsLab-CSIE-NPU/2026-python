# TEST_LOG.md

> 全部 54 項測試最終結果：
> ```
> Ran 54 tests in 0.002s
> OK
> ```

---

## 題1 資料清理（A區）

### Red
```
ImportError: No module named 'task1_sequence_clean'
Ran 1 test in 0.000s
FAILED (errors=1)
```
修改：建立 `task1_sequence_clean.py`

### Green
```
test_all_filtered_out ... ok
test_duplicates_removed ... ok
test_normal_case ... ok
test_single_divisible ... ok
test_single_not_divisible ... ok
test_solve_empty_input ... ok
test_solve_multiple_cases ... ok
test_negative_numbers ... ok
test_large_numbers ... ok
test_solve_empty_input (2) ... ok
test_single_group_all_match ... ok
test_single_group_none_match ... ok
test_three_groups ... ok
test_two_groups ... ok
----------------------------------------------------------------------
Ran 14 tests in 0.000s
OK
```

## 題2 凱撒密碼（A區）

### Red
```
ImportError: No module named 'task2_caesar_cipher'
FAILED (errors=1)
```
修改：建立 `task2_caesar_cipher.py`

### Green
```
test_empty_string ... ok
test_full_circle ... ok
test_lowercase_wrap ... ok
test_mixed_content_shift8 ... ok
test_non_letters_unchanged ... ok
test_sample_shift3 ... ok
test_uppercase_wrap ... ok
test_empty_input ... ok
test_single_line ... ok
test_two_lines ... ok
----------------------------------------------------------------------
Ran 10 tests in 0.000s
OK
```

## 題3 數字根（B區）

### Red
```
ImportError: No module named 'task3_digit_root'
FAILED (errors=1)
```
修改：建立 `task3_digit_root.py`

### Green
```
test_zero ... ok
test_single_digit_lt_base ... ok
test_two_digit_sum_lt_base ... ok
test_two_digit_sum_eq_base ... ok
test_three_digit ... ok
test_large_number ... ok
test_another_large ... ok
test_big_number ... ok
test_empty_input ... ok
test_multiple_with_base11 ... ok
test_sample_multi_line ... ok
test_single_line_zero ... ok
----------------------------------------------------------------------
Ran 12 tests in 0.000s
OK
```

## 題4 二分搜尋（C區）

### Red
```
ImportError: No module named 'task4_search_lab'
FAILED (errors=1)
```
修改：建立 `task4_search_lab.py`

### Green
```
test_empty_array ... ok
test_found_first ... ok
test_found_last ... ok
test_found_mid ... ok
test_not_found ... ok
test_single_element_found ... ok
test_single_element_not_found ... ok
test_comparison_count_found ... ok
test_comparison_count_not_found ... ok
test_size ... ok
test_sorted ... ok
test_size_zero ... ok
test_size_negative ... ok
----------------------------------------------------------------------
Ran 18 tests in 0.000s
OK
```
