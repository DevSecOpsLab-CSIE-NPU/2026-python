# 5 索引與切片

## 概述

索引和切片是從序列（列表、字符串、元組等）中提取元素或子序列的基本操作。你必須已經「不需要解釋」就能看懂以下基本語法：

```python
a[0]          # 索引：獲取第一個元素
a[2:5]        # 切片：獲取從索引 2 到 4 的元素（不含 5）
```

---

## 索引（Indexing）

### 基本概念

索引用於存取序列中**特定位置**的單個元素。Python 使用「從 0 開始」的索引系統。

```python
# 索引序列
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
#          0        1         2         3      4
# 負索引： -5       -4        -3        -2     -1

# 正索引：從左到右，從 0 開始
first = fruits[0]       # 'apple'
second = fruits[1]      # 'banana'
third = fruits[2]       # 'cherry'

# 負索引：從右到左，從 -1 開始
last = fruits[-1]       # 'elderberry'
second_last = fruits[-2]  # 'date'
third_last = fruits[-3]   # 'cherry'
```

### 索引的可視化

```
正索引:  0     1        2        3      4
         ↓     ↓        ↓        ↓      ↓
列表:  ['apple', 'banana', 'cherry', 'date', 'elderberry']
         ↑     ↑        ↑        ↑      ↑
負索引: -5    -4       -3       -2     -1
```

### 字符串索引

```python
# 字符串也支持索引
text = "Hello"
#       01234  (正索引)
#      -5-4-3-2-1 (負索引)

first_char = text[0]      # 'H'
last_char = text[-1]      # 'o'
middle_char = text[2]     # 'l'
```

### 索引超出範圍

```python
items = [1, 2, 3]
first = items[0]         # ✅ 正常：1
last = items[2]          # ✅ 正常：3

# ❌ 索引超出範圍會報錯
# out_of_range = items[5]  # IndexError: list index out of range
# beyond_negative = items[-10]  # IndexError: list index out of range

# ✅ 使用 get() 方法（字典適用）
data = {'name': 'Alice'}
value = data.get('age', 'Unknown')  # 返回預設值，不報錯
```

### 字典 / 集合的「索引」

```python
# 字典不支持數字索引，使用鍵存取
person = {'name': 'Alice', 'age': 30}
name = person['name']       # 'Alice'
age = person['age']         # 30

# ❌ 不能使用數字索引
# first = person[0]          # KeyError or TypeError

# 集合不支持索引（因為無序）
colors = {'red', 'green', 'blue'}
# ❌ 不能用索引存取
# first_color = colors[0]    # TypeError: 'set' object is not subscriptable
```

---

## 切片（Slicing）

### 基本概念

切片用於從序列中提取**連續的子序列**。切片使用冒號 `:` 分隔起始和終止索引。

#### 基本切片語法

```python
sequence[start:stop:step]
# start  - 起始索引（包含），預設為 0
# stop   - 終止索引（不包含），預設為序列長度
# step   - 步長，預設為 1
```

### 常見切片用法

```python
# 基本切片
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# [start:stop] - 從 start 到 stop-1
first_three = numbers[0:3]      # [0, 1, 2]
middle = numbers[2:5]           # [2, 3, 4]
from_five = numbers[5:]         # [5, 6, 7, 8, 9]
to_five = numbers[:5]           # [0, 1, 2, 3, 4]
all_items = numbers[:]          # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (複製)

# [start:stop:step] - 按步長
every_other = numbers[::2]      # [0, 2, 4, 6, 8]
every_third = numbers[::3]      # [0, 3, 6, 9]
from_two_step_two = numbers[2:8:2]  # [2, 4, 6]

# 負索引切片
last_three = numbers[-3:]       # [7, 8, 9]
all_but_last = numbers[:-1]     # [0, 1, 2, 3, 4, 5, 6, 7, 8]
second_to_last = numbers[-2:]   # [8, 9]

# 倒序
reversed_list = numbers[::-1]   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
reversed_every_other = numbers[::-2]  # [9, 7, 5, 3, 1]
```

