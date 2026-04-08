# Week 02 AI 使用記錄 (AI_USAGE.md)

---

## 1. 詢問 AI 的問題

### Task 1 相關
- **Q**: 如何在 Python 中保持列表去重時的原始順序？
- **A**: 使用 `set` 追蹤已見過的元素，遍歷時檢查是否在 set 中，不在就加入結果列表。

### Task 2 相關
- **Q**: Python sorted 如何實現多條件排序（先分數降序，再年齡升序）？
- **A**: 使用 `sorted(..., key=lambda x: (-x[1], x[2], x[0]))` 實現多重排序。

### Task 3 相關
- **Q**: 如何統計字串出現次數並找最常見的？
- **A**: 使用 `collections.Counter` 的 `most_common()` 方法。

---

## 2. AI 建議與採用

### 採用 1：Task 2 排序
- **AI 建議**: 使用 `key=lambda x: (-x[1], x[2], x[0])`
- **採用原因**: 這是最簡潔且 Pythonic 的方式，一行實現三重排序

### 採用 2：Task 3 Counter
- **AI 建議**: 使用 `Counter.most_common(1)` 找最常見 action
- **採用原因**: 內建方法比手動遍歷 dict 找最大值更簡潔

---

## 3. AI 建議拒絕

### 拒絕：Task 1 使用 dict.fromkeys()
- **AI 建議**: 用 `list(dict.fromkeys(nums))` 去重
- **拒絕原因**: Python 3.7+ 雖然保證 dict 順序，但此方法不如手寫 loop 直觀，且題目限制「不可用 set 直接輸出去重結果」，用 dict 也可能違反精神

---
## 4. AI 誤導案例

### 案例：Task 3 空輸入處理
- **AI 建議**: 直接假設輸入一定會有 m 行
- **問題**: 當 m=0 時，迴圈會跳過但沒有正確返回空結果
- **自行修正**: 在函式開頭增加 `if m == 0: return {'users': [], 'top_action': ''}` 判斷

---

## 5. 總結

本週作業主要考驗的是對 Python 內建資料結構的理解（list/dict/set/Counter），以及排序和統計的概念。AI 提供的建議大部分正確，但仍需自行測試邊界情況（如空輸入、負數等）才能確保正確性。
