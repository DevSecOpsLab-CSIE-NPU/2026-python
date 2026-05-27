# Week 13 招生資料視覺化分析

## 學號

1114405013

## 作業內容

本作業使用 `assets/stu-data` 中的 109～114 學年度新生資料，完成兩個視覺化分析：

1. `task1_grouped_bar.py`：比較 112、113、114 學年度各系招生人數，輸出三年並排長條圖。
2. `task2_zipcode_heatmap.py`：將郵遞區號前三碼轉換為縣市，統計 109～114 學年度新生來源縣市，輸出縣市 × 年份熱力圖。

## 執行方式

```bash
cd weeks/week-13/solutions/1114405013
python task1_grouped_bar.py
python task2_zipcode_heatmap.py
python -m unittest discover -s tests -p "test_*.py" -v
```

## 輸出檔案

```text
output/task1.png
output/task2.png
```

## 設計說明

- 使用 `csv.DictReader` 讀取 CSV，並以 `encoding="utf-8-sig"` 處理 BOM。
- 使用 `Counter` 統計系所人數與縣市人數。
- 使用 `matplotlib` 繪製並排長條圖與熱力圖。
- 測試檔放在 `tests/`，以 unittest 驗證資料讀取、統計與排名函式。
