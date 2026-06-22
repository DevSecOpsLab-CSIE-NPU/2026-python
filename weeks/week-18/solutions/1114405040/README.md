# 第 4 題 Binary Search Eval

## 題目說明

我的學號末兩碼為 40，
因此搜尋目標為：

```text
K = 100 + 40
K = 140
```

程式建立升冪整數陣列：

```python
arr = list(range(1, 200001))
```

接著實作 Linear Search 與 Binary Search，
兩個函式都回傳 `(found, index, comparisons)`。
程式也使用 `timeit` 比較效能，
並使用 `matplotlib` 產生 `assets/radar.png`。

## 演算法說明

Linear Search 從陣列第一個元素開始逐一比較，
直到找到目標或走完整個陣列。
它不需要排序，
但最壞情況可能需要檢查所有元素。

Binary Search 使用左右邊界與中間索引進行搜尋。
每次比較後可以排除一半資料。
它的前提是資料必須已經排序。
本題陣列已經升冪排序，
所以可以直接使用 Binary Search。

## 時間複雜度

Linear Search：

```text
時間複雜度：O(n)
空間複雜度：O(1)
```

Binary Search：

```text
時間複雜度：O(log n)
空間複雜度：O(1)
```

## 測試方式

在本資料夾執行：

```bash
py -m unittest test_q4_binary_search_eval.py
```

或直接執行程式：

```bash
py q4_binary_search_eval.py
```

執行後會輸出搜尋結果、
兩種搜尋法的 `timeit` 秒數，
以及速度比較結論。
同時會建立：

```text
assets/radar.png
```

## 題目四效能比較

實測輸出範例：

```text
FOUND idx=139 cmp=140
FOUND idx=139 cmp=17
linear : 0.005 s
binary : 0.002 s
=> binary faster
```

Linear Search 找到 `140` 時，
會從 `1` 開始逐一比較，
所以比較次數為 140。

Binary Search 從中間位置開始縮小搜尋範圍，
因此在 200000 筆已排序資料中，
比較次數明顯較少。

## 題目四雷達圖說明

雷達圖輸出於：

```text
assets/radar.png
```

比較維度包含：

1. Small N Speed
2. Large N Speed
3. Need Sorting
4. Implementation Simplicity
5. Worst Case Comparisons

分數採 1 到 5 分，
分數越高代表該項表現越好。
`Need Sorting` 分數越高，
代表越不依賴排序。

Linear Search 的優勢是簡單、不需要排序；
Binary Search 的優勢是大型資料搜尋快、
最壞比較次數少，
但需要資料已排序。

## Edge Case

已檢查：

1. 找到 `K = 140` 並回傳索引 `139`。
2. Linear Search 比較次數為 `140`。
3. Binary Search 比較次數小於 Linear Search。
4. 找不到目標時可輸出 `NOT FOUND` 格式。
5. `assets/radar.png` 能自動建立。

## 結論

本題程式符合要求：
可直接執行、
自動建立 assets 資料夾、
自動輸出 radar.png、
並完成 Linear Search 與 Binary Search 的正確性和效能比較。
