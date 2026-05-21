# AI_USAGE.md

# AI Usage Report

學號：1114405029

---

# AI 協助方式說明

本次作業主要透過與 AI 討論：

- 資料分析流程
- 函式設計
- unittest 測試
- matplotlib 視覺化
- grouped bar chart 排版
- heatmap 分析
- 郵遞區號 mapping
- top10 統計邏輯

並在討論後：

- 自行整理需求
- 自行修改程式
- 自行重新測試
- 自行調整圖表設計
- 自行確認是否符合題目要求

AI 主要作為：

- 開發討論工具
- 除錯輔助工具
- 設計建議工具
- 測試流程輔助工具

而不是直接複製最終結果。

所有程式仍有經過：

- 自行理解
- 自行調整
- 自行驗證

後才整合進作業。

---

# 與 AI 討論的內容

本次主要討論內容包含：

---

## 1. CSV 資料分析流程

討論內容：

- 如何使用 csv.DictReader()
- 如何整理 CSV 欄位資料
- 如何統計系所與縣市招生人數
- 如何設計 dict[str, int] 結構
- 如何避免空資料影響統計

最後採用：

- DictReader
- Counter
- dict[str, int]

作為主要資料結構。

---

## 2. 函式結構設計

討論內容：

- 如何拆分函式
- 如何讓程式更容易維護
- 如何提高可測試性
- 如何避免單一函式過長
- 如何讓 unittest 更容易驗證

最後將功能拆分成：

Task 1：

```python
load_year()
get_top_depts()
```

Task 2：

```python
zip_to_county()
load_county_counts()
get_top_counties()
```

讓：

- 每個函式只負責單一功能
- 程式更容易閱讀
- 更容易維護
- 更容易測試

---

## 3. unittest 測試設計

討論內容：

- 如何先寫測試（Red）
- 如何驗證資料內容
- 如何驗證回傳型別
- 如何驗證 top_n 邏輯
- 如何驗證 mapping 是否正確
- 如何測試特殊情況

最後：

先建立：

```text
tests/test_task1.py
tests/test_task2.py
```

再依照：

```text
Red → Green
```

流程完成開發。

測試內容包含：

- dict 型別驗證
- 招生人數驗證
- top_n 驗證
- 郵遞區號 mapping 驗證
- 未知資料驗證

---

## 4. grouped bar chart 設計

討論內容：

- grouped bar 如何排列
- bar width 如何設定
- x 軸偏移量如何計算
- legend 如何放置
- bar label 如何避免重疊
- 如何提升圖表可讀性
- 如何避免圖表過度擁擠

最後調整：

- x 軸偏移量
- bar width
- tight_layout()
- legend 位置
- grid
- 數值標籤

讓圖表：

- 更容易閱讀
- 更容易比較年度差異
- 更符合資料視覺化習慣

---

## 5. heatmap 設計

討論內容：

- heatmap 適合哪些資料
- colorbar 如何使用
- annotation 如何設計
- 顏色深淺如何調整
- heatmap 如何提高可讀性
- 文字顏色如何避免看不清楚
- 如何讓高低差異更明顯

最後：

根據數值大小：

- 自動切換白字與黑字

提升 heatmap 可讀性。

另外：

也調整：

- colorbar
- grid
- annotation
- spacing
- 標題內容

讓 heatmap 更容易閱讀。

---

## 6. 郵遞區號對照設計

討論內容：

- 郵遞區號前三碼如何對應縣市
- mapping 如何建立
- 未知郵遞區號如何處理
- 如何避免 KeyError
- 如何讓 mapping 更容易維護

最後：

使用：

```python
ZIPCODE_TO_COUNTY
```

建立 mapping。

並將未知資料分類為：

```text
其他
```

避免：

- 程式崩潰
- mapping 錯誤
- heatmap 缺值問題

---

## 7. top10 分析邏輯

討論內容：

- 如何統計 6 年合計資料
- 如何選出前 10 名縣市
- 「其他」是否應該列入分析
- 如何避免排序錯誤
- 如何讓 heatmap 更有分析價值

最後決定：

- 排除「其他」

避免：

- 非縣市資料影響分析結果
- heatmap 出現不合理資料

讓圖表更符合題目要求。

---

## 8. Markdown 文件整理

討論內容：

- README.md 如何撰寫
- REPORT.md 如何增加完整度
- TEST_LOG.md 如何記錄測試流程
- AI_USAGE.md 如何正確描述 AI 使用方式
- 如何讓 Markdown 排版更清楚

