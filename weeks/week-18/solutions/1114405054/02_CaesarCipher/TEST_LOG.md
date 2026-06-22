# CaesarCipher 測試紀錄

## 測試指令
```bash
python -m unittest test_caesar_cipher.py
```

## 測試結果
```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```

## 測試案例

| 測試名稱 | 目的 |
|---|---|
| test_mixed_case_with_punctuation | 驗證大小寫混合與標點 |
| test_upper_and_lower | 驗證大小寫分開循環 |
| test_wrap_around_uppercase_V | 驗證 V 移 5 位繞回 A |
| test_wrap_around_uppercase_Z | 驗證 Z 移 5 位繞回 E |
| test_non_letters_unchanged | 驗證非字母字元保留 |
