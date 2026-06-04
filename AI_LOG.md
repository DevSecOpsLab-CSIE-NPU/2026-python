# AI_LOG

## 我問 AI 什麼

請幫我依 TDD 流程為 `sum_of_gcd(n)` 撰寫測試與實作，至少 3 個測試案例，包含至少 1 個 edge case 與 1 個 invalid-input case（n <= 0 應拋出例外）。

## AI 給了什麼

AI 幫我：
- 在 `weeks/week-15/solutions/fychao/0603/test_gcd.py` 新增測試（包含 n=2、n=10、n=1 以及 n=0 的 invalid-input 測試）。
- 在 `weeks/week-15/solutions/fychao/0603/gcd.py` 實作 `sum_of_gcd(n)`，並加入對 `n<1` 的輸入檢查，會拋出 `ValueError`。
- 協助修正測試匯入問題（在測試中加入 `sys.path` 以能匯入同目錄的模組）、建立分支 `feature/wk15-0603-d14405048`，並推到我的 fork。

## 我改了什麼

我檢查並確認 AI 的變更後：
- 把測試與實作的變更 commit 到分支 `feature/wk15-0603-d14405048`。
- 確認並補上測試中匯入模組所需的 `sys.path` 調整，確保本地能直接執行 `python -m unittest`。
- 最後將分支推送到我的 fork（d14405048-tech），準備開 PR。
