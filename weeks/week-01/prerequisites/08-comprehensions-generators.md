# 8 容器操作與推導式

你必須已經「不需要解釋」就能看懂：

```python
[x for x in data if x > 0]
{k: v for k, v in d.items()}
```

```python
(x * x for x in nums)
```

用途（對應第一章範例）：

- 過濾序列（1.16）
- 字典子集（1.17）
- `sum(...)` / `min(...)` / `join(...)`

## 註釋版範例（可直接貼到程式）

```python
# 1) List comprehension: 過濾出正數
data = [3, -1, 0, 7, -5]
positives = [x for x in data if x > 0]  # 先迭代 x，再套用條件 x > 0
print(positives)  # [3, 7]

# 2) Dict comprehension: 建立字典子集
d = {"apple": 5, "banana": 12, "cherry": 8}
expensive = {k: v for k, v in d.items() if v >= 10}  # 只保留 value >= 10
print(expensive)  # {'banana': 12}

# 3) Generator expression: 延遲計算（省記憶體）
nums = [1, 2, 3, 4]
gen = (x * x for x in nums)  # 這裡不會立刻算完所有平方值

# 常見搭配：直接餵給 sum/min/max 等函式
total = sum(x * x for x in nums)  # 等價於 sum([1,4,9,16])，但不需先建整個 list
print(total)  # 30

# 注意：generator 迭代一次就會耗盡
print(list(gen))  # [1, 4, 9, 16]
print(list(gen))  # []
```
