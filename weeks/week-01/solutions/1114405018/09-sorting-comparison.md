# 9 比較、排序與 key 函式

## 概述

比較運算是排序的基礎。Python 允許直接比較大多數內建類型，並提供靈活的排序機制。你必須已經「不需要解釋」就能看懂以下代碼：

```python
# 簡單比較
a < b
a <= b
a == b

# 排序列表
sorted(data, key=lambda x: x.price)

# 找最值
min(data, key=itemgetter('uid'))
```

---

## 比較運算符（Comparison Operators）

### 基本比較運算符

Python 提供 6 個比較運算符，它們返回布林值。

```python
# 等於
print(5 == 5)     # True
print(5 == 6)     # False

# 不等於
print(5 != 6)     # True
print(5 != 5)     # False

# 小於
print(5 < 10)     # True
print(10 < 5)     # False

# 小於等於
print(5 <= 5)     # True
print(6 <= 5)     # False

# 大於
print(10 > 5)     # True
print(5 > 10)     # False

# 大於等於
print(5 >= 5)     # True
print(5 >= 6)     # False
```

### 可比較的類型

Python 中許多類型都支持比較，包括數字、字符串、列表、元組等。

```python
# 數字比較
1 < 2           # True
1.5 < 2.5       # True
-5 < 0          # True

# 字符串比較（按字典順序）
'apple' < 'banana'      # True（'a' < 'b'）
'apple' < 'apricot'     # True（'pp' < 'pr'）
'apple' == 'apple'      # True
'Apple' < 'apple'       # True（大寫字母排序優先）

# 列表比較（逐元素比較）
[1, 2, 3] < [1, 2, 4]   # True（第 3 個元素：3 < 4）
[1, 2] < [1, 2, 3]      # True（較短的列表較小）
[1, 3] < [1, 2, 5]      # False（1 == 1，但 3 > 2）

# 元組比較（和列表相同）
(1, 2) < (1, 3)         # True
('a', 1) < ('a', 2)     # True
('a',) < ('b',)         # True

# 混淆：不同類型通常不可比較
# 1 < 'apple'  # ❌ TypeError: '<' not supported
```

### 字符串比較的特性

```python
# 字母順序（基於 Unicode）
'a' < 'b'           # True
'A' < 'B'           # True
'A' < 'a'           # True（大寫字母的 Unicode 值較小）

# 完整詞語
'apple' < 'banana'  # True
'apple' < 'apply'   # True（'pp' < 'pl'）
'apple' < 'apple'   # False（相等）

# 數字字符串按字典順序，不是數值順序
'10' < '2'          # True（字符 '1' < '2'）
'10' < '9'          # True（字符 '1' < '9'）

# 使用 int() 進行數值比較
int('10') < int('2')  # False（10 > 2）

# 空字符串是最小的
'' < 'a'            # True
```

### 鏈式比較

```python
# Python 允許鏈式比較
5 < 10 < 15         # True（5 < 10 AND 10 < 15）
5 < 10 < 8          # False（5 < 10 BUT 10 > 8）
1 <= 2 <= 3 <= 4    # True

# 這等同於
5 < 10 and 10 < 15  # True

# 更複雜的鏈式比較
x = 7
1 < x < 10          # True
x > 5 and x < 10    # True（需要明確使用 and）

# 常見用途：檢查範圍
age = 25
if 18 <= age < 65:  # 年齡在 18 到 64 之間
    print("Work age")
```

---

## sorted() 函式與 key 參數

### 基本 sorted() 用法

```python
# sorted() 返回新的排序列表（原列表不變）

numbers = [3, 1, 4, 1, 5, 9, 2]

# 升序排列
sorted_asc = sorted(numbers)
# [1, 1, 2, 3, 4, 5, 9]

# 降序排列
sorted_desc = sorted(numbers, reverse=True)
# [9, 5, 4, 3, 2, 1, 1]

# 字符串排列
words = ['cherry', 'apple', 'banana']
sorted_words = sorted(words)
# ['apple', 'banana', 'cherry']

# 原列表不變
original = [3, 1, 4]
sorted_list = sorted(original)
print(original)      # [3, 1, 4]
print(sorted_list)   # [1, 3, 4]

# 原地排序：使用 list.sort()
original.sort()
print(original)      # [1, 3, 4]（修改原列表）
```

