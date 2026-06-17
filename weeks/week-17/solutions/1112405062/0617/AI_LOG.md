# AI_LOG — 0617 timeit + 搜尋效能評估

## 階段一：timeit 裝飾器（完整 TDD）

### 規格檢查表問答

| AI 反問 | 我怎麼回答 |
|---------|-----------|
| 簽名與回傳型別？repeat 放哪？ | 回傳 wrapper 函式；裝飾後函式型別同原函式（functools.wraps）；repeat 放在裝飾器參數（@timeit(repeat=N)）。 |
| 邊界條件？ | repeat 最小值 1；0 或負數 raise ValueError。 |
| 例外行為？ | 僅 repeat < 1 拋 ValueError（不用 assert），無其他。 |
| 邊緣案例：被裝飾函式拋例外？ | f.records 不記錄該次；f.last_elapsed 保持前次值（首次則 None）。 |
| 驗收標準？ | 測試沒過 = 紅燈。 |

### 實作摘要

- 測試 9 案例：回傳值、metadata、records/avg、invalid repeat、repeat=1、無 print、例外處理、預設 repeat=3、avg 正確性
- `timeit` 支援 `@timeit` 與 `@timeit(repeat=N)` 雙模式，`repeat < 1` 在 decorator 層 fail-fast

### 觀念題

| AI 問 | 我怎麼回答 |
|-------|-----------|
| repeat 檢查為何放 decorator 層而非 wrapper 內？ | fail fast，只檢查一次不浪費。放 wrapper 裡會延遲故障且每次呼叫都檢查。 |

---

## 階段二：search.py（輕量評估）

### 規格檢查表問答

| AI 反問 | 我怎麼回答 |
|---------|-----------|
| linear_search 簽名？ | `(data: list, target) -> int`，找到回 index，找不到回 -1。 |
| 空 list 輸入？ | 回 -1。 |
| binary_search 未排序行為？ | undefined behavior，不檢查。 |
| 邊緣案例？ | 頭、尾、中間、單一元素、大量資料。 |
| 驗收標準？ | 所有測試通過即算驗收，不要求嚴格 TDD。 |

---

## 我改了什麼

- 在 test_timing.py 補了 `test_exception_leaves_records_unchanged`（當裝飾函式拋例外時，確認 records 不追加、last_elapsed 不更新）——這是規格討論時確定的 edge case，AI 初始沒寫到
- benchmark.py 呼叫時發現 `@timeit(repeat=30)` 裝飾 benchmark 函式後，函式內的 data/target 參數仍正確傳入，驗證了 wrapper 的 `*args, **kwargs` 轉發正確
