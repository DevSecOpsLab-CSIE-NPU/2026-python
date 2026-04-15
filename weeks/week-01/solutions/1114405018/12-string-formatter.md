# 12 Python 字串格式化（string formatter）

## 概述

字串格式化是把「資料」轉成「可讀文字」的關鍵能力。你會在報表輸出、CLI 顯示、例外訊息、除錯 log、表格列印中大量使用。

你必須已經「不需要解釋」就能看懂：

```python
name = 'ACME'
price = 91.1

# f-string（推薦）
text = f'{name} price = {price:.2f}'

# format 方法
text2 = '{} price = {:.2f}'.format(name, price)
```

---

## 三種常見字串格式化方式

### 1. f-string（推薦）

```python
name = 'Alice'
score = 95.678

msg = f'學生 {name} 的分數是 {score:.2f}'
print(msg)  # 學生 Alice 的分數是 95.68
```

特點：

1. 可讀性高，語法直覺。
2. 支援在 `{}` 內直接放表達式。
3. Python 3.6+ 可用，現代 Python 首選。

### 2. `str.format()`

```python
name = 'Alice'
score = 95.678

msg = '學生 {} 的分數是 {:.2f}'.format(name, score)
print(msg)  # 學生 Alice 的分數是 95.68
```

特點：

1. 相容舊版 Python。
2. 可使用位置或名稱參數。
3. 對複雜模板有時仍實用。

### 3. `%` 舊式格式化（了解即可）

```python
name = 'Alice'
score = 95.678

msg = '學生 %s 的分數是 %.2f' % (name, score)
print(msg)  # 學生 Alice 的分數是 95.68
```

特點：

1. 舊程式常見。
2. 新專案通常不再優先使用。

---

## f-string 詳解

### 基本語法

```python
user = 'Nina'
age = 20

print(f'使用者：{user}，年齡：{age}')
```

### 在 `{}` 內放運算式

```python
a = 10
b = 3

print(f'{a} + {b} = {a + b}')      # 10 + 3 = 13
print(f'{a} / {b} = {a / b:.2f}')  # 10 / 3 = 3.33
```

### 呼叫方法與屬性

```python
name = 'alice'
items = [1, 2, 3]

print(f'大寫：{name.upper()}')
print(f'項目數量：{len(items)}')
```

### 除錯格式（Python 3.8+）

```python
x = 42
y = 3.14

print(f'{x=}, {y=}')
# 輸出：x=42, y=3.14
```

這在除錯時非常方便，能同時看到變數名稱與值。

---

## format spec（格式規格）

格式規格放在冒號 `:` 後面，例如 `{value:.2f}`。

```python
price = 91.1
print(f'{price:.2f}')  # 91.10
```

### 常見數值格式

```python
n = 1234.5678

print(f'{n:.2f}')   # 1234.57（小數 2 位）
print(f'{n:.0f}')   # 1235（四捨五入到整數）
print(f'{n:,.2f}')  # 1,234.57（千分位）
print(f'{n:.2e}')   # 1.23e+03（科學記號）
print(f'{n:.1%}')   # 123456.8%（乘以 100 後加 %）
```

### 整數進位表示

```python
num = 42

print(f'{num:d}')  # 42（十進位）
print(f'{num:b}')  # 101010（二進位）
print(f'{num:o}')  # 52（八進位）
print(f'{num:x}')  # 2a（十六進位，小寫）
print(f'{num:X}')  # 2A（十六進位，大寫）
```

### 寬度、對齊、填充

```python
word = 'cat'

print(f'|{word:<10}|')   # 靠左
print(f'|{word:>10}|')   # 靠右
print(f'|{word:^10}|')   # 置中
print(f'|{word:*^10}|')  # 用 * 填充後置中
```

輸出示意：

```text
|cat       |
|       cat|
|   cat    |
|***cat****|
```

### 正負號顯示

```python
pos = 12
neg = -12

print(f'{pos:+d}')  # +12
print(f'{neg:+d}')  # -12
print(f'{pos: d}')  #  12（正數前空白）
```

---

## `str.format()` 詳解

### 位置參數

```python
template = 'Name: {}, Age: {}'
text = template.format('Alice', 20)
print(text)
```

### 編號位置

```python
template = '{1} 比 {0} 大'
text = template.format(3, 5)
print(text)  # 5 比 3 大
```

