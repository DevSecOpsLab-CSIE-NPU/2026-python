# 0617 Search Evaluation

本次練習實作 `timeit` decorator，並用它比較 `linear_search` 與 `binary_search` 的搜尋效能。

在 `n = 100000` 的資料下，`binary_search` 通常會比 `linear_search` 快，因為 binary search 每次都能把搜尋範圍減半。不過 binary search 的前提是資料已經排序，如果資料原本沒有排序，單次搜尋時「先排序再 binary search」不一定划算；若要查詢很多次，排序後重複使用 binary search 才比較有價值。