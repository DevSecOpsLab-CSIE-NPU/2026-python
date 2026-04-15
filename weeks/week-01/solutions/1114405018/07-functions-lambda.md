# 7 函式與 lambda

## 概述

函式是組織可重複使用程式碼的基礎。lambda 是建立簡短匿名函式的快速方式。你必須已經「不需要解釋」就能看懂以下三種基本函式語法：

```python
# 基本函式：接受一個參數，返回結果
def f(x):
    return x * 2

# 函式：帶預設參數
def f(a, b=0):
    return a + b

# lambda 函式：匿名函式，用於簡短操作
lambda x: x['price']
```

---

## 函式定義（Functions）

### 基本語法

函式使用 `def` 關鍵字定義，包含名稱、參數和函數體。

```python
def function_name(parameters):
    """文件字符串（可選）"""
    # 函式體
    return result  # 返回值（可選）
```

### 簡單函式

```python
# 最簡單的函式
def greet():
    print("Hello, World!")

greet()  # 輸出：Hello, World!

# 函式接受參數
def add(a, b):
    return a + b

result = add(3, 5)  # result = 8

# 函式接受多個參數
def describe(name, age, city):
    return f"{name} is {age} years old and lives in {city}"

info = describe("Alice", 30, "Taipei")  # "Alice is 30 years old and lives in Taipei"

# 函式沒有返回值時隱含返回 None
def no_return():
    x = 1 + 1
    # 沒有 return 語句

result = no_return()  # result = None
```

### 預設參數（Default Parameters）

使用預設參數讓某些參數可選。

```python
# 函式帶預設參數
def greet(name="World"):
    return f"Hello, {name}!"

print(greet())           # "Hello, World!"
print(greet("Alice"))    # "Hello, Alice!"

# 多個預設參數
def create_user(name, age=18, city="Unknown"):
    return {
        'name': name,
        'age': age,
        'city': city
    }

user1 = create_user("Bob")  # 使用預設年齡和城市
user2 = create_user("Alice", 30)  # 指定年齡，使用預設城市
user3 = create_user("Charlie", 25, "NYC")  # 全部指定

# ⚠️ 預設參數必須在非預設參數之後
# ❌ def bad_func(a=10, b):  # SyntaxError
# ✅ def good_func(a, b=10):  # 正確
```

### 可變參數（*args 和 **kwargs）

#### *args（非關鍵字可變參數）

```python
# *args 允許接受任意數量的位置參數
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))  # 15

# *args 本質上是元組
def print_args(*args):
    print(type(args))  # <class 'tuple'>
    for arg in args:
        print(arg)

print_args(1, 'hello', 3.14)  # 輸出 args 是元組，然後逐個打印參數

# 使用 *args 從列表/元組解包
def multiply(a, b, c):
    return a * b * c

numbers = [2, 3, 4]
result = multiply(*numbers)  # 解包為 multiply(2, 3, 4)
```

#### **kwargs（關鍵字可變參數）

```python
# **kwargs 允許接受任意數量的關鍵字參數
def create_dict(**kwargs):
    return kwargs

result = create_dict(name="Alice", age=30, city="Taipei")
print(result)  # {'name': 'Alice', 'age': 30, 'city': 'Taipei'}

# **kwargs 本質上是字典
def print_kwargs(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Bob", score=95)

# 使用 **kwargs 從字典解包
data = {'x': 10, 'y': 20}
def add(x, y):
    return x + y

result = add(**data)  # 解包為 add(x=10, y=20)
```

#### 組合使用

```python
# 標準參數 + *args + **kwargs
def flexible_func(a, b=5, *args, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")

flexible_func(1, 2, 3, 4, 5, name="Alice", age=30)
# 輸出：
# a=1, b=2
# args=(3, 4, 5)
# kwargs={'name': 'Alice', 'age': 30}

# 參數順序很重要：位置 → 預設 → *args → **kwargs
def correct_order(x, y=0, *args, **kwargs):
    pass

# ❌ 錯誤的順序（會報錯）
# def wrong_order(*args, y=0, x):
#     pass
```

### 返回多個值

```python
# 函式可以返回多個值（實際是返回元組）
def get_coordinates():
    return 10, 20  # 返回 (10, 20)

x, y = get_coordinates()  # 自動解包
print(x, y)  # 10 20

# 返回多個值用於交換
def swap(a, b):
    return b, a

x, y = 1, 2
x, y = swap(x, y)
print(x, y)  # 2 1

# 命名返回值讓程式碼更清晰
def get_user_info():
    name = "Alice"
    age = 30
    email = "alice@example.com"
    return name, age, email  # 返回元組

name, age, email = get_user_info()
```

