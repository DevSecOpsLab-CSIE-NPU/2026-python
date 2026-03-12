# AI_USAGE.md - AI 協助反思

本文件記錄本作業中如何使用 AI 的過程、AI 的建議、採納與拒絕的理由，以及自我修正的實例。

---

## 我向 AI 提問的主要問題

### 1. **「如何在 Python 中實現去重同時保留原始順序？」**

**AI 回答**: 提供三種方案：
- ❌ `list(set(nums))` - 簡單但順序破壞
- ⚠️ `list(dict.fromkeys(nums))` - 利用 Python 3.7+ dict 維持插入順序
- ✅ `seen set + 迴圈` - 最明確、易測試

**採納決策**: 選擇第三種方案

**理由**: 雖然 `dict.fromkeys()` 更簡潔，但 `seen set + 迴圈` 對初學者更清楚，易於理解和測試。

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

---

### 2. **「Python 中如何實現複合條件排序？」**

**AI 回答**: 提供多種方案：
- ❌ 巢狀 for 迴圈交換排序 - 低效且易出錯
- ⚠️ 多次呼叫 `sorted()` - 正確性取決於排序穩定性
- ✅ `sorted(key=lambda x: (...)` with tuple - 最清晰

**採納決策**: 使用 tuple key 配合 lambda

```python
# 正確方式：單一 sorted，tuple key
sorted_students = sorted(
    students,
    key=lambda s: (-s.score, s.age, s.name)
)
```

**拒絕的建議**: 多次 sorted() 方案

```python
# ❌ AI 的替代建議（被拒絕）
students = sorted(students, key=lambda s: s.name)
students = sorted(students, key=lambda s: s.age)
students = sorted(students, key=lambda s: (-s.score))
```

**拒絕理由**: 雖然在穩定排序下也能工作，但：
- 多次排序性能差（O(n³) vs O(n log n)）
- 維護困難：修改優先級時容易出錯
- 易誤導初學者：以為需要多次排序

---

### 3. **「Python 中 defaultdict vs Counter 的使用時機？」**

**AI 回答**: 
- `defaultdict(int)` - 當需要累計計數時最好用
- `Counter` - 專為計數優化，有 `most_common()` 等便利方法

**採納決策**: 兩者都用！在 Task 3 中：
- `defaultdict(int)` 計算使用者事件數
- `Counter` 統計行為出現次數

```python
# Task 3 中
user_count = defaultdict(int)
for user, action in logs:
    user_count[user] += 1  # 累計計數

action_counter = Counter(actions)
top_action, count = action_counter.most_common(1)[0]  # 找最常見
```

**拒絕的建議**: 
- AI 曾建議全部用 `Counter` 不用 `defaultdict`
- **拒絕理由**: `Counter` 會在初次訪問時創建鍵，但需要事先遍歷一遍才能統計，不如 `defaultdict` 在累計時清晰

---

### 4. **「如何設計完整的單元測試框架？」**

**AI 回答**: 使用 `unittest` 框架
- 按功能分類建立 TestCase
- 每個測試方法測試一個「場景」
- 使用 `setUp()` 初始化共同資源

**採納決策**: 採用 unittest，按以下結構組織：

```python
class TestDeduplication(unittest.TestCase):
    def test_deduplicate_preserves_first_occurrence(self): ...
    def test_deduplicate_no_duplicates(self): ...
    def test_deduplicate_all_same(self): ...
```

**自行改進**: 
- 每個測試類對應一個邏輯單元（不是按 Task 分類）
- 使用清晰的測試名稱描述場景而非功能

```python
# ✅ 好的命名
def test_sort_tie_break_by_age(self):

# ❌ 不好的命名
def test_sort_2(self):
```

---

### 5. **「如何處理邊界情況和無效輸入？」**

**AI 回答**: 
- 主動檢查 `if not logs:` 等邊界
- 拋出 `ValueError` 時提供清晰的錯誤訊息
- 編寫測試驗證錯誤處理

**採納決策**: 完全採納，加入邊界檢查

```python
# Task 3 中的邊界檢查
def get_top_action(logs):
    if not logs:
        return None, 0
    
    # ... 正常邏輯
```

**自行擴充**:
```python
# 在 parse_logs 中也加入驗證
if len(parts) != 2:
    raise ValueError(f"Invalid format: {line}")
```

---

## AI 建議中被我採納的項目

### ✅ 項目 A: 使用 `lambda` 的複合排序

**AI 建議**:
```python
sorted(students, key=lambda s: (-s.score, s.age, s.name))
```

**採納原因**:
- 簡潔、清晰、Python 習慣寫法
- 性能最優（O(n log n)）
- 易於修改優先級

**驗證**: Task 2 的 15 個測試全部通過

---

### ✅ 項目 B: 為 Student 類別加入 `__repr__()` 和 `__eq__()`

**AI 建議**:
```python
def __repr__(self):
    return f"{self.name} {self.score} {self.age}"

def __eq__(self, other):
    return (self.name == other.name and 
            self.score == other.score and 
            self.age == other.age)
```

**採納原因**:
- 便於測試驗證
- 提升物件可用性
- 標準物件導向做法

**驗證**: 透過 `assertEqual()` 直接比較 Student 物件

---

### ✅ 項目 C: 分離主程式邏輯到 `main()` 函式

