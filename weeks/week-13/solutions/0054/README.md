## 完成項目

- Task 1：112-114 學年度各系招生人數並排長條圖
- Task 2：109-114 學年度各縣市招生人數熱力圖

## 執行方式

```bash
python task1_grouped_bar.py
python task2_zipcode_heatmap.py
python -m unittest discover -s tests -p "test_*.py" -v
```

## 資料分析心得

詳見 REPORT.md。

## 遇到的 Bug 及修正

在 Task 2 的 `load_county_counts` 中，部分學生的郵遞區號為空字串，直接取 `zipcode[:3]` 會得到空字串而找不到對應縣市。修正方式：在 `zip_to_county` 中對空字串的輸入回傳「其他」。
