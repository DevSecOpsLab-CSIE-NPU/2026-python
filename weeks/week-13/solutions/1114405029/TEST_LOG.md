# TEST_LOG.md

# Week 13 測試紀錄

學號：1114405029

---

# 測試策略說明

本次作業採用：

- Test Driven Development（TDD）
- Red → Green 測試流程

開發方式進行。

流程如下：

1. 先撰寫 unittest 測試
2. 執行測試並觀察失敗（Red）
3. 完成功能實作
4. 再次執行測試直到全部通過（Green）

這樣可以：

- 提前驗證函式需求
- 避免資料格式錯誤
- 確保函式輸出穩定
- 降低後續圖表產生錯誤的風險

---

# Task 1｜Grouped Bar Chart 測試紀錄

## Red 階段（先寫測試）

一開始先建立：

- tests/test_task1.py

並先撰寫：

- load_year()
- get_top_depts()

相關測試。

先執行：

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

當時因為：

- task1_grouped_bar.py 尚未完成
- load_year()
- get_top_depts()

尚未實作，

因此出現：

- ImportError
- AssertionError

代表測試成功偵測功能尚未完成。

---

## Green 階段（完成功能）

後續完成：

- load_year()
- get_top_depts()

後再次執行：

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

測試結果：

```text
test_get_top_depts_includes_popular ... ok
test_get_top_depts_length ... ok
test_load_year_counts_correct ... ok
test_load_year_returns_dict ... ok
test_load_year_total_positive ... ok
```

```text
Ran 5 tests

OK
```

代表：

- 系所統計功能正常
- 回傳格式正確
- 資料內容正確
- 熱門系所分析正常

---

## Task 1 測試內容

### test_load_year_returns_dict

確認：

- load_year() 回傳 dict
- key 為系所名稱字串
- value 為招生人數整數

確保函式輸出格式正確，
方便後續圖表與統計使用。

---

### test_load_year_counts_correct

驗證已知資料：

- 114 年觀光休閒系招生人數應為 58 人

利用固定資料驗證，
避免 CSV 讀取錯誤或欄位解析錯誤。

---

### test_load_year_total_positive

確認：

- 單一年份總招生人數大於 0

避免：

- CSV 未正確讀取
- 空資料
- 路徑錯誤

等問題。

---

### test_get_top_depts_length

確認：

- get_top_depts() 回傳數量不超過 top_n

避免：

- top_n 邏輯錯誤
- union 過程出現異常結果

---

### test_get_top_depts_includes_popular

確認熱門系所：

- 觀光休閒系

應存在於結果中。

用來驗證：

- 排序邏輯
- 熱門系所分析
- top_n 篩選

是否正確。

---

## Task 1 設計說明

在 Task 1 中：

使用：

```python
collections.Counter()
```

進行系所人數統計。

優點：

- 不需要手動判斷 key 是否存在
- 程式碼更簡潔
- 可讀性更高
- 適合大量資料統計

此外：

函式回傳型別使用：

```python
dict[str, int]
```

可以讓：

- 函式結構更清楚
- unittest 更容易驗證
- IDE 型別提示更完整

在圖表部分：

使用：

- grouped bar chart
- legend
- grid
- 數值標籤

讓：

- 三年資料更容易比較
- 圖表可讀性更高
- 更符合資料分析圖表習慣

---

# Task 2｜Heatmap 測試紀錄

## Red 階段（先寫測試）

先建立：

- tests/test_task2.py

並先撰寫：

- zip_to_county()
- load_county_counts()
- get_top_counties()

相關測試。

第一次執行時：

- 郵遞區號對照尚未完成
- 澎湖縣資料尚未正確處理
- 部分資料無法正確分類

因此：

- test_zip_to_county_penghu 失敗
- test_load_county_counts_penghu_positive 發生錯誤

代表測試成功偵測資料問題。

---

## Green 階段（修正功能）

後續完成：

- ZIPCODE_TO_COUNTY
- zip_to_county()
- load_county_counts()
- get_top_counties()

並修正：

- 郵遞區號對應問題
- 資料分類問題

再次執行：

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

結果：

```text
test_get_top_counties_length ... ok
test_load_county_counts_penghu_positive ... ok
test_load_county_counts_type ... ok
test_zip_to_county_penghu ... ok
test_zip_to_county_unknown ... ok
```

```text
Ran 10 tests in 0.027s

OK
```

代表：

- 郵遞區號對應正常
- 縣市統計正常
- heatmap 資料來源正確
- top10 分析正常

---

## Task 2 測試內容

### test_zip_to_county_penghu

確認：

- 880 應正確對應為澎湖縣

驗證：

- 郵遞區號 mapping 正常

---

### test_zip_to_county_unknown

確認：

- 未知郵遞區號應回傳「其他」

避免：

- KeyError
- 程式崩潰

增加程式穩定性。

---

### test_load_county_counts_type

確認：

- load_county_counts() 回傳 dict

驗證：

- 縣市統計格式正確

---

### test_load_county_counts_penghu_positive

確認：

- 澎湖縣招生人數大於 0

避免：

- 郵遞區號解析失敗
- 縣市分類錯誤

---

### test_get_top_counties_length

確認：

- get_top_counties() 回傳數量不超過 top_n

驗證：

- top10 篩選邏輯正確

---

## Task 2 設計說明

在 Task 2 中：

使用：

```python
ZIPCODE_TO_COUNTY
```

將：

- 郵遞區號前三碼

轉換成：

- 縣市名稱

方便後續進行：

- 縣市統計
- heatmap 分析

另外：

由於部分郵遞區號：

- 不存在 mapping
- 或資料不完整

因此：

會被分類為：

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

在 heatmap 圖表中：

使用：

- colorbar
- annotation
- grid
- 熱度顏色差異

讓：

- 高低招生人數差異更明顯
- 圖表更容易閱讀
- 更符合資料視覺化習慣

---

# 最終測試結果

最終所有測試皆成功通過：

- Task 1：5 個測試通過
- Task 2：5 個測試通過

總計：

- 10 個測試全部通過

代表：

- 函式結構正確
- 測試流程完整
- 圖表資料正確
- 資料分析功能正常
- 程式具有穩定性與可維護性