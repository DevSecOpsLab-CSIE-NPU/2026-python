# AI_LOG — 0617 timeit + 搜尋效能評估

> 本檔根據本次 AI 協作對話、測試紀錄與 benchmark 結果整理。
> 送出前請再次確認是否符合你的實際操作，尤其是提示詞是否完整逐字。

## 基本資訊

| 項目 | 內容 |
|---|---|
| 日期 | 0617 |
| 任務 | timeit + 搜尋效能評估 |
| 目標 | 用 TDD 完成 `timeit`，再用 `timeit` 粗略比較 linear search 與 binary search |
| 學號 | 1114405014 |
| 分支 | `0617-1114405014-凃彥任` |

## 我使用的提示詞紀錄

> 課堂要求提示詞逐字記錄。以下依照本次對話整理，送出前請確認是否和你實際輸入一致。

### Prompt 1

```text
說明任務流程
```

### Prompt 2

```text
進行測試檔補全
```

### Prompt 3

```text
直接提供五題對應答案並提交說明且記憶
```

### Prompt 4

```text
補全測試檔
```

### Prompt 5

```text
進行timiet填充(空函式 pass)
```

### Prompt 6

```text
進行實作
```

### Prompt 7

```text
撰寫test_search.py
```

### Prompt 8

```text
撰寫search.py
```

### Prompt 9

```text
如何用timeit 測linear  vs binary?
```

### Prompt 10

```text
進行任務check清單
```

### Prompt 11

```text
根據提供資料整理、撰寫README.md、TEST_LOG.md、PR.md、AI_LOG.md。有被限制的問題留空並回報，我們進行討論
```

### Prompt 12

```text
進行問題填充
```

## AI 反問我什麼 / 我怎麼回答

| 階段 | AI 反問 | 我怎麼回答 |
|---|---|---|
| timeit 規格確認 | `timeit` 要支援 `@timeit`、`@timeit(repeat=3)`，還是兩種都支援？ | 我決定主要支援 `@timeit(repeat=3)`，並讓 `repeat` 預設為 3。 |
| timeit 邊界條件 | `repeat` 的有效範圍是否只接受整數 `>= 1`？浮點數或字串要不要拒絕？ | 我決定 `repeat` 必須是整數且大於等於 1；`0`、負數、浮點數與字串都視為無效。 |
| timeit 例外行為 | 無效的 `repeat` 要怎麼處理？ | 我決定無效 `repeat` 要使用 `raise ValueError`，不能用 `assert`。 |
| timeit 副作用 | 被裝飾函式如果有副作用，`repeat=3` 時是否真的執行 3 次？ | 我決定要真的執行 3 次，因為 `repeat` 的目的就是實際多次量測。 |
| timeit records | `records` 是跨呼叫累積，還是每次呼叫清空？ | 我決定 `records` 跨呼叫累積，不在每次呼叫時清空。 |
| 紅燈驗收 | 什麼情況算紅燈？ | 在尚未建立或尚未完成 `timing.py` 前，測試應該失敗；完成實作後測試才全綠。 |
| search 行為 | `binary_search` 收到未排序資料時要怎麼定義？ | 我決定不主動檢查資料是否排序；若傳入未排序資料，結果不保證正確，並寫在 docstring。 |
| 效能判斷 | `binary_search` 很快，但排序成本是否一定划算？ | 我判斷如果資料已排序或會重複查詢，`binary_search` 較划算；如果資料未排序且只查一次，排序成本可能不划算。 |

## 檢查表狀態

| 項目 | 狀態 | 說明 |
|---|---|---|
| 函式簽名與回傳型別 | ✅ | `timeit(repeat=3)`；`linear_search(data, target) -> int`；`binary_search(data, target) -> int` |
| 輸入範圍／邊界條件 | ✅ | `repeat` 必須是 `int >= 1` |
| 例外行為 | ✅ | 無效 `repeat` 使用 `raise ValueError` |
| edge case 清單 | ✅ | `repeat=1`、副作用函式、records 跨呼叫累積、空 list、找不到目標、重複元素 |
| 驗收標準 | ✅ | 紅燈先失敗，完成實作後 `pytest` 全綠 |

## 我改了什麼

