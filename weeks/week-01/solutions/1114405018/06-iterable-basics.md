# 6 可迭代物件（iterable）觀念

## 概述

可迭代物件是 Python 中的核心概念。理解什麼是 iterable 和 iterator 對於編寫高效的 Python 程式至關重要。

你需要知道（不一定會實作）：

- 什麼是**可迭代物件**（iterable）
- 常見的可迭代物件：`list` / `tuple` / `dict` / `set` / `str` / `file`
- 什麼是**迭代器**（iterator）
- iterator 的特性：只能**走一次**
- 常見的 iterator：`zip`, `filter`, `map`, `groupby`

---

## 可迭代物件（Iterable）

### 什麼是可迭代物件？

**可迭代物件**是能夠用 for 迴圈遍歷的物件，或者具有 `__iter__()` 方法的物件。

```python
# 簡單理解：能被 for 迴圈使用的物件就是 iterable
for item in iterable_object:
    print(item)
```

### 常見的可迭代物件

#### 1. **list（列表）**

```python
numbers = [1, 2, 3, 4, 5]

# 列表是可迭代的
for num in numbers:
    print(num)  # 依次輸出：1、2、3、4、5

# 可以多次遍歷
for num in numbers:
    print(num * 2)  # 依次輸出：2、4、6、8、10

# 再次遍歷仍然可以
for num in numbers:
    print(num)      # 再次從頭開始
```

**特性：**
- ✅ 可多次遍歷
- ✅ 支援索引存取
- ✅ 可變（可修改元素）

#### 2. **tuple（元組）**

```python
coordinates = (10, 20, 30)

# 元組是可迭代的
for coord in coordinates:
    print(coord)  # 依次輸出：10、20、30

# 可以多次遍歷
for coord in coordinates:
    print(coord * 2)  # 依次輸出：20、40、60
```

**特性：**
- ✅ 可多次遍歷
- ✅ 支援索引存取
- ❌ 不可變（無法修改元素）

#### 3. **dict（字典）**

```python
person = {'name': 'Alice', 'age': 30, 'city': 'Taipei'}

# 字典是可迭代的（預設遍歷鍵）
for key in person:
    print(key)  # 依次輸出：name、age、city

# 可以遍歷值
for value in person.values():
    print(value)  # 依次輸出：Alice、30、Taipei

# 可以遍歷鍵值對
for key, value in person.items():
    print(f"{key}: {value}")
    # 輸出：name: Alice、age: 30、city: Taipei

# 可以多次遍歷
for key in person:
    print(key)  # 再次遍歷所有鍵
```

**特性：**
- ✅ 可多次遍歷
- ✅ 支援鍵存取
- ✅ 可變（可修改項目）

#### 4. **set（集合）**

```python
colors = {'red', 'green', 'blue'}

# 集合是可迭代的
for color in colors:
    print(color)  # 輸出順序不確定（集合無序）

# 可以多次遍歷
for color in colors:
    print(color.upper())  # 轉大寫，再次遍歷
```

**特性：**
- ✅ 可多次遍歷
- ❌ 無序（不支援索引）
- ✅ 可變（可添加/移除元素）

#### 5. **str（字符串）**

```python
text = "Hello"

# 字符串是可迭代的（逐字符遍歷）
for char in text:
    print(char)  # 依次輸出：H、e、l、l、o

# 可以多次遍歷
for char in text:
    print(char.upper())  # 轉大寫：H、E、L、L、O
```

**特性：**
- ✅ 可多次遍歷
- ✅ 支援索引存取
- ❌ 不可變（無法修改字符）

#### 6. **file（文件）**

```python
# 文件物件是可迭代的
with open('data.txt', 'r') as file:
    for line in file:
        print(line.strip())  # 逐行讀取檔案

# 注意：文件迭代器只能讀一次
# 如果再次迭代，需要重新打開或使用 seek(0)
```

**特性：**
- ✅ 可多次遍歷（重新打開或 seek(0)）
- ✅ 逐行遍歷
- 🔄 需要注意文件指針位置

---

## 迭代器（Iterator）

### 什麼是迭代器？

**迭代器**是一種有狀態的物件，能夠記住遍歷的位置。迭代器具有 `__iter__()` 和 `__next__()` 方法。

```python
# 迭代器的核心特性：只能走一次
# 當到達終點時，迭代就結束了
```

### 迭代器 vs 可迭代物件

