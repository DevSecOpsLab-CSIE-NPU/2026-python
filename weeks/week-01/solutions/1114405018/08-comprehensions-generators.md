# 8 容器操作與推導式

## 概述

推導式（comprehensions）是 Python 中快速建立序列的語法糖。它們比傳統的迴圈方式更簡潔、更高效。你必須已經「不需要解釋」就能看懂以下推導式：

```python
# 列表推導式：過濾並轉換數據
[x for x in data if x > 0]

# 字典推導式：建立新字典
{k: v for k, v in d.items()}

# 生成器表達式：懶惰評估
(x * x for x in nums)
```

---

## 列表推導式（List Comprehension）

### 基本概念

列表推導式提供了一種簡潔的方式來建立列表。它比迴圈方式更可讀、更高效。

#### 基本語法

```python
# 基本形式
[expression for item in iterable]

# 帶條件
[expression for item in iterable if condition]

# 嵌套
[expression for item1 in iterable1 for item2 in iterable2]
```

### 簡單推導式

```python
# 等價的兩種方式

# 方式 1：傳統迴圈
squares = []
for x in range(5):
    squares.append(x ** 2)
# 結果：[0, 1, 4, 9, 16]

# 方式 2：列表推導式（更簡潔）
squares = [x ** 2 for x in range(5)]
# 結果：[0, 1, 4, 9, 16]

# 更多例子
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]           # [2, 4, 6, 8, 10]
as_strings = [str(x) for x in numbers]       # ['1', '2', '3', '4', '5']
lengths = [len(word) for word in ['a', 'bb', 'ccc']]  # [1, 2, 3]
```

### 帶條件的推導式

```python
# 過濾：只包含符合條件的元素

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 傳統方式
evens = []
for x in numbers:
    if x % 2 == 0:
        evens.append(x)
# 結果：[2, 4, 6, 8, 10]

# 推導式方式
evens = [x for x in numbers if x % 2 == 0]
# 結果：[2, 4, 6, 8, 10]

# 更多例子
larger_than_5 = [x for x in numbers if x > 5]  # [6, 7, 8, 9, 10]
positive_squares = [x**2 for x in [-2, -1, 0, 1, 2] if x > 0]  # [1, 4]

# 多個條件
result = [x for x in numbers if x > 3 if x < 8]  # [4, 5, 6, 7]
# 等同於 [x for x in numbers if x > 3 and x < 8]
```

### 嵌套推導式

```python
# 嵌套迴圈的推導式

# 傳統方式：建立 2 維列表
matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(i * 3 + j)
    matrix.append(row)
# 結果：[[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# 推導式方式
matrix = [[i * 3 + j for j in range(3)] for i in range(3)]
# 結果：[[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# 注意：外層迴圈是左邊第二個，內層是最右邊

# 展平列表
nested = [[1, 2, 3], [4, 5], [6, 7, 8]]

# 傳統方式
flat = []
for sublist in nested:
    for item in sublist:
        flat.append(item)
# 結果：[1, 2, 3, 4, 5, 6, 7, 8]

# 推導式方式
flat = [item for sublist in nested for item in sublist]
# 結果：[1, 2, 3, 4, 5, 6, 7, 8]

# 帶條件的嵌套
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 只提取大於 4 的元素
result = [x for row in matrix for x in row if x > 4]
# 結果：[5, 6, 7, 8, 9]
```

### 推導式與 if-else

```python
# 在推導式中使用 if-else

numbers = [1, 2, 3, 4, 5, 6]

# if-else：轉換每個元素
# 語法：[true_expr if condition else false_expr for item in iterable]
result = [x * 2 if x % 2 == 0 else x for x in numbers]
# 結果：[1, 4, 3, 8, 5, 12]
# 解釋：偶數 × 2，奇數不變

# 多個 if-elif-else
grades = [85, 92, 78, 88, 95, 72]
letter_grades = ['A' if x >= 90 else 'B' if x >= 80 else 'C' if x >= 70 else 'F' 
                 for x in grades]
# 結果：['B', 'A', 'C', 'B', 'A', 'F']
```

