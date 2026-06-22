# Test Log - Q3: Digit Root (Base 16)

## Red 階段

```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```

- **測試數**: 9 | **通過**: 0 | **失敗**: 9
- **說明**: 測試已寫，實作未完成。

## Green 階段

```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```

```
test_hex_abc ... ok
test_invalid_negative ... ok
test_invalid_negative_large ... ok
test_large_number ... ok
test_power_of_16 ... ok
test_random_value ... ok
test_single_digit ... ok
test_two_hex_digits ... ok
test_zero ... ok
----------------------------------------------------------------------
Ran 9 tests in 0.000s
OK
```

- **通過**: 9 | **失敗**: 0

### 修改
- 公式 `1 + (n - 1) % 15` 計算 base-16 數字根
- 首次測試 `digit_root_base16(100) == 1` 寫錯（正確為 10），修正後全綠