```python
# 可迭代物件：可多次遍歷
my_list = [1, 2, 3]
for item in my_list:
    print(item)
for item in my_list:         # ✅ 可以再次遍歷
    print(item)

# 迭代器：只能走一次
my_iterator = iter(my_list)  # 從可迭代物件建立迭代器
print(next(my_iterator))     # 1
print(next(my_iterator))     # 2
print(next(my_iterator))     # 3
# print(next(my_iterator))   # ❌ StopIteration 例外

# 另一個迭代器可以再次走
my_iterator2 = iter(my_list)  # ✅ 建立新的迭代器
print(next(my_iterator2))    # 1
```

### 常見的迭代器

#### 1. **zip() - 並行迭代**

```python
# zip 返回一個迭代器，配對多個序列
names = ['Alice', 'Bob', 'Charlie']
ages = [30, 25, 35]
cities = ['Taipei', 'NYC', 'London']

pairs = zip(names, ages)
# <zip object at 0x...> - 這是一個迭代器

# ✅ 第一次遍歷
for name, age in pairs:
    print(f"{name}: {age}")
    # 輸出：Alice: 30、Bob: 25、Charlie: 35

# ❌ 第二次遍歷會是空的（迭代器已耗盡）
for name, age in pairs:
    print(f"{name}: {age}")  # 沒有輸出

# ✅ 需要重新建立 zip 物件
pairs = zip(names, ages)
for name, age in pairs:
    print(f"{name}: {age}")  # ✅ 現在可以再次遍歷

# 如果序列長度不同，zip 在最短的序列結束時停止
longer = [1, 2, 3, 4, 5]
shorter = ['a', 'b']
for num, letter in zip(longer, shorter):
    print(f"{num}, {letter}")
    # 輸出：1, a、2, b（3, 4, 5 被忽略）
```

#### 2. **filter() - 篩選元素**

```python
# filter 返回一個迭代器，只包含符合條件的元素
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 建立一個篩選偶數的迭代器
even_numbers = filter(lambda x: x % 2 == 0, numbers)
# <filter object at 0x...> - 這是一個迭代器

# ✅ 第一次遍歷
for num in even_numbers:
    print(num)  # 輸出：2、4、6、8、10

# ❌ 第二次遍歷會是空的
for num in even_numbers:
    print(num)  # 沒有輸出

# ✅ 需要重新建立 filter 物件
even_numbers = filter(lambda x: x % 2 == 0, numbers)
for num in even_numbers:
    print(num)  # 現在可以再次遍歷

# 轉換成列表可以多次使用
even_list = list(filter(lambda x: x % 2 == 0, numbers))
for num in even_list:
    print(num)  # ✅ 第一次
for num in even_list:
    print(num)  # ✅ 第二次也可以
```

#### 3. **map() - 轉換元素**

```python
# map 返回一個迭代器，將函式應用於所有元素
numbers = [1, 2, 3, 4, 5]

# 建立一個將所有數字平方的迭代器
squared = map(lambda x: x ** 2, numbers)
# <map object at 0x...> - 這是一個迭代器

# ✅ 第一次遍歷
for num in squared:
    print(num)  # 輸出：1、4、9、16、25

# ❌ 第二次遍歷會是空的
for num in squared:
    print(num)  # 沒有輸出

# ✅ 轉換成列表可多次使用
squared_list = list(map(lambda x: x ** 2, numbers))
print(squared_list)  # [1, 4, 9, 16, 25]
for num in squared_list:
    print(num)  # ✅ 第一次
for num in squared_list:
    print(num)  # ✅ 第二次
```

#### 4. **groupby() - 分組迭代**

```python
from itertools import groupby

# groupby 返回一個迭代器，按鍵分組元素
data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4]

for key, group in groupby(data):
    group_list = list(group)
    print(f"{key}: {group_list}")
    # 輸出：1: [1, 1, 1]、2: [2, 2]、3: [3, 3, 3, 3]、4: [4]

# 注意：groupby 返回的 group 也是迭代器，只能走一次
for key, group in groupby(data):
    # ✅ 立即消費迭代器
    first = next(group)
    print(f"{key}: 第一個元素是 {first}")
    
    # ❌ 如果再次嘗試遍歷 group，會是空的
    for item in group:
        print(item)  # 可能沒有輸出或不完整
```

---

## 解包 iterable

### 基本解包

```python
# 直接解包可迭代物件
a, b, c = [1, 2, 3]  # a=1, b=2, c=3
x, y = ('hello', 'world')  # x='hello', y='world'

# 使用星號進行部分解包
first, *rest = [1, 2, 3, 4, 5]
# first=1, rest=[2, 3, 4, 5]

first, *middle, last = range(10)
# first=0, middle=[1,2,3,4,5,6,7,8], last=9

# 忽略某些值
a, _, c = [1, 2, 3]  # a=1, c=3 (2 被忽略)
```

