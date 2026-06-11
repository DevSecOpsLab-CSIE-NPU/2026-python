# 6/11 排序效能實驗室報告

## 方法

本實驗用 `@timeit` 裝飾器量測 bubble sort、quick sort、merge sort、Python 內建 `sorted()`，以及加速版排序。資料由 `make_data(n, seed=42)` 產生，固定 seed 讓結果可重現，每個資料量重複 3 次後取平均秒數。

## 結果圖

![benchmark](assets/benchmark.png)

## 解讀

`built_in_sorted` 最快，因為它是 Python 內建 Timsort 且核心實作高度最佳化。`bubble_sort` 屬於 O(n^2)，資料量增加後時間成長最明顯；`quick_sort`、`merge_sort` 與 `optimized_quick_sort` 接近 O(n log n)，曲線斜率較平緩。`optimized_quick_sort` 使用 median-of-three pivot 與小區間 insertion sort，在 4000 筆資料約由 0.00441 秒降到 0.00298 秒，約 1.48x 加速。
