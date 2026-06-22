# AI_LOG

## 開工前資訊檢查表

### ① 函式簽名

本題不是只寫函式，而是整支程式讀 stdin、印 stdout。  
主要程式檔為 `main.py`。  
程式從標準輸入讀入多行文字，處理後輸出多行文字。

### ② 輸入邊界

輸入可能有多行文字，讀到 EOF 結束。  
每一行都要處理，輸出行數要和輸入行數相同。  
文字中可能包含大寫英文字母、小寫英文字母、空白、標點符號、數字。

### ③ 例外處理

非英文字母不做位移，直接保留原字元。  
空白、逗號、驚嘆號、數字與其他符號都保持不變。  
如果輸入為空，程式不輸出任何內容。

### ④ edge case

我測試 `wxyz WXYZ`，因為 SHIFT = 4 時需要從 z/Z 循環回 a/A。  
預期輸出是 `abcd ABCD`。

### ⑤ 驗收標準

SHIFT 固定為 4。  
大寫 A-Z 往後位移 4 格，小寫 a-z 往後位移 4 格。  
超過 Z 或 z 要循環回開頭。  
非英文字母保持不變。  
輸出必須和 expected output 完全一致，包含換行。

---


## 我問了 AI 什麼

1. 我請 AI 根據第二題 Caesar Cipher 題目，先設計 unittest 測試。
2. 我告訴 AI 這題是整支程式讀 stdin、印 stdout，不是只寫函式。
3. 我提供題目規格：SHIFT 固定為 4、大小寫英文字母要位移、非英文字母保持不變、讀到 EOF 結束。
4. 我要求 AI 先只產生測試檔，不要寫正式實作。
5. 我後來要求把測試檔名稱改成 `test_caesar_cipher.py`。
6. 我確認 red test 失敗，並完成 `test:` commit 後，請 AI 幫我建立 `main.py`。

## AI 給了我什麼

1. AI 幫我設計了 3 個 unittest 測試案例：
   - 一般案例：測大小寫字母位移與標點保留。
   - edge case：測 `z/Z` 超過後循環回 `a/A`。
   - 特殊案例：測數字、標點、空白行保持不變。
2. AI 建立了測試檔：

   ```text
   test_caesar_cipher.py


## 我改了什麼

我確認本題的 SHIFT 是 4，不是 sample 上的 SHIFT = 3。  
所以我把 sample 重新計算為：  
`Hello, NPU!` 會輸出 `Lipps, RTY!`，  
`abc XYZ` 會輸出 `efg BCD`。  
我也確認 edge case：`wxyz WXYZ` 應輸出 `abcd ABCD`。  
我先執行 unittest 確認紅燈，再建立 `main.py`，最後重新執行 unittest 確認綠燈。