# AI_LOG - 第一題 資料清理

## 學生資訊
- 學號: 1114405003
- 姓名: 李玉落
- D = 5 (個位 3 % 4 + 2 = 5)

---

## 協作過程記錄

### 1. 開工前資訊檢查表

**AI 問我的問題：**
1. 函式簽名：你想用什麼函式名稱？回傳什麼型別？
2. 例外處理：輸入格式錯誤（非數字、空行）要怎麼處理？
3. Edge case：你想到哪些邊界案例？

**我的回答：**
1. 函式簽名：`def clean_data(nums: list[int], d: int) -> list[int]:`
2. 例外處理：假設輸入合法（CPE 標準）
3. Edge case：n=1、全部重複、全部被過濾掉、含0、含負數

### 2. AI 幫我做的事

| 步驟 | 內容 | 結果 |
|------|------|------|
| 建立測試 | `test_data_cleaning.py` (14 個測試案例) | ✅ 全紅 (ModuleNotFoundError) |
| 建立實作 | `data_cleaning.py` (主程式 + clean_data 函式) | ✅ 全綠 (14 tests OK) |
| 測試主程式 | 輸入範例測資 | ✅ 輸出 NONE / 5 正確 |
| 建立文件 | README.md + TEST_LOG.md | ✅ 完成 |

### 3. 我改了什麼

- 手動確認 D=5 的計算：第1組 NONE、第2組 5
- 確認 edge case 測試涵蓋完整
- 確認 Git 分支命名 `submit/week-18-1114405003`

### 4. 驗收標準

- [x] 函式簽名正確
- [x] 14 個測試全過
- [x] 範例測資輸出正確
- [x] README.md 包含使用說明
- [x] TEST_LOG.md 包含測試紀錄
- [x] Git commit 完成

---

## 提示詞逐字記錄

### 提示詞 1
```
read this D:\0622\2026-python\weeks\week-18\README.md
```
**AI 回應：** 讀取並摘要 README.md 內容

### 提示詞 2
```
第一題 資料清理 (Data Cleaning) A 區 ‧ 保底 30 分...
```
**AI 回應：** 讀取題目，建立資訊檢查表，詢問簽名/例外/edge case

### 提示詞 3
```
幫我選最好的
```
**AI 回應：** 幫忙選擇最佳選項，填滿檢查表

### 提示詞 4
```
做出來的 幫我放進D:\0622\2026-python\weeks\week-18\solutions\1114405003
```
**AI 回應：** 
- 建立 test_data_cleaning.py (紅燈)
- 建立 data_cleaning.py (綠燈)
- 建立 TEST_LOG.md
- 建立 README.md
- 建立 Git 分支並 commit

### 提示詞 5
```
AI_LOG.md 我需要
```
**AI 回應：** 建立本 AI_LOG.md 文件
