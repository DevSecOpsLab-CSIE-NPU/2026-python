# 題目三 Digit Root

## 開發前思考

本題依照題目表格使用 `base = 2`。
我把問題拆成兩個部分：
先計算某個整數在 base 進位下的所有位數和，
再重複這個步驟，
直到結果小於 base 為止。

## 函式簽名

```python
def digit_root_base(x, base):
```

輸入為非負整數 `x` 與進位值 `base`，
輸出為反覆加總位數後得到的結果。
程式另外建立 `digit_sum_in_base(x, base)`，
負責計算單次 base 進位的位數和。

## 輸入邊界

輸入為逐行提供的非負整數，
直到 EOF 結束。
題目限制為：

```text
0 <= x <= 10^9
```

程式使用 `for line in sys.stdin` 逐行處理，
空白行會略過。

## 例外處理

題目限制輸入為非負整數，
因此主程式按照有效整數處理。
若輸入為 `0`，
函式直接回傳 `0`。

本題不使用外部套件，
只使用整數除法與取餘數取得 base 進位的每一位。

## Edge Case

我檢查了以下情況：

1. `0`：最小輸入值，應直接輸出 `0`。
2. `1`：已經小於 `base = 2`，應直接輸出 `1`。
3. `2`：二進位為 `10`，位數和為 `1`，應輸出 `1`。
4. `3`：二進位為 `11`，位數和為 `2`，需要再算 `10 -> 1`，應輸出 `1`。
5. `63`：題目範例，應輸出 `1`。
6. `1000000000`：接近輸入上限的大數，可以正常結束。
4. 多行輸入可以逐行輸出結果。

## Red 階段

我先建立測試檔 `test_q3_digit_root.py`，
在尚未加入主程式時執行測試，
結果為失敗。
失敗原因是 `q3_digit_root.py` 尚未存在，
符合先建立測試再完成實作的流程。

測試包含：

```text
63
0
1000000000
1
2
3
```

預期輸出：

```text
1
0
1
1
1
1
```

## Green 階段

我加入 `q3_digit_root.py` 後重新執行測試，
`py -m unittest test_q3_digit_root.py` 通過。
另外也直接執行程式確認多行輸入輸出格式正確。

通過結果：

```text
Ran 3 tests
OK
```

## Commit 紀錄

本題提交紀錄：

```text
test(q3): add failing test
feat(q3): implement solution
docs(q3): update development log and README
```

本題沒有發現需要額外修正的明顯錯誤，
因此沒有加入 `fix(q3): handle edge case` 提交。

## PR 紀錄

Branch：

```text
0622-1114405040-洪士閔-q3
```

PR Title：

```text
第3題0622 1114405040洪士閔
```

PR Base / Compare：

```text
Base: main
Compare: 0622-1114405040-洪士閔-q3
```

PR 說明會包含 What、Why、Test 三個部分，
並列出 sample 測試、edge case 測試與最終驗證結果。
