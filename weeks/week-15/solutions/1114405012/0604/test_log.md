# 0604 平方數計數 - 測試執行日誌

## 2026-06-04：單元測試

執行指令：
`cd "/Users/yehallen/Desktop/暫存檔案/2026-python/weeks/week-15/solutions/1114405012/0604" && /Users/yehallen/Desktop/暫存檔案/.venv/bin/python -m unittest`

結果：
```text
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

## 2026-06-04：手動驗證

執行內容：
- `count_squares(1, 10)` 回傳 `3`
- `count_squares(1, 1)` 回傳 `1`
- `count_squares(5, 2)` 會丟出 `ValueError("a must be <= b")`

結果：
- 以上情況皆符合 0604 作業題目要求
