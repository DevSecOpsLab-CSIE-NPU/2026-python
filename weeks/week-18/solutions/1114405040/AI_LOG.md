# 題目一 Data Cleaning

## 開發前思考

我先根據學號末兩碼 40 取得個位數 `u = 0`，
再依照題目公式計算：

```text
D = u % 4 + 2
D = 0 % 4 + 2
D = 2
```

本題的處理順序是先去除重複資料，
而且要保留第一次出現順序；
接著只留下可以被 2 整除的數字；
最後才把結果由小到大排序。

## 函式簽名

```python
def data_cleaning(nums):
```

輸入為整數串列 `nums`，
輸出為處理完成後的整數串列。
主程式負責讀取多組測資並依照格式輸出。

## 輸入邊界

輸入包含多組測資。
每組先讀取 `n`，
再讀取 `n` 個整數。
當讀到 `n = 0` 時代表結束，
該組不需要處理。

題目限制 `1 <= n <= 100000`，
因此我使用 `set` 記錄出現過的數字，
讓去重判斷維持較好的效率。
同時使用串列保存第一次出現順序，
避免只使用 `set` 造成順序遺失。

## 例外處理

若去重與篩選後沒有任何數字可被 2 整除，
輸出 `NONE`。

程式使用 `sys.stdin.buffer.read().split()` 讀取輸入，
所以可以支援 EOF。
輸出時不加入任何提示文字。

## Edge Case

我檢查了以下情況：

1. 所有數字都重複，確認只保留第一次出現。
2. 所有數字都不能被 2 整除，確認輸出 `NONE`。
3. 一開始就讀到 `n = 0`，確認不輸出任何內容。
4. 多組測資連續輸入，確認每組各輸出一行。

## Red 階段

我先建立測試檔 `test_q1_data_cleaning.py`，
在尚未加入主程式時執行測試，
結果為失敗。
失敗原因是 `q1_data_cleaning.py` 尚未存在，
符合先建立測試再完成實作的流程。

測試包含：

```text
8
4 7 4 2 9 2 6 7
3
1 3 5
0
```

預期輸出：

```text
2 4 6
NONE
```

## Green 階段

我加入 `q1_data_cleaning.py` 後重新執行測試，
`py -m unittest test_q1_data_cleaning.py` 通過。
另外也用範例輸入確認輸出格式正確。

通過結果：

```text
Ran 3 tests
OK
```

## Commit 紀錄

本題提交紀錄：

```text
test(q1): add failing test
feat(q1): implement solution
docs(q1): update development log and README
```

本題沒有發現需要額外修正的明顯錯誤，
因此沒有加入 `fix(q1): handle edge case` 提交。

## PR 紀錄

Branch：

```text
0622-1114405040-洪士閔-q1
```

PR Title：

```text
第1題0622 1114405040洪士閔
```

PR Base / Compare：

```text
Base: main
Compare: 0622-1114405040-洪士閔-q1
```

PR 說明會包含 What、Why、Test 三個部分，
並列出 sample 測試、edge case 測試與最終驗證結果。
