# 9 比較、排序與 key 函式

你必須已經「不需要解釋」就能看懂：

```python
# 基本比較運算子：檢查 a 是否小於 b
a < b
```

```python
# sorted 函數：使用 key 函數來自定義排序規則
# lambda x: x.price 表示以每個元素的 price 屬性作為排序依據
sorted(data, key=lambda x: x.price)

# min 函數：使用 itemgetter 來指定比較的鍵
# itemgetter('uid') 表示以字典中 'uid' 鍵的值作為比較依據
min(data, key=itemgetter('uid'))
```

用途（對應第一章範例）：

- tuple 比較順序：元組按元素順序比較，第一個元素相同才比較下一個
- 為何 `(priority, index, item)` 可排序：因為元組的比較規則，可以用於多重排序條件
- Top-N：使用 sorted 和 key 來取得前 N 個最大或最小的元素
- dict / object 排序：使用 key 函數指定排序依據
- groupby 前置排序：itertools.groupby 需要數據先按分組鍵排序