---

## Lambda 函式

### 基本概念

Lambda 是建立**匿名函式**（沒有名稱的函式）的快速方式。適合用於簡短的、一次性的函式。

```python
# lambda 語法
# lambda 參數: 返回值表達式

# 最簡單的 lambda
square = lambda x: x ** 2
print(square(5))  # 25

# 多個參數
add = lambda x, y: x + y
print(add(3, 5))  # 8

# 複雜一點的邏輯
max_of_three = lambda a, b, c: max([a, b, c])
print(max_of_three(3, 7, 2))  # 7
```

### Lambda vs 普通函式

```python
# 這兩種方式等價

# 方式 1：普通函式
def double(x):
    return x * 2

# 方式 2：lambda 函式
double = lambda x: x * 2

# 兩者效果相同
print(double(5))  # 10

# Lambda 適合簡短操作，但複雜邏輯應該用 def
# ✅ 好的 lambda：單行邏輯
increment = lambda x: x + 1

# ❌ 不推薦用 lambda：複雜邏輯
# process = lambda x: (x * 2 if x > 0 else -x, x ** 2, ... 很多東西 ...)

# ✅ 複雜邏輯應該用 def
def process(x):
    if x > 0:
        result1 = x * 2
    else:
        result1 = -x
    result2 = x ** 2
    # ... 其他邏輯
    return result1, result2
```

### Lambda 常用場景：與高階函式組合

```python
# Lambda 最常用於高階函式（接受函式作為參數的函式）

# 場景 1：使用 map() 轉換元素
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# 場景 2：使用 filter() 篩選元素
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# 場景 3：使用 sorted() 的 key 參數排序
students = [
    {'name': 'Alice', 'score': 95},
    {'name': 'Bob', 'score': 87},
    {'name': 'Charlie', 'score': 92}
]

# 按分數排序
sorted_by_score = sorted(students, key=lambda s: s['score'])
print(sorted_by_score)
# [{'name': 'Bob', 'score': 87}, {'name': 'Charlie', 'score': 92}, {'name': 'Alice', 'score': 95}]

# 場景 4：使用 sorted() 倒序排序
# 低分到高分
ascending = sorted(numbers, key=lambda x: x)
# 高分到低分
descending = sorted(numbers, key=lambda x: x, reverse=True)
```

---

## 高階函式（Higher-Order Functions）

高階函式是接受函式作為參數或返回函式的函式。

### 1. map()

```python
# map 將函式應用於序列的每個元素
numbers = [1, 2, 3, 4, 5]

# 使用 lambda
doubled = list(map(lambda x: x * 2, numbers))
# [2, 4, 6, 8, 10]

# 使用普通函式
def square(x):
    return x ** 2

squared = list(map(square, numbers))
# [1, 4, 9, 16, 25]

# map 也可以用於多個序列
a = [1, 2, 3]
b = [10, 20, 30]
results = list(map(lambda x, y: x + y, a, b))
# [11, 22, 33]
```

### 2. filter()

```python
# filter 保留序列中符合條件的元素
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 篩選偶數
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6, 8, 10]

# 篩選大於 5 的數字
greater_than_five = list(filter(lambda x: x > 5, numbers))
# [6, 7, 8, 9, 10]

# 使用普通函式
def is_positive(x):
    return x > 0

numbers_with_negative = [-2, -1, 0, 1, 2, 3]
positives = list(filter(is_positive, numbers_with_negative))
# [1, 2, 3]
```

### 3. sorted() 的 key 參數

```python
# sorted 的 key 參數指定排序的依據

# 按字符串長度排序
words = ["apple", "pie", "zoo", "a"]
by_length = sorted(words, key=lambda w: len(w))
# ['a', 'pie', 'zoo', 'apple']

# 按字典的特定鍵排序
records = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

by_age = sorted(records, key=lambda r: r['age'])
# [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]

# 倒序排序
by_age_desc = sorted(records, key=lambda r: r['age'], reverse=True)

# 複合排序（先按年齡，再按名字字母順序）
by_age_then_name = sorted(records, key=lambda r: (r['age'], r['name']))

# 按絕對值排序
numbers = [-3, 1, -5, 2, -1]
by_abs = sorted(numbers, key=lambda x: abs(x))
# [1, -1, 2, -3, -5]
```

### 4. min() 和 max() 的 key 參數

