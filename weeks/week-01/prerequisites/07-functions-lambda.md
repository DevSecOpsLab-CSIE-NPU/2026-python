# 7 函式與 lambda

你必須已經「不需要解釋」就能看懂：

```python
def f(x):
    return x * 2
```

```python
def f(a, b=0):
    return a + b
```

```python
lambda x: x['price']
```

用途（對應第一章範例）：

- `drop_first_last`
- `is_int`
- `sorted(..., key=...)`
- `heapq.nsmallest(..., key=...)`
- `min(..., key=...)`
