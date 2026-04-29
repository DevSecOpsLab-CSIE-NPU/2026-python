# AI_USAGE.md

## AI 使用記錄

---

## 1. 询问的问题

1. **Python 如何实现列表去重但保留第一次出现顺序？**
   - 原因：不希望用 set 直接去重破坏顺序

2. **sorted 函数的 key 参数如何实现多重条件排序？**
   - 原因：Task 2 需要按 score、age、name 三个条件排序

3. **defaultdict 和 Counter 的区别是什么？**
   - 原因：Task 3 需要选择合适的数据结构统计

4. **Python unittest 如何组织测试用例？**
   - 原因：第一次写单元测试，需要了解基本结构

5. **如何处理空输入的边界情况？**
   - 原因：确保程序在特殊输入下不会崩溃

---

## 2. 采纳的 AI 建议

1. **去重时使用 seen + seen_set 双列表/集合组合**
   - `seen` 列表保持顺序，`seen_set` 加速查询
   - 实际代码：
     ```python
     seen = []
     seen_set = set()
     for n in nums:
         if n not in seen_set:
             seen.append(n)
             seen_set.add(n)
     ```

2. **多重排序使用元组作为 key**
   - 实际代码：
     ```python
     sorted_students = sorted(
         students_data,
         key=lambda s: (-s[1], s[2], s[0])
     )
     ```

3. **使用 Counter.most_common() 获取最常见元素**
   - 简化了找出 top_action 的逻辑

---

## 3. 拒绝的 AI 建议

1. **直接使用 set(nums) 去重**
   - 拒绝原因：题目要求保留第一次出现顺序，set 会破坏顺序

2. **使用 heapq 做排序**
   - 拒绝原因：题目明确要求使用 sorted()，且 heapq 不适合这个场景

3. **使用 pandas 处理数据**
   - 拒绝原因：作业要求仅使用标准库，pandas 不是标准库

---

## 4. AI 可能误导的案例

### 案例：空字符串处理

**AI 建议**：
```python
nums = list(map(int, nums_str.split()))
```
AI 认为这样可以自动处理空字符串。

**实际情况**：
```python
"".split()  # 返回 ['']
int('')     # 抛出 ValueError
```

**自行修正**：
```python
def process_sequence(nums_str):
    if not nums_str or not nums_str.strip():
        return {'dedupe': [], 'asc': [], 'desc': [], 'evens': []}
    nums = list(map(int, nums_str.split()))
    # ... 其余逻辑
```

**教训**：AI 对边界情况的处理不够仔细，需要自己验证各种输入场景。

---

## 5. 总结

- AI 在语法和标准库使用方面提供了很好的帮助
- 对于边界情况和作业特殊要求，需要自己判断和验证
- 建议先用 AI 生成草稿，再根据实际测试结果进行调整
