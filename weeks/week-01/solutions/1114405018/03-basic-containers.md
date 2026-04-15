# 3 基本容器型別

## 概述

容器型別是用來存儲多個元素的資料結構。你必須已經「不需要解釋」就能看懂以下四種基本容器：

```python
list = [1, 2, 3]           # 列表：可變的、有序的集合
tuple = (1, 2)             # 元組：不可變的、有序的集合
set = {1, 2, 3}            # 集合：無序的、唯一元素的集合
dict = {'a': 1}            # 字典：鍵值對的集合
```

---

## 四種基本容器詳解

### 1. **list（列表）**

列表是 Python 中最常用的容器，用於存儲多個項目的有序集合。列表是**可變的**（可以修改）。

#### 基本特徵
- **有序**：元素按加入順序排列
- **可變**：可以添加、刪除、修改元素
- **可重複**：可以包含重複的元素
- **用方括號定義**：`[元素1, 元素2, ...]`

#### 建立列表

```python
# 方式 1：直接列出元素
numbers = [1, 2, 3, 4, 5]              # 整數列表
names = ['Alice', 'Bob', 'Charlie']    # 字串列表
mixed = [1, 'hello', 3.14, True]       # 混合型別列表

# 方式 2：空列表
empty_list = []

# 方式 3：使用 list() 建構子
list_from_string = list('abc')         # 結果：['a', 'b', 'c']
list_from_range = list(range(1, 4))    # 結果：[1, 2, 3]
```

#### 常見操作

```python
# 存取元素（使用索引）
fruits = ['apple', 'banana', 'cherry']
first = fruits[0]                      # 第一個元素：'apple'
last = fruits[-1]                      # 最後一個元素：'cherry'

# 切片（獲取多個元素）
some_fruits = fruits[0:2]              # 前兩個元素：['apple', 'banana']
all_fruits = fruits[:]                 # 複製整個列表

# 添加元素
fruits.append('date')                  # 在末尾添加：['apple', ..., 'date']
fruits.insert(1, 'blueberry')          # 在索引 1 插入

# 移除元素
removed = fruits.pop()                 # 移除並返回最後一個元素
fruits.remove('apple')                 # 移除第一個匹配的 'apple'
del fruits[0]                          # 按索引刪除

# 查找元素
index = fruits.index('banana')         # 獲取 'banana' 的索引
count = fruits.count('apple')          # 計算 'apple' 出現的次數

# 列表長度
length = len(fruits)                   # 列表中有多少個元素

# 排序
numbers = [3, 1, 4, 1, 5]
numbers.sort()                         # 原地排序：[1, 1, 3, 4, 5]
sorted_desc = sorted(numbers, reverse=True)  # 降序排列
```

**應用場景：**
```python
# 存儲購物清單
shopping_list = ['牛奶', '麵包', '雞蛋']

# 迴圈遍歷列表
for item in shopping_list:
    print(f"購買：{item}")

# 列表推導式（快速建立列表）
squares = [x**2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]
```

---

### 2. **tuple（元組）**

元組與列表類似，但元組是**不可變的**（建立後無法修改）。元組通常用於保護數據不被意外修改。

#### 基本特徵
- **有序**：元素按加入順序排列
- **不可變**：建立後無法修改、添加或刪除元素
- **可重複**：可以包含重複的元素
- **用圓括號定義**：`(元素1, 元素2, ...)`

#### 建立元組

```python
# 方式 1：直接列出元素
coordinates = (10, 20)                 # 二維座標
rgb = (255, 128, 0)                    # 顏色值（紅、綠、藍）
data = (1, 'hello', 3.14)              # 混合型別

# 方式 2：單元素元組（注意逗號）
single = (42,)                         # 必須加逗號，否則就是普通數字
not_tuple = (42)                       # 這只是普通整數 42，不是元組

# 方式 3：空元組
empty = ()

# 方式 4：使用 tuple() 建構子
tuple_from_list = tuple([1, 2, 3])     # 結果：(1, 2, 3)
tuple_from_string = tuple('abc')       # 結果：('a', 'b', 'c')
```

#### 常見操作

```python
# 存取元素（與列表相同）
point = (10, 20, 30)
x = point[0]                           # 第一個坐標：10
last = point[-1]                       # 最後一個坐標：30

# 切片（與列表相同）
partial = point[0:2]                   # 前兩個元素：(10, 20)

# 列表長度
length = len(point)                    # 3

# 查找元素
index = point.index(20)                # 找 20 的位置：1
count = point.count(10)                # 計算 10 出現次數：1

# ❌ 不能修改（會報錯）
# point[0] = 100                       # TypeError: 不能修改元組
# point.append(40)                     # AttributeError: 元組沒有 append 方法
```