### 解包 zip 結果

```python
names = ['Alice', 'Bob', 'Charlie']
ages = [30, 25, 35]

# 解包 zip 結果
for name, age in zip(names, ages):
    print(f"{name}: {age}")

# 也可以完全解包 zip 結果
name1, name2, name3 = zip(names, ages)[0]  # 錯誤，zip 返回迭代器
# 需要轉換成列表
pairs = list(zip(names, ages))
(n1, a1), (n2, a2), (n3, a3) = pairs
```

### 解包生成器表達式

```python
# 生成器表達式也是迭代器
squared = (x**2 for x in range(3))  # (是圓括號，不是方括號)

# ✅ 第一次解包
a, b, c = squared
print(a, b, c)  # 0 1 4

# ❌ 第二次解包會失敗（迭代器已耗盡）
# try:
#     x, y, z = squared  # ValueError
```

---

## 生成器（generator）

### 什麼是生成器？

生成器是一種特殊的迭代器，使用 `yield` 關鍵字定義。生成器會懶惰地（按需）生成值，而不是一次性生成所有值。

```python
# 生成器函式：使用 yield
def count_up_to(n):
    i = 1
    while i <= n:
        yield i      # 每次返回一個值，然後暫停
        i += 1

# 建立生成器物件
counter = count_up_to(3)
# <generator object count_up_to at 0x...>

# ✅ 第一次遍歷
for num in counter:
    print(num)  # 依次輸出：1、2、3

# ❌ 第二次遍歷會是空的
for num in counter:
    print(num)  # 沒有輸出

# ✅ 需要重新建立生成器
counter = count_up_to(3)
for num in counter:
    print(num)  # 現在可以再次遍歷
```

### 生成器表達式

```python
# 列表推導式（一次性建立所有元素）
squares_list = [x**2 for x in range(10)]

# 生成器表達式（按需生成元素）
squares_gen = (x**2 for x in range(10))

# 列表推導式會佔用更多記憶體
print(type(squares_list))  # <class 'list'>
print(type(squares_gen))   # <class 'generator'>

# 但生成器只能走一次
for sq in squares_gen:
    print(sq)  # 輸出：0、1、4、9、16、...

for sq in squares_gen:
    print(sq)  # 沒有輸出（已耗盡）
```

---

## 常用工具函式

### 1. **compress() - 根據條件選擇元素**

```python
from itertools import compress

# compress 返回一個迭代器
data = ['A', 'B', 'C', 'D', 'E']
selectors = [True, False, True, False, True]

result = compress(data, selectors)

# ✅ 第一次遍歷
for item in result:
    print(item)  # 輸出：A、C、E

# ❌ 第二次遍歷會是空的
for item in result:
    print(item)  # 沒有輸出

# ✅ 轉換成列表
result = list(compress(data, selectors))
for item in result:
    print(item)  # ✅ 可多次遍歷
```

### 2. **enumerate() - 獲取索引和值**

```python
# enumerate 返回一個迭代器
items = ['apple', 'banana', 'cherry']

enumerated = enumerate(items)
# <enumerate object at 0x...>

# ✅ 第一次遍歷
for index, item in enumerated:
    print(f"{index}: {item}")
    # 輸出：0: apple、1: banana、2: cherry

# ❌ 第二次遍歷會是空的
for index, item in enumerated:
    print(f"{index}: {item}")  # 沒有輸出

# ✅ 轉換成列表
enumerated_list = list(enumerate(items))
for index, item in enumerated_list:
    print(f"{index}: {item}")  # 可多次遍歷
```

### 3. **reversed() - 反向迭代**

```python
# reversed 返回一個反向迭代器
numbers = [1, 2, 3, 4, 5]

reversed_iter = reversed(numbers)

# ✅ 第一次遍歷
for num in reversed_iter:
    print(num)  # 輸出：5、4、3、2、1

# ❌ 第二次遍歷會是空的
for num in reversed_iter:
    print(num)  # 沒有輸出

# ✅ 轉換成列表
reversed_list = list(reversed(numbers))
for num in reversed_list:
    print(num)  # ✅ 可多次遍歷
```

---

## 衡量記憶體使用

### 迭代器的優勢

