# 第 1 題 PR SOP

## Branch

Branch 名稱：

```text
0622-1114405040-洪士閔-q1
```

## Red -> Commit

先建立測試檔，
確認尚未實作時測試失敗。

Commit：

```text
test(q1): add failing test
```

## Green -> Commit

加入 `q1_data_cleaning.py`，
讓測試通過。

Commit：

```text
feat(q1): implement solution
```

## Push

推送分支：

```bash
git push -u origin 0622-1114405040-洪士閔-q1
```

## PR

PR Title：

```text
第1題0622 1114405040洪士閔
```

## Base / Compare

```text
Base: main
Compare: 0622-1114405040-洪士閔-q1
```

## What

完成第 1 題 Data Cleaning：

- 去除重複數字並保留第一次出現順序
- 保留可被 `D = 2` 整除的數字
- 將結果升冪排序
- 無符合結果時輸出 `NONE`
- 補上測試、README、開發紀錄

## Why

本題練習使用集合處理去重、
使用條件篩選資料，
並依照題目指定格式輸出結果。

## Test

已執行：

```bash
py -m unittest test_q1_data_cleaning.py
```

測試結果：

```text
Ran 3 tests
OK
```

Sample 測試輸出：

```text
2 4 6
NONE
10 12
```
