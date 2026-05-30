# Week 13 HOMEWORK: 招生資料視覺化分析

本目錄為 Week 13 的作業，主要內容為使用 `matplotlib` 進行新生資料庫的資料視覺化實作。包含兩個 Task 的腳本、產出來的圖表 (`output/`)、單元測試 (`tests/`) 與各種分析報告。

## 執行方式
需安裝相關套件 (`matplotlib`, `numpy`) 後執行腳本：
```bash
python3 task1_grouped_bar.py
python3 task2_zipcode_heatmap.py
```
執行後會於 `output/` 目錄中生成 `task1.png` 與 `task2.png`。

## 測試方式
使用 Python 內建的 unittest：
```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```

## 目錄結構
- `task1_grouped_bar.py`: 分析各系三年的人數，生成群組長條圖
- `task2_zipcode_heatmap.py`: 分析縣市與年份人數變化，生成熱力圖
- `/tests`: 以上兩個腳本的單元測試
- `/output`: 自動匯出的圖表 PNG
- `REPORT.md`: 作業規定須回答的問題探討心得
- `TEST_LOG.md`: 執行的 Test-Driven Development (TDD) 紅綠燈結果紀錄
- `AI_USAGE.md`: AI 使用說明
