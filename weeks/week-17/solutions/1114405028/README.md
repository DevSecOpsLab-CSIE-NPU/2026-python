搜尋效能輕量評估（使用自製 timeit 裝飾器）
- 執行：python eval_search.py
- 設定：對每個資料量（n）用 repeat=5 測 5 次平均

簡短結論（直覺 + 試驗重點）
- 若資料已排序，binary search 在單次搜尋上比 linear search 明顯快（O(log n) vs O(n)）。
- 若資料未排序且只做單次搜尋，必須先排序（O(n log n)），因此「排序 + binary」通常比不上直接 linear，除非會做大量查詢（多次搜尋時排序成本攤平）。
- 實驗輸出會列出：linear(ms)、binary(ms)、sort(ms)、sort+binary(ms)。請自行在本機跑一次觀察交叉點（會依硬體與 Python 實作而不同）。
- 建議：若資料經常要查詢且變動少，維持排序或使用索引/集合結構（如 dict / set）通常更合適。