---

## 集合推導式（Set Comprehension）

### 基本概念

集合推導式的語法與列表推導式類似，但使用大括號 `{}` 並自動去除重複元素。

```python
# 基本語法
{expression for item in iterable}

# 帶條件
{expression for item in iterable if condition}
```

### 集合推導式例子

```python
# 建立集合：自動去除重複
numbers = [1, 2, 2, 3, 3, 3, 4]

# 傳統方式
unique = set()
for x in numbers:
    unique.add(x)
# 結果：{1, 2, 3, 4}

# 推導式方式
unique = {x for x in numbers}
# 結果：{1, 2, 3, 4}

# 平方後去重
squares = {x ** 2 for x in range(-3, 4)}
# 結果：{0, 1, 4, 9}（9 只出現一次，即使 (-3)² 和 3² 都是 9）

# 帶條件：只包含偶數的平方
even_squares = {x ** 2 for x in range(10) if x % 2 == 0}
# 結果：{0, 4, 16, 36, 64}

# 將字符串字符轉換成集合（去重）
unique_chars = {char for char in "hello"}
# 結果：{'h', 'e', 'l', 'o'}
```

---

## 字典推導式（Dictionary Comprehension）

### 基本概念

字典推導式用於快速建立字典。它需要同時指定鍵和值。

```python
# 基本語法
{key: value for item in iterable}

# 帶條件
{key: value for item in iterable if condition}
```

### 字典推導式例子

```python
# 建立數字到平方的映射
numbers = [1, 2, 3, 4, 5]

# 傳統方式
squares_dict = {}
for x in numbers:
    squares_dict[x] = x ** 2
# 結果：{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 推導式方式
squares_dict = {x: x ** 2 for x in numbers}
# 結果：{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 從現有字典建立新字典（變換值）
data = {'a': 1, 'b': 2, 'c': 3}
doubled = {k: v * 2 for k, v in data.items()}
# 結果：{'a': 2, 'b': 4, 'c': 6}

# 交換鍵和值
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
# 結果：{1: 'a', 2: 'b', 3: 'c'}

# 篩選字典元素
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
filtered = {k: v for k, v in data.items() if v > 2}
# 結果：{'c': 3, 'd': 4, 'e': 5}

# 列表轉字典
words = ['apple', 'banana', 'cherry']
word_lengths = {word: len(word) for word in words}
# 結果：{'apple': 5, 'banana': 6, 'cherry': 6}
```

### 字典推導式的進階用法

```python
# 從列表中建立字典
keys = ['name', 'age', 'city']
values = ['Alice', 30, 'Taipei']

# 方式 1：使用 zip
person = {k: v for k, v in zip(keys, values)}
# 結果：{'name': 'Alice', 'age': 30, 'city': 'Taipei'}

# 方式 2：同時變換鍵和值
numbers = [1, 2, 3, 4, 5]
result = {f"num_{x}": x ** 2 for x in numbers}
# 結果：{'num_1': 1, 'num_2': 4, 'num_3': 9, 'num_4': 16, 'num_5': 25}

# 建立預設字典（所有鍵都有相同的初始值）
keys = ['a', 'b', 'c']
default_dict = {k: 0 for k in keys}
# 結果：{'a': 0, 'b': 0, 'c': 0}
```

---

## 生成器表達式（Generator Expression）

### 基本概念

生成器表達式與列表推導式的語法幾乎相同，但使用圓括號 `()` 而不是方括號 `[]`。生成器使用**懶惰評估**，只在需要時生成值。

```python
# 基本語法
(expression for item in iterable)

# 帶條件
(expression for item in iterable if condition)
```

### 列表推導式 vs 生成器表達式

