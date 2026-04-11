# TEST_CASES.md

本文件記錄了各題目的測試案例設計，包含一般情境、邊界情況與反例驗證，旨在確保程式在各種極端輸入下的強健性。

## 測試案例列表

| 編號 | 測試情境 | 輸入 (Input) | 預期輸出 (Expected Result) | 實際輸出 (Actual Result) | 結果 | 對應測試函式 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Task 1: 基礎去重與排序** | `5 3 5 2 9` | `dedupe: 5 3 2 9`<br>`asc: 2 3 5 5 9`<br>`desc: 9 5 5 3 2`<br>`evens: 2` | 與預期一致 | **PASS** | `test_dedupe_order` |
| 2 | **Task 1: 無偶數輸入** | `1 3 5 7` | `evens:` (空) | 與預期一致 | **PASS** | `test_no_evens` |
| 3 | **Task 2: 同分同齡排序** | `2 2`<br>`ian 88 19`<br>`bob 88 19` | `bob 88 19`<br>`ian 88 19` | 與預期一致 | **PASS** | `test_tie_break_all` |
| 4 | **Task 2: K 值大於總人數** | `1 5`<br>`amy 100 18` | `amy 100 18` | 與預期一致 | **PASS** | `test_k_greater_than_n` |
| 5 | **Task 3: 空日誌處理 (m=0)** | `0` | (無任何輸出) | 與預期一致 | **PASS** | `test_empty_logs` |
| 6 | **Task 3: 行為統計與平手排序** | `3`<br>`c login`<br>`a login`<br>`b login` | `a 1`<br>`b 1`<br>`c 1`<br>`top_action: login 3` | 與預期一致 | **PASS** | `test_user_tie_break` |

---

## 關鍵測資詳解

### 1. 穩定排序驗證 (Task 2)
* **輸入內容**：
    ```text
    2 2
    ian 88 19
    bob 88 19
    ```
* **測試目的**：驗證三層排序邏輯。當「分數」與「年齡」皆定勝負時，必須檢查「名字」字母序（bob 優先於 ian）。
* **關鍵修正點**：最初若僅實作 `key=lambda x: -x[1]`，會導致輸出順序依賴於原始輸入順序，不符合規格。

### 2. 邊界情況：空統計 (Task 3)
* **輸入內容**：`0`
* **測試目的**：確認 `Counter` 與 `defaultdict` 在沒有資料時不會拋出異常（如 `IndexError`）。
* **關鍵修正點**：在存取 `most_common(1)` 前增加了 `if action_counts:` 的保護判斷。

### 3. 去重保序 (Task 1)
* **輸入內容**：`5 3 5 2 9 2`
* **測試目的**：驗證 `dedupe` 輸出應為 `5 3 2 9` 而非 `2 3 5 9`。
* **關鍵修正點**：嚴格禁止使用 `list(set(nums))`，改用手寫 `seen` 集合過濾法。