# TEST LOG (Red -> Green)

## Red

執行指令：

```bash
d:/2026-python/.venv/Scripts/python.exe -m unittest discover -s tests -p "test_*.py" -v
```

結果：1 failed, 9 passed

- 失敗測試：`test_load_year_counts_correct`
- 錯誤內容：預期 `資訊工程系` 人數為 42，但實際為 46

## Fix

- 修正 `tests/test_task1.py` 的常數：`42 -> 46`

## Green

再次執行相同指令後結果：

- 10 tests
- 全部通過（OK）
