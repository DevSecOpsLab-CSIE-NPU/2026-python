# README.md

# Week 13 Python Data Visualization Assignment

學號：1114405029

---

# 作業目標

本次作業主要練習：

- Python 資料分析
- CSV 資料讀取
- matplotlib 資料視覺化
- unittest 測試
- 函式化設計
- heatmap 與 grouped bar chart 圖表製作

並搭配：

- Python3 Cookbook 第七章（函式）
- Python3 Cookbook 第八章（類別與物件）

的函式結構與模組化概念進行實作。

---

# 作業完成內容

本次作業完成兩個主要任務：

---

# Task 1｜Grouped Bar Chart

檔案：

```text
task1_grouped_bar.py
```

功能：

- 讀取 109～114 年新生資料 CSV
- 統計各系所招生人數
- 找出熱門系所
- 使用 grouped bar chart 比較不同年度招生情況
- 自動輸出圖表至 output/task1.png

圖表特色：

- grouped bar chart
- legend
- grid
- 數值標籤
- 中文字型處理
- 自動調整版面配置

---

# Task 2｜County Heatmap

檔案：

```text
task2_zipcode_heatmap.py
```

功能：

- 使用郵遞區號前三碼對應縣市
- 統計各縣市招生人數
- 計算 6 年合計前 10 名縣市
- 使用 heatmap 呈現縣市 × 年份招生資料
- 自動輸出圖表至 output/task2.png

圖表特色：

- heatmap
- colorbar
- annotation
- grid
- 熱度顏色差異
- 中文字型支援

---

# 使用技術

本次作業使用：

```python
csv
collections.Counter
pathlib.Path
matplotlib
numpy
unittest
```

主要用途：

| 技術 | 用途 |
|---|---|
| csv | 讀取 CSV 資料 |
| Counter | 統計招生人數 |
| pathlib | 處理跨平台路徑 |
| matplotlib | 繪製圖表 |
| numpy | heatmap 矩陣資料 |
| unittest | 單元測試 |

---

# 設計理念

本次作業在資料統計部分，
主要使用：

- collections.Counter
- dict[str, int]

進行資料整理。

使用 Counter 的原因是：

- 適合大量計數統計
- 不需要手動判斷 key 是否存在
- 可以讓程式碼更簡潔
- 提高程式可讀性

另外：

使用 pathlib.Path 處理路徑，
可以避免：

- Windows
- macOS
- Linux

不同平台的路徑差異問題，
提高程式可攜性。

---

# 資料視覺化設計

Task 1 使用：

```text
grouped bar chart
```

原因是：

- 適合同時比較多個年度資料
- 容易觀察不同系所變化
- 適合做招生人數年度比較

因此：

可以更清楚觀察：

- 熱門系所
- 招生變化
- 年度差異

---

Task 2 使用：

```text
heatmap
```

原因是：

- 更適合觀察大量數值分布
- 可以快速看出高低差異
- 顏色變化更容易辨識趨勢

因此：

能更直觀觀察：

- 各縣市招生來源
- 年份之間的變化
- 招生熱區分布

---

另外：

在 Task 2 中：

由於部分郵遞區號：

- 不存在 mapping
- 或資料不完整

因此會被分類為：

```text
其他
```

但因為題目要求：

```text
只顯示 6 年合計人數前 10 名的縣市
```

因此：

在統計 top10 時：

刻意排除：

```text
其他
```

避免：

- 非縣市資料干擾分析
- heatmap 出現不合理結果
- 影響圖表分析價值

---

# 函式設計

本次作業強調：

- 函式化
- 可維護性
- 可測試性

每個功能皆拆分成獨立函式，
方便：

- unittest 測試
- 程式維護
- 功能重複使用

---

# Task 1 函式

```python
load_year(year, data_dir)
```

功能：

- 讀取單一年份 CSV
- 回傳：

```python
dict[str, int]
```

格式的系所招生人數資料。

---

```python
get_top_depts(year_data, top_n)
```

功能：

- 找出熱門系所
- 回傳前 top_n 系所名稱清單

---

# Task 2 函式

```python
zip_to_county(zipcode)
```

功能：

- 將郵遞區號前三碼轉成縣市名稱

---

```python
load_county_counts(year, data_dir)
```

功能：

- 統計單一年份各縣市招生人數

---

```python
get_top_counties(all_years, top_n)
```

功能：

- 統計 6 年合計前 top_n 名縣市
- 排除「其他」
- 避免非縣市資料影響 heatmap 分析

---

# 測試設計（TDD）

本次作業採用：

```text
Red → Green
```

測試流程。

流程如下：

1. 先撰寫 unittest
2. 執行測試（Red）
3. 完成功能實作
4. 再次執行測試直到全部通過（Green）

這樣可以：

- 提前驗證函式需求
- 避免資料格式錯誤
- 確保函式輸出穩定
- 降低後續圖表錯誤風險

---

# 測試結果

Task 1：

- 5 個測試全部通過

Task 2：

- 5 個測試全部通過

總計：

```text
10 個測試全部通過
```

最終結果：

```text
Ran 10 tests

OK
```

---

# 圖表輸出

執行程式後會自動產生：

```text
output/task1.png
output/task2.png
```

---

# 專案結構

```text
1114405029/
├── output/
│   ├── task1.png
│   └── task2.png
│
├── tests/
│   ├── test_task1.py
│   └── test_task2.py
│
├── task1_grouped_bar.py
├── task2_zipcode_heatmap.py
├── README.md
├── REPORT.md
├── TEST_LOG.md
└── AI_USAGE.md
```

---

# 作業學習成果

透過本次作業，我學習到：

- CSV 資料分析
- Python 函式化設計
- unittest 測試流程
- matplotlib 圖表繪製
- grouped bar chart 設計
- heatmap 視覺化
- 郵遞區號資料轉換
- Counter 統計技巧
- pathlib 路徑管理
- 中文字型處理

同時也更加理解：

- TDD 測試流程
- 函式結構設計
- 資料視覺化可讀性
- Python 模組化設計
- 資料分析流程
- 圖表設計與可讀性