### 關鍵字參數

```python
template = 'Name: {name}, Score: {score:.1f}'
text = template.format(name='Bob', score=88.66)
print(text)  # Name: Bob, Score: 88.7
```

### 從字典取值

```python
data = {'name': 'Nina', 'city': 'Taipei'}
text = '姓名：{name}，城市：{city}'.format(**data)
print(text)
```

---

## 百分比格式化與比率顯示

### 以小數表示比例

```python
ratio = 0.87654
print(f'{ratio:.2%}')  # 87.65%
```

### 常見業務情境

```python
passed = 87
total = 100
pass_rate = passed / total

print(f'通過率：{pass_rate:.1%}')  # 通過率：87.0%
```

---

## 日期時間格式化

```python
from datetime import datetime

now = datetime(2026, 4, 15, 14, 30, 5)

print(f'{now:%Y-%m-%d}')          # 2026-04-15
print(f'{now:%H:%M:%S}')          # 14:30:05
print(f'{now:%Y/%m/%d %H:%M}')    # 2026/04/15 14:30
```

常見代碼：

1. `%Y` 四位年份
2. `%m` 月份（01-12）
3. `%d` 日期（01-31）
4. `%H` 小時（24hr）
5. `%M` 分鐘
6. `%S` 秒

---

## 輸出對齊（表格報表）

```python
rows = [
	('apple', 3, 1.2),
	('banana', 12, 0.5),
	('cherry', 25, 2.35),
]

print(f"{'品名':<10}{'數量':>6}{'單價':>10}")
print('-' * 26)
for name, qty, price in rows:
	print(f'{name:<10}{qty:>6d}{price:>10.2f}')
```

輸出示意：

```text
品名            數量      單價
--------------------------
apple            3      1.20
banana          12      0.50
cherry          25      2.35
```

---

## 字串格式化與除錯訊息

### 例外訊息

```python
value = 'abc'
try:
	n = int(value)
except ValueError as e:
	print(f'轉換失敗：value={value!r}, error={e}')
```

### `!r`、`!s`、`!a` 轉換旗標

```python
text = '你好\nPython'

print(f'!s -> {text!s}')
print(f'!r -> {text!r}')
```

`!r` 常用於除錯，會顯示較完整、可重建的字串表示。

---

## 常見錯誤與注意事項

1. 忘記加 `f`

```python
name = 'Alice'

# ❌
print('{name}')

# ✅
print(f'{name}')
```

2. 大括號顯示問題

```python
# 想輸出字面的大括號，需要雙寫
print(f'{{"name": "Alice"}}')
```

3. 精度格式寫錯

```python
price = 9.876

# ❌
# print(f'{price:2f}')

# ✅
print(f'{price:.2f}')
```

4. 百分比格式誤解

```python
ratio = 0.25
print(f'{ratio:.0%}')  # 25%

# 若 ratio 已是 25，就不該再用 % 格式
already_percent = 25
print(f'{already_percent}%')
```

5. 不必要的複雜模板

```python
# ❌ 過於複雜不易維護
msg = '{} {} {}'.format(a, b, c)

# ✅ 更可讀
msg = f'{a} {b} {c}'
```

---

## 實際應用場景

### 1. 成績單輸出

```python
name = 'Nina'
score = 93.456
rank = 3

print(f'姓名：{name:<8} 分數：{score:>6.2f} 名次：{rank:>3d}')
```

### 2. 金額報表

```python
amount = 1234567.8
tax = 0.05

print(f'未稅：{amount:,.2f}')
print(f'稅額：{amount * tax:,.2f}')
print(f'含稅：{amount * (1 + tax):,.2f}')
```

### 3. API / log 訊息

```python
uid = 1001
status = 200
latency_ms = 23.456

log = f'uid={uid} status={status} latency={latency_ms:.1f}ms'
print(log)
```

用途：

- 輸出對齊
- 結果顯示
- 除錯訊息
- 報表格式化

---

## 最小檢查清單

你完成本章後，至少應能：

1. 使用 f-string 做基本字串插值。
2. 用 `:.2f`、`:,`、`:.1%` 做數值顯示。
3. 使用 `<`、`>`、`^` 控制對齊與欄寬。
4. 理解 `format()` 與 f-string 的差異。
5. 排查常見格式化錯誤（漏 `f`、大括號、精度寫法）。
