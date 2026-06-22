# 題4 AI_LOG（C區：二分搜尋效能）

## AI 反問我什麼 / 我怎麼回答

| AI 問 | 我答 |
|-------|------|
| 函式簽名？ | `binary_search(arr, target)` -> `(idx, cmp)`；`linear_search` 同 |
| 輸入邊界？ | 陣列 `>= 10^5`；`K = 100 + 07 = 107` |
| 例外處理？ | 空陣列 -> `NOT FOUND cmp=0` |
| Edge case？ | `K` 在頭/尾；`K` 小於最小值；`K` 大於最大值 |
| 驗收標準？ | `FOUND/NOT FOUND cmp=N`；`timeit` 兩行 + 結論 |

## 我問了 AI 什麼（本題）
1. 先寫 binary/linear search 測試，再實作通過。
2. 補上 `timeit` 比較與雷達圖輸出。

## AI 建議採用 / 修正
- 用 `time.perf_counter()` 量測多次平均。
- 雷達圖採固定維度（速度、是否需排序、易實作、比較次數）。
- 中文標籤顯示問題時改成英文標籤。

## Git PR SOP（本題）
- [x] 分支：`0622-1114405007`
- [x] 先紅後綠：
	- Red commit：`8616edb`（test: add failing tests for search_lab）
	- Green commit：`2fd6f05`（feat: implement search_lab）
- [x] PR base:compare：`DevSecOpsLab-CSIE-NPU/2026-python:main <- GuZhe-Yu/2026-python:0622-1114405007`
- [x] PR 描述三要件：
	- 題目摘要：已描述題4二分搜尋效能與 `K=107`
	- 測試結果：已提供測試通過紀錄（見 `TEST_LOG.md`）
	- 我跟 AI 改了什麼：已在本檔完整記錄