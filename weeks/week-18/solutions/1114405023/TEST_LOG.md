# TEST_LOG.md

## CPE 模擬實戰測試紀錄

## 基本資料

* 學號後兩碼：`23`
* 個位數：`3`
* 十位數：`2`

## 參數設定

| 題目          | 參數      |  數值 |
| ----------- | ------- | --: |
| 第一題：資料清理    | `D`     |   5 |
| 第二題：凱撒密碼    | `SHIFT` |   4 |
| 第三題：任意進位數字根 | `base`  |   3 |
| 第四題：二分搜尋效能  | `K`     | 123 |

---

# 第一題：資料清理 Data Cleaning

## 紅燈測試

### 測試指令

```bash
python .\test_p1_data_cleaning.py
```

### 測試結果

```text
Traceback (most recent call last):
  File "test_p1_data_cleaning.py", line 7, in <module>
    from p1_data_cleaning import clean_numbers, solve
ModuleNotFoundError: No module named 'p1_data_cleaning'
```

### 判斷

紅燈成功。
原因是 `test_p1_data_cleaning.py` 已建立，但 `p1_data_cleaning.py` 尚未建立或尚未實作。

---

## 綠燈測試

### 測試指令

```bash
python .\test_p1_data_cleaning.py
```

### 測試結果

```text
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

### 判斷

第一題綠燈成功。
代表資料清理功能可正常處理：

* 去除重複值
* 保留第一次出現順序
* 篩選可被 `D = 5` 整除的數字
* 排序輸出
* 沒有符合條件時輸出 `NONE`

---

## 手動測試

### 測試指令

```bash
python .\p1_data_cleaning.py
```

### 測試輸入

```text
3
1 3 5
0
```

### 預期輸出

```text
5
```

### 判斷

手動測試成功。
因為 `1 3 5` 中只有 `5` 可以被 `D = 5` 整除。

---

# 第二題：凱撒密碼 Caesar Cipher

## 紅燈測試

### 測試指令

```bash
python .\test_p2_caesar_cipher.py
```

### 測試結果

```text
Traceback (most recent call last):
  File "test_p2_caesar_cipher.py", line 7, in <module>
    from p2_caesar_cipher import caesar_cipher, shift_char
ModuleNotFoundError: No module named 'p2_caesar_cipher'
```

### 判斷

紅燈成功。
原因是 `test_p2_caesar_cipher.py` 已建立，但 `p2_caesar_cipher.py` 尚未建立或尚未實作。

---

## 綠燈測試

### 測試指令

```bash
python .\test_p2_caesar_cipher.py
```

### 測試結果

```text
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

### 判斷

第二題綠燈成功。
代表凱撒密碼功能可正常處理：

* 大寫字母位移
* 小寫字母位移
* `Z/z` 循環位移
* 非英文字母保持原樣
* 多行輸入直到 EOF

---

## 手動測試

### 測試指令

```bash
python .\p2_caesar_cipher.py
```

### 測試輸入

```text
Hello, NPU
abc XYZ
```

### 實際輸出

```text
Lipps, RTY
efg BCD
```

### 判斷

手動測試成功。
因為本題 `SHIFT = 4`，所以：

* `Hello` → `Lipps`
* `NPU` → `RTY`
* `abc` → `efg`
* `XYZ` → `BCD`

---

# 第三題：任意進位的數字根

## 紅燈測試

### 測試指令

```bash
python .\test_p3_digit_root_base.py
```

### 測試結果

```text
Traceback (most recent call last):
  File "test_p3_digit_root_base.py", line 7, in <module>
    from p3_digit_root_base import digit_root, solve, sum_digits_in_base
ModuleNotFoundError: No module named 'p3_digit_root_base'
```

### 判斷

紅燈成功。
原因是 `test_p3_digit_root_base.py` 已建立，但 `p3_digit_root_base.py` 尚未建立或尚未實作。

---

## 綠燈測試

### 測試指令

```bash
python .\test_p3_digit_root_base.py
```

### 測試結果

