# 9 比較、排序與 key 函式

你必須已經「不需要解釋」就能看懂：

## 📚 基本比較運算

```python
# 比較運算子：< > <= >= == !=
a < b  # 小於
# Python 可以比較多種類型：數字、字串、tuple、list 等
# 字串按字典順序（lexicographical order）比較
# tuple/list 按元素逐一比較
```

## 🔧 排序與 key 函式

```python
# sorted() - 回傳排序後的新列表（不改變原資料）
# key 參數：指定「用什麼標準」來排序

# 使用 lambda 函式作為排序鍵
sorted(data, key=lambda x: x.price)
# 解釋：
# - data 是要排序的資料（例如：商品物件的列表）
# - lambda x: x.price 是「取出價格」的函式
# - 結果：依照每個物件的 price 屬性由小到大排序

# 使用 itemgetter 取得特定欄位（需先 from operator import itemgetter）
min(data, key=itemgetter('uid'))
# 解釋：
# - min() 找出最小值
# - itemgetter('uid') 等同於 lambda x: x['uid']
# - 結果：找出 uid 值最小的那筆資料
```

## 💡 核心概念詳解

### 1️⃣ Tuple 比較順序（重要！）

```python
# Tuple 從左到右逐一比較元素
(1, 2, 3) < (1, 2, 4)  # True，因為第三個元素 3 < 4
(1, 3, 0) < (1, 2, 9)  # False，因為第二個元素 3 > 2（後面不用再比）
(1, 2) < (1, 2, 0)     # True，前面相同，較短的 tuple 較小

# 實際應用：多重排序條件
data = [(3, 'C'), (1, 'A'), (1, 'B'), (2, 'D')]
sorted(data)  # [(1, 'A'), (1, 'B'), (2, 'D'), (3, 'C')]
# 先依第一個元素排序，相同時再依第二個元素排序
```

### 2️⃣ 為何 `(priority, index, item)` 可排序？

```python
# 優先佇列（Priority Queue）的常見技巧
items = [
    (1, 0, 'urgent'),      # (優先級, 索引, 項目)
    (3, 1, 'low'),
    (1, 2, 'also_urgent')
]
sorted(items)
# 結果：[(1, 0, 'urgent'), (1, 2, 'also_urgent'), (3, 1, 'low')]
# 
# 排序邏輯：
# 1. 先比 priority（數字越小優先級越高）
# 2. priority 相同時，比 index（保持穩定排序）
# 3. 這樣可以確保相同優先級的項目按照加入順序處理
```

## 🎯 實際應用範例

### 3️⃣ Top-N（找出前 N 名）

```python
# 找出最貴的 3 個商品
products = [
    {'name': 'Apple', 'price': 30},
    {'name': 'Banana', 'price': 10},
    {'name': 'Cherry', 'price': 50},
    {'name': 'Date', 'price': 40}
]

# 方法 1：使用 sorted
top3 = sorted(products, key=lambda x: x['price'], reverse=True)[:3]

# 方法 2：使用 heapq.nlargest（大數據時更高效）
from heapq import nlargest
top3 = nlargest(3, products, key=lambda x: x['price'])
```

### 4️⃣ 字典/物件排序

```python
from operator import itemgetter, attrgetter

# 字典列表排序
students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Carol', 'score': 78}
]
sorted(students, key=itemgetter('score'))  # 依分數排序

# 物件列表排序（假設有 Student 類別）
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

students_obj = [Student('Alice', 85), Student('Bob', 92)]
sorted(students_obj, key=attrgetter('score'))  # 依分數排序

# 多重排序條件
sorted(students, key=itemgetter('grade', 'score'))  # 先依年級，再依分數
```

### 5️⃣ groupby 前置排序

```python
from itertools import groupby

# groupby 需要「先排序」才能正確分組
data = [
    {'category': 'fruit', 'name': 'apple'},
    {'category': 'vegetable', 'name': 'carrot'},
    {'category': 'fruit', 'name': 'banana'},
    {'category': 'vegetable', 'name': 'broccoli'}
]

# 必須先排序（依照要分組的欄位）
sorted_data = sorted(data, key=itemgetter('category'))

# 再進行分組
for category, items in groupby(sorted_data, key=itemgetter('category')):
    print(f"{category}: {list(items)}")
# 輸出：
# fruit: [{'category': 'fruit', 'name': 'apple'}, {'category': 'fruit', 'name': 'banana'}]
# vegetable: [{'category': 'vegetable', 'name': 'carrot'}, {'category': 'vegetable', 'name': 'broccoli'}]
```

## 📋 常用排序技巧總結

```python
# 1. 反向排序
sorted(data, reverse=True)

# 2. 多重條件排序（使用 tuple）
sorted(data, key=lambda x: (x.age, x.name))  # 先依年齡，再依姓名

# 3. 反向其中一個條件（用負號）
sorted(data, key=lambda x: (-x.score, x.name))  # 分數高到低，姓名 A-Z

# 4. lambda vs itemgetter vs attrgetter
key=lambda x: x['name']      # 適用：字典、任意運算
key=itemgetter('name')       # 適用：字典、tuple（效能較好）
key=attrgetter('name')       # 適用：物件屬性

# 5. 原地排序（改變原列表）
data.sort(key=lambda x: x.value)  # 使用 .sort()，不回傳值
```

## 💡 學習重點

1. **理解 tuple 比較規則**：從左到右逐一比較，這是多重排序的基礎
2. **掌握 key 參數**：不是「比較兩個物件」，而是「從每個物件取出比較值」
3. **itemgetter vs lambda**：功能相同，itemgetter 效能較好、程式碼更簡潔
4. **groupby 陷阱**：必須先排序，否則相同類別會被拆成多組
5. **sorted() vs .sort()**：sorted() 回傳新列表，.sort() 原地排序