最後：

使用：

- 標題分層
- code block
- 條列式整理
- 區段分隔線

讓文件：

- 更容易閱讀
- 更有專案感
- 更符合正式作業格式

---

# AI 建議後有採用的部分

本次採用的設計包含：

- Counter 統計資料
- pathlib.Path 處理路徑
- unittest 測試流程
- grouped bar chart 排版
- heatmap annotation
- tight_layout()
- colorbar
- top_n 統計邏輯
- dict[str, int] 回傳格式
- 自動文字顏色切換
- ZIPCODE_TO_COUNTY mapping
- Markdown 文件分層設計

---

# AI 建議後自行調整的部分

本次也有自行修改與調整：

- grouped bar 間距
- x 軸文字 spacing
- legend 位置
- heatmap 字體顏色
- top10 排序
- 「其他」排除邏輯
- 中文字型設定
- heatmap 標題內容
- 圖表 spacing
- bar label 顯示方式
- annotation 字體大小
- heatmap 顏色配置
- Markdown 文件內容

並多次重新執行：

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

確認修改後功能仍正常。

---

# 自行完成的部分

除了與 AI 討論外：

以下內容為自行整理與完成：

- unittest 執行
- 圖表結果檢查
- heatmap top10 邏輯確認
- grouped bar 排版調整
- heatmap annotation 檢查
- output 圖片確認
- TEST_LOG.md
- README.md
- REPORT.md
- 專案資料夾整理
- Markdown 排版整理
- 程式碼細節調整
- 最終測試確認

---

# 與 AI 實際討論的問題範例

本次作業中，
曾實際與 AI 討論以下問題：

---

## 1. 如何讓 grouped bar chart 不重疊？

討論內容：

- bar width 如何設定
- x 軸偏移量如何計算
- 多年度 bar 如何排列

最後：

透過：

- 調整 width
- 調整 offset
- tight_layout()

改善圖表排版。

---

## 2. Heatmap 的文字顏色如何自動切換？

討論內容：

- 深色背景如何避免黑字看不清楚
- 淺色背景如何避免白字消失

最後：

根據數值大小：

- 自動切換白字與黑字

提升 heatmap 可讀性。

---

## 3. 為什麼「其他」不應該列入 top10？

討論內容：

- 「其他」是否屬於真正縣市
- 是否會影響資料分析結果

最後：

決定：

- 在 top10 統計時排除「其他」

避免 heatmap 分析失真。

---

## 4. unittest 應該測哪些內容？

討論內容：

- 是否只測回傳型別
- 是否需要測資料內容
- 是否需要測特殊情況

最後：

加入：

- dict 驗證
- 招生人數驗證
- mapping 驗證
- top_n 驗證
- 未知資料驗證

讓測試更完整。

---

## 5. 為什麼使用 heatmap 而不是 line chart？

討論內容：

- 哪種圖比較適合：
  - 縣市 × 年份
  - 大量數值資料

最後：

選擇：

```text
heatmap
```

因為：

- 更容易看出高低差異
- 更適合二維資料分析
- 更容易觀察招生熱區變化

---

# AI 使用心得

透過與 AI 討論：

我更容易理解：

- matplotlib 圖表設計
- heatmap 分析方式
- grouped bar chart 排版
- unittest 測試流程
- 函式拆分方式
- top_n 分析邏輯
- 資料視覺化設計

AI 對於：

- 除錯
- 提供設計方向
- 解釋函式概念
- 協助分析資料流程
- 協助整理測試流程

很有幫助。

但：

最終仍需要：

- 自行驗證資料正確性
- 自行測試程式
- 自行調整圖表
- 自行確認是否符合題目要求
- 自行檢查 heatmap 與 grouped bar 結果

才能完成較完整且穩定的作業。

---

# AI 使用後的學習成果

透過本次與 AI 討論：

我更加熟悉：

- Python 資料分析流程
- unittest 測試設計
- matplotlib 視覺化技巧
- heatmap 分析
- grouped bar chart 設計
- Markdown 文件整理

並理解：

- 程式不只是能執行
- 還需要：
  - 可讀性
  - 可維護性
  - 可測試性
  - 可分析性

以及：

- 如何讓資料分析結果更容易閱讀
- 如何讓圖表更具有分析價值
- 如何透過測試提高程式穩定性