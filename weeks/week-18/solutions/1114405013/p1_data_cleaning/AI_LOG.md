## 開工前資訊檢查表

### ① 函式簽名

本題不是只寫函式，而是整支程式讀 stdin、印 stdout。  
主要程式檔為 `main.py`。  
程式從標準輸入讀入多組數字資料，依照題目規則處理後輸出結果。

### ② 輸入邊界

輸入讀到 EOF 結束。  
每一組資料可能包含多個整數。  
數字中可能有重複值，需要先去除重複。  
我的學號參數為 D = 5，因此要篩選可以被 5 整除的數字。

### ③ 例外處理

題目主要處理合法整數輸入。  
如果某一組資料沒有任何數字可以被 D = 5 整除，輸出 `NONE`。  
如果輸入為空，程式不輸出任何內容。  
不額外擴充題目沒有要求的非法格式處理。

### ④ edge case

我設計「沒有任何數字可以被 5 整除」作為 edge case。  
例如第一組 sample：`4 7 4 2 9 2 6 7`，去重後為 `4 7 2 9 6`，沒有任何數字可以被 5 整除，所以輸出 `NONE`。

### ⑤ 驗收標準

D 固定為 5。  
每一組資料要先去除重複數字，再篩選可以被 5 整除的數字，最後由小到大排序輸出。  
如果沒有符合條件的數字，輸出 `NONE`。  
我會用 `python -m unittest -v test_data_cleaning.py` 驗證。  
測試必須先紅燈，再完成 `main.py` 實作後變綠燈。  
輸出必須和 expected output 完全一致，包含換行。

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
