# Pull Request 說明文件

*   **PR 標題：** `Week 13 - 1114405035 - 戴言廷`
*   **分支名稱：** `submit/week-13-1114405035`
*   **提交路徑：** `weeks/week-13/solutions/1114405035/`

---

## 1. 說明 (Description)

本 PR 已完成 Week 13（函數進階、類別設計、招生資料視覺化）的所有要求。

### CPE 題目部分
完成了 5 題 CPE 演算法解題，包含：
1.  **11005 (Cheapest Base)** - 進位制轉換、枚舉成本。
2.  **11063 (RGB -> XYZ)** - 數學計算、格式化輸出。
3.  **11150 (Frog Single Log Bridge)** - 動態規劃，並實作路徑壓縮優化。
4.  **11321 (Inke's Trap Path)** - 併查集 (DSU) 與 8 連通障礙鏈判定。
5.  **11332 (Mirror Visibility)** - 極角排序與中點射線投射判定。

每題皆提供標準版、易記版 (`*-easy.py`)、`unittest` 測試以及對應的 `test_XXXXX.log` 日誌。

### 招生資料視覺化部分
1.  **Task 1 三年並排長條圖** (`task1_grouped_bar.py`):
    *   整合 112、113、114 年新生資料庫。
    *   過濾出任一年度曾進前 8 名的熱門系所。
    *   繪製橫向並排長條圖，顯示各學系招收人數比較，輸出至 `output/task1.png`。
2.  **Task 2 來源縣市熱力圖** (`task2_zipcode_heatmap.py`):
    *   讀取 109～114 年新生資料庫。
    *   利用前 3 碼郵遞區號轉換生源縣市。
    *   統計合計人數前 10 名的縣市，繪製 10x6 矩陣熱力圖，輸出至 `output/task2.png`。

---

## 2. 測試驗證 (Verification)

已執行 `python -m unittest discover -s tests -p "test_*.py" -v`，所有 17 個單元測試均全數通過（OK）。

```text
test_sample_case (test_11005.Test11005.test_sample_case) ... ok
test_sample_case (test_11063.Test11063.test_sample_case) ... ok
test_sample_case (test_11150.Test11150.test_sample_case) ... ok
test_sample_case (test_11321.Test11321.test_sample_case) ... ok
test_sample_case_2 (test_11321.Test11321.test_sample_case_2) ... ok
test_sample_case_1 (test_11332.Test11332.test_sample_case_1) ... ok
test_sample_case_2 (test_11332.Test11332.test_sample_case_2) ... ok
test_get_top_depts_includes_popular (test_task1.TestTask1.test_get_top_depts_includes_popular) ... ok
test_get_top_depts_length (test_task1.TestTask1.test_get_top_depts_length) ... ok
test_load_year_counts_correct (test_task1.TestTask1.test_load_year_counts_correct) ... ok
test_load_year_returns_dict (test_task1.TestTask1.test_load_year_returns_dict) ... ok
test_load_year_total_positive (test_task1.TestTask1.test_load_year_total_positive) ... ok
test_get_top_counties_length (test_task2.TestTask2.test_get_top_counties_length) ... ok
test_load_county_counts_penghu_positive (test_task2.TestTask2.test_load_county_counts_penghu_positive) ... ok
test_load_county_counts_type (test_task2.TestTask2.test_load_county_counts_type) ... ok
test_zip_to_county_penghu (test_task2.TestTask2.test_zip_to_county_penghu) ... ok
test_zip_to_county_unknown (test_task2.TestTask2.test_zip_to_county_unknown) ... ok

----------------------------------------------------------------------
Ran 17 tests in 0.021s

OK
```

---

## 3. 分析與文件
*   `REPORT.md` 中詳細回答了食品科學系三年招生人數大幅起落的外部原因，探討了澎湖縣本地新生比例（約佔 6.56%）及非預期第一名縣市（台中市，佔 15.61%）的有趣地理現象，並剖析了六年全校新生人數衰退近 40% 的少子化衝擊。
*   `TEST_LOG.md` 完整紀錄了 TDD 開發歷程。
*   `AI_USAGE.md` 詳細聲明並紀錄了 AI 輔助與人類開發者的具體分工。
