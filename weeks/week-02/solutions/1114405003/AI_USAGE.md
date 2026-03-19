# AI 使用記錄 (AI_USAGE.md)

## 概述
本文檔記錄在完成 Week 02 作業過程中如何使用 AI 協助及相關的思考過程。

---

## AI 提問過程

### 問題 1: 如何設計 Task 1 的函數接口和測試
**問題描述**: 題目要求四種不同的輸出（dedupe、asc、desc、evens），應該如何設計接收和返回參數？

**AI 建議**:
- ✅ **接受建議**: 使用字典返回多個結果 `{'dedupe': [...], 'asc': [...], ...}`
- ✅ **原因**: 更清晰、易於測試、易於擴展
- 替代方案（拒絕）: 使用元組 `(dedupe, asc, desc, evens)` - 雖然簡潔但不夠可讀

### 問題 2: Task 1 中如何實現去重且保留順序
**問題描述**: 題目明確說不能用 set 直接輸出，需要保留第一次出現順序

**AI 建議**:
- ✅ **接受建議**: 使用 set 跟蹤已見值，但用列表保存結果的方案
  ```python
  seen = set()
  result = []
  for num in numbers:
      if num not in seen:
          result.append(num)
          seen.add(num)
  ```
- ✅ **原因**: 正確實現了題目要求且時間複雜度為 O(n)

### 問題 3: Task 2 的多鍵排序實現
**問題描述**: 需要按分數↓、年齡↑、名字↑ 排序，Python sorted() 如何實現？

**AI 建議**:
- ✅ **接受建議**: 使用 `key=lambda x: (-score, age, name)` 的方式
  - 分數取反 `-score` 實現降序
  - age 和 name 保持正值實現升序
- ✅ **原因**: 簡潔且符合 Python 習慣
- ✅ **後續改進**: 重構時，建議提取 `_ranking_key()` 函數替代 lambda，提高可讀性

### 問題 4: Task 3 中使用 Counter vs defaultdict
**問題描述**: 題目要求「需使用 defaultdict 或 Counter」，兩者如何選擇？

**AI 建議**:
- ✅ **接受建議**: 使用 Counter（兩個都創建）
  - Counter 更簡潔，特別是用 `max(..., key=lambda x: x[1])` 獲取最大值
  - 代碼行數少，可讀性好
  - `Counter.most_common()` 方法可備選
- ⚠️ **部分採用**: 雖然提議用 defaultdict，但實際用 Counter 更合適

### 問題 5: 如何組織測試用例覆蓋
**問題描述**: 每個 Task 需要至少 3 個測試，但何種測試最能發現錯誤？

**AI 建議**:
- ✅ **接受建議**: 優先設計以下類型測試：
  1. **正常情況**: 驗證基本功能
  2. **邊界情況**: 單元素，空輸入、極值
  3. **反例**: 最容易寫錯的場景
     - Task 1: evens 保留原始順序（易誤認為要排序）
     - Task 2: 多級平分的排序優先級
     - Task 3: 空輸入和 top_action 返回格式
- ✅ **原因**: 這些測試最容易暴露實現錯誤

---

## AI 可能誤導但我自行修正的案例

### 案例 1: Counter.most_common() 的返回格式
**AI 初期建議**:
```python
top_action = action_counter.most_common(1)[0]  # 返回 (action, count)
```

**問題**: 這在 action_counter 非空時工作，但空輸入時會報 IndexError

**我的修正**:
```python
if action_counter:
    top_action = max(action_counter.items(), key=lambda x: x[1])
else:
    top_action = (None, 0)
```

**原因**: 明確處理空輸入邊界情況，更健壯

---

### 案例 2: Task 2 中關於 k 值的邊界處理
**AI 初期建議**:
```python
if k <= 0:
    return []
elif k > len(students):
    return sorted_students
else:
    return sorted_students[:k]
```

**問題**: 代碼冗長，實際上 Python 的列表切片已自動處理

**我的優化**:
```python
sorted_students = sorted(students, key=_ranking_key)
return sorted_students[:k]  # Python 自動處理 k <= 0 或 k > n
```

**原因**: 更 Pythonic，避免不必要的條件判斷

---

### 案例 3: Task 1 中對負數取模的理解
**AI 說**: "負數的偶數判斷可能有問題"

**我的驗證**:
```python
# Python: -2 % 2 == 0 (True - 正確)
# 而不是某些語言中的 -2 % 2 == -0
```

**修正**: 測試包含了 `test_negative_numbers`，驗證 Python 的模運算是正確的，無需特殊處理。

---

## AI 有建議但我拒絕的例子

### 拒絕 1: 使用 collections.defaultdict 替代 Counter
**AI 建議**: 同時演示 defaultdict 的用法以"展示多個解決方案"

