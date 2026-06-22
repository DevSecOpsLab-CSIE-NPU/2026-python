# DataCleaning 測試紀錄

## 測試指令
```bash
python -m unittest test_data_cleaning.py
```

## 測試結果
```
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

## 測試案例

| 測試名稱 | 目的 |
|---|---|
| test_normal_dedupe_and_filter | 驗證基本去重與偶數篩選 |
| test_all_odd_returns_empty | 驗證全奇數回傳空 list |
| test_negatives_and_zero | 驗證負數與 0 的處理 |
| test_repeated_even_numbers | 驗證重複偶數的去重 |
