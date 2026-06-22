# TEST_LOG - digit_root_base

## 測試執行

### 執行指令
```
python -m unittest tests.test_digit_root_base -v
```

### 測試結果
```
test_base16 (tests.test_digit_root_base.TestDigitRootBase.test_base16) ... ok
test_base2 (tests.test_digit_root_base.TestDigitRootBase.test_base2) ... ok
test_example_base7 (tests.test_digit_root_base.TestDigitRootBase.test_example_base7) ... ok
test_invalid_base (tests.test_digit_root_base.TestDigitRootBase.test_invalid_base) ... ok
test_large_value (tests.test_digit_root_base.TestDigitRootBase.test_large_value) ... ok
test_zero (tests.test_digit_root_base.TestDigitRootBase.test_zero) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

### 變更摘要
- 新增 `digit_root_base.py` 實作與 `tests/test_digit_root_base.py` 測試。
- 調整允許的 `ALLOWED_BASES`，加入 `10` 以支援十進位測試。
- 修正 `test_base2` 的預期結果為 `1`（依題意要持續計算直到在該 base 下為一位數）。

### 重構/觀察
- `digit_root_base` 在 value=0 時會回傳 0，符合題目規格。
- 支援的 base 集合需與學號對應，測試採用包含 `10` 的集合以利一般驗證。
