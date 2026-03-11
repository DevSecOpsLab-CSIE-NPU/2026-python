# AI_USAGE.md - AI 使用記錄與反思

## 概述
本檔案記錄整個作業過程中如何使用AI協助，以及批判性的採納或拒絕建議。

---

## 你問了哪些問題

### 問題 1：「如何在Python中實現去重但保留順序？」
- **目的**：Task 1的去重功能不能用set（會破壞順序）
- **AI回答**：建議使用set追蹤已見元素，配合循環維持順序
- **採納情況**：✓ 完全採納

### 問題 2：「sorted()如何實現複合排序鍵？」
- **目的**：Task 2需要三層排序（score、age、name）
- **AI回答**：建議使用lambda表達式的tuple: `key=lambda s: (-score, age, name)`
- **採納情況**：✓ 完全採納

### 問題 3：「collections.Counter和defaultdict何時使用？」
- **目的**：Task 3需要統計，兩種工具都可行
- **AI回答**：Counter適合計數任務，defaultdict則較通用但需手動更新
- **採納情況**：✓ 選用Counter（更簡潔）

### 問題 4：「如何設計測試案例確保覆蓋邊界情況？」
- **目的**：作業要求「正常、邊界、反例」各3個以上測試
- **AI回答**：
  - 邊界：空輸入、單一元素、全相同
  - 反例：容易寫錯的組合（如負數排序、同分同齡排序）
  - 最強測試：多層條件同時生效的案例
- **採納情況**：✓ 採納框架，但自己設計具體案例

### 問題 5：「Red → Green → Refactor的具體實踐步驟？」
- **目的**：理解TDD流程
- **AI回答**：
  1. 先寫測試（預期會失敗）
  2. 寫最小可行實現讓測試通過
  3. 重構（改進命名、提取函式、提升可讀性）
- **採納情況**：✓ 採納（本作業就遵循此流程）

---

## AI給了哪些建議你有採用

### 採用建議 1：使用set追蹤去重

**原始建議**：
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

**採納原因**：
- 清晰易懂，時間複雜度O(n)
- 明確體現「去重但保留順序」的邏輯
- 易於測試和驗證

**實際使用**：✓ task1_sequence_clean.py 直接採用

---

### 採用建議 2：lambda tuple作為複合排序鍵

**原始建議**：
```python
sorted(students, key=lambda s: (-s.score, s.age, s.name))
```

**採納原因**：
- tuple的排序遵循字典序，自動實現多層排序
- 負號用於降序很自然（-score相當於desc）
- 代碼簡潔且性能優良

**實際使用**：✓ task2_student_ranking.py 直接採用

---

### 採用建議 3：Counter.most_common()找最頻繁元素

**原始建議**：
```python
from collections import Counter
action_counts = Counter()
for log in logs:
    action_counts[log.split()[1]] += 1
top_action, count = action_counts.most_common(1)[0]
```

**採納原因**：
- Counter直接支援計數，無需初始化defaultdict
- most_common(1)一行搞定最常見元素
- 代碼比手寫迴圈查找更短

**實際使用**：✓ task3_log_summary.py 直接採用

---

### 採用建議 4：建立Student類別提升語義

**原始建議**：
```python
class Student:
    def __init__(self, name: str, score: int, age: int):
        self.name = name
        self.score = score
        self.age = age
```

**採納原因**：
- 比tuple更易讀（student.name優於student[0]）
- lambda key更清晰（lambda s: -s.score優於lambda x: -x[1]）
- 易於擴展（若未來需添加屬性）

**實際使用**：✓ task2_student_ranking.py 直接採用

---

### 採用建議 5：使用unittest而非pytest

**原始建議**：使用Python內建unittest
- 無需額外安裝
- class+method結構清晰
- 測試發現和執行方便

**採納原因**：
- 作業明確說「建議使用Python內建unittest」
- 無依賴安裝的麻煩
- 符合課程要求

**實際使用**：✓ 所有tests/test_*.py採用unittest

---

## AI有哪些建議你拒絕及原因

### 拒絕建議 1：使用列表推導式實現去重

**AI建議**：
```python
# 不行，破壞順序
def deduplicate(numbers):
    return list(dict.fromkeys(numbers))  # Python 3.7+的做法
```

**拒絕原因**：
- 雖然dict.fromkeys()可保留順序（Python 3.7+），但降低可讀性
- 題目明確說「不可用set直接輸出」，應該用容易理解的方式
- （雖然技術上可行）但為了教學目的，明確的set迴圈更好

**實際做法**：✓ 堅持用set+迴圈

---

### 拒絕建議 2：用operator.itemgetter排序

**AI建議**：
```python
from operator import itemgetter
sorted(students, key=itemgetter('score', 'age', 'name'))
```

