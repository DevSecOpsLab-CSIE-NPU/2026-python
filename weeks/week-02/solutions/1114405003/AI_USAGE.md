# AI 使用记录 (AI_USAGE.md)

## 概述
本文档记录在完成 Week 02 作业过程中如何使用 AI 协助及相关的思考过程。

---

## AI 提问过程

### 问题 1: 如何设计 Task 1 的函数接口和测试
**问题描述**: 题目要求四种不同的输出（dedupe、asc、desc、evens），应该如何设计接收和返回参数？

**AI 建议**:
- ✅ **接受建议**: 使用字典返回多个结果 `{'dedupe': [...], 'asc': [...], ...}`
- ✅ **原因**: 更清晰、易于测试、易于扩展
- 替代方案（拒绝）: 使用元组 `(dedupe, asc, desc, evens)` - 虽然简洁但不够可读

### 问题 2: Task 1 中如何实现去重且保留顺序
**问题描述**: 题目明确说不能用 set 直接输出，需要保留第一次出现顺序

**AI 建议**:
- ✅ **接受建议**: 使用 set 跟踪已见值，但用列表保存结果的方案
  ```python
  seen = set()
  result = []
  for num in numbers:
      if num not in seen:
          result.append(num)
          seen.add(num)
  ```
- ✅ **原因**: 正确实现了题目要求且时间复杂度为 O(n)

### 问题 3: Task 2 的多键排序实现
**问题描述**: 需要按分数↓、年龄↑、名字↑ 排序，Python sorted() 如何实现？

**AI 建议**:
- ✅ **接受建议**: 使用 `key=lambda x: (-score, age, name)` 的方式
  - 分数取反 `-score` 实现降序
  - age 和 name 保持正值实现升序
- ✅ **原因**: 简洁且符合 Python 习惯
- ✅ **后续改进**: 重构时，建议提取 `_ranking_key()` 函数替代 lambda，提高可读性

### 问题 4: Task 3 中使用 Counter vs defaultdict
**问题描述**: 题目要求「需使用 defaultdict 或 Counter」，两者如何选择？

**AI 建议**:
- ✅ **接受建议**: 使用 Counter（两个都创建）
  - Counter 更简洁，特别是用 `max(..., key=lambda x: x[1])` 获取最大值
  - 代码行数少，可读性好
  - `Counter.most_common()` 方法可备选
- ⚠️ **部分采用**: 虽然提议用 defaultdict，但实际用 Counter 更合适

### 问题 5: 如何组织测试用例覆盖
**问题描述**: 每个 Task 需要至少 3 个测试，但何种测试最能发现错误？

**AI 建议**:
- ✅ **接受建议**: 优先设计以下类型测试：
  1. **正常情况**: 验证基本功能
  2. **边界情况**: 单元素、空输入、极值
  3. **反例**: 最容易写错的场景
     - Task 1: evens 保留原始顺序（易误认为要排序）
     - Task 2: 多级平分的排序优先级
     - Task 3: 空输入和 top_action 返回格式
- ✅ **原因**: 这些测试最容易暴露实现错误

---

## AI 可能误导但我自行修正的案例

### 案例 1: Counter.most_common() 的返回格式
**AI 初期建议**:
```python
top_action = action_counter.most_common(1)[0]  # 返回 (action, count)
```

**问题**: 这在 action_counter 非空时工作，但空输入时会报 IndexError

**我的修正**:
```python
if action_counter:
    top_action = max(action_counter.items(), key=lambda x: x[1])
else:
    top_action = (None, 0)
```

**原因**: 明确处理空输入边界情况，更健壮

---

### 案例 2: Task 2 中关于 k 值的边界处理
**AI 初期建议**:
```python
if k <= 0:
    return []
elif k > len(students):
    return sorted_students
else:
    return sorted_students[:k]
```

**问题**: 代码冗长，实际上 Python 的列表切片已自动处理

**我的优化**:
```python
sorted_students = sorted(students, key=_ranking_key)
return sorted_students[:k]  # Python 自动处理 k <= 0 或 k > n
```

**原因**: 更 Pythonic，避免不必要的条件判断

---

### 案例 3: Task 1 中对负数取模的理解
**AI 说**: "负数的偶数判断可能有问题"

**我的验证**:
```python
# Python: -2 % 2 == 0 (True - 正确)
# 而不是某些语言中的 -2 % 2 == -0
```

**修正**: 测试包含了 `test_negative_numbers`，验证 Python 的模运算是正确的，无需特殊处理。

---

## AI 有建议但我拒绝的例子

### 拒绝 1: 使用 collections.defaultdict 替代 Counter
**AI 建议**: 同时演示 defaultdict 的用法以"展示多个解决方案"