**應用場景：**
```python
# 函式回傳多個值（自動打包成元組）
def get_user():
    return 'Alice', 30, 'Taipei'       # 自動成為 ('Alice', 30, 'Taipei')

name, age, city = get_user()

# 字典的鍵（只能用不可變型別）
locations = {
    (10, 20): '地點 A',                # 元組作為鍵
    (30, 40): '地點 B'
}

# 保護重要數據
RGB_COLORS = {
    'red': (255, 0, 0),                # 預設顏色值不會被改變
    'green': (0, 255, 0)
}
```

---

### 3. **set（集合）**

集合用於存儲**唯一的、無序的元素**。集合適合用於去除重複、檢查成員和進行集合運算。

#### 基本特徵
- **無序**：元素沒有特定順序
- **唯一**：自動去除重複元素
- **可變**：可以添加和移除元素
- **用大括號定義**：`{元素1, 元素2, ...}`

#### 建立集合

```python
# 方式 1：直接列出元素
colors = {'red', 'green', 'blue'}      # 字串集合
numbers = {1, 2, 3, 4, 5}              # 整數集合
mixed = {1, 'hello', 3.14}             # 混合型別

# 方式 2：自動去重
unique = {1, 2, 2, 3, 3, 3}            # 結果：{1, 2, 3}

# 方式 3：空集合（注意與空字典的區別）
empty_set = set()                      # 正確的空集合
not_set = {}                           # 這是空字典，不是集合

# 方式 4：使用 set() 建構子
set_from_list = set([1, 2, 2, 3])      # 結果：{1, 2, 3}
set_from_string = set('hello')         # 結果：{'h', 'e', 'l', 'o'}（l 只出現一次）
```

#### 常見操作

```python
# 添加元素
fruits = {'apple', 'banana'}
fruits.add('cherry')                   # 添加單個元素
fruits.update(['date', 'elderberry'])  # 添加多個元素

# 移除元素
fruits.remove('apple')                 # 移除存在的元素（不存在會報錯）
fruits.discard('grape')                # 移除元素（不存在不報錯）
removed = fruits.pop()                 # 移除並返回任意元素

# 檢查成員
'apple' in fruits                      # 檢查元素是否存在：True/False

# 集合長度
length = len(fruits)                   # 集合中有多少個元素

# 集合運算
set_a = {1, 2, 3}
set_b = {2, 3, 4}

union = set_a | set_b                  # 並集：{1, 2, 3, 4}
intersection = set_a & set_b           # 交集：{2, 3}
difference = set_a - set_b             # 差集：{1}
symmetric_diff = set_a ^ set_b         # 對稱差：{1, 4}
```

**應用場景：**
```python
# 去除列表中的重複元素
numbers = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = list(set(numbers))    # [1, 2, 3, 4]

# 檢查是否有重複
has_duplicate = len(numbers) != len(set(numbers))  # True

# 查找共同元素
python_skills = {'列表', '元組', '字典', '函式'}
javascript_skills = {'物件', '陣列', '函式', '類別'}
common = python_skills & javascript_skills  # {'函式'}
```

---

### 4. **dict（字典）**

字典用於存儲**鍵值對**的集合。字典是**可變的**，並且是無序的（Python 3.7+ 保持插入順序）。

#### 基本特徵
- **鍵值對**：每個元素由鍵和值組成
- **無序**（Python 3.7+ 保持插入順序）
- **可變**：可以添加、修改、刪除項目
- **鍵必須唯一且不可變**：通常是字串或整數
- **用大括號定義**：`{鍵1: 值1, 鍵2: 值2, ...}`

#### 建立字典

```python
# 方式 1：直接定義
person = {
    'name': 'Alice',                   # 字串鍵
    'age': 30,                         # 整數值
    'city': 'Taipei'
}

# 方式 2：空字典
empty_dict = {}

# 方式 3：使用 dict() 建構子
from_tuples = dict([('a', 1), ('b', 2)])  # 從元組列表建立
from_keys = dict.fromkeys(['x', 'y', 'z'], 0)  # 結果：{'x': 0, 'y': 0, 'z': 0}
```

#### 常見操作