**拒絕原因**：
- 需額外import，增加代碼複雜度
- 無法實現score的降序（itemgetter無法加負號）
- lambda更直觀，對初學者友善

**實際做法**：✓ 堅持使用lambda

---

### 拒絕建議 3：使用heapq.nlargest()提取排名結果

**AI建議**：
```python
import heapq
top_k = heapq.nlargest(k, students, key=lambda s: s.score)
```

**拒絕原因**：
- heapq只適合單一排序鍵，無法實現複合規則
- 題目需要三層排序（score、age、name）
- sorted()後[:k]更簡單明瞭

**實際做法**：✓ 堅持sorted()後切片

---

### 拒絕建議 4：預先組合排序鍵為單一tuple

**AI建議**：
```python
# 先轉換為(score, age, name)的tuple再排序
students_tuples = [(s.name, (-s.score, s.age, s.name)) for s in students]
```

**拒絕原因**：
- 複雜且重複name
- 破壞對象中心的設計
- lambda s: (-s.score, s.age, s.name)更簡潔

**實際做法**：✓ 直接在key中組合

---

### 拒絕建議 5：對測試案例進行數據驅動參數化

**AI建議**：
```python
@parameterized.expand([
    ([5, 3, 5], [5, 3]),
    ([1, 1, 1], [1]),
])
def test_deduplicate(self, input, expected):
    ...
```

**拒絕原因**：
- 需額外安裝parameterized套件
- 題目明確要求「測試骨架必須由學生自行撰寫」
- 使用簡單的test_*方法更透明易讀

**實際做法**：✓ 用傳統的test_method方式

---

## AI可能誤導你的案例

### 案例 1：sorted()的穩定性誤解

**AI初始建議**：「Python的sorted()是穩定的，可以依次多次排序實現複合排序」

**你自行驗證發現的誤導**：
- 理論上正確，但實踐上很容易出錯
- 如果多次sorted()順序反了就完全錯誤
- 例如以下代碼是**錯誤的**：

```python
# 錯誤做法（按age先排，再按score排，但順序反了）
result = sorted(students, key=lambda s: s.age)
result = sorted(result, key=lambda s: -s.score)  # 最後按score排，卻無法保留age的效果
```

**你的修正方式**：
- 放棄多次排序，改用tuple單次排序
- tuple排序遵循字典序，不會有順序錯誤的風險

```python
# 正確做法
sorted(students, key=lambda s: (-s.score, s.age, s.name))
```

**學到的教訓**：雖然多次排序在某些情境可行，但tuple一次排序更直觀且不易出錯。

---

### 案例 2：Counter的計數順序假設

**AI初始建議**：「Counter會自動按計數降序排列」

**你自行驗證發現的誤導**：
- Counter**不會**自動排序！
- `.most_common(n)`才會按計數降序
- 直接迭代Counter會按插入順序（Python 3.7+）

```python
# 錯誤假設
counter = Counter(["a", "b", "a"])
for item, count in counter.items():  # 不是按count排序！
    print(item, count)  # a 2, b 1（恰好對，但無法保證）
```

**你的修正方式**：
- 明確使用`.most_common(1)[0]`
- 對使用者計數用sorted()配合key

```python
# 正確做法
most_common_action, count = action_counts.most_common(1)[0]
sorted_users = sorted(user_counts.items(), key=lambda x: (-x[1], x[0]))
```

**學到的教訓**：不要假設库的行為，總是查文檔或實驗驗證。

---

### 案例 3：set()與去重順序的誤解

**AI初始建議**：「Python 3.7+的set保留插入順序」

**你自行驗證發現的誤導**：
- set**不保留**插入順序！那是dict的特性
- 即使Python 3.7+，set也是無序的

```python
# 錯誤嘗試
s = set([5, 3, 5, 2])
list(s)  # [2, 3, 5]（順序不同！）而非[5, 3, 2, 5]去重後[5, 3, 2]
```

**你的修正方式**：
- set只用來追蹤「已見」，不用來存儲結果
- 結果存在list中，set只是輔助

```python
# 正確做法（你已實現）
seen = set()
result = []
for num in numbers:
    if num not in seen:
        seen.add(num)
        result.append(num)
```

**學到的教訓**：set適合O(1)查找，dict適合有序去重。

---

## 總結

| 建議類別 | 數量 | 採納率 |
|---------|------|--------|
| 完全採納 | 5 | 100% |
| 部分採納 | 0 | 0% |
| 徹底拒絕 | 5 | - |
| 被發現誤導 | 3 | - |

**核心做法**：
1. ✓ AI提供框架和起點
2. ✓ 自己設計測試案例驗證
3. ✓ 實踐中發現和修正誤導
4. ✓ 優先選擇可讀性和安全性而非奇巧淫技

