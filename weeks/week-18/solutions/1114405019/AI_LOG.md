# AI 使用紀錄：第三題（任意進位的數字根）

依 week-18 README 的「AI 使用方式」五步驟，實際操作紀錄如下。

## 1. 讀題目設計 unit test，加繁中註解

先把題目（base 依學號查表得 6、需多輪收斂、x=0 特例、base 可能是 16）整理成假設與函式簽名提案，經我確認後才寫測試：

- 產出 `test_digital_root.py`，針對 `digit_sum_in_base` 與 `digital_root` 兩個函式設計測試，涵蓋：
  - 0 的特例（規定值，非公式算出）
  - x < base 的單一位數（免迭代）
  - 63 案例需要兩輪才收斂（最容易漏掉的邊界）
  - 大數（10^9）確認不死迴圈
  - base=16 時數字大於 9 仍以十進位數值相加
- 在實作之前先跑一次測試，確認是紅燈（`ModuleNotFoundError`），紀錄於 `test_red.txt`。

## 2. 寫程式並跑完測試，保留測試紀錄

確認測試案例後才寫 `digital_root.py`（拆成 `digit_sum_in_base` 轉進位＋相加、`digital_root` 收斂迴圈、`main` 用 EOF 讀取輸入）。跑測試轉綠燈，紀錄於 `test_green.txt`；另用題目 Sample I/O（0/8/63）驗證實際輸出，紀錄於 `sample_io.txt`。

## 3. 加上繁體中文的註解說明

為 `digital_root.py` 補上逐行的繁體中文註解，說明 `x % base` / `x // base` 的短除法概念，以及收斂迴圈的終止條件。

## 4. 更簡單、更好記的版本（`-easy`）

請 AI 提供不拆 helper function、單一函式內用巢狀迴圈完成的「好記版」，產出 `digital_root-easy.py`，並用同一組 Sample I/O 驗證輸出與手打版一致（`sample_io_easy.txt`）。

## 5. 加上繁體中文的詳細註解說明

為 `digital_root-easy.py` 補上詳細的繁體中文註解，包含口訣式的邏輯說明（「只要還是兩位數以上就繼續加總，直到變成一位數」）及 x=0 為何不需要特例判斷。

## 使用的 AI 工具

Claude Code（claude-sonnet-4-6）。

## 人工確認事項

- 函式簽名提案、測試案例內容、Sample I/O 預期輸出（base=6 下 0/8/63 → 0/3/3）均由我手動確認後才進入下一步。
- 所有測試與 Sample I/O 結果均實際執行驗證，未盲目採信 AI 輸出。
