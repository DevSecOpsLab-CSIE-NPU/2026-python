# AI_USAGE.md — AI 使用紀錄

## 使用工具

- Claude Code（Anthropic）

---

## Task 1：三年並排長條圖

**提示詞（Prompt）：**
> 請根據 HOMEWORK.md 要求，實作 `load_year` 和 `get_top_depts` 函式，並用 matplotlib 畫出 112/113/114 學年度各系招生人數的並排長條圖（horizontal grouped bar chart），只顯示任一年前 8 名的系所，輸出至 `output/task1.png`。

**AI 所做的事：**
- 設計 `load_year` 用 csv.DictReader 讀取 CSV，回傳 `{系所名稱: 人數}` dict。
- 設計 `get_top_depts` 收集三年各自前 top_n 名的系所聯集。
- 用 `matplotlib` 繪製水平並排長條圖，加上數值標籤與圖例。

**我自己調整的部分：**
- 修正 DATA_DIR 路徑（HOMEWORK.md 寫 4 個 parent，實際需要 5 個）。
- 確認字型自動偵測邏輯，避免中文亂碼。

---

## Task 2：來源縣市熱力圖

**提示詞（Prompt）：**
> 請實作 `load_county_counts`、`get_top_counties`、`zip_to_county`，使用 HOMEWORK.md 提供的郵遞區號對照表，畫出「縣市 × 年份」熱力圖，只顯示 6 年合計前 10 名縣市，輸出至 `output/task2.png`。

**AI 所做的事：**
- 複製 HOMEWORK 提供的 `ZIPCODE_TO_COUNTY` 對照表。
- 實作函式讀取每年資料並統計縣市人數。
- 用 `imshow` 繪製熱力圖，加上數值標注與色條。

---

## 測試撰寫

**提示詞：**
> 請根據 HOMEWORK.md 的測試要求，為 task1 和 task2 分別撰寫 unittest，包含 5 個指定測試函式。

**AI 所做的事：**
- 撰寫 `test_task1.py` 和 `test_task2.py`，涵蓋所有指定的 5 個測試案例。
- 確保 import 路徑正確（透過 `sys.path.insert`）。

---

## 注意事項

- 所有程式邏輯均由 AI 產生後，由本人檢閱確認正確性。
- 圖表風格微調（figsize、顏色、字型偵測）由本人與 AI 協作完成。
- REPORT.md 的觀察分析由本人根據圖表結果自行撰寫。