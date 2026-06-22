# Q1 AI_LOG - Data Cleaning

## 我問 AI 什麼

我請 AI 依照學號參數 `D=3`，分析資料清理題的函式簽名、輸入邊界、例外、edge case、測試與實作方式。

## AI 建議什麼

AI 建議把流程拆成 `dedupe_keep_order`、`filter_divisible`、`clean_numbers`、`solve`，先測試去重保序，再測試篩選與排序，並補 `NONE`、負數、0、多組測資與 `n=1`。

## 我如何修改

我確認 D 是 3，補了數量不符合 `n`、`d=0`、缺少資料列的例外檢查。也確認 EOF 與 `n=0` 結束行為正確，輸出不會多出空白。

## 對應檔案

- 程式：`q1.py`
- 測試：`test_q1.py`

