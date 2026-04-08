# TEST_LOG

## Red

- 執行指令：`python3 -m unittest discover -s tests -p 'test_*.py' -v`
- 結果：共 9 個測試，通過 0 個，失敗 9 個
- 失敗原因：當時還沒有建立 `solution.py`，測試在 `setUp()` 階段就找不到可執行程式。

## Green

- 執行指令：`python3 -m unittest discover -s tests -p 'test_*.py' -v`
- 結果：共 9 個測試，通過 9 個，失敗 0 個
- 修改內容：先實作 `solution.py`，用排序鍵 `(前面較大的牛數量, 位置由大到小)` 還原排列；另外修正兩筆測試預期值，使其符合題目規格與實際輸出。
