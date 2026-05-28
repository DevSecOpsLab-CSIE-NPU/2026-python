# Week 13 Homework Solution

本資料夾包含 Week 13 回家作業的兩個任務實作與測試。

## 檔案結構

- `task1_grouped_bar.py`：Task 1 三年並排長條圖
- `task2_zipcode_heatmap.py`：Task 2 來源縣市熱力圖
- `tests/test_task1.py`：Task 1 單元測試
- `tests/test_task2.py`：Task 2 單元測試
- `output/task1.png`：Task 1 輸出圖
- `output/task2.png`：Task 2 輸出圖
- `TEST_LOG.md`：Red → Green 測試紀錄
- `REPORT.md`：資料觀察與分析
- `AI_USAGE.md`：AI 協作說明

## 執行方式

在本目錄下執行：

```bash
d:/2026-python/.venv/Scripts/python.exe task1_grouped_bar.py
d:/2026-python/.venv/Scripts/python.exe task2_zipcode_heatmap.py
d:/2026-python/.venv/Scripts/python.exe -m unittest discover -s tests -p "test_*.py" -v
```

## 實作重點

- Task 1：
  - 讀取 112～114 年 CSV，統計各系招生人數
  - 篩出三年中熱門系所（最多 8 個）
  - 畫出 grouped horizontal bar chart
- Task 2：
  - 使用郵遞區號前三碼對應縣市
  - 統計 109～114 年各縣市人數
  - 取 6 年累計前 10 縣市畫出 heatmap
