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

---

## Python 的基本比較

```python
a < b
```

這是最基本的比較運算，結果會是 `True` 或 `False`。

Python 也可以比較 tuple：

```python
(1, 3) < (1, 5)
```

比較規則是從左到右逐項比較：

- 第一個值不同，就用第一個值決定大小
- 第一個值相同，才比較第二個值
- 依此類推

所以：

```python
(1, 3) < (1, 5)  # True
(2, 0) < (1, 99) # False
```

這個規則常用在排序多個條件時。

---

## sorted() 與 key 函式

```python
sorted(data, key=lambda x: x.price)
```

`sorted()` 會回傳新的排序結果，不會修改原本的 `data`。

`key` 的作用是告訴 Python：「排序時要拿什麼值來比較」。

例如：

```python
items = [
    {"name": "apple", "price": 30},
    {"name": "banana", "price": 15},
]

result = sorted(items, key=lambda item: item["price"])
```

這裡不是直接比較整個 dict，而是拿每個 dict 的 `price` 來排序。

---

## itemgetter 與 attrgetter

```python
min(data, key=itemgetter('uid'))
```

`itemgetter('uid')` 常用在 dict，意思是取出 `data[i]['uid']` 當作比較值。

如果資料是物件，常見寫法是：

```python
sorted(users, key=attrgetter("user_id"))
```

`attrgetter("user_id")` 會取出 `user.user_id` 當作排序依據。

這兩種寫法和 `lambda` 功能接近，只是語意比較明確。

---

## 為什麼 `(priority, index, item)` 可以排序

在優先佇列中常看到這種資料：

```python
(priority, index, item)
```

Python 會先比較 `priority`。

如果 `priority` 相同，就比較 `index`。

這樣可以避免直接比較 `item`，因為有些物件本身不能比較大小。

範例：

```python
(1, 0, "task-a") < (1, 1, "task-b")  # True
```

兩個任務 priority 相同時，`index` 較小者會排在前面。

---

## Top-N 與排序的選擇

如果只需要前幾名，可以使用 `heapq.nlargest()` 或 `heapq.nsmallest()`。

如果需要完整排序，才使用 `sorted()`。

概念上：

- `sorted(data)`：把全部資料排好
- `nlargest(3, data)`：只找最大的 3 筆

資料量小時差異不明顯；資料量大時，選對方法會比較省時間。

---

## groupby 前要先排序

`itertools.groupby()` 只會把「相鄰且 key 相同」的資料分在一起。

所以使用 `groupby()` 前，通常要先依同一個 key 排序。

```python
data = sorted(data, key=lambda x: x.category)
```

如果沒有先排序，相同類別的資料可能會被拆成多組。
