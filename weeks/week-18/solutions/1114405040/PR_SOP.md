# 第 4 題 PR SOP

## Branch

Branch 名稱：

```text
0622-1114405040-洪士閔-q4
```

## Red -> Commit

先建立測試檔，
確認尚未實作時測試失敗。

Commit：

```text
test(q4): add failing test
```

## Green -> Commit

加入 `q4_binary_search_eval.py`，
讓測試通過。

Commit：

```text
feat(q4): implement solution
```

## Push

推送分支：

```bash
git push -u origin 0622-1114405040-洪士閔-q4
```

若主倉庫沒有寫入權限，
改推送到個人 fork。

## PR

PR Title：

```text
第4題0622 1114405040洪士閔
```

## Base / Compare

```text
Base: main
Compare: 0622-1114405040-洪士閔-q4
```

## What

完成第 4 題 Binary Search Eval：

- 建立 `arr = list(range(1, 200001))`
- 設定 `K = 140`
- 實作 Linear Search
- 實作 Binary Search
- 使用 `timeit` 比較效能
- 使用 `matplotlib` 產生 `assets/radar.png`
- 補上測試、README、開發紀錄

## Why

本題練習比較線性搜尋與二分搜尋，
並透過比較次數、實測時間與雷達圖整理兩種方法的差異。

## Test

已執行：

```bash
py -m unittest test_q4_binary_search_eval.py
```

測試結果：

```text
Ran 3 tests
OK
```

Sample 測試輸出：

```text
FOUND idx=139 cmp=140
FOUND idx=139 cmp=17
linear : 0.005 s
binary : 0.002 s
=> binary faster
```

並確認產生：

```text
assets/radar.png
```
