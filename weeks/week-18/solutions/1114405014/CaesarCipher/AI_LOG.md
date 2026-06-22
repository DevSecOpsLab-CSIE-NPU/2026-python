# AI_LOG.md

## 題目

第二題：凱撒密碼（Caesar Cipher）

## 我問 AI 什麼

本題不是只問 AI 一次，而是依照 TDD 開發流程，分成多個階段與 AI 對話：

1. 我先上傳題目圖片，請 AI 說明第二題任務內容。
2. 我請 AI 撰寫第二題的測試檔 `test_caesar_cipher.py`。
3. 我請 AI 撰寫第二題的主程式 `caesar_cipher.py`。
4. 我上傳主程式、測試檔、測試紀錄與 AI_LOG 範本，請 AI 協助整理 `AI_LOG.md`、`README.md`、`PR.md`、`TEST_LOG.md`。
5. 我再次請 AI 重新撰寫 `AI_LOG.md`，因為原本內容沒有完整呈現整個對話與開發過程。
6. 我又進一步提醒 AI：「包含我們對話的紀錄並不只有一次」，要求 AI_LOG 必須反映多次對話、修改與人工判斷，而不是只寫成單次詢問紀錄。

## AI 給了什麼

AI 第一次先說明第二題是凱撒密碼題目，重點包含：

- 輸入為多行文字。
- 程式需要讀到 EOF 結束。
- `SHIFT` 依照學號末碼個位數 `u` 計算：`SHIFT = u % 25 + 1`。
- 大寫英文字母 `A-Z` 要在大寫範圍內循環。
- 小寫英文字母 `a-z` 要在小寫範圍內循環。
- 空白、數字、標點符號、換行等非英文字元要原樣保留。

接著 AI 提供測試檔 `test_caesar_cipher.py`，使用 `unittest` 測試核心函式與多行輸入處理，案例包含：

- 大寫字母位移。
- 小寫字母位移。
- 非英文字元保留。
- 大寫循環，例如 `XYZ -> ABC`。
- 小寫循環，例如 `xyz -> abc`。
- 空字串。
- 不同 shift 值。
- 多行輸入。
- 空行保留。

之後 AI 提供主程式 `caesar_cipher.py`，包含：

- `STUDENT_LAST_DIGIT = 4`
- `SHIFT = STUDENT_LAST_DIGIT % 25 + 1`
- `caesar_cipher(text, shift)`
- `process_text(input_text, shift)`
- `main()`
- 使用 `sys.stdin.read()` 讀取標準輸入直到 EOF。

最後 AI 協助整理文件，包含 AI_LOG、README、PR、TEST_LOG，並在我要求重新撰寫 AI_LOG 後，再補強「我改了什麼」與「人工判斷」內容。

## 我改了什麼

我不是直接複製 AI 的答案，而是依照題目要求與實際執行結果做了以下判斷與修正：

1. **確認 SHIFT 設定**

   AI 提醒 `SHIFT = u % 25 + 1`，我確認自己的學號末碼為 `4`，因此在主程式中設定：

   ```python
   STUDENT_LAST_DIGIT = 4
   SHIFT = STUDENT_LAST_DIGIT % 25 + 1
   ```

   所以實際執行時 `SHIFT = 5`。

2. **確認不能只讀一行**

   題目要求多行輸入直到 EOF，因此我判斷主程式不能只使用 `input()`，否則只能處理單行。最後採用：

   ```python
   input_text = sys.stdin.read()
   ```

   讓程式可以一次讀入所有輸入，直到 EOF 結束。

3. **保留測試使用不同 shift 值**

   雖然我的學號末碼讓正式執行的 `SHIFT` 是 `5`，但我沒有把測試全部寫死成 `SHIFT = 5`。我保留測試檔中使用 `shift=3`、`shift=1`、`shift=10` 的案例，因為這樣可以確認 `caesar_cipher()` 是真正依照參數運作，而不是只針對單一學號結果硬寫。

