# 测试执行日志 (TEST_LOG.md)

## 概述
本文档记录 Week 02 作业的测试执行过程，遵循 TDD (Test-Driven Development) 的 Red → Green → Refactor 流程。

---

## 第一次测试执行 - RED 阶段 ❌
**时间**: 2026-03-19（作业初期）  
**状态**: 测试失败（预期行为）

### 执行指令
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### 结果摘要
- **测试总数**: 27
- **通过数**: 0
- **失败数**: 27
- **成功率**: 0%

### 主要错误信息
所有测试都以 `TypeError: 'NoneType' object is not subscriptable` 失败，这是因为函数体仅返回 `None`。

### 失败例子
```
ERROR: test_normal_case (test_task1.TestTask1SequenceClean.test_normal_case)
...
TypeError: 'NoneType' object is not subscriptable
```

### 修改内容
1. **Task 1** (`task1_sequence_clean.py`)
   - 实现 `process_sequence()` 函数
   - 实现去重逻辑（保留首次出现顺序）
   - 实现升序/降序排序
   - 实现偶数过滤

2. **Task 2** (`task2_student_ranking.py`)
   - 实现 `rank_students()` 函数
   - 使用 `sorted(..., key=lambda x: (-x[1], x[2], x[0]))` 实现多键排序

3. **Task 3** (`task3_log_summary.py`)
   - 实现 `summarize_logs()` 函数
   - 使用 `Counter` 计数用户和操作

---

## 第二次测试执行 - GREEN 阶段 ✅
**时间**: 2026-03-19（实现所有功能后）  
**状态**: 所有测试通过

### 执行指令
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### 结果摘要
```
Ran 27 tests in 0.013s
OK
```

- **测试总数**: 27
- **通过数**: 27
- **失败数**: 0
- **成功率**: 100%

### 通过测试列表

#### Task 1: Sequence Clean (9个测试)
✅ test_all_even_numbers - 全偶数序列  
✅ test_all_same_numbers - 相同数字  
✅ test_dedupe_maintains_first_occurrence - 去重保留首次顺序  
✅ test_evens_maintain_original_order - 偶数保留原始顺序  
✅ test_negative_numbers - 负数处理  
✅ test_no_even_numbers - 全奇数序列  
✅ test_normal_case - 正常情况  
✅ test_single_element - 单个元素  
✅ test_zero_in_sequence - 包含零  

#### Task 2: Student Ranking (9个测试)
✅ test_all_same_score_sort_by_age - 同分按年龄排序  
✅ test_k_greater_than_total_students - k > 学生数  
✅ test_k_zero - k = 0  
✅ test_multiple_tiebreaks - 多级平分  
✅ test_normal_case - 正常情况  
✅ test_same_score_and_age_sort_by_name - 完全平分按名字  
✅ test_score_descending_primary_sort - 分数主排序  
✅ test_single_student - 单个学生  
✅ test_top_1 - 获取前1名  

#### Task 3: Log Summary (9个测试)
✅ test_case_sensitivity - 大小写敏感性  
✅ test_different_actions_same_user - 同用户不同操作  
✅ test_empty_logs - 空日志  
✅ test_many_actions_one_most_common - 明确的最常见操作  
✅ test_normal_case - 正常情况  
✅ test_same_user_count_sorted_by_name - 相同计数按名字排序  
✅ test_single_log - 单条日志  
✅ test_single_user - 单个用户  
✅ test_top_action_with_tie - 操作计数平分  

---

## 第三次测试执行 - REFACTOR 阶段 ✅
**时间**: 2026-03-19（代码重构后）  
**状态**: 所有测试仍然通过

### 执行指令
```bash
python -m unittest discover -s tests -p "test_*.py"
```

### 结果摘要
```
Ran 27 tests in 0.005s
OK
```

- **测试总数**: 27
- **通过数**: 27
- **失败数**: 0
- **成功率**: 100%

### 重构改进内容

1. **Task 1 重构**
   - 提取 `deduplicate()` 为独立函数
   - 提取 `get_evens()` 为独立函数
   - 增加详细的文档字符串和注释
   - 提高代码可读性和可维护性

2. **Task 2 重构**
   - 提取 `_ranking_key()` 为独立函数
   - 使用具名辅助函数替代 lambda（提高可读性）
   - 增加详细的排序优先级说明
   - 改进函数和参数文档

3. **Task 3 重构**
   - 提取 `_user_count_key()` 为排序键函数
   - 提取 `_get_top_action()` 为独立函数
   - 添加详细的文档（包括示例）
   - 利用 Counter 的特性简化代码
   - 移除未使用的 `defaultdict` 导入

### 重构后代码质量提升
- ✅ 代码更易读（函数分解）
- ✅ 函数职责单一（SRP 原则）
- ✅ 文档更完整（所有公共函数有 docstring）
- ✅ 排序逻辑更清晰（独立的 key 函数）
- ✅ 所有测试仍然通过（无回归）

---

## TDD 工作流总结

### Red → Green → Refactor 流程
1. **Red 阶段**: 编写 27 个测试用例，全部失败
2. **Green 阶段**: 实现最小可行代码，使所有测试通过
3. **Refactor 阶段**: 改进代码质量，测试仍然全部通过

### 关键收获
- ✅ 测试首先指导了代码设计和接口定义
- ✅ 充分的测试覆盖确保了重构的安全性
- ✅ 从最小可行实现逐步优化是 TDD 的核心实践
- ✅ 通过测试数量和覆盖面积（27 个测试）验证了实现的正确性

---

## 测试执行环境
- **Python 版本**: 3.x
- **测试框架**: unittest (Python 内建)
- **测试定位方式**: `-s tests -p "test_*.py"`
- **详细输出**: `-v` (verbose mode)