**我的拒絕理由**:
- ❌ Task 3 的題目主要目的不是比較工具
- ❌ defaultdict 不如 Counter 直觀易懂
- ✅ 選擇最合適的工具（Counter）並精深掌握更重要

### 拒絕 2: 使用類來封裝 Task 3 的邏輯
**AI 建議**: "為了面向對象，定義 `LogAnalyzer` 類"

**我的拒絕理由**:
- ❌ 題目要求只是函數實現，過度設計
- ❌ 單個函數足以滿足需求
- ✅ KISS 原則（Keep It Simple）更優先

### 拒絕 3: 在測試中大量使用 pytest fixtures
**AI 建議**: 用 pytest 而非 unittest，使用 fixtures 創建測試數據

**我的拒絕理由**:
- ❌ 題目明確說「使用 Python 內建 unittest」
- ❌ fixtures 增加學習成本而非簡化理解
- ✅ unittest 足夠完成作業要求

---

## 重要的自行糾正的地方

### 糾正 1: 測試框架的選擇
**初期想法**: 使用 pytest（更流行）

**最終選擇**: unittest（Python 內建，題目要求）

**糾正原因**: 題目明確要求 "建議使用 Python 內建 unittest（不需額外安裝套件）"

---

### 糾正 2: 代碼覆蓋度的理解
**初期想法**: 每個 Task 寫 3~4 個測試就夠了

**最終實踐**: 每個 Task 寫了 9 個測試（27 個總計）

**糾正原因**: 充分的測試覆蓋確保了：
1. 邊界情況都被考慮
2. 重構時能放心進行
3. 對代碼的理解更深入

---

### 糾正 3: 對"不用 set 直接輸出"的理解
**初期誤解**: 題目禁止一切使用 set 的方案

**正確理解**: 題目說「不可用 set 直接輸出去重結果」，意思是：
- ❌ `list(set(numbers))` - 會破壞順序
- ✅ `set()` 用於輔助跟蹤，結果用 list 保存 - 正確

**糾正原因**: 閱讀題目更仔細，set 用於邏輯輔助是完全可以的

---

## AI 協助的總體效果評價

### 有效的應用
| AI 協助內容 | 採用程度 | 說明 |
|-----------|--------|------|
| 函數接口設計 | ✅ 完全採用 | 字典返回方案簡潔高效 |
| 排序鍵函數（lambda vs 獨立函數） | ✅ 採用+改進 | 先用 lambda，後重構為獨立函數 |
| 測試用例設計思路 | ✅ 完全採用 | 正常/邊界/反例的分類很有幫助 |
| 邊界情況的處理 | ✅ 採用+改進 | 學會了 Python 切片的自動邊界處理 |
| Counter 的使用 | ✅ 完全採用 | 簡潔高效，比 defaultdict 更合適 |

### 有限的應用
| AI 協助內容 | 採用程度 | 說明 |
|-----------|--------|------|
| 多個實現方案展示 | ⚠️ 部分採用 | 聚焦最佳方案比展示所有方案更划算 |
| OOP 設計建議 | ❌ 未採用 | 過度設計，不符合題意 |
| 工具替代方案 | ❌ 未採用 | 題目指明具體工具，無需探索 |

---

## 關鍵收穫

### 技能提升
1. ✅ TDD 工作流的實際體驗（Red → Green → Refactor）
2. ✅ Python sorted() 的多鍵排序用法
3. ✅ set 與 list 的權衡使用
4. ✅ Counter 工具的高效應用
5. ✅ unittest 框架的系統使用

### 思維方式優化
1. ✅ AI 建議不是教科書，需要結合題意自行判斷
2. ✅ 充分的測試覆蓋是安心重構的保障
3. ✅ 簡單解決方案優於複雜的"最佳實踐"
4. ✅ 題目閱讀的精確性很重要（如 set 的使用限制）

### 後續改進方向
- 📌 測試用例設計能力還可進一步提升
- 📌 對異常處理的考慮可以更全面
- 📌 效能分析（時間/空間複雜度）可以更深入

---

## 總結

AI 在以下方面提供了有價值的幫助：
- **設計思路** (接口、測試策略)
- **工具選擇** (Counter vs defaultdict)
- **代碼風格** (Python 習慣用法)
- **錯誤預防** (邊界情況、類型安全)

同時，我通過以下方式確保作業質量：
- **獨立思考**: 評估 AI 建議是否真的適合當前任務
- **動手實驗**: 通過測試驗證理論
- **務實選擇**: 優先簡單正確的方案，而非"完美"的設計
- **充分文檔**: 記錄所有關鍵決策和理由

這體現了「在 AI 協助下，培養規格判讀、測資設計、結果驗證、錯誤復盤能力」的作業目標。
