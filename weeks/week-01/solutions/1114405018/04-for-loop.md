# 4 for 迴圈

## 概述

for 迴圈是 Python 中最常用的控制流結構，用於**遍歷可迭代物件**（如列表、字符串、字典等）中的每個元素。你必須已經「不需要解釋」就能看懂以下基本語法：

```python
for x in items:
    # 做某事
    print(x)
```

---

## 基本概念

### for 迴圈的工作原理

for 迴圈會依次遍歷 `items` 中的每個元素，每次迭代時將該元素指定給變數 `x`。

```python
# 簡單例子
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)      # 依次輸出：apple、banana、cherry

# 讀取方式：
# 「對於 fruits 中的每個 fruit，執行迴圈體」
```

### for 迴圈的基本語法

```python
for 變數 in 可迭代物件:
    # 迴圈體（縮排的程式碼）
    # 每次迭代執行一次

# 迴圈後的程式碼（與迴圈體同級）
```

**重要提示：**
- 迴圈體必須**縮排**（通常 4 個空格）
- 可迭代物件必須是能遍歷的物件
- 變數在每次迭代時被重新指定

---

## 遍歷不同類型的物件

### 1. 遍歷列表

```python
# 基本列表遍歷
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(f"數字：{num}")

# 修改迴圈變數（不會影響原列表）
for num in numbers:
    num = num * 2      # 只改變迴圈變數，原列表不變
print(numbers)         # 仍然是 [1, 2, 3, 4, 5]

# 如果要修改列表中的元素，需要使用索引
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)         # 現在是 [2, 4, 6, 8, 10]
```

### 2. 遍歷字符串

```python
# 字符串也是可迭代的
text = "hello"
for char in text:
    print(char)        # 依次輸出：h、e、l、l、o

# 計數字符出現次數
word = "banana"
count = 0
for char in word:
    if char == 'a':
        count += 1
print(f"'a' 出現 {count} 次")  # 輸出：'a' 出現 3 次
```

### 3. 遍歷字典

```python
# 遍歷字典的鍵
person = {'name': 'Alice', 'age': 30, 'city': 'Taipei'}
for key in person:
    print(key)         # 依次輸出：name、age、city

# 或使用 .keys() 方法
for key in person.keys():
    print(key)

# 遍歷字典的值
for value in person.values():
    print(value)       # 依次輸出：Alice、30、Taipei

# 遍歷字典的鍵值對（最常用）
for key, value in person.items():
    print(f"{key}: {value}")
    # 輸出：name: Alice、age: 30、city: Taipei
```

### 4. 遍歷集合

```python
# 集合是無序的
colors = {'red', 'green', 'blue'}
for color in colors:
    print(color)       # 順序不確定（集合無序）

# 檢查集合中是否包含特定元素
for color in colors:
    if color == 'red':
        print("找到紅色！")
```

### 5. 遍歷元組

```python
# 元組的遍歷與列表相同
coordinates = [(1, 2), (3, 4), (5, 6)]
for x, y in coordinates:  # 直接解包元組
    print(f"座標:({x}, {y})")
    # 輸出：座標:(1, 2)、座標:(3, 4)、座標:(5, 6)
```

---

## 進階 for 迴圈技巧

### 1. 使用 range() 生成序列

```python
# range(end) - 從 0 到 end-1
for i in range(5):
    print(i)           # 輸出：0、1、2、3、4

# range(start, end) - 從 start 到 end-1
for i in range(2, 5):
    print(i)           # 輸出：2、3、4

# range(start, end, step) - 按步長遍歷
for i in range(0, 10, 2):
    print(i)           # 輸出：0、2、4、6、8

# 倒序遍歷
for i in range(5, 0, -1):
    print(i)           # 輸出：5、4、3、2、1
```

**應用場景：**
```python
# 使用索引遍歷列表
items = ['a', 'b', 'c', 'd']
for i in range(len(items)):
    print(f"索引 {i}: {items[i]}")
```

### 2. 使用 enumerate() 同時獲取索引和值

```python
# enumerate() 返回 (索引, 元素) 的元組
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
    # 輸出：0: apple、1: banana、2: cherry

# 從指定位置開始計數
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
    # 輸出：1. apple、2. banana、3. cherry
```

**應用場景：**
```python
# 列出菜單項目
menu = ['披薩', '漢堡', '沙拉']
for num, item in enumerate(menu, 1):
    print(f"{num}. {item}")
```

### 3. 使用 zip() 同時遍歷多個序列

```python
# zip() 將多個序列配對
names = ['Alice', 'Bob', 'Charlie']
scores = [95, 87, 92]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
    # 輸出：Alice: 95、Bob: 87、Charlie: 92

# 如果序列長度不同，zip() 會停在最短的序列
longer = [1, 2, 3, 4, 5]
shorter = ['a', 'b']
for num, letter in zip(longer, shorter):
    print(f"{num}, {letter}")
    # 輸出：1, a、2, b（3, 4, 5 被忽略）
```

**應用場景：**
```python
# 配對坐標
x_coords = [1, 2, 3]
y_coords = [10, 20, 30]
for x, y in zip(x_coords, y_coords):
    print(f"點：({x}, {y})")
```

