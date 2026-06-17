# TEST_LOG — 0617 timeit + search

## 測試環境

| 項目 | 內容 |
|---|---|
| OS | Windows |
| Python | 3.13.9 |
| 測試工具 | pytest 8.4.2 |
| 專案路徑 | `D:\2026-python\weeks\week-17\solutions\1114405014` |

## 測試紀錄摘要

### 1. timeit 紅燈：尚未建立 `timing.py`

執行指令：

```bash
pytest
```

結果：

```text
collected 0 items / 1 error

ERROR collecting test_timing.py
ModuleNotFoundError: No module named 'timing'
```

判斷：

這是任務一的紅燈狀態，代表測試已經先寫好，但 `timing.py` 尚未完成或尚未存在。

---

### 2. timeit 綠燈：完成 `timing.py`

執行指令：

```bash
pytest
```

結果：

```text
collected 6 items

test_timing.py ...... [100%]

6 passed in 0.02s
```

判斷：

`timeit` 裝飾器已通過測試，包含回傳值、metadata、records、last_elapsed、repeat 邊界與不 print 等測試。

---

### 3. search 紅燈：尚未建立 `search.py`

執行指令：

```bash
pytest
```

結果：

```text
collected 6 items / 1 error

ERROR collecting test_search.py
ModuleNotFoundError: No module named 'search'
```

判斷：

這是任務二搜尋函式的紅燈狀態，代表 `test_search.py` 已建立，但 `search.py` 尚未完成或尚未存在。

---

### 4. 全部測試通過

執行指令：

```bash
pytest
```

結果：

```text
collected 17 items

test_search.py ........... [ 64%]
test_timing.py ......      [100%]

17 passed in 0.04s
```

判斷：

`timing.py`、`search.py` 與其對應測試皆通過。

---

## benchmark 紀錄

執行指令：

```bash
python benchmark_search.py
```

結果：

```text
linear_search result: 99999
binary_search result: 99999
linear_search average elapsed: 0.002735066000132065
binary_search average elapsed: 1.4110001029621344e-06
linear_search records count: 100
binary_search records count: 100
```

判斷：

在 `DATA_SIZE=100_000`、`REPEAT=100`、target 為最後一筆資料時，`binary_search` 明顯快於 `linear_search`。
