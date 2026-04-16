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
