# TEST LOG

## Red Phase

執行指令：
```bash
python -m unittest test_main -v
```

結果：
```text
ModuleNotFoundError: No module named 'main'
```

測試總數：10
通過：0
失敗：10

修正方式：建立新的獨立資料夾版本，加入 `main.py` 與對應測試。

## Green Phase

執行指令：
```bash
python -m unittest test_main -v
```

結果：
```text
OK
```

測試總數：10
通過：10
失敗：0