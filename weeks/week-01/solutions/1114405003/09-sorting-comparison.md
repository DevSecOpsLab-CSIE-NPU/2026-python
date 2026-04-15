# 9 比較、排序與 key 函式

你必須已經「不需要解釋」就能看懂：

```python
# Python 會先比較左邊，再決定是否要看右邊。
# 這種基本比較行為是排序、最小值、最大值的基礎。
a < b
```

```python
# sorted(..., key=...) 會先對每個元素計算 key，再根據 key 進行排序。
# lambda x: x.price 表示「用物件的 price 屬性作為排序依據」。
sorted(data, key=lambda x: x.price)

# itemgetter('uid') 會從字典中取出 uid 欄位當作比較用的 key。
# 這比手寫 lambda 更精簡，也常用在需要高可讀性的排序邏輯中。
min(data, key=itemgetter('uid'))
```

用途（對應第一章範例）：

- tuple 比較順序
- 為何 `(priority, index, item)` 可排序
- Top-N
- dict / object 排序
- groupby 前置排序

## 補充說明

這一章的重點，不只是「會排序」，而是要理解 Python 真的在比什麼。

- tuple 會依序比較第一個、第二個、第三個元素，所以 `(priority, index, item)` 可以自然地表達優先順序。
- `key=` 的精神是「先轉成可比較的值，再排序」，這可以避開直接比較複雜物件的問題。
- `sorted()` 會回傳新列表，不會改動原資料；`list.sort()` 則是原地排序。
- 當你需要穩定性時，可以利用 Python 排序的穩定特性，讓原本順序成為第二層條件。

```python
# 範例：先用 priority 排序，priority 相同時再用 index 保持原始順序。
items = sorted(items, key=lambda item: (item.priority, item.index))
```

如果你的資料是字典、物件或自訂類別，優先思考要拿哪個欄位當排序基準，而不是硬把整個物件拿去比。這樣程式通常更穩定，也更容易讀懂。
