# 題目二 Caesar Cipher

## 開發前思考

我先根據學號末兩碼 40 取得個位數 `u = 0`，
再依照題目公式計算：

```text
SHIFT = u % 25 + 1
SHIFT = 0 % 25 + 1
SHIFT = 1
```

本題只需要對英文字母做 Caesar Cipher 右移，
其他字元必須保持原樣。
大寫與小寫字母的範圍不同，
所以我分開處理 `A` 到 `Z` 與 `a` 到 `z`。

## 函式簽名

```python
def caesar_cipher(line):
```

輸入為單行文字 `line`，
輸出為完成位移後的字串。
主程式逐行讀取直到 EOF，
每一行都交給函式處理後輸出。

## 輸入邊界

輸入可以包含多行文字，
直到 EOF 結束。
每一行可能包含：

1. 大寫英文字母
2. 小寫英文字母
3. 空白
4. 數字
5. 標點符號

程式使用 `for line in sys.stdin` 逐行讀取，
因此會保留原本的換行格式。

## 例外處理

非英文字元不做轉換，
直接加入結果。
若輸入為空，
程式不輸出任何內容並正常結束。

字母轉換使用 `ord()` 與 `chr()`，
並使用 `% 26` 處理循環，
確保 `Z` 右移後成為 `A`，
`z` 右移後成為 `a`。

## Edge Case

我檢查了以下情況：

1. `Z` 右移後變成 `A`。
2. `z` 右移後變成 `a`。
3. 空白、數字與標點符號保持原樣。
4. 多行輸入可逐行輸出。

## Red 階段

我先建立測試檔 `test_q2_caesar_cipher.py`，
在尚未加入主程式時執行測試，
結果為失敗。
失敗原因是 `q2_caesar_cipher.py` 尚未存在，
符合先建立測試再完成實作的流程。

測試包含題目範例：

```text
Hello, NPU!
abc XYZ
```

預期輸出：

```text
Ifmmp, OQV!
bcd YZA
```

也測試 `Zz Aa`，
預期輸出 `Aa Bb`。

## Green 階段

我加入 `q2_caesar_cipher.py` 後重新執行測試，
`py -m unittest test_q2_caesar_cipher.py` 通過。
另外也用範例輸入確認輸出格式正確。

通過結果：

```text
Ran 3 tests
OK
```

## Commit 紀錄

本題提交紀錄：

```text
test(q2): add failing test
feat(q2): implement solution
docs(q2): update development log and README
```

本題沒有發現需要額外修正的明顯錯誤，
因此沒有加入 `fix(q2): handle edge case` 提交。

## PR 紀錄

Branch：

```text
0622-1114405040-洪士閔-q2
```

PR Title：

```text
第2題0622 1114405040洪士閔
```

PR Base / Compare：

```text
Base: main
Compare: 0622-1114405040-洪士閔-q2
```

PR 說明會包含 What、Why、Test 三個部分，
並列出 sample 測試、edge case 測試與最終驗證結果。
