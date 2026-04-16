# 9 比較、排序與 key 函式

你必須已經「不需要解釋」就能看懂：

```python
a < b
```

```python
sorted(data, key=lambda x: x.price)
min(data, key=itemgetter('uid'))
```

用途（對應第一章範例）：

- tuple 比較順序
- 為何 `(priority, index, item)` 可排序
- Top-N
- dict / object 排序
- groupby 前置排序