```python
# 列表推導式：一次性建立所有元素
list_comp = [x ** 2 for x in range(10)]
# 立即建立 10 個元素：[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 生成器表達式：按需生成元素
gen_exp = (x ** 2 for x in range(10))
# <generator object ...>（不會立即計算）

# 類型區別
print(type(list_comp))  # <class 'list'>
print(type(gen_exp))    # <class 'generator'>

# 記憶體佔用
# 列表推導式：建立完整列表，佔用更多記憶體
# 生成器表達式：按需生成，節省記憶體（特別是大數據）

# 多次遍歷
list_comp = [x ** 2 for x in range(5)]
for x in list_comp:
    print(x)  # ✅ 可以遍歷
for x in list_comp:
    print(x)  # ✅ 可以再次遍歷

gen_exp = (x ** 2 for x in range(5))
for x in gen_exp:
    print(x)  # ✅ 第一次遍歷
for x in gen_exp:
    print(x)  # ❌ 沒有輸出（生成器已耗盡）
```

### 生成器表達式的使用場景

```python
# 場景 1：與函式組合，節省記憶體
numbers = range(1000000)  # 100 萬個數字

# ❌ 不推薦：建立中間列表（佔用記憶體）
large_list = [x ** 2 for x in numbers if x % 2 == 0]  # 50 萬個元素的列表
result = sum(large_list)

# ✅ 推薦：使用生成器（節省記憶體）
gen = (x ** 2 for x in numbers if x % 2 == 0)  # 按需生成
result = sum(gen)

# 場景 2：使用 any() 和 all()
numbers = [1, 2, 3, 4, 5]

# 檢查是否有數字大於 3
has_large = any(x > 3 for x in numbers)  # True

# 檢查所有數字都小於 10
all_small = all(x < 10 for x in numbers)  # True

# 場景 3：與 map、filter 組合
words = ['apple', 'pie', 'zoo', 'a']

# 取得前 3 個單詞的長度（按需計算）
lengths = (len(word) for word in words[:3])
for length in lengths:
    print(length)  # 5、3、3

# 場景 4：建立無限序列
def infinite_numbers():
    i = 0
    while True:
        yield i
        i += 1

# 取前 5 個數字
first_five = [x for x in infinite_numbers() for _ in range(5) if x < 5]
# 注意：直接用列表推導式可能會無限迴圈
# 應該用 itertools.islice 或其他方式控制
```

---

## 使用 sum()、min()、max()、join() 與推導式

### 與 sum() 組合

```python
numbers = [1, 2, 3, 4, 5]

# 所有數字之和
total = sum(numbers)  # 15

# 所有數字平方之和
sum_of_squares = sum(x ** 2 for x in numbers)  # 55

# 條件求和
numbers = [1, 2, 3, 4, 5, 6]
sum_evens = sum(x for x in numbers if x % 2 == 0)  # 12（2+4+6）

# 購物車總價
items = [
    {'name': 'apple', 'price': 1.5, 'qty': 2},
    {'name': 'banana', 'price': 0.5, 'qty': 3},
    {'name': 'orange', 'price': 2.0, 'qty': 1}
]

total_cost = sum(item['price'] * item['qty'] for item in items)  # 6.5
```

### 與 min() 和 max() 組合

```python
numbers = [1, 2, 3, 4, 5]

# 所有數字的最小值
minimum = min(numbers)  # 1

# 所有數字平方的最小值
min_square = min(x ** 2 for x in numbers)  # 1

# 絕對值最小的數字
numbers = [-3, 1, -5, 2]
closest_to_zero = min(numbers, key=abs)  # 1

# 在複雜資料中找最小值
products = [
    {'name': 'apple', 'price': 1.5},
    {'name': 'banana', 'price': 0.5},
    {'name': 'orange', 'price': 2.0}
]

cheapest = min(products, key=lambda p: p['price'])
# {'name': 'banana', 'price': 0.5}

# 最小的 N 個元素
smallest_n = heapq.nsmallest(2, numbers, key=abs)
```

### 與 join() 組合

