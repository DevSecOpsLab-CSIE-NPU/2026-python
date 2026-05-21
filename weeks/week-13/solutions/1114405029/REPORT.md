# REPORT.md

# Week 13 Python Data Visualization Assignment Report

學號：1114405029

---

# 作業說明

本次作業主要使用：

- Python 資料分析
- matplotlib 資料視覺化
- unittest 測試

完成：

- grouped bar chart
- heatmap

兩種不同型態的資料分析圖表。

資料來源為：

```text
assets/stu-data/109～114年新生資料庫.csv
```

並參考：

- Python3 Cookbook Chapter 7（函式）
- Python3 Cookbook Chapter 8（類別與物件）

中的函式化與模組化設計概念。

---

# 開發流程

本次作業採用：

```text
Test Driven Development（TDD）
```

方式進行開發。

流程如下：

```text
Red → Green
```

也就是：

1. 先撰寫 unittest
2. 執行測試並觀察失敗
3. 完成功能實作
4. 再次執行測試直到全部通過

這樣可以：

- 提前驗證函式需求
- 避免資料格式錯誤
- 提高程式穩定性
- 降低後續圖表錯誤

---

# Task 1｜Grouped Bar Chart

## 任務目標

Task 1 的目標是：

- 統計不同年度熱門系所招生人數
- 使用 grouped bar chart 比較不同年度差異

最後輸出：

```text
output/task1.png
```

---

## 資料處理方式

在資料處理部分：

先使用：

```python
csv.DictReader()
```

讀取 CSV。

之後：

使用：

```python
collections.Counter()
```

統計：

- 系所名稱
- 招生人數

並回傳：

```python
dict[str, int]
```

格式資料。

---

## 熱門系所分析

在熱門系所分析部分：

使用：

```python
get_top_depts()
```

統計：

- 多個年度熱門系所

並使用：

```python
set()
```

避免重複系所。

最後：

依照招生人數篩選熱門系所，
並用於 grouped bar chart。

---

## 圖表設計原因

Task 1 使用：

```text
grouped bar chart
```

原因是：

- 適合比較不同年度資料
- 容易觀察系所變化
- 容易比較招生趨勢

此外：

也加入：

- legend
- grid
- bar label
- 中文字型

提升：

- 圖表可讀性
- 資料辨識度
- 視覺化品質

---

## Task 1 遇到的問題

在開發過程中：

曾遇到：

- 中文字型顯示問題
- bar label 重疊
- grouped bar 間距問題
- top_n 統計問題

---

## 解決方式

中文部分：

使用：

```python
plt.rcParams["font.sans-serif"]
```

設定中文字型。

---

在 bar chart 排版部分：

使用：

```python
tight_layout()
```

避免：

- 標題重疊
- x 軸文字擠在一起

---

另外：

也調整：

- bar width
- x 軸偏移量
- legend 位置

讓圖表更容易閱讀。

---

# Task 2｜County Heatmap

## 任務目標

Task 2 的目標是：

- 將郵遞區號轉成縣市
- 統計不同縣市招生人數
- 使用 heatmap 呈現：

```text
縣市 × 年份
```

資料分布。

最後輸出：

```text
output/task2.png
```

---

## 郵遞區號處理

在資料處理部分：

使用：

```python
ZIPCODE_TO_COUNTY
```

進行：

- 郵遞區號前三碼
- 對應縣市名稱

例如：

```python
"880" → "澎湖縣"
```

並透過：

```python
zip_to_county()
```

統一處理轉換邏輯。

---

## Heatmap 資料分析

在 heatmap 分析部分：

使用：

```python
load_county_counts()
```

統計：

- 單一年份各縣市招生人數

再透過：

```python
get_top_counties()
```

計算：

```text
6 年合計前 10 名縣市
```

作為 heatmap 顯示資料。

---

## 為什麼使用 Heatmap

Task 2 使用：

```text
heatmap
```

原因是：

- 適合大量數值資料
- 顏色變化容易看出趨勢
- 可以快速辨識高低差異

比起：

- bar chart
- line chart

更適合：

```text
縣市 × 年份
```

