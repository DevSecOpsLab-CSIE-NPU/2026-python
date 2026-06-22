# 二分搜尋效能比較

## 題目設定

本題搜尋目標固定為 `K = 113`。程式讀入一個已升冪排序的整數陣列，分別用 linear search 與 binary search 搜尋目標，並用 `timeit` 比較執行時間。

## 雷達圖維度

雷達圖放在 `assets/radar.png`，用下列維度比較 linear search 與 binary search：

1. 速度：使用 `timeit` 測得的時間，時間越短分數越高。
2. 比較次數：搜尋時的 `cmp` 次數，次數越少分數越高。
3. 大 n 擴充性：依時間複雜度評分，binary search 是 O(log n)，linear search 是 O(n)。
4. 不需排序：linear search 不要求資料先排序，binary search 需要排序資料。
5. 實作簡單度：linear search 流程較直覺，binary search 需要維護左右邊界。

## 正規化方式

每個維度都正規化到 0 到 1，數值越大代表表現越好。速度使用 `最快時間 / 該方法時間`，比較次數使用 `最少比較次數 / 該方法比較次數`。大 n 擴充性、不需排序、實作簡單度則依演算法特性給定 0 到 1 的分數。

## 比較結果解讀

binary search 通常在速度、比較次數與大 n 擴充性勝出，因為每次比較都能排除一半資料，所以比較次數約為 log2(n)。linear search 在不需排序與實作簡單度勝出，因為它可以直接從頭掃描，不需要資料先排序。

binary search 通常比較快，是因為它不需要逐一檢查每個元素；但 binary search 需要排序資料，因為它依靠「中間值比目標大或小」來決定下一步要搜尋左半邊或右半邊。如果資料沒有排序，這個判斷就不可靠。