**AI 建議**:
```python
def main():
    """互動式主程式"""
    print("輸入整數序列:")
    input_str = input().strip()
    results = process_sequence(input_str)
    # ...

if __name__ == "__main__":
    main()
```

**採納原因**:
- 使程式可測試（不會自動執行）
- 符合 Python 最佳實踐
- 易於集成到其他程式

---

### ✅ 項目 D: 使用 docstring 記錄函式功能

**AI 建議**:
```python
def deduplicate(numbers):
    """
    去重，保留第一次出現的順序
    
    Args:
        numbers: list of integers
        
    Returns:
        list: 去重後的列表
    """
```

**採納原因**:
- 提高程式可讀性
- 自動生成文件
- IDE 能提供智能提示

---

## AI 建議中被我拒絕或修改的項目

### ❌ 項目 1: 全部使用 Counter（拒絕）

**AI 建議**:
```python
# 用 Counter 統計所有東西
all_counter = Counter(logs)
user_count = Counter(user for user, action in logs)
```

**拒絕原因**:
- `Counter` 是針對計數優化的容器，但需要遍歷一遍才能得到結果
- `defaultdict(int)` 在邊走邊累計時更自然
- 混用會使邏輯不清不楚

**修改後**:
```python
# ✅ 分工清楚
user_count = defaultdict(int)  # 累計
for user, action in logs:
    user_count[user] += 1

action_counter = Counter(actions)  # 統計
```

---

### ⚠️ 項目 2: 使用 dict.fromkeys() 去重（修改）

**AI 建議**:
```python
# 簡潔，但初學者不易理解
def deduplicate(numbers):
    return list(dict.fromkeys(numbers))
```

**修改原因**:
- 過於 Pythonic，對初學者不清晰
- 作業要求「不可用 set」，但也應讓邏輯清楚
- 測試時也不利於部分驗證

**修改後**:
```python
# 更清楚，且容易演化（例如加入條件篩選）
def deduplicate(numbers):
    seen =set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
```

---

### ⚠️ 項目 3: 字串分割時使用正則表達式（修改）

**AI 建議**:
```python
import re
parts = re.split(r'\s+', line.strip())
```

**修改原因**:
- 過度設計，簡單的 `.split()` 已足夠
- 加入不必要的依賴（re 模組）
- 非初學者友善

**修改後**:
```python
parts = line.strip().split()  # 簡單、清晰、內建
```

---

### ⚠️ 項目 4: 使用 TypeError 和 AttributeError（修改）

**AI 建議**:
```python
try:
    # implicit type conversion
    int_list = [int(x) for x in parts]
except (TypeError, ValueError):
    raise ValueError("Invalid input")
```

**修改原因**:
- 明確用 `ValueError` 即可
- 不需要區分不同錯誤型別
- 簡化異常處理

**修改後**:
```python
try:
    numbers = list(map(int, input_string.split()))
except ValueError:
    print("錯誤：無效的輸入")
```

---

## AI 可能誤導我的實例：「多次 sorted() 的穩定性」

### 事件發生

**AI 說**: 「Python 的 sorted() 是穩定排序，所以多次排序也能得到正確的多層排序結果。」

```python
# AI 的建議
students = sorted(students, key=lambda s: s.name)
students = sorted(students, key=lambda s: s.age, stable=True)
students = sorted(students, key=lambda s: (-s.score), stable=True)
```

### 我的疑慮

- 雖然穩定，但效率低（O(n³) 在最差情況）
- 維護性差：優先級改變時容易出錯
- 初學者易誤解「應該多次排序」

### 自我修正過程

1. **測試驗證**: 設計案例 2.5，確認多次排序確實能工作
2. **性能分析**: 比較單一 sort vs 多次 sort，發現性能差異
3. **風格檢查**: 查閱 Python 最佳實踐和 PEP 8
4. **最終決定**: 採用 tuple key 的單一排序

```python
# ✅ 最終版本
sorted_students = sorted(
    students,
    key=lambda s: (-s.score, s.age, s.name)
)
```

### 技能收穫

- **穩定性 ≠ 最佳做法**: 雖然多次排序能工作，但單一排序更好
- **AI 的回答可能在技術上正確，但未必最佳**
- **需要臨界思考**: 驗證和比較 AI 提出的選項

---

## 總結與反思

### AI 使用策略

| 使用方式 | 效果 | 例子 |
|---------|------|------|
| ✅ 概念理解 | 很好 | 去重、排序的多種方案對比 |
| ✅ 程式框架 | 很好 | unittest 結構、class 設計 |
| ✅ 邊界檢查 | 好 | 空輸入的處理提醒 |
| ⚠️ 性能優化 | 一般 | 多次排序也能跑，但非最優 |
| ❌ 判斷優先級 | 差 | 過度推薦 Pythonic 寫法 |

### 我的學習

1. **AI 是助手不是導師**: AI 提供方案，我負責評估和選擇
2. **測試是驗證**: 疑慮時用測試案例驗證 AI 的說法
3. **多角度思考**: 技術上正確 ≠ 實務上最好
4. **保持臨界思維**: 不盲目接受 AI 建議

### 對後續學習的建議

- 使用 AI 時問「為什麼」而非直接用答案
- 設計邊界測試案例驗證 AI 的建議
- 定期查閱官方文件確認最佳實踐
- 記錄自我修正的過程

