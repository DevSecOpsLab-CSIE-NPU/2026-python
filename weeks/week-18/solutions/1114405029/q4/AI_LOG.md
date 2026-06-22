# Q4 AI_LOG - Search Performance

## 我問 AI 什麼

我請 AI 依照 `K=129` 完成 linear search、binary search、timeit benchmark、比較次數與 radar.png 產生。

## AI 建議什麼

AI 建議搜尋函式回傳 `(found, idx, cmp)`，benchmark 另回傳 timeit 秒數，雷達圖比較搜尋速度、比較次數、是否需要排序、實作簡易度與最壞情況效率。

## 我如何修改

我確認 K 是 129，補了空陣列、單一元素、找不到、K 在第一個和最後一個的 edge case。我檢查 linear search 與 binary search 都會回傳 found 狀態、索引和 cmp 比較次數，並用 `timeit` 輸出 linear/binary 的時間與 faster 結論。我也把 Q4 主要輸出格式修正為 `FOUND 128 cmp=129` 這種考卷格式，確認 `q4/assets/radar.png` 可以由 `create_radar_chart` 產生，並用 unittest 檢查檔案存在且大小大於 0。

## 對應檔案

- 程式：`q4.py`
- 測試：`test_q4.py`
- 圖檔：`assets/radar.png`

