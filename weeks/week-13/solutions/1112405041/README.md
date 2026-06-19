# Week 13 作業 — 招生資料視覺化分析

## 學號
1112405041

## 5 階段開發流程

| Stage | 檔案 | 狀態 |
|-------|------|------|
| 1 | data_loader.py — 資料載入 | ✅ |
| 2 | analysis.py — 分析邏輯 | ✅ |
| 3 | plot.py — 圖表繪製 | ✅ |
| 4 | 輸出驗證（task1.png + task2.png） | ✅ |
| 5 | 安全自掃（test_security.py） | ✅ |

## 執行方式

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## 輸出圖片

- `output/task1.png` — 各系 112/113/114 學年度招生人數並排長條圖
- `output/task2.png` — 各縣市 109～114 學年度招生人數熱力圖
