# 9 比較、排序與 key 函式

你必須已經「不需要解釋」就能看懂：

```python
a < b  # 比較運算子，用於比較兩個值的大小
```

```python
sorted(data, key=lambda x: x.price)  # 使用 sorted 函式，以 x.price 作為排序鍵
min(data, key=itemgetter('uid'))  # 使用 min 函式，以 'uid' 鍵作為比較鍵
```

用途（對應第一章範例）：

- tuple 比較順序  # tuple 按元素順序比較
- 為何 `(priority, index, item)` 可排序  # tuple 可以作為排序鍵，因為它們是可比較的
- Top-N  # 使用 key 函式找到前 N 個元素
- dict / object 排序  # 對字典或物件列表進行排序
- groupby 前置排序  # groupby 需要資料預先排序
