# AI_USAGE.md 內容紀錄

## 1. 我問 AI 的 3~5 個問題

1. 我問：幫我糾錯並改寫這段代碼（最初問 robot_game.py 改寫需求）。
2. 我問：生成測試（要求建立 test_robot.py）。
3. 我問：生成 TEST_LOG.md（附上測試流程與結果紀錄）。
4. 我問：生成 TEST_CASES.md （需包含 8 組測資）。
5. 我問：按照要求生成 README.md（須包含 7 個項目）。

## 2. 我採用的建議與原因

1. 建議：改寫 robot_game.py 成 Pygame 互動遊戲，包含 L/R/F/N/C/G/ESC 控制。
   - 原因：符合題目的遊戲規格和 MVP 要求，覆蓋功能需求最完整。
2. 建議：拆分核心邏輯到 robot_core.py，並寫測試 `test_robot.py`。
   - 原因：提高可測試性、拆分職責，方便 unittest 驗證方向旋轉、邊界、scent。
3. 建議：在 TEST_LOG 和 TEST_CASES 寫格式模板（問題給出要字數和欄位）。
   - 原因：快速完成格式要求，方便後續補實際測試結果。
4. 建議：README 加上 bug 修正紀錄與回放說明。
   - 原因：符合題目必做項目要求，且清楚說明流程。

## 3. 我拒絕的建議與原因

1. AI 建議：不用寫scent，直接把越界無限跳過。
   - 原因：不符合題目要求，漏掉核心機制。
2. AI 建議：不要做 GIF 回放，寫簡單 print 交互。
   - 原因：要求中明確要至少「可重播 play 過程」，需 GIF 或等效，print 副本不足。
3. AI 建議：把所有邏輯寫入一個大函式、不拆 file。
   - 原因：不利於單元測試與可讀性，且題目要求 Test-Oriented Development 多個測試檔要驗證。

## 4. AI 建議不完整且自行修正案例

- 案例：起初 AI 生成的 `robot_game.py` 內，`move_forward` 沒有 `robot_core.py` 拆分，且 `F` 越界後即使 scent 存在也仍設 `lost=True`。
- 自行修正：
  - 新建 `robot_core.py`，拆分 `Robot` 及 `move_forward` 行為。
  - 修正 scent 邏輯為：若 `(x,y,dir)` 已存在則不設 `lost`、不移動；否則才設定 `lost`、新增 scent。
  - 向 `robot_game.py` 導入 `Robot` 類，讓 UI 只能處理互動與繪製。

