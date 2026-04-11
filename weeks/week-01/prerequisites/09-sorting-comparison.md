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

## 註釋版範例（可直接貼到程式）

```python
from itertools import groupby
from operator import itemgetter

# 1) tuple 比較：由左到右逐一比較
print((1, 9, 5) < (2, 0, 0))   # True，因為第一個元素 1 < 2
print((1, 9, 5) < (1, 10, 0))  # True，第一個元素相同，再比第二個 9 < 10

# 2) 為何 (priority, index, item) 可排序
#    常用在優先佇列：先比 priority，再比 index，item 只是負載資料
tasks = [
	(2, 1, "write report"),
	(1, 3, "fix bug"),
	(1, 2, "reply email"),
]
print(sorted(tasks))
# [(1, 2, 'reply email'), (1, 3, 'fix bug'), (2, 1, 'write report')]

# 3) dict 排序：依 uid 排
users = [
	{"uid": 30, "name": "A"},
	{"uid": 10, "name": "B"},
	{"uid": 20, "name": "C"},
]
print(sorted(users, key=itemgetter("uid")))

# 4) object 排序：依 price 排
class Product:
	def __init__(self, name, price):
		self.name = name
		self.price = price

	def __repr__(self):
		return f"Product(name={self.name}, price={self.price})"

products = [Product("pen", 20), Product("book", 120), Product("eraser", 10)]
print(sorted(products, key=lambda p: p.price))

# 5) Top-N：先按 score 由大到小，再切前 N 筆
scores = [
	{"name": "Tom", "score": 75},
	{"name": "Amy", "score": 92},
	{"name": "Bob", "score": 88},
	{"name": "Leo", "score": 95},
]
top2 = sorted(scores, key=lambda x: x["score"], reverse=True)[:2]
print(top2)

# 6) groupby 之前要先用同一個 key 排序
records = [
	{"dept": "HR", "name": "A"},
	{"dept": "IT", "name": "B"},
	{"dept": "HR", "name": "C"},
	{"dept": "IT", "name": "D"},
]

records = sorted(records, key=itemgetter("dept"))  # 先排序，groupby 才會正確分群
for dept, group in groupby(records, key=itemgetter("dept")):
	members = [r["name"] for r in group]
	print(dept, members)
```
