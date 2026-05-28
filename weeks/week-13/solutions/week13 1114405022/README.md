# Week 13 作業說明

這份解答包含兩個分析腳本：

- `task1_grouped_bar.py`：讀取 112、113、114 學年度資料，畫出各系招生人數的三年並排長條圖。
- `task2_zipcode_heatmap.py`：讀取 109～114 學年度資料，將郵遞區號前 3 碼轉成縣市後，畫出縣市 × 年份熱力圖。

## 執行方式

在此資料夾內執行：

```bash
python task1_grouped_bar.py
python task2_zipcode_heatmap.py
```

執行後會在 `output/` 產生 `task1.png` 與 `task2.png`。

## 測試方式

```bash
python tests/test_task1.py
python tests/test_task2.py
```

## 檔案說明

- `REPORT.md`：三題資料分析文字說明。
- `TEST_LOG.md`：Red → Green 測試紀錄。
- `AI_USAGE.md`：AI 使用說明。