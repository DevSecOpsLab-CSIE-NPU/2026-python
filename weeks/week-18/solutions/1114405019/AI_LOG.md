# AI_LOG

## 我問 AI 什麼

請 AI 依「凱薩位移密碼（SHIFT=10，讀到 EOF 結束）」的題目規格，先提出函式簽名與測試規劃（不要直接寫完整程式），確認後才寫測試（紅燈）再寫實作（轉綠燈）。

## AI 給了什麼

提出 `shift_char`（單字元位移）、`shift_line`（整行）、`main`（讀到 EOF 的 I/O 迴圈）三個函式的簽名與 9 個測試案例規劃（基本位移、大小寫循環邊界 Q→A/q→a、非字母不變、空白行、整行非字母、混合大小寫數字標點、Sample 驗算、EOF 終止）。我確認後 AI 才動手寫 `test_solution.py`，跑出 `ModuleNotFoundError` 確認紅燈，再寫 `solution.py` 讓全部測試轉綠燈。

## 我改了什麼

- 確認 `main` 用 `for line in sys.stdin` 而非 `input()`，因為這題是讀到 EOF 結束（跟其他題讀到終止值 n=0 不同），需要正確區分「空白行」與「真正的輸入結束」，這點我有要求 AI 在動手前先說明清楚。
- 額外要求用真實 stdin pipe（非 mock）跑一次 Sample I/O 驗證，確認輸出 `Rovvy, XZE!` / `klm HIJ` 與我自行手算的預期完全一致，不只是依賴 unit test 通過。
- 補充要求每個測試案例要寫清楚「驗證的原因」（例如 q→a 是為了避免大寫公式誤套用在小寫字元上的常見 bug），而不是只斷言輸出值。