```python
# join() 連接序列中的字符串

# 簡單連接
words = ['hello', 'world']
result = ' '.join(words)  # 'hello world'

# 使用推導式轉換後連接
numbers = [1, 2, 3, 4, 5]
result = ','.join(str(x) for x in numbers)  # '1,2,3,4,5'

# 條件連接（只連接偶數）
result = ','.join(str(x) for x in numbers if x % 2 == 0)  # '2,4'

# 連接字典的值
data = {'a': 1, 'b': 2, 'c': 3}
result = ','.join(f"{k}={v}" for k, v in data.items())
# 'a=1,b=2,c=3'

# HTML 標籤生成
items = ['apple', 'banana', 'cherry']
html = '<ul>' + ''.join(f'<li>{item}</li>' for item in items) + '</ul>'
# '<ul><li>apple</li><li>banana</li><li>cherry</li></ul>'
```

---

## 實際應用場景

### 1. 過濾序列（1.16）

```python
# 從股票記錄中過濾價格大於 100 的股票
records = [
    {'symbol': 'GOOG', 'price': 150.25},
    {'symbol': 'MSFT', 'price': 85.50},
    {'symbol': 'AAPL', 'price': 185.30},
    {'symbol': 'TSLA', 'price': 245.60}
]

# 傳統方式
expensive = []
for record in records:
    if record['price'] > 100:
        expensive.append(record)

# 推導式方式
expensive = [r for r in records if r['price'] > 100]
# [{'symbol': 'GOOG', 'price': 150.25}, 
#  {'symbol': 'AAPL', 'price': 185.30}, 
#  {'symbol': 'TSLA', 'price': 245.60}]

# 只提取符號
symbols = [r['symbol'] for r in records if r['price'] > 100]
# ['GOOG', 'AAPL', 'TSLA']
```

### 2. 建立字典子集（1.17）

```python
# 從大字典中建立小字典

portfolio = {
    'GOOG': {'price': 150.25, 'shares': 10},
    'MSFT': {'price': 85.50, 'shares': 20},
    'AAPL': {'price': 185.30, 'shares': 5},
    'TSLA': {'price': 245.60, 'shares': 15}
}

# 方式 1：選擇特定的鍵
selected_keys = ['GOOG', 'AAPL']
subset = {k: portfolio[k] for k in selected_keys}
# {'GOOG': {...}, 'AAPL': {...}}

# 方式 2：過濾字典項目
expensive_portfolio = {k: v for k, v in portfolio.items() 
                       if v['price'] > 100}

# 方式 3：轉換字典值
shares_only = {k: v['shares'] for k, v in portfolio.items()}
# {'GOOG': 10, 'MSFT': 20, 'AAPL': 5, 'TSLA': 15}

# 方式 4：計算投資組合總值
total_value = {k: v['price'] * v['shares'] 
               for k, v in portfolio.items()}
# {'GOOG': 1502.5, 'MSFT': 1710, 'AAPL': 926.5, 'TSLA': 3684}
```

### 3. 使用 sum()、min()、join() 的實際例子

```python
# 計算投資組合統計

portfolio = [
    {'symbol': 'GOOG', 'price': 150.25, 'shares': 10},
    {'symbol': 'MSFT', 'price': 85.50, 'shares': 20},
    {'symbol': 'AAPL', 'price': 185.30, 'shares': 5}
]

# 總投資額
total = sum(item['price'] * item['shares'] for item in portfolio)
# 4751.5

# 最便宜的股票
cheapest = min(portfolio, key=lambda x: x['price'])
# {'symbol': 'MSFT', 'price': 85.50, 'shares': 20}

# 建立字符串報告
report = ' | '.join(f"{item['symbol']}: {item['price']:.2f}" 
                     for item in portfolio)
# 'GOOG: 150.25 | MSFT: 85.50 | AAPL: 185.30'

# 購買最多股票的
most_shares = max(portfolio, key=lambda x: x['shares'])
# {'symbol': 'MSFT', 'price': 85.50, 'shares': 20}
```

---

## 性能比較