```python
# 使用 key 參數找最小/最大元素

# 按絕對值找最小的
numbers = [-3, 1, -5, 2, -1]
smallest_abs = min(numbers, key=lambda x: abs(x))
# 1

# 找最長的單詞
words = ["apple", "pie", "zoo"]
longest = max(words, key=lambda w: len(w))
# "apple"

# 按字典的特定鍵找
records = [
    {'name': 'Alice', 'score': 95},
    {'name': 'Bob', 'score': 87},
    {'name': 'Charlie', 'score': 92}
]

highest_score = max(records, key=lambda r: r['score'])
# {'name': 'Alice', 'score': 95}

lowest_score = min(records, key=lambda r: r['score'])
# {'name': 'Bob', 'score': 87}
```

### 5. heapq.nsmallest() 和 heapq.nlargest()

```python
import heapq

# 找最小的 N 個元素
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
three_smallest = heapq.nsmallest(3, numbers)
# [1, 1, 2]

three_largest = heapq.nlargest(3, numbers)
# [9, 6, 5]

# 使用 key 參數進行複雜排序
records = [
    {'name': 'Alice', 'score': 95},
    {'name': 'Bob', 'score': 87},
    {'name': 'Charlie', 'score': 92},
    {'name': 'David', 'score': 88}
]

top_2_scores = heapq.nlargest(2, records, key=lambda r: r['score'])
# [{'name': 'Alice', 'score': 95}, {'name': 'Charlie', 'score': 92}]

bottom_2_scores = heapq.nsmallest(2, records, key=lambda r: r['score'])
# [{'name': 'Bob', 'score': 87}, {'name': 'David', 'score': 88}]
```

---

## 函式作為參數傳遞

```python
# 函式可以作為參數傳遞給其他函式

def apply_operation(x, y, operation):
    """執行操作並返回結果"""
    return operation(x, y)

# 使用不同的函式
result1 = apply_operation(5, 3, lambda a, b: a + b)  # 8
result2 = apply_operation(5, 3, lambda a, b: a - b)  # 2
result3 = apply_operation(5, 3, lambda a, b: a * b)  # 15

# 或使用已定義的函式
def power(a, b):
    return a ** b

result4 = apply_operation(2, 3, power)  # 8
```

---

## 實際應用場景

### 1. drop_first_last（移除首尾元素）

```python
# 常見需求：移除序列的第一個和最後一個元素
def drop_first_last(items):
    return items[1:-1]

# 或使用 lambda
drop_ends = lambda items: items[1:-1]

data = [1, 2, 3, 4, 5]
print(drop_first_last(data))  # [2, 3, 4]
print(drop_ends(data))         # [2, 3, 4]
```

### 2. is_int（檢查是否為整數）

```python
# 檢查一個值是否是整數（排除布林值）
def is_int(value):
    return isinstance(value, int) and not isinstance(value, bool)

# 或使用 lambda
is_int = lambda value: isinstance(value, int) and not isinstance(value, bool)

print(is_int(5))       # True
print(is_int(5.0))     # False
print(is_int(True))    # False（True 是 bool，不是 int）
print(is_int("5"))     # False
```

### 3. sorted() 的 key 參數

```python
# 股票記錄
records = [
    {'symbol': 'GOOG', 'price': 150.25, 'shares': 100},
    {'symbol': 'MSFT', 'price': 310.50, 'shares': 50},
    {'symbol': 'AAPL', 'price': 185.30, 'shares': 200}
]

# 按價格排序
by_price = sorted(records, key=lambda r: r['price'])

# 按股份數排序
by_shares = sorted(records, key=lambda r: r['shares'], reverse=True)

# 按總價值排序（價格 × 股份數）
by_value = sorted(records, key=lambda r: r['price'] * r['shares'])
```

### 4. heapq.nsmallest() 的 key 參數

```python
import heapq

# 找股價最低的 3 檔股票
records = [
    {'symbol': 'GOOG', 'price': 150.25},
    {'symbol': 'MSFT', 'price': 310.50},
    {'symbol': 'AAPL', 'price': 185.30},
    {'symbol': 'TSLA', 'price': 245.60}
]

cheapest_3 = heapq.nsmallest(3, records, key=lambda r: r['price'])
# [{'symbol': 'GOOG', 'price': 150.25}, 
#  {'symbol': 'AAPL', 'price': 185.30}, 
#  {'symbol': 'TSLA', 'price': 245.60}]
```

### 5. min() 的 key 參數

```python
# 在股票記錄中找價格最低的
records = [
    {'symbol': 'GOOG', 'price': 150.25},
    {'symbol': 'MSFT', 'price': 310.50},
    {'symbol': 'AAPL', 'price': 185.30}
]

cheapest = min(records, key=lambda r: r['price'])
# {'symbol': 'GOOG', 'price': 150.25}

# 字符串最短的記錄
data = ['apple', 'pie', 'zoo']
shortest = min(data, key=len)
# 'pie'
```

