# AI_LOG

## 任務一：timeit 裝飾器 （TDD）

| 階段 | 我問 AI 什麼 | AI 給了什麼 | 我改了什麼 |
|---|---|---|---|
| 測試 (紅燈) | 拆 ≥3 個 test case（含 ≥1 個 edge case） | 先依教案走開發訪談模式，反問簽名、邊界、例外、edge case、驗收標準；填滿檢查表後給 7 個測試（含 repeat=1、副作用多次執行、多函式互不干擾 3 個 edge case） | |
| 實作 (綠燈) | 寫實作 → 跑到綠燈 → commit | `timing.py`：`timeit` 裝飾器，`repeat<1 raise ValueError`、`functools.wraps`、`records` / `last_elapsed` | |

| AI 反問我什麼 | 我怎麼回答 |
|---|---|
| repeat 參數合法範圍？repeat=0 怎麼處理？ | 整數且 repeat>=1，repeat<1 raise ValueError |
| Edge cases 有哪些？ | 副作用會執行 repeat 次 |
| 驗收標準？ | 測試正常執行，並正確證明需求尚未被滿足 |

## 任務二：search.py（輕量評估）

| 階段 | 我問 AI 什麼 | AI 給了什麼 | 我改了什麼 |
|---|---|---|---|
| 測試 (紅燈) | 任務二拆 ≥3 個 test case（含 ≥1 個 edge case） | 反問邊界、例外、edge case；填滿後給 15 個測試（linear 7 + binary 8，含空 list、單一元素、不修改 data 驗證） | |
| 實作 (綠燈) | 寫實作 → 跑到綠燈 → commit | `search.py`：`linear_search` 逐一比對，`binary_search` 左右指標；precondition 寫進 docstring | |

| AI 反問我什麼 | 我怎麼回答 |
|---|---|
| 空 list 時回傳什麼？ | -1 |
| binary_search 收到未排序 data 怎麼處理？ | 不檢查，視為 precondition |
| Edge cases 有哪些？ | 空 list、只有一個元素 |
