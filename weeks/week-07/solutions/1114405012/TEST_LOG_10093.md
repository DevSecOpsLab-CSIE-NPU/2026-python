# TEST_LOG_10093

## Red

- 執行指令：`python3 -m unittest discover -s tests -p 'test_*.py' -v`
- 結果：10093 相關測試失敗（程式例外）
- 失敗原因：`10093.py` 與測試使用了 `int.bit_count()`，在 Python 3.9 環境不支援。

## Green

- 執行指令：`python3 -m unittest tests.test_10093 -v`
- 結果：共 2 個測試，通過 2 個，失敗 0 個
- 修改內容：將 `bit_count()` 改為 `bin(x).count('1')`，修正 Python 3.9 相容性後全數通過。
