# DigitalRoot 測試紀錄

## 測試指令
```bash
python -m unittest test_digital_root.py
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
| test_zero | 驗證輸入 0 回傳 0 |
| test_eight | 驗證 8 → 4 |
| test_sixty_three | 驗證 63 → 3（多輪轉換） |
| test_equal_to_base | 驗證 5 → 1 |
| test_single_digit | 驗證個位數不轉換 |