### 使用 key 參數進行自訂排序

#### 基於屬性排序

```python
# 排序字典列表（按特定鍵）

products = [
    {'name': 'apple', 'price': 1.5},
    {'name': 'banana', 'price': 0.5},
    {'name': 'orange', 'price': 2.0}
]

# 方式 1：使用 lambda
by_price = sorted(products, key=lambda x: x['price'])
# 結果：
# [{'name': 'banana', 'price': 0.5},
#  {'name': 'apple', 'price': 1.5},
#  {'name': 'orange', 'price': 2.0}]

# 方式 2：使用 operator.itemgetter
from operator import itemgetter
by_price = sorted(products, key=itemgetter('price'))
# 結果相同

# 反向排序
by_price_desc = sorted(products, key=lambda x: x['price'], reverse=True)
```

#### 基於物件屬性排序

```python
# 排序物件列表（基於屬性）

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __repr__(self):
        return f"Student({self.name}, {self.grade})"

students = [
    Student('Alice', 85),
    Student('Bob', 92),
    Student('Charlie', 78)
]

# 方式 1：使用 lambda
by_grade = sorted(students, key=lambda s: s.grade)
# [Student(Charlie, 78), Student(Alice, 85), Student(Bob, 92)]

# 方式 2：使用 operator.attrgetter
from operator import attrgetter
by_grade = sorted(students, key=attrgetter('grade'))
# 結果相同

# 按名字排序
by_name = sorted(students, key=lambda s: s.name)
# [Student(Alice, 85), Student(Bob, 92), Student(Charlie, 78)]
```

### 多條件排序（Tuple Key）

```python
# 使用元組作為 key 進行多條件排序

data = [
    {'name': 'Alice', 'priority': 1, 'index': 2},
    {'name': 'Bob', 'priority': 2, 'index': 1},
    {'name': 'Charlie', 'priority': 1, 'index': 1},
]

# 先按優先級，再按索引
sorted_data = sorted(data, key=lambda x: (x['priority'], x['index']))
# 結果：
# [{'name': 'Charlie', 'priority': 1, 'index': 1},
#  {'name': 'Alice', 'priority': 1, 'index': 2},
#  {'name': 'Bob', 'priority': 2, 'index': 1}]

# 這是為什麼 (priority, index, item) 可以排序的原因
# Python 逐元素比較元組

# 降序優先級，升序索引
sorted_data = sorted(data, 
                     key=lambda x: (-x['priority'], x['index']))
# 結果：
# [{'name': 'Bob', 'priority': 2, 'index': 1},
#  {'name': 'Charlie', 'priority': 1, 'index': 1},
#  {'name': 'Alice', 'priority': 1, 'index': 2}]
```

### 複雜的排序鍵

```python
# 排序字符串，忽略大小寫
words = ['Apple', 'banana', 'Cherry']

# 預設：大寫字母優先
print(sorted(words))  # ['Apple', 'Cherry', 'banana']

# 忽略大小寫
print(sorted(words, key=str.lower))  # ['Apple', 'banana', 'Cherry']

# 自訂 key 函式
def get_sort_key(item):
    """複雜的排序邏輯"""
    if isinstance(item, str):
        return (0, item.lower())  # 字符串優先，按小寫排序
    else:
        return (1, item)          # 非字符串次要

mixed = ['cherry', 3, 'apple', 1, 'banana']
sorted_mixed = sorted(mixed, key=get_sort_key)
# [('apple', 1), ('banana', 1), ('cherry', 0), (1, 1), (3, 1)]
```

---

## min() 和 max() 與 key 參數

### 基本用法

```python
numbers = [3, 1, 4, 1, 5, 9, 2]

# 無 key 參數
min_val = min(numbers)  # 1
max_val = max(numbers)  # 9

# 有 key 參數：基於某個標準找最值
words = ['apple', 'pie', 'zoo', 'a']
longest = max(words, key=len)  # 'apple'（5 個字符）
shortest = min(words, key=len)  # 'a'（1 個字符）
```

### 基於複雜條件找最值

