# TEST_LOG

## Stage 1 — timeit

```
$ python -m unittest test_timing.py -v
test_exception_propagation ... ok
test_no_print_in_decorator ... ok
test_preserves_function_metadata ... ok
test_records_each_repeat_and_average ... ok
test_records_reset_on_each_call ... ok
test_rejects_float_repeat ... ok
test_rejects_invalid_repeat ... ok
test_repeat_one ... ok
test_returns_original_result ... ok
test_returns_original_result_different_types ... ok
test_works_without_parentheses ... ok
test_wraps_class_method ... ok
test_wraps_static_method ... ok
----------------------------------------------------------------------
Ran 13 tests in 0.094s
OK
```

## Stage 2 — 搜尋

```
$ python -m unittest test_search.py -v
test_does_not_mutate_data ... ok
test_empty_list ... ok
test_found_first_element ... ok
test_found_last_element ... ok
test_found_middle_element ... ok
test_not_found ... ok
test_rejects_non_list_data ... ok
test_single_element_found ... ok
test_single_element_not_found ... ok
test_unsorted_data_returns_minus_one ... ok
test_does_not_mutate_data ... ok
test_empty_list ... ok
test_found_first_element ... ok
test_found_last_element ... ok
test_found_middle_element ... ok
test_not_found ... ok
test_rejects_non_list_data ... ok
test_returns_first_occurrence_for_duplicates ... ok
test_single_element_found ... ok
test_single_element_not_found ... ok
test_target_none ... ok
----------------------------------------------------------------------
Ran 21 tests in 0.001s
OK
```
