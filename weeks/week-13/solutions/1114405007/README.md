# Week 13 Homework - 1114405007

本作業完成兩個視覺化分析任務：

- Task 1：112~114 年各系招生人數三年並排長條圖
- Task 2：109~114 年來源縣市熱力圖（郵遞區號前 3 碼對照）
- 自由觀察：觀休人最多

## 檔案說明

- `task1_grouped_bar.py`：Task 1 程式
- `task2_zipcode_heatmap.py`：Task 2 程式
- `tests/test_task1.py`：Task 1 單元測試
- `tests/test_task2.py`：Task 2 單元測試
- `output/task1.png`：Task 1 圖檔
- `output/task2.png`：Task 2 圖檔
- `TEST_LOG.md`：Red -> Green 測試紀錄
- `REPORT.md`：資料分析心得
- `AI_USAGE.md`：AI 使用紀錄

## 執行方式

在此目錄執行：

```bash
python task1_grouped_bar.py
python task2_zipcode_heatmap.py
python -m unittest discover -s tests -p "test_*.py" -v
```