---

## 組合高階函式

```python
# 將多個高階函式組合使用

records = [
    {'name': 'Alice', 'age': 30, 'salary': 60000},
    {'name': 'Bob', 'age': 25, 'salary': 50000},
    {'name': 'Charlie', 'age': 35, 'salary': 80000},
    {'name': 'David', 'age': 28, 'salary': 55000}
]

# 例子 1：找薪水大於 55000 的員工，並按名字排序
result = sorted(
    filter(lambda r: r['salary'] > 55000, records),
    key=lambda r: r['name']
)

# 例子 2：計算每個員工的年收入，然後找最高的
salaries_with_bonus = list(map(lambda r: {**r, 'annual': r['salary'] * 12}, records))
highest_annual = max(salaries_with_bonus, key=lambda r: r['annual'])

# 例子 3：用列表推導式代替（通常更清晰）
high_earners = [r for r in records if r['salary'] > 55000]
sorted_by_name = sorted(high_earners, key=lambda r: r['name'])
```

---

## 函式的文件字符串（Docstring）

```python
# 好的實踐：為函式添加文件字符串
def calculate_total(price, quantity, tax_rate=0.1):
    """
    計算商品的總價格，包括稅金。
    
    參數：
        price (float)：商品單價
        quantity (int)：購買數量
        tax_rate (float)：稅率，預設 0.1（10%）
    
    返回：
        float：包括稅金的總價格
    
    例子：
        >>> calculate_total(100, 2, 0.1)
        220.0
        >>> calculate_total(50, 3)
        165.0
    """
    subtotal = price * quantity
    tax = subtotal * tax_rate
    return subtotal + tax

# 使用 help() 查看文件字符串
help(calculate_total)
```

---

## 重要提示

⚠️ **常見錯誤與注意事項：**

1. **Lambda 的局限性**
   ```python
   # ❌ Lambda 只能包含單個表達式，不能有多行邏輯
   # process = lambda x: (result = x * 2; print(result))  # 語法錯誤
   
   # ✅ 複雜邏輯應使用 def
   def process(x):
       result = x * 2
       print(result)
       return result
   ```

2. **Lambda 中的變數作用域**
   ```python
   # ❌ Lambda 會捕獲外層變數的引用（不是值）
   functions = []
   for i in range(3):
       functions.append(lambda x: x + i)  # 所有 lambda 都引用最後的 i
   
   print(functions[0](10))  # 12（期待 10，但 i=2）
   print(functions[1](10))  # 12
   print(functions[2](10))  # 12
   
   # ✅ 使用預設參數修正
   functions = []
   for i in range(3):
       functions.append(lambda x, i=i: x + i)  # 固定 i 的值
   
   print(functions[0](10))  # 10
   print(functions[1](10))  # 11
   print(functions[2](10))  # 12
   ```

3. **忘記 key 參數返回的是單一值**
   ```python
   data = ['apple', 'pie', 'zoo', 'a']
   
   # ✅ 正確：key 返回用於排序的單一值
   sorted_by_length = sorted(data, key=len)
   sorted_by_length = sorted(data, key=lambda x: len(x))
   
   # ❌ 錯誤：不要在 key 中返回元組進行排序（除非有特殊需要）
   # 如果想按多個準則排序，請返回元組
   sorted_by_criteria = sorted(data, key=lambda x: (len(x), x))  # 先按長度，再按字母順序
   ```

4. **預設參數的可變物件陷阱**
   ```python
   # ❌ 危險：可變物件作為預設參數
   def append_to(element, to=[]):
       to.append(element)
       return to
   
   list1 = append_to(1)
   list2 = append_to(2)
   print(list1)  # [1, 2]（期待 [1]）
   print(list2)  # [1, 2]（期待 [2]）
   # 問題：所有呼叫共享同一個預設列表
   
   # ✅ 正確做法：使用 None 作為預設值
   def append_to(element, to=None):
       if to is None:
           to = []
       to.append(element)
       return to
   ```

5. **參數順序很重要**
   ```python
   # ✅ 正確的參數順序
   def func(a, b=5, *args, **kwargs):
       pass
   
   # ❌ 錯誤的參數順序（會報 SyntaxError）
   # def func(a, *args, b=5, **kwargs):
   #     pass
   
   # ✅ 如果使用 * 而不是 *args，之後的參數必須用關鍵字指定
   def func(a, *, b=5, **kwargs):
       pass
   
   func(1, b=10, x=20)  # ✅ 正確
   # func(1, 10, x=20)   # ❌ 錯誤：b 必須用關鍵字指定
   ```