這種二維資料分析。

---

## 「其他」資料處理

在開發過程中：

發現部分郵遞區號：

- 不存在 mapping
- 或資料不完整

因此：

會被分類為：

```text
其他
```

但：

題目要求：

```text
只顯示 6 年合計人數前 10 名縣市
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

提升圖表分析品質。

---

## Heatmap 圖表設計

在 heatmap 設計部分：

使用：

- colorbar
- annotation
- grid
- 顏色深淺差異

提升：

- 數值辨識度
- 圖表可讀性
- 視覺化效果

另外：

也根據：

- 數值大小

自動切換：

- 白字
- 黑字

避免文字與背景顏色混在一起。

---

# 資料分析觀察

## Task 1：哪個系三年之間人數變化最大？你認為可能的原因是什麼？

從圖表中可以觀察到：

```text
食品科學系
```

的人數變化最大。

112 學年度招生人數為：

```text
52 人
```

但到了：

```text
113 學年度
```

下降至：

```text
24 人
```

之後：

114 學年度回升至：

```text
29 人
```

其中：

```text
52 → 24
```

的變化非常明顯，
幾乎下降一半。

我認為可能原因包括：

- 招生名額調整
- 學生選填志願改變
- 科系熱門程度變化
- 少子化影響招生狀況

另外：

```text
資訊管理系
```

也呈現持續下降趨勢：

```text
42 → 33 → 24
```

顯示部分科系近年招生壓力較大。

---

## Task 2：澎湖縣學生佔全校幾成？哪個縣市排第二？有沒有出乎意料的地方？

從 heatmap 可以發現：

```text
台中市
```

是六年合計招生人數最多的縣市。

第二名則是：

```text
高雄市
```

這點讓我有些意外，
因為我原本認為學校所在地的：

```text
澎湖縣
```

學生比例應該會更高。

但從資料中可以發現：

澎湖縣雖然屬於招生來源較高的縣市之一，
但並不是招生人數最多的來源。

這代表：

學校的招生來源其實相當多元，
並不只集中在澎湖地區。

---

## 自由觀察：從資料中，你還注意到什麼有趣的現象？

我發現：

```text
觀光休閒系
```

在三個年度中：

- 61 人
- 60 人
- 58 人

都維持非常高的人數。

代表：

該系在近年仍然具有穩定吸引力。

另外：

```text
資訊工程系
```

招生人數也維持在相對高的水準，
顯示資訊相關科系仍然受到學生歡迎。

另一方面：

部分科系的人數波動較大，
代表不同年度學生選擇方向差異明顯。

從 heatmap 中也能發現：

招生來源主要集中在：

- 台中市
- 高雄市
- 新北市
- 台南市

顯示：

學生來源多集中在人口較多的城市。

而：

```text
台北市
```

的人數反而不高，
這點與我原本的預期不同，
算是比較有趣的地方。

---

# 測試設計

本次作業共完成：

```text
10 個 unittest 測試
```

其中：

Task 1：

- 5 個測試

Task 2：

- 5 個測試

---

# 測試內容

測試內容包含：

- 回傳型別驗證
- 資料內容驗證
- top_n 邏輯驗證
- 郵遞區號 mapping 驗證
- 資料數量驗證

例如：

```python
test_zip_to_county_penghu()
```

會驗證：

```python
880 → 澎湖縣
```

是否正確。

---

# 最終測試結果

最終執行：

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

結果：

```text
Ran 10 tests

OK
```

代表：

- 所有函式正常
- 所有測試通過
- 資料分析結果正確
- 圖表資料來源正常

---

# 作業學習成果

透過本次作業：

我學習到：

- CSV 資料分析
- Python 函式化設計
- unittest 測試流程
- matplotlib 視覺化
- grouped bar chart
- heatmap
- Counter 統計技巧
- pathlib 路徑管理
- 中文字型處理

另外：

也更加理解：

- TDD 測試流程
- 函式結構設計
- 資料分析流程
- 圖表可讀性
- 資料視覺化設計

以及：

- 如何提升程式可維護性
- 如何讓程式更容易測試
- 如何將資料分析結果有效視覺化