```python
# 找最便宜的產品
products = [
    {'name': 'apple', 'price': 1.5},
    {'name': 'banana', 'price': 0.5},
    {'name': 'orange', 'price': 2.0}
]

cheapest = min(products, key=lambda x: x['price'])
# {'name': 'banana', 'price': 0.5}

# 找分數最高的學生
students = [
    Student('Alice', 85),
    Student('Bob', 92),
    Student('Charlie', 78)
]

top_student = max(students, key=lambda s: s.grade)
# Student(Bob, 92)

# 找絕對值最小的數字
numbers = [-3, 1, -5, 2]
closest_to_zero = min(numbers, key=abs)
# 1（|-3| = 3，|1| = 1，|-5| = 5，|2| = 2）

# 找最接近目標值的數字
target = 7
numbers = [2, 5, 9, 12]
closest = min(numbers, key=lambda x: abs(x - target))
# 5（|5 - 7| = 2，是最小的差距）
```

### 使用 operator 模組

```python
from operator import itemgetter, attrgetter, methodcaller

# itemgetter：基於字典鍵
max_price = max(products, key=itemgetter('price'))

# attrgetter：基於物件屬性
max_grade_student = max(students, key=attrgetter('grade'))

# methodcaller：調用方法
words = ['hello', 'world', 'python']
longest = max(words, key=methodcaller('__len__'))  # 等同於 key=len
```

---

## Tuple 比較與優先級隊列

### 為什麼 Tuple 可以比較？

```python
# Python 逐元素比較元組

(1, 2) < (1, 3)         # True（第一個元素相等，比較第二個）
(1, 2) < (2, 1)         # True（1 < 2，不需要檢查第二個）
(1, 2, 5) < (1, 2, 3)   # False（1 == 1，2 == 2，5 > 3）

# 這允許優先級排序
priorities = [
    (2, 'task_b'),
    (1, 'task_a'),
    (2, 'task_c')
]

sorted_priorities = sorted(priorities)
# [(1, 'task_a'), (2, 'task_b'), (2, 'task_c')]
```

### (priority, index, item) 模式

```python
# 常見的優先級隊列模式

import heapq

tasks = [
    (2, 0, 'urgent'),
    (1, 1, 'normal'),
    (3, 2, 'low'),
    (1, 3, 'another_normal')
]

# 小頂堆排序
heapq.heapify(tasks)

# 按優先級提取
while tasks:
    priority, index, task = heapq.heappop(tasks)
    print(f"Priority {priority}: {task}")

# 輸出：
# Priority 1: normal
# Priority 1: another_normal
# Priority 2: urgent
# Priority 3: low

# index 的作用：當優先級相同時，按插入順序排列（FIFO）
```

---

## Groupby 前置排序

### 為什麼要在 groupby 前排序？

```python
from itertools import groupby

# groupby() 只能分組「相鄰」的元素

data = [1, 1, 2, 2, 2, 1, 3, 3]

# ❌ 直接使用 groupby（不排序）
for key, group in groupby(data):
    print(f"{key}: {list(group)}")

# 輸出：
# 1: [1, 1]
# 2: [2, 2, 2]
# 1: [1]           ← 1 重新出現
# 3: [3, 3]

# ✅ 先排序再使用 groupby（推薦）
sorted_data = sorted(data)
for key, group in groupby(sorted_data):
    print(f"{key}: {list(group)}")

# 輸出：
# 1: [1, 1, 1]
# 2: [2, 2, 2]
# 3: [3, 3]
```

### 實際應用：按鍵分組

```python
people = [
    {'name': 'Alice', 'city': 'Taipei'},
    {'name': 'Bob', 'city': 'Kaohsiung'},
    {'name': 'Charlie', 'city': 'Taipei'},
    {'name': 'David', 'city': 'Kaohsiung'}
]

# 先排序（按城市）
sorted_people = sorted(people, key=lambda x: x['city'])

# 再分組
for city, group in groupby(sorted_people, key=lambda x: x['city']):
    names = [p['name'] for p in group]
    print(f"{city}: {names}")

# 輸出：
# Kaohsiung: ['Bob', 'David']
# Taipei: ['Alice', 'Charlie']
```

---

## Top-N 問題

