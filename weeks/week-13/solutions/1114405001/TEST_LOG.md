# TEST LOG

## Red

- 先寫 `tests/test_task1.py` 與 `tests/test_task2.py`，初次執行 `python -m unittest discover -s tests -v` 時因 `DATA_DIR` 路徑少一層目錄而失敗。

## Green

- 修正 `task1_grouped_bar.py` 與 `task2_zipcode_heatmap.py` 的資料路徑後，重新執行 `python -m unittest discover -s tests -v`，10 個測試全數通過。