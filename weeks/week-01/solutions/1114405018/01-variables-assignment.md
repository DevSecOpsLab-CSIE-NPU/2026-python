# 1 變數與指定（assignment）

## 概述

變數與指定是 Python 程式設計的基礎。你必須已經「不需要解釋」就能看懂以下程式碼：

```python
x = 10              # 將整數 10 指定給變數 x
name = 'ACME'       # 將字串 'ACME' 指定給變數 name
```

---

## 基本概念

### 什麼是變數？

變數是用來存儲值的容器。可以把它想象成有標籤的盒子，盒子裡存放著資料。

```python
# 基本變數指定語法：變數名 = 值
age = 25            # 將數字 25 存儲在變數 age 中
city = "Taipei"     # 將字串 "Taipei" 存儲在變數 city 中
is_student = True   # 將布林值 True 存儲在變數 is_student 中
```

### 什麼是指定（assignment）？

指定是使用 `=` 運算子將值存儲到變數中。注意：`=` 不是「等於」，而是「指定」。

```python
# 指定運算子的工作方式
x = 10              # 讀取：「將 10 指定給 x」
y = x + 5           # 讀取：「將 x+5 的結果指定給 y」（y = 15）
```

---

## 進階概念

### 1. 多重指定（Multiple Assignment）

同時將多個值指定給多個變數。

```python
# 方式 1：使用逗號分隔
a, b = 3, 5
# 說明：將 3 指定給 a，將 5 指定給 b

# 方式 2：使用多行寫法（更清晰）
x = 10
y = 20
z = 30

# 方式 3：連鎖指定（同一個值指定給多個變數）
a = b = c = 0
# 說明：a、b、c 都被指定為 0
```

**應用場景：**
```python
# 初始化多個相關變數
width, height = 800, 600  # 設定視窗大小

# 在迴圈中同時指定
for i in range(3):
    x, y = i, i*2  # 每次迴圈指定不同的 x 和 y
```

---

### 2. 解包（Unpacking）

從一個序列（如列表、元組、字串）中提取多個值，並分別指定給不同的變數。

```python
# 解包元組
point = (4, 9)      # 這是一個含有兩個元素的元組
x, y = point        # 解包：x = 4，y = 9
# 說明：point 中的第一個值 (4) 給 x，第二個值 (9) 給 y

# 解包列表
colors = ['red', 'green', 'blue']
first, second, third = colors
# 說明：first = 'red'，second = 'green'，third = 'blue'

# 解包字串
a, b, c = 'xyz'
# 說明：a = 'x'，b = 'y'，c = 'z'

# 使用星號 (*) 進行部分解包
first, *rest = [1, 2, 3, 4, 5]
# 說明：first = 1，rest = [2, 3, 4, 5]

first, *middle, last = [1, 2, 3, 4, 5]
# 說明：first = 1，middle = [2, 3, 4]，last = 5
```

**應用場景：**
```python
# 交換兩個變數的值（不需要臨時變數）
a, b = 5, 10
a, b = b, a  # 現在 a = 10，b = 5

# 從元組中提取特定值
user_data = ('Alice', 30, 'alice@example.com')
name, age, email = user_data
```

---

### 3. 函式回傳值接收（Receiving Function Return Values）

函式可以回傳一個值或多個值，我們使用變數接收這些值。

```python
# 定義一個回傳單一值的函式
def get_count():
    return 42

count = get_count()  # 接收函式的回傳值
# 說明：count = 42

# 定義一個回傳多個值的函式（實際上是回傳元組）
def get_point():
    return 4, 9      # Python 會自動將 4, 9 打包成 (4, 9)

# 方式 1：接收為元組
point = get_point()  # point = (4, 9)

# 方式 2：直接解包（推薦）
px, py = get_point()  # px = 4，py = 9
# 說明：函式回傳 (4, 9)，直接解包給 px 和 py

# 更常見的例子
def get_user_info():
    return 'Alice', 30, 'Taipei'  # 回傳三個值

name, age, city = get_user_info()
# 說明：name = 'Alice'，age = 30，city = 'Taipei'
```

**應用場景：**
```python
# 獲取字串的分割結果
text = "apple,banana,cherry"
fruit1, fruit2, fruit3 = text.split(',')
# 說明：字串.split() 回傳列表，我們直接解包

# 獲取字典的鍵值對
data = {'name': 'Bob'}
for key, value in data.items():  # items() 回傳 (鍵, 值) 的元組
    print(f"{key}: {value}")
```

---

## 用途（對應第一章範例）

### 例子 1：解包座標
```python
# 假設 p 是一個座標點 (4, 9)
x, y = p
# 說明：將元組 p 中的兩個值分別指定給 x 和 y
```

### 例子 2：多重指定
```python
# 同時指定多個值
a, b, c = 1, 2, 3
# 說明：a = 1，b = 2，c = 3

# 也可以交換值
temp = a
a = b
b = temp
# Python 中更簡潔的做法：a, b = b, a
```

### 例子 3：函式回傳值接收
```python
def get_point():
    return 4, 9

# 接收並解包函式的回傳值
px, py = get_point()
# 說明：get_point() 回傳 (4, 9)，px = 4，py = 9
```

---

## 常見用法與技巧

### 忽略某些值

使用底線 `_` 來忽略不需要的值：

```python
# 只需要第一個和最後一個值
first, _, _, _, last = [1, 2, 3, 4, 5]
# 說明：first = 1，last = 5，中間的值被忽略

# 也可以使用星號忽略多個值
first, *_, last = [1, 2, 3, 4, 5]
# 說明：first = 1，last = 5，*_ 忽略中間的所有值
```

### 解包嵌套結構

```python
# 解包嵌套元組
(x, y), (a, b) = ((1, 2), (3, 4))
# 說明：x = 1，y = 2，a = 3，b = 4

# 列表中的字典
records = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25}
]
for name, age in [(r['name'], r['age']) for r in records]:
    print(f"{name}: {age}")
```

### 重新指定

變數可以被多次指定不同的值：

```python
x = 10           # 第一次指定
x = 20           # 重新指定（原值被覆寫）
x = x + 5        # 使用舊值進行重新指定（x = 25）

# 使用增量運算子簡化
x += 5           # 等同於 x = x + 5
x -= 3           # 等同於 x = x - 3
x *= 2           # 等同於 x = x * 2
```

---

## 重要提示

⚠️ **常見的新手錯誤：**

1. **混淆 = 和 ==**
   ```python
   x = 10           # 指定：將 10 指定給 x
   if x == 10:      # 比較：檢查 x 是否等於 10
       print("相等")
   ```

2. **解包數量不匹配**
   ```python
   a, b = [1, 2, 3]  # ❌ 錯誤：3 個值無法指定給 2 個變數
   a, b, c = [1, 2]  # ❌ 錯誤：2 個值無法指定給 3 個變數
   
   # ✅ 正確的做法
   a, b, c = [1, 2, 3]  # 正確
   a, *rest = [1, 2, 3]  # 使用星號
   ```

3. **變數名稱的命名規則**
   ```python
   x = 10              # ✅ 可以（簡單變數）
   user_name = "Bob"   # ✅ 可以（蛇形命名法）
   _private = 100      # ✅ 可以（慣例表示私有）
   
   # ❌ 不可以的命名
   2x = 10             # 不能以數字開頭
   user-name = "Bob"   # 不能使用連字符
   my name = "Bob"     # 不能有空格
   ```