### 方法 1：sorted()

```python
# 找前 N 個最大/最小的元素

numbers = [7, 2, 9, 1, 5, 8, 3]

# 前 3 個最大
top_3_largest = sorted(numbers, reverse=True)[:3]
# [9, 8, 7]

# 前 3 個最小
top_3_smallest = sorted(numbers)[:3]
# [1, 2, 3]

# 複雜資料：前 3 個最貴的產品
products = [
    {'name': 'apple', 'price': 1.5},
    {'name': 'banana', 'price': 0.5},
    {'name': 'orange', 'price': 2.0},
    {'name': 'grape', 'price': 3.5}
]

top_3_expensive = sorted(products, key=lambda x: x['price'], reverse=True)[:3]
# [{'name': 'grape', 'price': 3.5},
#  {'name': 'orange', 'price': 2.0},
#  {'name': 'apple', 'price': 1.5}]

# 效率：O(n log n)
```

### 方法 2：heapq.nlargest / nsmallest（更高效）

```python
import heapq

numbers = [7, 2, 9, 1, 5, 8, 3]

# 前 3 個最大（高效）
top_3_largest = heapq.nlargest(3, numbers)
# [9, 8, 7]

# 前 3 個最小
top_3_smallest = heapq.nsmallest(3, numbers)
# [1, 2, 3]

# 基於 key 的 Top-N
top_3_expensive = heapq.nlargest(3, products, key=lambda x: x['price'])

# 效率：O(n log k)，其中 k 是要找的個數（k < n 時更快）
```

### 效率比較

```python
# 對於大數據集

# sorted()：O(n log n)
# 用於： 需要完整排序或 k 很大時

# heapq.nlargest/nsmallest：O(n log k)
# 用於： 只需要前 k 個元素，且 k << n 時

# 實例
import heapq
import timeit

numbers = list(range(100000, 0, -1))

# 方法 1：sorted()
def with_sorted():
    return sorted(numbers, reverse=True)[:10]

# 方法 2：heapq
def with_heapq():
    return heapq.nlargest(10, numbers)

# heapq.nlargest 通常更快
print(timeit.timeit(with_sorted, number=100))    # 較慢
print(timeit.timeit(with_heapq, number=100))     # 較快
```

---

## 物件排序與 `__lt__`

### 自訂比較

```python
# 定義物件的比較方式

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    # 預設比較方式：按分數
    def __lt__(self, other):
        return self.grade < other.grade
    
    def __eq__(self, other):
        return self.grade == other.grade
    
    def __repr__(self):
        return f"Student({self.name}, {self.grade})"

students = [
    Student('Alice', 85),
    Student('Bob', 92),
    Student('Charlie', 78)
]

# 甚至不需要 key 參數
sorted_students = sorted(students)
# [Student(Charlie, 78), Student(Alice, 85), Student(Bob, 92)]

# 但通常更推薦使用明確的 key 參數，以提高代碼可讀性
sorted_by_name = sorted(students, key=lambda s: s.name)
```

---

## 實際應用場景

### 1. 事件排序與 Top-N

```python
# 找分數最高的課程成績

scores = [
    {'course': 'Python', 'score': 85, 'semester': 1},
    {'course': 'Math', 'score': 92, 'semester': 1},
    {'course': 'English', 'score': 78, 'semester': 1},
    {'course': 'Physics', 'score': 88, 'semester': 2},
]

# 前 2 個最高分
top_2 = sorted(scores, key=lambda x: x['score'], reverse=True)[:2]
# [{'course': 'Math', 'score': 92, ...},
#  {'course': 'Physics', 'score': 88, ...}]

# 按課程排序後找高分
by_course = sorted(scores, key=lambda x: x['course'])
for course, group in groupby(by_course, key=lambda x: x['course']):
    print(f"{course}: {[s['score'] for s in group]}")
```

### 2. 異構數據排序

```python
# 混合整數和字符串，按自訂規則排序

def mixed_key(item):
    """將混合類型轉換為可比較的形式"""
    if isinstance(item, int):
        return (0, item)           # 整數優先
    else:
        return (1, item.lower())   # 字符串次要，忽略大小寫

data = [5, 'apple', 3, 'Banana', 7, 'cherry']
sorted_data = sorted(data, key=mixed_key)
# [3, 5, 7, 'apple', 'Banana', 'cherry']
```

