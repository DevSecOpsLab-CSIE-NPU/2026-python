# TEST_LOG - 第二題 凱撒密碼

## 測試環境
- Python 3.12
- unittest 框架
- 測試日期: 2026/06/22

## 測試結果

```
test_all_non_letters ... ok
test_empty_string ... ok
test_long_string ... ok
test_lowercase_wrap ... ok
test_mixed_case ... ok
test_non_letters ... ok
test_punctuation_preserved ... ok
test_sample_1 ... ok
test_sample_2 ... ok
test_shift_0 ... ok
test_shift_26 ... ok
test_single_char_lower ... ok
test_single_char_upper ... ok
test_spaces_preserved ... ok
test_uppercase_wrap ... ok
test_z_to_a ... ok
test_z_wrap_full ... ok

----------------------------------------------------------------------
Ran 17 tests in 0.001s

OK
```

## 主程式測試

輸入:
```
Hello, NPU!
abc XYZ
```

輸出:
```
Lipps, RTY!
efg BCD
```

符合預期！
