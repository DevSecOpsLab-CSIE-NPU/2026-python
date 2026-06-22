# AI_LOG — 第一題：資料清理 (Data Cleaning)

## 第一題：資料清理 (Data Cleaning)

### 我問 AI 什麼
1. 告知 AI 要開始第一題「資料清理」，並跟 AI 討論拆解 $\ge 3$ 個 test cases。
2. 要求 AI 建立測試檔案、執行並確認紅燈、完成 `test:` commit。
3. 要求 AI 寫實作代碼、執行確認綠燈、完成 `feat:` commit。
4. 請 AI 用我的學號參數 $D = 4$ 計算 Sample Input 的兩組預期輸出。

### AI 反問我什麼 / 我怎麼回答
*   **AI 反問**：「函式簽名與回傳型別」打算如何定義？無數值符合時回傳空 list 還是 `"NONE"` 字串？
    *   **我回答**：定義為 `def clean_data(data: list, d: int) -> list:`，無符合者回傳 `"NONE"`。
*   **AI 反問**：回傳 `"NONE"` 字串與簽名中的 `-> list` 衝突，建議將計算與輸出分離，或使用 `list | str` 聯集型別，想選哪種？
    *   **我回答**：堅持函式直接回傳 `"NONE"` 字串。
*   **AI 反問**：`d = 0` 的例外、空 list 邊界、全被篩掉的 edge case 怎麼處理？
    *   **我回答**：`d = 0` 拋 `ValueError`，其餘皆回傳 `"NONE"`。
*   **AI 反問**：(提供測試檔後) 這 5 個 test cases 是否足夠，是否需要加其他特殊案例？
    *   **我回答**：修改我的決定，把原本的 `d = 0` 拋 `ValueError`，改為 `d = 0` 直接回傳 `"NONE"`，並要求更新測試。

### AI 給了什麼
1. 建立了含有 5 個測試案例的 `test_clean_data.py`。
2. 配合我修改的要求，更新 `test_d_zero_returns_none` 測試。
3. 實作了 `clean_data.py`（使用 set 進行 O(N) 複雜度保序去重，隨後進行篩選與排序）。

### 我改了什麼
1.  **修改了例外處理設計**：原本決定 `d = 0` 拋 `ValueError`，但後來考量程式的魯棒性，決定改成當 `d = 0` 時與找不到資料一樣「回傳 `"NONE"`」。我主動抓出原本測試設計的衝突，並指引 AI 修改 `test_d_zero_raises_valueerror` 為 `test_d_zero_returns_none`。
2.  **型別優化**：主動確認傳入 `list` 而回傳 `list | str` 的動態型別混合處理，確保測試跟實作的斷言完全一致。