### 字符串切片

```python
text = "Hello, World!"
#       012345678...  (正索引)

# 基本切片
greeting = text[0:5]      # "Hello"
world = text[7:12]        # "World"

# 常用操作
first_word = text[:5]     # "Hello"
second_word = text[7:]    # "World!"
every_other = text[::2]   # "Hlowrd"
reversed_text = text[::-1]  # "!dlroW ,olleH"
```

### 切片的可視化

```
列表：  [0]  [1]  [2]  [3]  [4]  [5]  [6]  [7]  [8]  [9]
         |    |    |    |    |    |    |    |    |    |

numbers[2:5]   選中 2, 3, 4 (從索引2, 在5前停止)
         ├────┼────┼────┤
         2    3    4    5

numbers[::2]   選中 0, 2, 4, 6, 8 (每隔一個)
         ├────+────┼────+────┼────+────┼────+────┼
         0    1    2    3    4    5    6    7    8    9

numbers[::-1]  反向選中所有元素
         ├─────────────────────────────────────→ (反向)
         0              ...                      9
```

---

## 進階概念

### 1. 使用變數作為索引

```python
items = ['a', 'b', 'c', 'd', 'e']

# 動態索引
index = 2
value = items[index]       # 'c'

# 索引運算
start = 1
length = 3
subset = items[start:start+length]  # ['b', 'c', 'd']

# 計算最後 N 個元素
n = 2
last_n = items[-n:]        # ['d', 'e']
```

### 2. 使用 slice() 物件

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 建立 slice 物件
s = slice(2, 5)            # start=2, stop=5
result = numbers[s]        # [2, 3, 4]

# 帶步長的 slice 物件
s_step = slice(0, 10, 2)   # start=0, stop=10, step=2
result = numbers[s_step]   # [0, 2, 4, 6, 8]

# 反向 slice
s_reverse = slice(None, None, -1)
result = numbers[s_reverse]  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# slice 物件的優點：方便重複使用
record = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
middle_section = record[s]  # [3, 4, 5]
```

### 3. 元組和列表的存取

```python
# 直接是二維結構
data = [
    ('Alice', 30, 'Taipei'),
    ('Bob', 25, 'NYC'),
    ('Charlie', 35, 'London')
]

# 存取特定記錄和欄位
first_person = data[0]      # ('Alice', 30, 'Taipei')
first_name = data[0][0]     # 'Alice'
first_age = data[0][1]      # 30

# 提取所有第一列（名字）
names = [record[0] for record in data]  # ['Alice', 'Bob', 'Charlie']

# 使用切片和索引組合
ages = [record[1] for record in data[:2]]  # [30, 25]（前兩人的年齡）
```

---

## 實際應用場景

### 1. 記錄字段存取（record[20:23]）

```python
# CSV 記錄可能是固定寬度格式
record = "GOOG  1034.57  87  100"
#         012345678...

# 使用切片提取字段
symbol = record[0:4]        # "GOOG"
price = record[6:12]        # "1034.5"
shares = record[14:16]      # "87"
cost = record[18:21]        # "100"

# 或使用 split() 分割
fields = record.split()     # ['GOOG', '1034.57', '87', '100']
symbol = fields[0]          # 'GOOG'
price = float(fields[1])    # 1034.57
```

### 2. 處理固定格式日期

```python
date_str = "2025-04-15"
#           0123456789

year = date_str[0:4]        # "2025"
month = date_str[5:7]       # "04"
day = date_str[8:10]        # "15"

# 或使用索引和切片組合
first_four = date_str[:4]   # "2025"
last_four = date_str[-4:]   # "0415"
```

### 3. 提取子序列（slice 物件）

```python
# 定義常用的切片
PRODUCT_NAME = slice(0, 10)     # 前 10 個字符
CATEGORY = slice(10, 15)        # 之後 5 個字符
PRICE = slice(15, 22)           # 之後 7 個字符