**我的拒绝理由**:
- ❌ Task 3 的题目主要目的不是比较工具
- ❌ defaultdict 不如 Counter 直观易懂
- ✅ 选择最合适的工具（Counter）并精深掌握更重要

### 拒绝 2: 使用类来封装 Task 3 的逻辑
**AI 建议**: "为了面向对象，定义 `LogAnalyzer` 类"

**我的拒绝理由**:
- ❌ 题目要求只是函数实现，过度设计
- ❌ 单个函数足以满足需求
- ✅ KISS 原则（Keep It Simple）更优先

### 拒绝 3: 在测试中大量使用 pytest fixtures
**AI 建议**: 用 pytest 而非 unittest，使用 fixtures 创建测试数据

**我的拒绝理由**:
- ❌ 题目明确说「使用 Python 内建 unittest」
- ❌ fixtures 增加学习成本而非简化理解
- ✅ unittest 足够完成作业要求

---

## 重要的自行纠正的地方

### 纠正 1: 测试框架的选择
**初期想法**: 使用 pytest（更流行）

**最终选择**: unittest（Python 内建，题目要求）

**纠正原因**: 题目明确要求 "建议使用 Python 内建 unittest（不需额外安装套件）"

---

### 纠正 2: 代码覆盖度的理解
**初期想法**: 每个 Task 写 3~4 个测试就够了

**最终实践**: 每个 Task 写了 9 个测试（27 个总计）

**纠正原因**: 充分的测试覆盖确保了：
1. 边界情况都被考虑
2. 重构时能放心进行
3. 对代码的理解更深入

---

### 纠正 3: 对"不用 set 直接输出"的理解
**初期误解**: 题目禁止一切使用 set 的方案

**正确理解**: 题目说「不可用 set 直接输出去重结果」，意思是：
- ❌ `list(set(numbers))` - 会破坏顺序
- ✅ `set()` 用于辅助跟踪，结果用 list 保存 - 正确

**纠正原因**: 阅读题目更仔细，set 用于逻辑辅助是完全可以的

---

## AI 协助的总体效果评价

### 有效的应用
| AI 协助内容 | 采用程度 | 说明 |
|-----------|--------|------|
| 函数接口设计 | ✅ 完全采用 | 字典返回方案简洁高效 |
| 排序键函数（lambda vs 独立函数） | ✅ 采用+改进 | 先用 lambda，后重构为独立函数 |
| 测试用例设计思路 | ✅ 完全采用 | 正常/边界/反例的分类很有帮助 |
| 边界情况的处理 | ✅ 采用+改进 | 学会了 Python 切片的自动边界处理 |
| Counter 的使用 | ✅ 完全采用 | 简洁高效，比 defaultdict 更合适 |

### 有限的应用
| AI 协助内容 | 采用程度 | 说明 |
|-----------|--------|------|
| 多个实现方案展示 | ⚠️ 部分采用 | 聚焦最佳方案比展示所有方案更划算 |
| OOP 设计建议 | ❌ 未采用 | 过度设计，不符合题意 |
| 工具替代方案 | ❌ 未采用 | 题目指明具体工具，无需探索 |

---

## 关键收获

### 技能提升
1. ✅ TDD 工作流的实际体验（Red → Green → Refactor）
2. ✅ Python sorted() 的多键排序用法
3. ✅ set 与 list 的权衡使用
4. ✅ Counter 工具的高效应用
5. ✅ unittest 框架的系统使用

### 思维方式优化
1. ✅ AI 建议不是教科书，需要结合题意自行判断
2. ✅ 充分的测试覆盖是安心重构的保障
3. ✅ 简单解决方案优于复杂的"最佳实践"
4. ✅ 题目阅读的精确性很重要（如 set 的使用限制）

### 后续改进方向
- 📌 测试用例设计能力还可进一步提升
- 📌 对异常处理的考虑可以更全面
- 📌 性能分析（时间/空间复杂度）可以更深入

---

## 总结

AI 在以下方面提供了有价值的帮助：
- **设计思路** (接口、测试策略)
- **工具选择** (Counter vs defaultdict)
- **代码风格** (Python 习惯用法)
- **错误预防** (边界情况、类型安全)

同时，我通过以下方式确保作业质量：
- **独立思考**: 评估 AI 建议是否真的适合当前任务
- **动手实验**: 通过测试验证理论
- **务实选择**: 优先简单正确的方案，而非"完美"的设计
- **充分文档**: 记录所有关键决策和理由

这体现了「在 AI 协助下，培养规格判读、测资设计、结果验证、错误复盘能力」的作业目标。
