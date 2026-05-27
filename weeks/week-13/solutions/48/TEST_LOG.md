# TEST LOG

## Red

- 先跑 `python -m unittest discover -s tests -p "test_*.py" -v`，測試在匯入 `matplotlib` 時失敗，環境尚未安裝繪圖套件。
- 補裝 `matplotlib` 後再次執行，同一組測試又因資料路徑少了一層父目錄而失敗。

## Green

- 修正兩支程式的 `DATA_DIR` 指向專案根目錄後，重新執行同一個 unittest 指令，全數通過。
- 另外執行 `python task1_grouped_bar.py` 與 `python task2_zipcode_heatmap.py`，成功產生 `output/task1.png` 與 `output/task2.png`。