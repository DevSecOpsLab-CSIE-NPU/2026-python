# 第二題 AI LOG

## 基本資訊
- **學生**：1114405054 蔡珽州 (座號 54)
- **參數**：SHIFT=5

## 開工前檢查
1. 函式簽名：`caesar_cipher(text: str, shift: int) -> str`
2. 輸入邊界：長度 <= 1000，多行直到 EOF 結束。
3. 例外處理：非字母字元（如數字、符號、空白）原樣保留，不進行位移。
4. Edge Case：'V' 移 5 位循環回 'A'；'Z' 移 5 位循環回 'E'。
5. 驗收標準：大小寫分開循環，一行對一行輸出加密字串。

## AI 協作紀錄（訪談摘要）

| 問題 | 學生回答 | checklist 狀態 |
|---|---|---|
| 函式簽名是什麼？ | `caesar_cipher(text: str, shift: int) -> str` | ✅ |
| 輸入邊界？ | 長度 <= 1000，多行直到 EOF 結束 | ✅ |
| 例外處理？ | 非字母字元原樣保留，不進行位移 | ✅ |
| Edge case？ | 'V' → 'A'、'Z' → 'E'，循環繞回 | ✅ |
| 驗收標準？ | 大小寫分開循環，一行對一行輸出加密字串 | ✅ |

紅燈 commit：`test: add CaesarCipher test cases`
綠燈 commit：`feat: implement CaesarCipher (shift=5)`
