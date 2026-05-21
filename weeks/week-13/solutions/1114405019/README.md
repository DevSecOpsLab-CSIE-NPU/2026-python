# Week 13 — 招生資料視覺化分析

**學號**：1114405019　**姓名**：洪翊滕

---

## 執行環境

- Python 3.11+
- 相依套件：`matplotlib`、`numpy`（標準 CSV 無需額外安裝）

## 執行方式

```bash
# 進入解題目錄
cd weeks/week-13/solutions/1114405019

# 執行 Task 1（產生 output/task1.png）
python task1_grouped_bar.py

# 執行 Task 2（產生 output/task2.png）
python task2_zipcode_heatmap.py

# 執行 Task 3（產生 output/task3_dashboard.png）
python task3_dashboard.py

# 執行所有測試
python -m unittest discover -s tests -v
```

## 檔案說明

| 檔案 | 說明 |
|------|------|
| `task1_grouped_bar.py` | 112–114 學年度前 8 名各系並排水平長條圖 |
| `task2_zipcode_heatmap.py` | 109–114 各縣市招生人數熱力圖 |
| `task3_dashboard.py` | 2×2 綜合儀表板（趨勢、圓餅、長條、多線折線） |
| `output/task1.png` | Task 1 輸出圖片 |
| `output/task2.png` | Task 2 輸出圖片 |
| `output/task3_dashboard.png` | Task 3 輸出圖片 |
| `tests/test_task1.py` | Task 1 的 5 個 unittest |
| `tests/test_task2.py` | Task 2 的 5 個 unittest |
| `TEST_LOG.md` | TDD Red → Green 執行紀錄 |
| `REPORT.md` | 資料分析心得 |
| `AI_USAGE.md` | AI 使用說明 |

## 資料來源

`assets/stu-data/109～114年新生資料庫.csv`（相對於專案根目錄）

讀取時使用 `encoding='utf-8-sig'` 處理 BOM。

## Task 3 儀表板說明

`task3_dashboard.py` 以 `plt.subplots(2, 2, figsize=(16, 12))` 繪製四象限綜合看板：

| 象限 | 圖表類型 | 內容 |
|------|----------|------|
| 左上 | 折線圖（含填充） | 全校 109–114 年招生總人數趨勢 |
| 右上 | 圓餅圖 | 114 學年度各入學管道比例 |
| 左下 | 水平長條圖 | 114 學年度各系招生人數前 10 名 |
| 右下 | 多線折線圖 | 6 個主要系所的歷年招生趨勢 |

## 主要發現

- **Task 1**：食品科學系三年人數跨幅最大（52 → 24 → 29），降幅達 54%。
- **Task 2**：台中市是最大生源縣市（15.6%），澎湖縣本地生僅佔 6.6%。
- **Task 3**：全校六年總招生降幅約 40%（682 → 412）；甄選入學（44.9%）與聯合分發（41.5%）為主要入學管道。
