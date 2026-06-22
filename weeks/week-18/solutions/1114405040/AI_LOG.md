# 題目四 Binary Search Eval

## 開發前思考

我先根據學號末兩碼 40 計算搜尋目標：

```text
K = 100 + 40
K = 140
```

本題要建立 `arr = list(range(1, 200001))`，
並比較 Linear Search 與 Binary Search。
因為陣列已經是升冪排序，
所以 Binary Search 可以直接使用。

## 函式簽名

```python
def linear_search(arr, target):
def binary_search(arr, target):
```

兩個函式都輸入整數陣列與搜尋目標，
並回傳：

```text
(found, index, comparisons)
```

其中 `found` 表示是否找到，
`index` 表示目標位置，
`comparisons` 表示比較次數。

## 輸入邊界

本題不需要從標準輸入讀取資料。
程式內直接建立：

```python
ARR = list(range(1, 200001))
K = 140
```

陣列長度為 200000，
內容為 1 到 200000 的升冪整數。

## 例外處理

若找到目標值，
輸出格式為：

```text
FOUND idx=<index> cmp=<comparisons>
```

若找不到目標值，
輸出格式為：

```text
NOT FOUND cmp=<comparisons>
```

雷達圖輸出前會自動建立 `assets` 資料夾，
避免資料夾不存在時無法儲存圖片。

## Edge Case

我檢查了以下情況：

1. `K = 140` 可找到索引 `139`。
2. Linear Search 比較次數為 `140`。
3. Binary Search 可用較少比較次數找到同一索引。
4. 找不到目標時可輸出 `NOT FOUND cmp=<comparisons>`。
5. `assets/radar.png` 可正常產生。

## Red 階段

我先建立測試檔 `test_q4_binary_search_eval.py`，
在尚未加入主程式時執行測試，
結果為失敗。
失敗原因是 `q4_binary_search_eval.py` 尚未存在，
符合先建立測試再完成實作的流程。

測試內容包含搜尋結果、
找不到格式、
程式輸出與雷達圖檔案產生。

## Green 階段

我加入 `q4_binary_search_eval.py` 後重新執行測試，
`py -m unittest test_q4_binary_search_eval.py` 通過。
另外也直接執行程式確認輸出格式正確，
並確認 `assets/radar.png` 已產生。

通過結果：

```text
Ran 3 tests
OK
```

## Commit 紀錄

本題提交紀錄：

```text
test(q4): add failing test
feat(q4): implement solution
docs(q4): update development log and README
```

本題沒有發現需要額外修正的明顯錯誤，
因此沒有加入 `fix(q4): handle edge case` 提交。

## PR 紀錄

Branch：

```text
0622-1114405040-洪士閔-q4
```

PR Title：

```text
第4題0622 1114405040洪士閔
```

PR Base / Compare：

```text
Base: main
Compare: 0622-1114405040-洪士閔-q4
```

PR 說明會包含 What、Why、Test 三個部分，
並列出 sample 測試、edge case 測試與最終驗證結果。
