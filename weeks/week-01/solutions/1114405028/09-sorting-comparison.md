# 9 比較、排序與 key 函式

你必須已經「不需要解釋」就能看懂：

```python
a < b  # 比較運算子：用於比較兩個物件的大小。在 Python 中，大多數型別都支援比較運算子。
```

```python
sorted(data, key=lambda x: x.price)  # sorted 函式：對 data 進行排序，使用 lambda 函式指定排序鍵為 x.price。key 函式決定排序的依據。
min(data, key=itemgetter('uid'))  # min 函式：從 data 中找出最小值，使用 itemgetter 從字典中提取 'uid' 鍵的值作為比較依據。
```

用途（對應第一章範例）：

- tuple 比較順序  # tuple 的比較是按元素順序進行的，第一個不同的元素決定大小。
- 為何 `(priority, index, item)` 可排序  # 因為 tuple 是可比較的，且元素型別一致，可以用作排序鍵來實現優先隊列。
- Top-N  # 使用 key 函式和 nlargest/nsmallest 找到資料中的前 N 個元素。
- dict / object 排序  # 對包含字典或物件的列表進行排序，需要指定 key 函式來提取排序依據。
- groupby 前置排序  # itertools.groupby 要求資料預先按分組鍵排序，否則分組會不正確。
