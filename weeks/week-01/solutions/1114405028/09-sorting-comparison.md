# 9 比較、排序與 key 函式

你必須已經「不需要解釋」就能看懂：

```python
a < b  # 基本的比較運算符，用於比較兩個值的大小
```

```python
sorted(data, key=lambda x: x.price)  # 使用 sorted 函式對 data 進行排序，key 參數指定排序依據為每個元素的 price 屬性，使用 lambda 匿名函式提取屬性
min(data, key=itemgetter('uid'))  # 使用 min 函式找到 data 中 uid 最小的元素，itemgetter 從每個元素中提取 'uid' 鍵的值作為比較依據
```

用途（對應第一章範例）：

- tuple 比較順序：元組會按照元素從左到右的順序進行比較，如果第一個元素相等，則比較第二個，以此類推
- 為何 `(priority, index, item)` 可排序：因為元組是可比較的，且按照字典序排序，這允許我們根據優先級、索引和項目進行排序
- Top-N：使用排序來找到前 N 個最大或最小的元素
- dict / object 排序：對字典或物件列表進行排序，需要使用 key 函式指定排序依據
- groupby 前置排序：使用 itertools.groupby 之前，需要先對數據進行排序，因為 groupby 假設輸入是已排序的
