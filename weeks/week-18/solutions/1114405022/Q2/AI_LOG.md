# AI_LOG — 第二題：凱撒密碼 (Caesar Cipher)

## 第二題：凱撒密碼 (Caesar Cipher)

### 我問 AI 什麼
1. 告知 AI 開始第二題，並要求拆解 $\ge 3$ 個 test cases。
2. 要求 AI 依照我的學號位移量 `SHIFT = 3` 進行 TDD 流程（寫測試 $\to$ 紅燈 $\to$ commit $\to$ 實作 $\to$ 綠燈 $\to$ commit）。

### AI 反問我什麼 / 我怎麼回答
*   **AI 反問**：函式簽名與回傳型別為何？
    *   **我回答**：回傳將 `text` 依照 `shift` 位移後的加密字串。參數包括 `text` (str) 與 `shift` (int)。
*   **AI 反問**：`shift` 非整數的例外、空字串與純數字符號的邊界、以及 `SHIFT = 3` 的 `A`、`z`、`"Hello, NPU!"` 該如何加密？
    *   **我回答**：
        1.  問 AI 關於 `shift` 非整數的處理建議，隨後聽取 AI 的建議選擇「嚴謹做法，明確拋出 `TypeError`」。
        2.  非英文字元（數字、符號、空白）保持不變。
        3.  `A` 移 3 格變 `D`，小寫 `z` 循環變 `c`。在 AI 協助下，釐清 `"Hello, NPU!"` 會被加密成 `"Khoor, QSX!"`。
*   **AI 反問**：進一步舉例 `"abc XYZ"` 在 `SHIFT = 3` 該加密成什麼？
    *   **我回答**：理解了字母表末端循環的原理，得出 `"def ABC"` 的正確預期。

### AI 給了什麼
1. 建立了 `test_caesar.py`，包含 4 個測試（基本、末端循環、非字母與空字串、TypeError 測試）。
2. 實作了 `caesar.py`（利用 `ord()` 和 `chr()` 計算大小寫字母位移，並透過 `% 26` 完美實現循環與負數處理）。

### 我改了什麼
1.  **決策例外處理策略**：在 AI 給予多種分析後（Implicit casting vs TypeError），我主動選擇了最符合軟體工程 Fail-Fast 原則的 `TypeError` 當作例外阻擋條件。
2.  **補充驗證案例**：在討論階段，我主動提出對 `"abc XYZ"` 這種跨越字母表末端的連續大寫/小寫組合進行確認，補足了 AI 原始構想中對多重邊界的信心。