```python
# 存取值
person = {'name': 'Bob', 'age': 25, 'city': 'NYC'}
name = person['name']                  # 直接存取：'Bob'
name = person.get('name')              # 安全存取：'Bob'
unknown = person.get('email', 'N/A')   # 如果不存在返回預設值：'N/A'

# 添加或修改
person['email'] = 'bob@example.com'    # 添加新鍵值對
person['age'] = 26                     # 修改現有值

# 刪除
del person['email']                    # 按鍵刪除
removed_value = person.pop('age')      # 移除並返回值

# 檢查鍵
'name' in person                       # 檢查鍵是否存在：True
'email' in person                      # 檢查鍵是否存在：False

# 獲取所有鍵、值、項目
keys = person.keys()                   # 所有鍵：dict_keys(['name', 'city'])
values = person.values()               # 所有值：dict_values(['Bob', 'NYC'])
items = person.items()                 # 所有項目：dict_items([('name', 'Bob'), ...])

# 遍歷字典
for key in person:                     # 遍歷鍵
    print(f"{key}: {person[key]}")

for key, value in person.items():      # 遍歷鍵值對（推薦）
    print(f"{key}: {value}")

# 字典長度
length = len(person)                   # 有多少個鍵值對

# 更新字典
person.update({'age': 27, 'job': 'Engineer'})  # 添加或更新多個項目
```

**應用場景：**
```python
# 存儲用戶信息
users = {
    'user001': {'name': 'Alice', 'email': 'alice@example.com'},
    'user002': {'name': 'Bob', 'email': 'bob@example.com'}
}

# 計數
word_count = {}
for word in ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']:
    word_count[word] = word_count.get(word, 0) + 1
# 結果：{'apple': 3, 'banana': 2, 'cherry': 1}

# 映射
age_groups = {'Alice': '20-30', 'Bob': '30-40', 'Charlie': '40-50'}
```

---

## 容器比較表

| 特性 | list | tuple | set | dict |
|------|------|-------|-----|------|
| **定義方式** | `[...]` | `(...)` | `{...}` | `{key: value}` |
| **有序** | ✅ | ✅ | ❌ | ✅ (3.7+) |
| **可變** | ✅ | ❌ | ✅ | ✅ |
| **允許重複** | ✅ | ✅ | ❌ | ❌ (鍵) |
| **可當字典鍵** | ❌ | ✅ | ❌ | ❌ |
| **支援索引** | ✅ | ✅ | ❌ | ❌ |
| **主要用途** | 序列數據 | 不變數據 | 唯一元素 | 鍵值對應 |

---

## 用途（對應第一章範例）

### 適用場景

**幾乎每一個例子都會用到容器型別：**

```python
# 列表：存儲多筆股票記錄
records = [
    {'symbol': 'GOOG', 'price': 150},
    {'symbol': 'MSFT', 'price': 300},
]

# 字典：存儲單筆記錄
record = {'symbol': 'GOOG', 'shares': 100, 'price': 150.5}

# 元組：函式回傳多個值
def split_record(line):
    parts = line.split(',')
    return parts[0], int(parts[1]), float(parts[2])  # 回傳元組

# 集合：去除重複
unique_symbols = set(record['symbol'] for record in records)
```

### 進階容器型別的基礎

以下進階容器型別都是建立在基本容器之上的：

```python
# defaultdict：預設值字典
from collections import defaultdict
word_count = defaultdict(int)  # 基於 dict，提供預設值

# Counter：計數容器
from collections import Counter
counts = Counter([1, 1, 2, 2, 2, 3])  # 基於 dict，用於計數

# ChainMap：鏈接多個字典
from collections import ChainMap
combined = ChainMap(dict1, dict2)  # 結合多個字典
```

---

## 重要提示

⚠️ **常見錯誤與注意事項：**

1. **混淆集合與字典的大括號**
   ```python
   my_set = {1, 2, 3}                 # ✅ 集合
   my_dict = {'a': 1, 'b': 2}         # ✅ 字典
   empty = set()                      # ✅ 空集合
   # empty = {}                       # ❌ 這是空字典，不是空集合
   ```

2. **元組的單元素陷阱**
   ```python
   single_tuple = (1,)                # ✅ 元組
   # not_tuple = (1)                  # ❌ 這只是普通整數
   ```

3. **列表是可變的，會影響副本**
   ```python
   original = [1, 2, 3]
   copy = original                    # ❌ 只是引用（指向同一物件）
   copy.append(4)                     # original 也被修改了
   
   # ✅ 正確的複製方式
   proper_copy = original[:]          # 切片複製
   proper_copy = original.copy()      # 使用 copy() 方法
   ```

4. **字典鍵必須不可變**
   ```python
   my_dict = {(1, 2): 'value'}        # ✅ 可以用元組做鍵
   # my_dict = {[1, 2]: 'value'}      # ❌ 不能用列表做鍵
   # my_dict = {{}: 'value'}           # ❌ 不能用字典做鍵
   ```

5. **字典 get() 方法的安全性**
   ```python
   user = {'name': 'Alice'}
   name = user['age']                 # ❌ KeyError: 'age' 不存在
   age = user.get('age')              # ✅ 返回 None，不報錯
   age = user.get('age', 'Unknown')   # ✅ 返回預設值 'Unknown'
   ```