```text
.....
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

### 判斷

第三題綠燈成功。
代表任意進位數字根功能可正常處理：

* `0`
* 小於 `base` 的數字
* 需要重複做各位數字相加的數字
* 多行輸入直到 EOF
* 負數例外處理

---

## 手動測試

### 測試指令

```bash
python .\p3_digit_root_base.py
```

### 測試輸入

```text
0
8
64
```

### 實際輸出

```text
0
2
2
```

### 判斷

手動測試成功。
本題 `base = 3`。

說明：

* `0` 的數字根為 `0`
* `8` 的三進位是 `22`，`2 + 2 = 4`，`4` 的三進位是 `11`，`1 + 1 = 2`
* `64` 經過 base 3 數字根運算後結果為 `2`

---

# 第四題：二分搜尋效能 Binary Search Performance

## 紅燈測試

### 測試指令

```bash
python .\test_p4_binary_search_perf.py
```

### 測試結果

```text
Traceback (most recent call last):
  File "test_p4_binary_search_perf.py", line 7, in <module>
    from p4_binary_search_perf import (
ModuleNotFoundError: No module named 'p4_binary_search_perf'
```

### 判斷

紅燈成功。
原因是 `test_p4_binary_search_perf.py` 已建立，但 `p4_binary_search_perf.py` 尚未建立或尚未實作。

---

## 綠燈測試

### 測試指令

```bash
python .\test_p4_binary_search_perf.py
```

### 測試結果

```text
...........
----------------------------------------------------------------------
Ran 11 tests in 0.074s

OK
```

### 判斷

第四題綠燈成功。
代表二分搜尋效能程式可正常處理：

* 陣列長度至少 `10^5`
* 升冪陣列
* `K = 123`
* linear search 比較次數
* binary search 比較次數
* 搜尋時間統計
* best case
* middle case
* worst case
* not_found case
* 不修改原始資料

---

## 效能測試：best / middle / worst / not_found

### 測試指令

```bash
python .\p4_binary_search_perf.py
```

執行後在等待輸入時按：

```text
Ctrl + Z
Enter
```

### 實際輸出

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

case=not_found
data_size=100000
target=123
target_index=-1
linear_index=-1
linear_comparisons=100000
binary_index=-1
```

### 判斷

第四題效能比較成功。

觀察結果：

| Case      | Linear Search 比較次數 | Binary Search 比較次數 | 判斷                     |
| --------- | -----------------: | -----------------: | ---------------------- |
| best      |                  1 |                 16 | Linear 在 best case 較有利 |
| middle    |              50001 |                 16 | Binary 明顯較有效率          |
| worst     |             100000 |                 17 | Binary 明顯較有效率          |
| not_found |             100000 |            約 16～17 | Binary 明顯較有效率          |

結論：

* linear search 的比較次數會受到目標位置影響。
* target 在最前面時，linear search 最快。
* target 在中間或最後面時，linear search 需要大量比較。
* not_found 時，linear search 必須掃完整個陣列。
* binary search 因為每次都將搜尋範圍砍半，所以比較次數穩定維持在約 `16~17` 次。

---

## 雷達圖產生測試

### 測試指令

```bash
python .\p4_binary_search_perf.py
```

### 產生結果

```text
radar=assets/radar.png
```

### 檔案位置

```text
assets/radar.png
```

### 判斷

雷達圖成功產生。

雷達圖比較項目包含：

* `BestCmp`
* `MiddleCmp`
* `WorstCmp`
* `NotFoundCmp`
* `BestTime`
* `MiddleTime`
* `WorstTime`
* `NotFoundTime`

比較次數與執行時間皆使用「越小越好」的正規化方式，因此分數越接近 `1.0` 表示該搜尋法在該項目表現越好。

---

# 總測試指令

```bash
python .\test_p1_data_cleaning.py
python .\test_p2_caesar_cipher.py
python .\test_p3_digit_root_base.py
python .\test_p4_binary_search_perf.py
python .\p4_binary_search_perf.py
```

---

# 總結

本次完成 CPE 模擬實戰四題測試與驗收：

| 題目          | 測試檔                             | 結果                     |
| ----------- | ------------------------------- | ---------------------- |
| 第一題：資料清理    | `test_p1_data_cleaning.py`      | OK                     |
| 第二題：凱撒密碼    | `test_p2_caesar_cipher.py`      | OK                     |
| 第三題：任意進位數字根 | `test_p3_digit_root_base.py`    | OK                     |
| 第四題：二分搜尋效能  | `test_p4_binary_search_perf.py` | OK                     |
| 第四題：雷達圖     | `p4_binary_search_perf.py`      | 已產生 `assets/radar.png` |


