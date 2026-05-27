# Week 13 Submission

## 內容

- `task1_grouped_bar.py`：112～114 學年度三年並排長條圖
- `task2_zipcode_heatmap.py`：109～114 學年度來源縣市熱力圖
- `tests/`：兩題的 unittest
- `REPORT.md`：三題分析回答
- `TEST_LOG.md`：Red → Green 測試紀錄
- `AI_USAGE.md`：AI 使用說明

## 執行方式

在此資料夾執行：

```bash
python3 task1_grouped_bar.py
python3 task2_zipcode_heatmap.py
python3 -m unittest discover -s tests -p "test_*.py" -v
```

執行後會在 `output/` 產生：

- `output/task1.png`
- `output/task2.png`

## 依賴套件

- `matplotlib`

其餘皆為 Python 標準函式庫。