```python
# 假設有很大的數據集
def large_dataset():
    for i in range(1000000):
        yield i  # 只在需要時生成

# 方法 1：列表（一次性建立所有 100 萬個元素）
big_list = list(range(1000000))  # 佔用大量記憶體

# 方法 2：生成器（按需生成，節省記憶體）
big_gen = large_dataset()  # 幾乎不佔記憶體

# 逐個處理
for num in big_gen:
    if num > 999990:
        print(num)  # 只在需要時計算
```

---

## 實際應用場景

### 1. 處理大文件

```python
# ❌ 不推薦：一次性讀取所有行（記憶體爆炸）
with open('huge_file.txt', 'r') as f:
    all_lines = f.readlines()  # 如果文件很大會很慢
    for line in all_lines:
        process(line)

# ✅ 推薦：逐行讀取（文件物件是迭代器）
with open('huge_file.txt', 'r') as f:
    for line in f:  # 按需讀取
        process(line)
```

### 2. 數據轉換管道

```python
# 建立轉換管道
numbers = range(1000000)

# 篩選偶數、平方、再篩選小於 10000 的
result = filter(lambda x: x < 10000,
                map(lambda x: x**2,
                    filter(lambda x: x % 2 == 0, numbers)))

# 或使用生成器表達式（更清晰）
result = (x**2 for x in numbers if x % 2 == 0 if x**2 < 10000)

# 按需計算（記憶體效率高）
for value in result:
    print(value)
```

### 3. 無限序列

```python
# 生成無限序列是可能的（因為迭代器按需生成）
def infinite_count():
    i = 0
    while True:
        yield i
        i += 1

# ✅ 可以從無限序列中取前 N 個元素
counter = infinite_count()
first_five = [next(counter) for _ in range(5)]
print(first_five)  # [0, 1, 2, 3, 4]
```

---

## 在循環中迴圈使用迭代器的正確做法

```python
def process_data():
    data = [1, 2, 3, 4, 5]
    filtered = filter(lambda x: x > 2, data)
    
    # ❌ 錯誤做法：多次使用同一迭代器
    # for item in filtered:
    #     print(item)  # 輸出：3、4、5
    # for item in filtered:
    #     print(item)  # 沒有輸出！
    
    # ✅ 正確做法 1：轉換成列表
    filtered_list = list(filter(lambda x: x > 2, data))
    for item in filtered_list:
        print(item)
    for item in filtered_list:
        print(item)  # ✅ 可以再次遍歷
    
    # ✅ 正確做法 2：在迴圈中重新建立
    for _ in range(2):
        filtered = filter(lambda x: x > 2, data)
        for item in filtered:
            print(item)
```

---

## 重要提示

⚠️ **常見錯誤與注意事項：**

1. **混淆迭代器和可迭代物件**
   ```python
   my_list = [1, 2, 3]  # ✅ 可迭代物件，可多次遍歷
   my_iter = iter(my_list)  # ❌ 迭代器，只能走一次
   
   for item in my_list:
       print(item)
   for item in my_list:           # ✅ 仍可遍歷
       print(item)
   
   for item in my_iter:
       print(item)
   for item in my_iter:           # ❌ 沒有輸出
       print(item)
   ```

2. **忘記迭代器是一次性的**
   ```python
   pairs = zip([1, 2], ['a', 'b'])
   for x, y in pairs:
       print(x, y)
   
   # 再次利用 pairs 結果會為空
   for x, y in pairs:            # ❌ 沒有輸出
       print(x, y)
   
   # ✅ 需要重新建立
   pairs = zip([1, 2], ['a', 'b'])
   ```

3. **生成器表達式 vs 列表推導式**
   ```python
   # 生成器表達式：( ... ) 圓括號
   gen = (x**2 for x in range(10))
   
   # 列表推導式：[ ... ] 方括號
   lst = [x**2 for x in range(10)]
   
   # 記住不要混淆！
   ```

4. **groupby 的陷阱**
   ```python
   from itertools import groupby
   
   data = [1, 1, 2, 2, 3]
   for key, group in groupby(data):
       # ❌ 如果在迴圈外保存 group，會無法存取
       saved_group = group
   
   for item in saved_group:  # 可能為空或不完整
       print(item)
   
   # ✅ 在迴圈內立即使用
   for key, group in groupby(data):
       group_list = list(group)  # 立即轉換成列表
       print(group_list)
   ```

5. **effect of consuming iterators**
   ```python
   it = iter([1, 2, 3])
   x = next(it)      # 1
   y = next(it)      # 2
   
   for z in it:
       print(z)      # 只會輸出 3，因為前兩個已消費
   ```