```text
我先補齊 test_timing.py，針對 timeit 的回傳值、metadata、records、last_elapsed、repeat=1、無效 repeat、不可 print 等規格撰寫測試。

接著我建立 timing.py，先用空函式讓測試可以 import，確認紅燈後，再實作 timeit 裝飾器。實作中使用 functools.wraps 保留函式資訊，使用 perf_counter 計算每次執行時間，並把每次耗時 append 到 wrapper.records，最後用 wrapper.last_elapsed 記錄平均耗時。

完成 timeit 後，我撰寫 test_search.py，測試 linear_search 與 binary_search 找到、找不到、空 list、不修改原資料等情況。

接著我建立 search.py，實作 linear_search 與 binary_search。linear_search 使用 enumerate 從左到右比對；binary_search 使用 left、right、middle 進行二分搜尋，並在 docstring 說明未排序資料的行為是不保證結果正確。

最後我建立 benchmark_search.py，用自己的 timeit 裝飾器測量 linear_search 與 binary_search 在 DATA_SIZE=100000、REPEAT=100 下的平均耗時，並把結果整理到 README.md、TEST_LOG.md、PR.md、AI_LOG.md。
```

## 我怎麼驗收

```text
我用 pytest 驗收紅燈與綠燈流程。

第一次 timeit 測試因為還沒有 timing.py，所以出現 ModuleNotFoundError: No module named 'timing'，這代表紅燈成功。

完成 timing.py 後再次執行 pytest，test_timing.py 的 6 個測試全部通過，代表 timeit 任務綠燈。

接著我撰寫 test_search.py，在 search.py 尚未建立時執行 pytest，出現 ModuleNotFoundError: No module named 'search'，代表搜尋測試也有先失敗。

完成 search.py 後再次執行 pytest，最後 test_search.py 與 test_timing.py 共 17 個測試全部通過，代表功能驗收完成。

效能部分，我執行 python benchmark_search.py，確認 linear_search 與 binary_search 都回傳 99999，且 records count 都是 100，代表 repeat 有正常執行。測試結果顯示 binary_search 平均耗時明顯低於 linear_search，因此我判斷在資料已排序且資料量較大時，binary_search 比 linear_search 更有效率。
```

## 測試結果摘要

### timeit 紅燈

```text
ModuleNotFoundError: No module named 'timing'
```

### timeit 綠燈

```text
6 passed in 0.02s
```

### search 紅燈

```text
ModuleNotFoundError: No module named 'search'
```

### 全部測試通過

```text
17 passed in 0.04s
```

## benchmark 結果摘要

```text
linear_search result: 99999
binary_search result: 99999
linear_search average elapsed: 0.002735066000132065
binary_search average elapsed: 1.4110001029621344e-06
linear_search records count: 100
binary_search records count: 100
```

## Git 紀錄

```text
658d570 test: add test_search
698ff2e feat: implement timeit decorator
2c3053b test: add timing tests
```

## Git 紀錄判斷

| 項目 | 狀態 | 說明 |
|---|---|---|
| timeit 測試 commit | ✅ | `2c3053b test: add timing tests` |
| timeit 實作 commit | ✅ | `698ff2e feat: implement timeit decorator` |
| timeit 是否 test before feat | ✅ | `test:` 在 `feat:` 前面 |
| search 測試 commit | ✅ | `658d570 test: add test_search` |
| search 是否有獨立 feat commit | 待確認 | 目前提供的 log 看不到獨立 `feat: implement search` commit |
| 工作區是否乾淨 | 待確認 | 目前尚未提供 `git status` 的完整輸出 |


## 我學到什麼

```text
這次練習讓我理解 TDD 的紅綠燈流程：先寫測試並確認失敗，再撰寫實作讓測試通過。timeit 的 repeat 可以降低單次量測誤差，records 可以保留每次測量資料，last_elapsed 則用來快速查看本次平均耗時。

在線性搜尋與二分搜尋的比較中，我觀察到資料量較大且資料已排序時，binary_search 明顯比 linear_search 快。不過 binary_search 不能直接用在未排序資料上，若資料原本沒有排序且只查詢一次，排序成本可能讓它不一定比 linear_search 划算。
```