data = "Apple Phone   12900.99"
product = data[PRODUCT_NAME]    # "Apple Phone"
category = data[CATEGORY]       # ""
price = data[PRICE]             # "12900.9"
```

### 4. 建立倒序副本

```python
# 反轉列表
numbers = [1, 2, 3, 4, 5]
reversed_list = numbers[::-1]   # [5, 4, 3, 2, 1]

# 反轉字符串
text = "hello"
backward = text[::-1]           # "olleh"

# 檢查是否是迴文
word = "racecar"
is_palindrome = word == word[::-1]  # True
```

### 5. 提取列表的一部分

```python
items = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# 提取中間部分
middle = items[2:5]             # ['c', 'd', 'e']

# 提取非連續的元素
alternating = items[::2]        # ['a', 'c', 'e', 'g']

# 提取最後 N 個
last_three = items[-3:]         # ['e', 'f', 'g']

# 移除第一個和最後一個
without_edges = items[1:-1]     # ['b', 'c', 'd', 'e', 'f']
```

---

## 列表切片的可變性

```python
# 注意：切片返回新列表，不是引用
numbers = [1, 2, 3, 4, 5]
subset = numbers[1:4]           # [2, 3, 4] （新列表）

subset[0] = 20                   # 修改副本
print(numbers)                   # [1, 2, 3, 4, 5]（原列表不變）

# 修改原列表必須直接操作
numbers[1:4] = [20, 30, 40]      # 使用切片指定
print(numbers)                   # [1, 20, 30, 40, 5]
```

---

## 邊界情況

```python
items = [1, 2, 3, 4, 5]

# 索引超出範圍
# items[10]                       # ❌ IndexError

# 切片在範圍外不會報錯
items[10:20]                     # ✅ [] (空列表)
items[2:100]                     # ✅ [3, 4, 5] (只返回存在的部分)

# 反向切片
items[5:2]                       # [] (start > stop，沒有符合的元素)
items[5:2:-1]                    # [5, 4, 3] (反向時可以)

# 空切片
items[:]                         # [1, 2, 3, 4, 5] (複製整個列表)
items[2:2]                       # [] (start = stop，空結果)
items[100:200]                   # [] (兩個都超出範圍)
```

---

## 重要提示

⚠️ **常見錯誤與注意事項：**

1. **混淆包含和不包含**
   ```python
   items = ['a', 'b', 'c', 'd']
   subset = items[1:3]            # ✅ ['b', 'c'] (包含 1，不包含 3)
   # 記住：start 包含，stop 不包含
   ```

2. **忘記切片返回新物件**
   ```python
   original = [1, 2, 3]
   copy = original[:]             # ✅ 建立副本
   copy[0] = 999
   print(original)                # [1, 2, 3] 不變
   
   reference = original           # ❌ 只是引用
   reference[0] = 999
   print(original)                # [999, 2, 3] 被修改了
   ```

3. **步長為負時的方向相反**
   ```python
   nums = [1, 2, 3, 4, 5]
   # nums[4:1]                    # ❌ [] 空的（正向從 4 到 1 不可能）
   print(nums[4:1:-1])            # ✅ [5, 4, 3] 反向工作
   ```

4. **索引與切片的差異**
   ```python
   items = ['a', 'b', 'c']
   item = items[0]                # ✅ 'a' （單個元素）
   subset = items[0:1]            # ✅ ['a'] （列表）
   subset = items[0:2:1]          # ✅ ['a', 'b'] （列表）
   ```

5. **字符串是不可變的**
   ```python
   text = "hello"
   # text[0] = 'H'                # ❌ TypeError: 字符串不支持項目指定
   
   # ✅ 必須建立新字符串
   new_text = 'H' + text[1:]      # "Hello"
   new_text = text.replace('h', 'H')  # "Hello"
   ```
