# 2 基本資料型別

## 概述

你必須已經「不需要解釋」就能看懂以下基本資料型別：

```python
int, float, str, bool
```

## 四大基本資料型別詳解

### 1. **int（整數）**

整數是沒有小數點的數字，可以是正數、負數或零。

```python
# 整數的例子
age = 25              # 年齡：25 歲
score = -10           # 負數：-10 分
count = 0             # 零：0

# 整數型別轉換
shares = int("100")   # 將字串 "100" 轉換成整數 100
value = int(3.14)     # 將浮點數 3.14 轉換成整數 3（向下取整）
```

**特徵：**
- 可以進行數學運算（+, -, *, /, //, %, **）
- 沒有精度問題，適合計數和精確計算
- 支援非常大的數字（Python 沒有上限）

---

### 2. **float（浮點數）**

浮點數是含有小數點的數字，用於表示實數。

```python
# 浮點數的例子
price = 19.99         # 價格：19.99 元
temperature = -5.5    # 溫度：-5.5 度
pi = 3.14159          # 圓周率：3.14159

# 浮點數型別轉換
amount = float("99.5")   # 將字串 "99.5" 轉換成浮點數 99.5
rate = float(5)          # 將整數 5 轉換成浮點數 5.0
```

**特徵：**
- 包含小數點，用於非整數計算
- 有精度限制（通常 15-17 位有效數字）
- 不適合需要精確值的金融計算
- 可以使用科學記號表示：`1.5e-3` 等於 `0.0015`

---

### 3. **str（字串）**

字串是用引號（單引號或雙引號）括起來的文字字元序列。

```python
# 字串的例子
name = 'Alice'                    # 用單引號
message = "Hello, World!"         # 用雙引號
company = "ACME Corporation"      # 公司名稱

# 字串型別轉換
str_number = str(123)             # 將整數 123 轉換成字串 "123"
str_float = str(3.14)             # 將浮點數 3.14 轉換成字串 "3.14"
str_bool = str(True)              # 將布林值 True 轉換成字串 "True"

# 常用的字串操作
upper_case = name.upper()         # 轉換成大寫："ALICE"
lower_case = name.lower()         # 轉換成小寫："alice"
length = len(message)             # 字串長度：13
```

**特徵：**
- 用單引號、雙引號或三引號括起來
- 是不可變資料型別（修改字串時會建立新的字串）
- 支援索引和切片操作
- 可以使用 `+` 連接，使用 `*` 重複

---

### 4. **bool（布林值）**

布林值只有兩種值：`True` 和 `False`，用於邏輯判斷。

```python
# 布林值的例子
is_active = True       # 用戶是否在線：是
is_deleted = False     # 記錄是否被刪除：否
is_valid = True        # 資料是否有效：是

# 布林值型別轉換
bool_int = bool(1)     # 將整數 1 轉換成布林值 True
bool_zero = bool(0)    # 將整數 0 轉換成布林值 False
bool_str = bool("abc") # 將非空字串轉換成 True
bool_empty = bool("")  # 將空字串轉換成 False

# 布林值通常用在條件判斷
if is_active:
    print("用戶在線")   # 這會被執行
```

**特徵：**
- 只有 `True` 和 `False` 兩個值（注意大寫）
- 在Python中，`True` 等同於 `1`，`False` 等同於 `0`
- 用於 `if`, `while`, `and`, `or`, `not` 等邏輯操作
- 任何物件都可以轉換成布林值（空物件為 False，非空為 True）

---

## 用途（對應第一章範例）

### 例子 1：轉換 CSV 記錄中的股份數量
```python
# record 是一個字典，SHARES 是一個鍵
shares = int(record[SHARES])
# 說明：從 record 中取出 SHARES 對應的值（通常是字串 "100"）
#       然後轉換成整數型別，方便進行數學運算
```

### 例子 2：轉換 CSV 記錄中的價格
```python
# record 是一個字典，PRICE 是一個鍵
price = float(record[PRICE])
# 說明：從 record 中取出 PRICE 對應的值（通常是字串 "19.95"）
#       然後轉換成浮點數型別，用於精確的價格計算
```

### 例子 3：將序列中的元素轉換成字串並用逗號連接
```python
# s 是一個序列（列表或元組），包含整數或其他型別
result = ','.join(str(x) for x in s)
# 說明：
#   1. for x in s：迭代序列 s 中的每個元素 x
#   2. str(x)：將每個元素轉換成字串
#   3. ','.join(...)：用逗號連接所有字串
# 例子：s = [1, 2, 3]
#       結果：result = "1,2,3"
```

---

## 型別轉換速查表

| 轉換目標 | 方式 | 例子 | 結果 |
|---------|------|------|------|
| 轉成整數 | `int()` | `int("42")` | `42` |
|  | `int()` | `int(3.99)` | `3` |
| 轉成浮點數 | `float()` | `float("3.14")` | `3.14` |
|  | `float()` | `float(5)` | `5.0` |
| 轉成字串 | `str()` | `str(123)` | `"123"` |
|  | `str()` | `str(True)` | `"True"` |
| 轉成布林值 | `bool()` | `bool(1)` | `True` |
|  | `bool()` | `bool(0)` | `False` |

---

## 重要提示

⚠️ **常見錯誤與注意事項：**

1. **型別不匹配導致的錯誤**
   ```python
   # ❌ 錯誤：無法直接將包含字母的字串轉換成整數
   int("abc")  # ValueError: invalid literal for int()
   
   # ✅ 正確：確保字串包含有效的數字
   int("123")  # 成功：123
   ```

2. **浮點數精度問題**
   ```python
   # ⚠️ 浮點數計算可能有精度誤差
   0.1 + 0.2 == 0.3  # False（實際上是 False，因為浮點數精度限制）
   
   # ✅ 對金融應用，考慮使用 decimal 模組
   from decimal import Decimal
   ```

3. **布林值的真假判定**
   ```python
   # 以下值被視為 False：
   bool(0)      # False
   bool("")     # False
   bool([])     # False
   bool(None)   # False
   
   # 其他大部分值都被視為 True
   bool(1)      # True
   bool(-1)     # True
   bool("text") # True
   bool([1])    # True
   ```
