# 第 3 題 PR SOP

## Branch

Branch 名稱：

```text
0622-1114405040-洪士閔-q3
```

## Red -> Commit

先建立測試檔，
確認尚未實作時測試失敗。

Commit：

```text
test(q3): add failing test
```

## Green -> Commit

加入 `q3_digit_root.py`，
讓測試通過。

Commit：

```text
feat(q3): implement solution
```

## Push

推送分支：

```bash
git push -u origin 0622-1114405040-洪士閔-q3
```

若主倉庫沒有寫入權限，
改推送到個人 fork。

## PR

PR Title：

```text
第3題0622 1114405040洪士閔
```

## Base / Compare

```text
Base: main
Compare: 0622-1114405040-洪士閔-q3
```

## What

完成第 3 題 Digit Root：

- 使用 `base = 2`
- 建立 `digit_root_base(x, base)`
- 逐行讀取輸入直到 EOF
- 正確處理 `0`、`1`、`2`、`3` 等 edge case
- 正確處理大數
- 補上測試、README、開發紀錄

## Why

本題練習 base 進位轉換與位數和計算，
並確認重複計算流程能在結果小於 base 時停止。

## Test

已執行：

```bash
py -m unittest test_q3_digit_root.py
```

測試結果：

```text
Ran 3 tests
OK
```

Sample 測試輸出：

```text
1
```

Edge Case 測試輸出：

```text
0
1
1
1
1
```