```python
import timeit

# 測試：建立 100,000 個數字的平方

# 方式 1：列表推導式
def with_list_comp():
    return [x ** 2 for x in range(100000)]

# 方式 2：傳統迴圈
def with_loop():
    result = []
    for x in range(100000):
        result.append(x ** 2)
    return result

# 方式 3：map() 函式
def with_map():
    return list(map(lambda x: x ** 2, range(100000)))

# 時間測試
print(timeit.timeit(with_list_comp, number=10))  # 最快
print(timeit.timeit(with_loop, number=10))       # 較慢
print(timeit.timeit(with_map, number=10))        # 中等

# 結論：列表推導式通常是最快的
```

---

## 複雜推導式範例

```python
# 將嵌套列表扁平化並過濾
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 提取大於 4 的所有元素
flat_filtered = [x for row in matrix for x in row if x > 4]
# [5, 6, 7, 8, 9]

# 建立字典映射：位置 → 值
positioned = {(i, j): val 
              for i, row in enumerate(matrix) 
              for j, val in enumerate(row)}
# {(0, 0): 1, (0, 1): 2, ..., (2, 2): 9}

# 轉置矩陣
transposed = [[matrix[j][i] for j in range(len(matrix))] 
              for i in range(len(matrix[0]))]
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# 或使用 zip（更簡潔）
transposed = list(zip(*matrix))
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
```

---

## 重要提示

⚠️ **常見錯誤與注意事項：**

1. **圓括號 vs 方括號**
   ```python
   # 方括號：列表（建立列表）
   list_comp = [x ** 2 for x in range(5)]  # [0, 1, 4, 9, 16]
   
   # 圓括號：生成器（按需生成）
   gen_exp = (x ** 2 for x in range(5))    # <generator object>
   
   # 記住：( ) 是生成器，[ ] 是列表
   ```

2. **推導式中的變數作用域**
   ```python
   # ✅ 推導式變數有自己的作用域
   result = [x for x in range(3)]
   print(x)  # ❌ NameError: x 不存在（在 Python 3 中）
   
   # 在 Python 2 中，x 會洩露到外層作用域
   ```

3. **複雜的嵌套推導式可能難以閱讀**
   ```python
   # ❌ 難以理解
   result = [[x for x in row if x > 2] for row in matrix if any(x > 2 for x in row)]
   
   # ✅ 分解為多行
   filtered_matrix = [row for row in matrix if any(x > 2 for x in row)]
   result = [[x for x in row if x > 2] for row in filtered_matrix]
   ```

4. **生成器只能走一次**
   ```python
   gen = (x ** 2 for x in range(3))
   print(list(gen))  # [0, 1, 4]
   print(list(gen))  # []（已耗盡）
   
   # ✅ 需要重新建立
   gen = (x ** 2 for x in range(3))
   print(list(gen))  # [0, 1, 4]
   ```

5. **字典推導式中的鍵重複**
   ```python
   # ❌ 如果鍵重複，後面的值會覆蓋前面的
   data = [('a', 1), ('b', 2), ('a', 3)]
   result = {k: v for k, v in data}
   # {'a': 3, 'b': 2}  # 'a' 的值被覆蓋成 3
   
   # ✅ 需要特殊邏輯處理重複鍵
   from collections import defaultdict
   grouped = defaultdict(list)
   for k, v in data:
       grouped[k].append(v)
   # defaultdict(<class 'list'>, {'a': [1, 3], 'b': [2]})
   ```

6. **條件位置很重要**
   ```python
   numbers = [1, 2, 3, 4, 5]
   
   # ✅ 過濾：if 在最後
   filtered = [x for x in numbers if x > 2]  # [3, 4, 5]
   
   # ❌ 轉換：if-else 在 expression 中
   # wrong = [x if x > 2 for x in numbers]  # 語法錯誤
   
   # ✅ 轉換：if-else 是完整的 expression
   transformed = [x * 2 if x > 2 else x for x in numbers]  # [1, 2, 6, 8, 10]
   ```
