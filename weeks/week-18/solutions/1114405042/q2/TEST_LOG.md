# Test Log - Q2: Caesar Cipher (SHIFT=3)

## Red 階段

```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```

- **測試總數**: 9
- **通過數**: 0
- **失敗數**: 9
- **說明**: 測試已寫，實作未完成。

## Green 階段

```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```

```
test_empty_string ... ok
test_example_abc_xyz ... ok
test_example_hello_npu ... ok
test_full_alphabet_lower ... ok
test_full_alphabet_upper ... ok
test_mixed_content ... ok
test_non_alpha_unchanged ... ok
test_wraparound_lowercase ... ok
test_wraparound_uppercase ... ok
----------------------------------------------------------------------
Ran 9 tests in 0.001s
OK
```

- **通過數**: 9 | **失敗數**: 0

### 修改說明
- `chr((ord(ch) - base + SHIFT) % 26 + base)` 實現字母循環位移
- 大寫小寫分開處理，非字母保留
