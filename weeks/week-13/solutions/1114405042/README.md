# Week 13 回家作業：招生資料視覺化分析

本目錄包含了第 13 週「招生資料視覺化分析」作業的解答。

## 目錄結構

- `task1_grouped_bar.py`: 繪製 112、113、114 學年度各系招生人數的三年並排長條圖。
- `task2_zipcode_heatmap.py`: 繪製 109-114 學年度全校招生來源縣市的熱力圖。
- `output/`: 自動生成的圖表結果。
  - `task1.png`: 三年並排長條圖。
  - `task2.png`: 來源縣市熱力圖。
- `tests/`: 包含對上述兩個任務的單元測試 (`unittest`)。
- `TEST_LOG.md`: 測試的 Red → Green 執行紀錄。
- `REPORT.md`: 資料分析觀察與心得。
- `AI_USAGE.md`: AI 輔助使用紀錄。

## 執行方式

請在命令列中執行以下指令來生成圖表：

```bash
python3 task1_grouped_bar.py
python3 task2_zipcode_heatmap.py
```

執行測試：

```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```