4. **確認大小寫必須分開處理**

   我判斷大寫與小寫不能用同一個 ASCII 基準處理，否則可能會讓大小寫混亂。因此主程式分別判斷：

   ```python
   if "A" <= char <= "Z":
       ...
   elif "a" <= char <= "z":
       ...
   ```

   大寫使用 `ord("A")` 為基準，小寫使用 `ord("a")` 為基準。

5. **確認非英文字元必須保留**

   題目要求非字母不變，因此我確認程式中 `else` 分支會直接保留原字元：

   ```python
   else:
       result.append(char)
   ```

   這可以保留空白、數字、標點符號、換行與空行。

6. **修正測試匯入錯誤**

   第一次執行 `pytest` 時發生：

   ```text
   ModuleNotFoundError: No module named 'caesar_cipher'
   ```

   我檢查後判斷是檔案名稱或放置位置造成測試檔無法匯入主程式，因此修正檔案命名或放置位置，讓 `test_caesar_cipher.py` 可以正確匯入：

   ```python
   from caesar_cipher import caesar_cipher, process_text
   ```

   修正後再次執行測試，10 個測試全部通過。

7. **要求重新撰寫 AI_LOG**

   我發現第一次整理的 AI_LOG 比較像單次紀錄，沒有完整呈現整個開發流程。因此我再次要求 AI 重新撰寫，並特別指出「我們對話的紀錄並不只有一次」。這次 AI_LOG 改成多階段紀錄，包含任務說明、測試檔、主程式、文件整理、測試錯誤修正與再次修改 AI_LOG 的過程。

## 使用 AI 後的人工判斷

- AI 提供的程式方向可以使用，但我必須自己確認題目要求，尤其是 EOF、多行輸入、大小寫循環與非字母保留。
- 測試不應只測範例，也要測 edge case，否則可能無法發現循環位移或空行處理錯誤。
- `caesar_cipher()`、`process_text()`、`main()` 分開設計比較好，因為可以分別測試核心邏輯、多行處理與標準輸入輸出。
- `pytest` 的第一次錯誤不是邏輯錯誤，而是模組匯入問題，因此要先確認檔名、路徑與測試執行位置。
- AI_LOG 不能只寫「AI 幫我寫了程式」，還要寫清楚自己判斷了什麼、修正了什麼，以及如何驗證結果。

## 測試結果紀錄

第一次執行測試時失敗：

```text
$ pytest
ERROR test_caesar_cipher.py
ModuleNotFoundError: No module named 'caesar_cipher'
```

修正檔案名稱或放置位置後再次執行：

```text
$ pytest
collected 10 items

test_caesar_cipher.py .......... [100%]

10 passed in 0.05s
```

## 對應題目要求

| 題目要求 | 實作方式 | 測試/檢查方式 |
|---|---|---|
| 多行輸入直到 EOF | 使用 `sys.stdin.read()` | `test_process_multiple_lines_until_eof` |
| 依學號末碼計算 SHIFT | `STUDENT_LAST_DIGIT = 4`，`SHIFT = 5` | 人工確認公式 |
| 大寫循環 | 以 `ord("A")` 為基準計算 | `test_uppercase_wrap_around` |
| 小寫循環 | 以 `ord("a")` 為基準計算 | `test_lowercase_wrap_around` |
| 非英文字元保留 | `else: result.append(char)` | `test_preserve_non_letters` |
| 空行保留 | `splitlines(keepends=True)` | `test_process_keeps_blank_lines` |
| 核心邏輯可重複測試 | `caesar_cipher(text, shift)` | 多個不同 shift 測試 |

## 結論

本題依照 TDD 流程完成。先確認題目需求，再撰寫測試檔，接著完成主程式，最後根據測試結果修正匯入問題。最終 `test_caesar_cipher.py` 共 10 個測試案例全部通過。這次 AI 的協助主要用於理解題目、產生測試方向與程式初稿，但我有自行確認學號位移、EOF 輸入方式、大小寫循環處理、非字母保留與測試錯誤修正。
