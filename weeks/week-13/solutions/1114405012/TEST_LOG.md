# 測試紀錄

## Red 階段

- 指令：`python3 -m unittest discover -s tests -p "test_*.py" -v`
- 結果：發生 `ModuleNotFoundError: No module named 'task1_grouped_bar'` 與 `ModuleNotFoundError: No module named 'task2_zipcode_heatmap'`

## Green 階段

- 指令：`python3 -m unittest discover -s tests -p "test_*.py" -v`
- 結果：10 個測試全部通過

## 輸出確認

- 指令：`python3 task1_grouped_bar.py && python3 task2_zipcode_heatmap.py`
- 結果：成功產生 `output/task1.png` 與 `output/task2.png`