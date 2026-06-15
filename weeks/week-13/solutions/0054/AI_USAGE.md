## 1. 我問了哪些問題

1. 如何在 matplotlib 中畫出並排長條圖（grouped bar chart）？
2. 如何使用 `ax.imshow()` 製作熱力圖並加上數值標註？
3. 郵遞區號前 3 碼如何對應到縣市名稱？

## 2. AI 建議我有採用的部分

- 使用 `np.arange` 搭配偏移量計算來繪製並排長條圖
- 使用 `ax.imshow()` 搭配 `cmap="YlOrRd"` 繪製熱力圖
- 使用 `ax.text()` 在熱力圖每個格子中標註數字，並根據背景色深淺調整文字顏色

## 3. AI 建議我拒絕的部分及原因

- AI 建議使用 `pandas` 來讀取 CSV 並進行 groupby 統計 — 拒絕，因為作業要求自行實作資料處理邏輯
- AI 建議將 ZIPCODE_TO_COUNTY 放在外部 JSON 檔案 — 拒絕，因為作業直接提供了 Python dict 格式，放在程式碼中更方便

## 4. AI 輸出我執行後發現有誤的案例

AI 提供的 get_top_depts 實作中使用了 `all_depts.update()` 但未考慮同名系所在不同年份的合併問題，導致重複系所可能多次出現。修正方式：使用 set 來收集系所名稱，最後再轉回 list，確保每個系所唯一。
