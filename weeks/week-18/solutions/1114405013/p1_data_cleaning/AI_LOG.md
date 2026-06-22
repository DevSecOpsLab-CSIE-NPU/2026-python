# AI 使用紀錄

## 我問了 AI 什麼

1. 請 AI 根據題目設計至少 3 個 test case，其中至少 1 個是 edge case。
2. 我補充本題的固定參數 `D = 5`。
3. 我確認本題要寫成「整支程式讀 stdin / 印 stdout」，不是只寫函式。
4. 我請 AI 幫我設計 `unittest` 測試案例，但先不要寫正式實作。
5. 我詢問測試檔案名稱、如何執行測試，以及 red test 後如何進入實作。
6. 我完成 red test 和 `test:` commit 後，請 AI 放入正式程式。

## AI 給了我什麼

1. AI 幫我整理了 4 個測試情境：
   - 一般案例
   - 邊界案例
   - 特殊案例
   - edge case
2. AI 提供了 `test_data_cleaning.py`，用 `unittest` 模擬 stdin / stdout。
3. AI 說明如何執行測試：

   ```bash
   python -m unittest -v test_data_cleaning.py
## 我改了什麼
我設定本題的固定參數為 D = 5。

我決定程式採用 stdin / stdout 格式。

我建立作業資料夾：

text
weeks/week-18/solutions/1114405013/p1_data_cleaning/
我放入測試檔：

text
test_data_cleaning.py
我先執行測試，確認 red test 失敗後，完成 test: commit。

我放入正式程式：

text
main.py
我再次執行 unittest，確認測試全部通過。
