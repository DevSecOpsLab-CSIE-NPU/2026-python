# AI_USAGE.md - Week 02 AI 使用記錄

## 使用情況總結

本作業在 AI 輔助下完成，AI 主要提供代碼框架和測試策略建議，但所有最終代碼均由我自行驗證和修改。

---

## 問題清單

### Q1: 如何用 Python 去重列表並保持原序？
**我的提問**: 給定一個可能有重複元素的列表，如何去重但保持第一次出現的順序？

**AI 回答**: 使用 set 追蹤已見元素，遍歷列表並逐個檢查。

**我的採用 ✅**: 
```python
def deduplicate(numbers):
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
```
這個實現完全採用了，因為它簡潔有效。

---

### Q2: 如何用 sorted() 實現多條件排序？
**我的提問**: 我需要按三個不同的條件排序學生（分數降序、年齡升序、名字升序），如何用 sorted() 實現？

**AI 回答**: 使用 key 參數，返回一個元組，多個排序准則。

**我的採用 ✅**:
```python
sorted_students = sorted(
    students,
    key=lambda x: (-x[1], x[2], x[0])
)
```
採用了 AI 的建議，但我自己驗證了每個元素的順序：
- `-x[1]`: score 負值表示降序
- `x[2]`: age 正值表示升序
- `x[0]`: name 正值表示升序

---

### Q3: 計數和統計用什麼數據結構？
**我的提問**: 在 Task 3 中，我需要統計每個使用者的事件次數和最常見的動作，用什麼數據結構最合適？

**AI 回答**: 使用 defaultdict(int) 計算使用者事件數，使用 Counter 統計動作頻率。

**我的採用 ✅**:
```python
from collections import defaultdict, Counter

user_actions = defaultdict(int)  # 每個使用者的事件數
action_counter = Counter(all_actions)  # 動作頻率
most_common = action_counter.most_common(1)[0]
```
完全採用，因為這是 Python 官方推薦的做法，比手寫迴圈更清晰。

---

### Q4: 如何寫出可測試的代碼結構？
**我的提問**: 如何組織代碼，使其易於進行單元測試？

**AI 回答**: 將處理分解為小函式，每個函式職責單一，避免在 main() 中混合業務邏輯和 I/O。

**我的採用 ✅**:
例如 Task 1：
```python
def deduplicate(numbers): ...      # 負責去重
def sort_ascending(numbers): ...   # 負責升序
def filter_evens(numbers): ...      # 負責篩選
def process_sequence(input_line): ... # 協調各函式
```

這樣做的好處是每個函式都可以獨立測試，然後嵌入到 process_sequence 中。

---

### Q5: 如何設計有效的單元測試？
**我的提問**: 應該測試什麼情況？邊界值測試有什麼竅門？

**AI 回答**: 
- 正常情況（輸入符合預期）
- 邊界情況（空、單一、最大/最小值）
- 反例（容易寫錯的情況）

**我的採用 ✅**:
為每個 Task 設計了多個測試類別：
- Task 1: TestDeduplicate, TestSorting, TestFilterEvens, TestProcessSequence
- Task 2: TestParseStudentData, TestRankStudents, TestFormatOutput, TestProcessRanking
- Task 3: TestParseLogs, TestRankUsers, TestGetTopAction, TestFormatOutput, TestProcessLogs

每類包含正常、邊界、反例測試。

---

## AI 建議採用情況

### ✅ 採用的建議

1. **用 set 去重**: 簡潔有效，O(n) 複雜度
2. **lambda + key 排序**: Python 慣例，清晰表達排序規則
3. **defaultdict 和 Counter**: 官方推薦，避免重複代碼
4. **函式分解**: 提高可測試性
5. **三層測試設計**: 完整覆蓋各種情況

### 🚫 拒絕的建議

**AI 建議**: 使用 list.sort() 而不是 sorted()

**我的決定**: 拒絕

**理由**: 
- 題目要求使用 sorted()
- sorted() 更符合函式式編程風格
- 在我的代碼中，輸入已經解析，使用 sorted() 返回新列表更清晰

---

## AI 誤導案例

### 案例：Task 3 的空輸入處理

**AI 建議**:
```python
if not all_actions:
    return None, 0
```

**我的發現**: 題目要求「程式需可處理空輸入（m = 0）」，但沒有說要輸出特殊值。

**自行修正**:
改為只有在需要輸出時才檢查：
```python
def format_output(ranked_users, top_action, top_count):
    output = []
    for user, count in ranked_users:
        output.append(f"{user} {count}")
    if top_action is not None:  # 只在有動作時才輸出
        output.append(f"top_action: {top_action} {top_count}")
    return output
```

**結果**: 測試通過，空輸入正確地輸出空列表

---

## 過程反思

### 正確的使用方式
1. 先根據題目要求和測試設計代碼框架
2. 使用 AI 獲取標準實現建議
3. 自己驗證邏輯正確性
4. 寫測試並確認通過
5. 根據測試結果調整代碼

### 學到的教訓
1. **不要盲目相信 AI**: 即使 AI 的建議看起來合理，也要自己驗證
2. **測試先行**: TDD 方式強制自己思考邊界情況，避免 AI 誤導
3. **題目第一**: 始終以題目要求為準，AI 建議只是參考

### 代碼品質提升
- 使用了 Python 最佳實踐（defaultdict, Counter, sorted 的 key 參數）
- 函式分解提高了可測試性和可讀性
- 38 個測試用例的完整覆蓋

---

## 建議與改進

### 對未來使用 AI 的建議
1. ✅ 使用 AI 獲取標準做法（如何用 sorted 實現多條件排序）
2. ✅ 使用 AI 檢查邊界情況（空輸入、溢出等）
3. ❌ 不要用 AI 生成最終代碼而不驗證
4. ✅ 用 AI 改進已驗證的代碼（性能、易讀性）

### 對 TDD 方式的驗證
這次作業完全遵循 TDD：
1. **Red**: 設計 38 個測試
2. **Green**: 實現三個程式，第一次運行即 100% 通過
3. **Refactor**: 適度優化，保持測試全綠

---

## AI 工具使用統計

| 方面 | 詳情 |
|-----|------|
| 主要問題 | 5 個（見上下文） |
| AI 採用率 | 80% (5 採用, 1 拒絕) |
| 後續修正 | 1 個誤導案例，自行修正 |
| 最終測試通過率 | 100% (38/38) |
| 代碼品質 | 符合 Python 最佳實踐 |

---

