# Week 05 測試執行日誌

## 執行環境

- Python 版本：3.10
- 測試框架：unittest
- 測試目錄：`weeks/week-05/solutions/1111405040/tests/`
- 測試指令：

```powershell
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s tests -p "test_*.py" -v
```

---

## 第一次執行（失敗）

### 執行結果摘要

- 測試總數：5（測試模組）
- 通過數：0
- 失敗數：5（import error）

### 錯誤重點

- `ModuleNotFoundError: No module named 'question_10041'`
- `ModuleNotFoundError: No module named 'question_10050'`
- `ModuleNotFoundError: No module named 'question_10055'`
- `ModuleNotFoundError: No module named 'question_10056'`
- `ModuleNotFoundError: No module named 'question_10057'`

### 從失敗到下一步的修改

1. 建立五個解題模組：`question_10041.py` 到 `question_10057.py`
2. 為每一題補上 `solve()` 與可單獨測試的核心函式

---

## 第二次執行（部分通過）

### 執行結果摘要

- 測試總數：20
- 通過數：17
- 失敗數：3

### 失敗重點

- 三個失敗都出現在 `question_10050.py`
- 問題不是程式邏輯，而是測試預期值把週末日數位置算錯

### 原因分析

- 這題 day 1 代表星期日
- 因此 14 天內的第 12 天仍是工作日，不該被排除
- 我原本把 `count_lost_days(14, [3])` 寫成 `2`，正確應為 `3`

### 調整內容

1. 將 `test_single_party` 的預期值改為 `3`
2. 將 `test_multiple_parties` 的預期值改為 `5`
3. 同步修正整體輸出測試

---

## 第三次執行（全通過）

### 執行結果摘要

- 測試總數：20
- 通過數：20
- 失敗數：0

### 結果

- `10041` 的中位數距離計算正確
- `10050` 的週末排除與重複罷工日處理正確
- `10055` 的 EOF 差值輸出正確
- `10056` 的機率計算與格式化正確
- `10057` 的中位區間分析正確

---

## Refactor 紀錄

在測試通過後，維持以下整理方式：

1. 每題都提供 `solve()`，方便手動執行與測試共用
2. 每題都拆出核心函式，讓單元測試能直接驗證邏輯
3. 解析輸入時以 token 方式處理，避免受換行格式限制
