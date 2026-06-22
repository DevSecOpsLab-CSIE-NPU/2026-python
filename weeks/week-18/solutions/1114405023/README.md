# 第四題：二分搜尋效能比較

## 題目目標

本題目標是比較 **linear search** 與 **binary search** 在不同搜尋情境下的效能差異。

本題依照學號後兩碼 `23` 設定：

| 參數       |     數值 |
| -------- | -----: |
| 搜尋目標 `K` |    123 |
| 陣列大小     | 100000 |
| 陣列排序     |   升冪排序 |

---

## 程式檔案

本題主要檔案如下：

| 檔案                              | 說明                     |
| ------------------------------- | ---------------------- |
| `p4_binary_search_perf.py`      | 第四題主程式，包含搜尋、效能比較與雷達圖產生 |
| `test_p4_binary_search_perf.py` | 第四題測試檔                 |
| `assets/radar.png`              | 搜尋效能雷達圖                |

---

## 實作內容

本題實作兩種搜尋法：

### 1. Linear Search

`linear_search_with_count(data, target=123)`

線性搜尋會從陣列第一個元素開始逐一比對，直到找到目標值或搜尋完整個陣列。

回傳格式：

```python
(index, comparison_count)
```

其中：

* `index`：找到時回傳目標所在位置
* 找不到時回傳 `-1`
* `comparison_count`：搜尋過程中的比較次數

---

### 2. Binary Search

`binary_search_with_count(data, target=123)`

二分搜尋的前提是資料必須已經升冪排序。
每次會檢查中間位置，並依照比較結果縮小搜尋範圍。

回傳格式：

```python
(index, comparison_count)
```

其中：

* `index`：找到時回傳目標所在位置
* 找不到時回傳 `-1`
* `comparison_count`：搜尋過程中的比較次數

---

## 效能比較設計

本題使用長度為 `100000` 的升冪陣列，並固定搜尋目標：

```text
K = 123
```

為了觀察不同情況下的搜尋效能，本題設計四種 case：

| Case      | 說明             | target index |
| --------- | -------------- | -----------: |
| best      | `K` 位於陣列第一個位置  |            0 |
| middle    | `K` 位於陣列中間位置   |        50000 |
| worst     | `K` 位於陣列最後一個位置 |        99999 |
| not_found | 陣列中不存在 `K`     |           -1 |

---

## 效能測試結果

執行：

```bash
python .\p4_binary_search_perf.py
```

在等待輸入時按：

```text
Ctrl + Z
Enter
```

程式會自動產生四組測試資料並輸出結果。

### 測試結果

```text
case=best
data_size=100000
target=123
target_index=0
linear_index=0
linear_comparisons=1
linear_time=2.6999972760677337e-06
binary_index=0
binary_comparisons=16
binary_time=5.6799966841936115e-06

case=middle
data_size=100000
target=123
target_index=50000
linear_index=50000
linear_comparisons=50001
linear_time=0.0074086999928113075
binary_index=50000
binary_comparisons=16
binary_time=6.579997716471553e-06

case=worst
data_size=100000
target=123
target_index=99999
linear_index=99999
linear_comparisons=100000
linear_time=0.013151360000483692
binary_index=99999
binary_comparisons=17
binary_time=5.439994856715202e-06
```

not_found case 會輸出 `linear_index=-1` 與 `binary_index=-1`，代表目標值不存在於陣列中。

---

## 效能分析

### Linear Search

linear search 的比較次數會受到目標位置影響很大。

| Case      | Linear Search 比較次數 |
| --------- | -----------------: |
| best      |                  1 |
| middle    |              50001 |
| worst     |             100000 |
| not_found |             100000 |

當目標值在陣列最前面時，linear search 只需要比較一次，因此是最佳情況。
但如果目標值在中間、最後，或根本不存在，linear search 就需要掃過大量資料。

---

### Binary Search

binary search 的比較次數相對穩定。

| Case      | Binary Search 比較次數 |
| --------- | -----------------: |
| best      |               約 16 |
| middle    |               約 16 |
| worst     |               約 17 |
| not_found |            約 16～17 |

binary search 每次都會將搜尋範圍縮小一半，所以即使資料量達到 `100000`，比較次數仍然維持在約 `16～17` 次。

---

## 搜尋提速方式

本題比較時採用以下共同提速方式，避免測量到搜尋以外的成本：

1. 資料先建立好，不把建立陣列的時間算進搜尋時間。
2. 不把 `input()` 與 `print()` 算進搜尋時間。
3. 找到目標後立刻 `return`，不做多餘比較。
4. 使用相同資料量、相同目標值與相同 repeat 次數。
5. binary search 的資料事先保證升冪排序，不在 benchmark 中重複排序。

---

## 雷達圖說明

本題會產生：

```text
assets/radar.png
```

雷達圖用來比較 linear search 與 binary search 在不同指標下的表現。

雷達圖維度包含：

| 維度             | 說明                   |
| -------------- | -------------------- |
| `BestCmp`      | best case 的比較次數      |
| `MiddleCmp`    | middle case 的比較次數    |
| `WorstCmp`     | worst case 的比較次數     |
| `NotFoundCmp`  | not_found case 的比較次數 |
| `BestTime`     | best case 的搜尋時間      |
| `MiddleTime`   | middle case 的搜尋時間    |
| `WorstTime`    | worst case 的搜尋時間     |
| `NotFoundTime` | not_found case 的搜尋時間 |

---

## 正規化邏輯

因為「比較次數」與「搜尋時間」都是越小越好，所以本題使用 smaller-is-better 的正規化方式：

```text
score = best_value / value
```

其中：

* `best_value` 是同一個維度中較小的數值
* 分數越接近 `1.0`，代表該搜尋法在該維度表現越好
* 同一個維度中表現最好的搜尋法分數會是 `1.0`

例如在 worst case 中：

```text
linear_comparisons = 100000
binary_comparisons = 17
```

所以：

```text
binary score = 17 / 17 = 1.0
linear score = 17 / 100000 = 0.00017
```

這代表 binary search 在 worst case 的比較次數表現明顯優於 linear search。

---

## 執行方式

### 執行測試

```bash
python .\test_p4_binary_search_perf.py
```

### 執行主程式並產生雷達圖

```bash
python .\p4_binary_search_perf.py
```

等待輸入時按：

```text
Ctrl + Z
Enter
```

成功後會產生：

```text
assets/radar.png
```

---

## 測試結果

```text
...........
----------------------------------------------------------------------
Ran 11 tests in 0.074s

OK
```

代表第四題測試全部通過。

---

## 結論

本題結果顯示：

1. linear search 在 best case 表現很好，因為目標值一開始就被找到。
2. linear search 在 middle、worst 與 not_found case 中需要大量比較。
3. binary search 在升冪陣列中表現穩定，即使資料量為 `100000`，比較次數仍約為 `16～17` 次。
4. 若資料已排序，binary search 在大資料量搜尋時比 linear search 更有效率。
5. 若只看 best case，linear search 可能比 binary search 快；但整體來看，binary search 在多數情境下更穩定。