### 4. break 和 continue 控制迴圈流程

```python
# break：提前結束迴圈
for i in range(10):
    if i == 5:
        break          # 當 i 等於 5 時結束迴圈
    print(i)           # 輸出：0、1、2、3、4

# continue：跳過本次迭代
for i in range(5):
    if i == 2:
        continue       # 跳過 i == 2 的情況
    print(i)           # 輸出：0、1、3、4

# 搜索列表中的元素
numbers = [2, 4, 6, 8, 10, 15, 20]
for num in numbers:
    if num % 2 != 0:   # 如果不是偶數
        break          # 停止搜索
    print(num)         # 輸出：2、4、6、8、10
```

### 5. 使用 else 子句

```python
# else 在迴圈正常結束（未 break）時執行
for i in range(3):
    print(i)
else:
    print("迴圈正常結束")  # 會被執行

# 搜索失敗的情況
search_list = [1, 3, 5, 7]
target = 4
for num in search_list:
    if num == target:
        print("找到了！")
        break
else:
    print(f"沒有找到 {target}")  # 會被執行，因為搜索失敗
```

---

## 列表推導式（List Comprehension）

列表推導式是建立列表的簡潔方式，本質上是 for 迴圈的簡化版本。

```python
# 傳統 for 迴圈
numbers = []
for i in range(5):
    numbers.append(i ** 2)
# 結果：[0, 1, 4, 9, 16]

# 列表推導式（更簡潔）
numbers = [i ** 2 for i in range(5)]
# 結果：[0, 1, 4, 9, 16]

# 帶條件的列表推導式
even_numbers = [i for i in range(10) if i % 2 == 0]
# 結果：[0, 2, 4, 6, 8]

# 嵌套列表推導式
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
# 結果：[[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

---

## 實際應用場景

### 1. dedupe（去除重複）

```python
# 方式 1：使用迴圈和列表
items = [1, 2, 2, 3, 3, 3, 4]
seen = []
for item in items:
    if item not in seen:  # 如果還沒看過
        seen.append(item)  # 就添加
print(seen)                # [1, 2, 3, 4]

# 方式 2：使用集合（更簡單）
unique = list(set(items))
```

### 2. Counter.update（計數更新）

```python
# 計算每個元素出現的次數
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
from collections import Counter

counter = Counter()
for word in words:
    counter[word] += 1

print(counter)  # Counter({'apple': 3, 'banana': 2, 'cherry': 1})

# 或直接使用 Counter 建構子
counter = Counter(words)
```

### 3. defaultdict 分組

```python
# 按第一個字母分組單詞
from collections import defaultdict

words = ['apple', 'apricot', 'banana', 'blueberry', 'cherry']
groups = defaultdict(list)

for word in words:
    first_letter = word[0]  # 獲取第一個字母
    groups[first_letter].append(word)

print(dict(groups))
# {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
```

### 4. groupby 迭代

```python
# 按條件分組
from itertools import groupby

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

for value, group in groupby(numbers):
    group_list = list(group)
    print(f"{value}: {group_list}")
    # 輸出：1: [1]、2: [2, 2]、3: [3, 3, 3]、4: [4, 4, 4, 4]
```

---

## 巢狀迴圈

```python
# 盤子裡有多種水果，每種水果有多個
fruits_inventory = {
    'apple': 3,
    'banana': 2,
    'cherry': 4
}

# 顯示每種水果的每一個
for fruit, count in fruits_inventory.items():
    for i in range(count):
        print(f"  {fruit}_{i+1}")
    # 輸出：apple_1、apple_2、apple_3、...

# 建立二維列表
matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(i * 3 + j)
    matrix.append(row)
# 結果：[[0, 1, 2], [3, 4, 5], [6, 7, 8]]
```

---

## 重要提示

⚠️ **常見錯誤與注意事項：**

1. **忘記縮排**
   ```python
   for i in range(3):
   print(i)           # ❌ 缺少縮排，IndentationError

   for i in range(3):
       print(i)       # ✅ 正確縮排
   ```

2. **修改迴圈變數不影響原容器**
   ```python
   items = [1, 2, 3]
   for item in items:
       item = item * 2  # ❌ 只改變迴圈變數，原列表不變

   # ✅ 正確做法：使用索引修改
   for i in range(len(items)):
       items[i] = items[i] * 2
   ```

3. **break 和 continue 的混淆**
   ```python
   for i in range(5):
       if i == 2:
           break      # 完全結束迴圈
       # continue     # 跳過本次迭代，繼續下一次
   ```

4. **zip() 不同長度的序列**
   ```python
   a = [1, 2, 3, 4]
   b = ['a', 'b']
   for x, y in zip(a, b):
       print(x, y)    # 輸出：1, a、2, b（3, 4 被省略）
   ```

5. **迴圈變數的作用域**
   ```python
   for i in range(5):
       name = f"item_{i}"

   print(i)           # ✅ 可以存取，i = 4
   print(name)        # ✅ 可以存取，name = "item_4"
                      # Python 中迴圈變數不建立新作用域
   ```