### 3. 購物車排序

```python
# 先按類別排序，再按價格排序

cart = [
    {'category': 'fruit', 'item': 'apple', 'price': 1.5},
    {'category': 'dairy', 'item': 'milk', 'price': 3.0},
    {'category': 'fruit', 'item': 'banana', 'price': 0.5},
    {'category': 'dairy', 'item': 'cheese', 'price': 5.0},
]

# 多條件排序
sorted_cart = sorted(cart, key=lambda x: (x['category'], x['price']))

for item in sorted_cart:
    print(f"{item['category']}: {item['item']} - ${item['price']}")

# 輸出：
# dairy: milk - $3.0
# dairy: cheese - $5.0
# fruit: banana - $0.5
# fruit: apple - $1.5
```

---

## 重要提示

⚠️ **常見錯誤與注意事項：**

1. **list.sort() vs sorted()**
   ```python
   # list.sort()：原地修改，返回 None
   nums = [3, 1, 2]
   nums.sort()  # nums 變為 [1, 2, 3]，返回 None
   
   # sorted()：返回新列表
   nums = [3, 1, 2]
   result = sorted(nums)  # [1, 2, 3]，nums 不變
   
   # 記住：sort() 返回 None
   result = nums.sort()  # result 是 None，❌
   ```

2. **key 參數中不要調用函式**
   ```python
   # ❌ 錯誤：key=len() 會直接調用函式
   sorted(words, key=len())  # TypeError
   
   # ✅ 正確：傳遞函式對象
   sorted(words, key=len)    # 正確
   ```

3. **比較不同類型**
   ```python
   # ❌ 不同類型無法直接比較
   # min([1, 'a', 2.5])  # TypeError
   
   # ✅ 需要轉換或自訂 key
   data = [1, 'a', 2.5]
   def safe_key(x):
       if isinstance(x, str):
           return (1, x)
       else:
           return (0, x)
   sorted(data, key=safe_key)
   ```

4. **groupby 必須先排序**
   ```python
   # ❌ 易犯錯誤
   data = [3, 1, 2, 1, 3]
   for k, g in groupby(data):
       print(k, list(g))
   # 結果：3 [3], 1 [1], 2 [2], 1 [1], 3 [3]
   
   # ✅ 先排序再分組
   data_sorted = sorted(data)
   for k, g in groupby(data_sorted):
       print(k, list(g))
   # 結果：1 [1, 1], 2 [2], 3 [3, 3]
   ```

5. **多條件排序中的負數**
   ```python
   # 降序排列需要特殊處理
   data = [
       {'priority': 2, 'index': 1},
       {'priority': 1, 'index': 2},
   ]
   
   # ❌ 不能直接反轉比較
   # sorted(data, key=lambda x: -x['priority'])  # 若 priority 是字符串則錯誤
   
   # ✅ 方式 1：reverse=True
   sorted(data, key=lambda x: x['priority'], reverse=True)
   
   # ✅ 方式 2：在 tuple 中控制順序
   sorted(data, key=lambda x: (-x['priority'], x['index']))
   ```

6. **效率考慮**
   ```python
   # 大數據集中的 Top-N
   
   import heapq
   
   # ❌ 低效：排序所有數據
   top_10 = sorted(data, reverse=True)[:10]  # O(n log n)
   
   # ✅ 高效：只堆排前 10 個
   top_10 = heapq.nlargest(10, data)         # O(n log 10)
   ```

7. **字符串排序的坑**
   ```python
   # 字符按 Unicode 排列，大寫 < 小寫
   sorted(['a', 'B', 'c', 'D'])  # ['B', 'D', 'a', 'c']
   
   # 忽略大小寫排序
   sorted(['a', 'B', 'c', 'D'], key=str.lower)  # ['a', 'B', 'c', 'D']
   
   # 數字字符串排列
   sorted(['10', '2', '1', '20'])  # ['1', '10', '2', '20']（字典順序）
   sorted(['10', '2', '1', '20'], key=int)  # ['1', '2', '10', '20']（數值順序）
   ```
