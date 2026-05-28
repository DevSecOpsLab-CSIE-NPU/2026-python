# TEST LOG

## Red

- 先執行 `python tests/test_task1.py; python tests/test_task2.py`，結果全部失敗。
- 失敗原因是 `DATA_DIR` 少跳一層，程式去找 `weeks/assets/stu-data`，所以找不到 CSV。

## Green

- 修正 `DATA_DIR` 後重新執行同一組測試，兩份 unittest 全部通過。
- 後續再執行 `task1_grouped_bar.py` 與 `task2_zipcode_heatmap.py`，確認可正常產生圖檔。