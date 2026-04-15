# 11 Hello World

## 概述

`Hello, World!` 是程式世界的第一個標準練習。它看起來很簡單，但其實可以用來確認「環境是否可執行、編碼是否正確、輸入輸出是否正常」。

你必須已經「不需要解釋」就能看懂：

```python
print('Hello, World!')
```

---

## 第一支 Python 程式

### 最小可執行範例

```python
print('Hello, World!')
```

執行後輸出：

```text
Hello, World!
```

### 這行程式在做什麼

1. `print(...)` 是 Python 內建函式，用來把內容輸出到終端機。
2. `'Hello, World!'` 是字串（string），用單引號包起來。
3. 程式執行時，Python 會把字串內容印出。

---

## print 基礎輸出

### 輸出字串、數字與多個值

```python
print('Hello')
print(123)
print(3.14)
print(True)

# 一次輸出多個值（預設用空白分隔）
print('Name:', 'Alice', 'Age:', 20)
```

輸出：

```text
Hello
123
3.14
True
Name: Alice Age: 20
```

### `sep` 與 `end` 參數

```python
# sep：指定多個值之間的分隔符號
print('2026', '04', '15', sep='-')

# end：指定列尾（預設是換行 \n）
print('Hello', end=' ')
print('World')
```

輸出：

```text
2026-04-15
Hello World
```

### 常見輸出格式

```python
name = 'Nina'
score = 95

print('學生：', name)
print('分數：', score)
print(f'學生：{name}，分數：{score}')
```

---

## 註解（Comments）

註解讓你說明程式意圖，不會被執行。

```python
# 這是一行註解
print('Hello, World!')  # 這也是註解
```

建議：

1. 註解重點在「為什麼」，不是重複「做了什麼」。
2. 新手練習時可多寫註解，熟悉後逐步精簡。

---

## 基本輸入（input）

Hello World 下一步通常是互動式輸入。

```python
name = input('請輸入你的名字：')
print(f'Hello, {name}!')
```

範例互動：

```text
請輸入你的名字：Alice
Hello, Alice!
```

### input 回傳型態注意

`input()` 永遠回傳字串。

```python
age_text = input('請輸入年齡：')
print(type(age_text))  # <class 'str'>

# 需要數字計算時要轉型
age = int(age_text)
print(age + 1)
```

---

## 字串引號與跳脫

### 單引號、雙引號

```python
print('Hello')
print("Hello")
```

兩者都可，請在專案中保持一致風格。

### 字串中包含引號

```python
print("I'm fine")
print('He said: "Python is great"')
```

### 換行與特殊字元

```python
print('第一行\n第二行')
print('Tab\t分隔')
```

---

## 程式檔案執行方式

假設檔案名為 `hello.py`。

```python
print('Hello, World!')
```

在終端機執行：

```powershell
python hello.py
```

若環境設定不同，也可能使用：

```powershell
py hello.py
```

用途：

1. 驗證 Python 安裝與 PATH 設定是否正常。
2. 確認編輯器、終端機、檔案編碼可正常配合。

---

## 常見錯誤與排查

### 1. 括號或引號漏掉

```python
# ❌ 錯誤
print('Hello, World!'

# ✅ 正確
print('Hello, World!')
```

### 2. 大小寫錯誤

```python
# ❌ 錯誤
Print('Hello')

# ✅ 正確
print('Hello')
```

### 3. Python 找不到

終端機顯示類似 `python 不是內部或外部命令` 時：

1. 檢查是否已安裝 Python。
2. 檢查 PATH 是否正確。
3. 在 VS Code 選擇正確的 Python 環境。

### 4. 中文顯示亂碼

1. 檔案請使用 UTF-8 編碼。
2. 終端機字型與編碼需支援中文。

---

## 從 Hello World 到小工具

### 範例 1：打招呼程式

```python
name = input('請輸入名字：')
print(f'你好，{name}！歡迎學習 Python。')
```

### 範例 2：兩數相加

```python
a = int(input('輸入第一個整數：'))
b = int(input('輸入第二個整數：'))
print(f'總和 = {a + b}')
```

### 範例 3：簡易成績顯示

```python
student = input('學生姓名：')
score = float(input('成績：'))
print(f'學生：{student}，成績：{score:.1f}')
```

---

## 與前面章節的連結

Hello World 雖然簡單，但會串到很多先備知識：

1. 變數：`name = ...`
2. 型別轉換：`int(...)`, `float(...)`
3. 字串格式化：`f'...'`
4. 例外處理：`try/except` 可保護錯誤輸入

例如：

```python
value = input('請輸入整數：')
try:
	n = int(value)
	print(f'你輸入的是 {n}')
except ValueError:
	print('這不是合法整數')
```

---

## 最小檢查清單

你完成本章後，至少應該能做到：

1. 寫出並執行 `print('Hello, World!')`。
2. 用 `input()` 接收使用者輸入。
3. 理解 `input()` 回傳字串，必要時做型別轉換。
4. 排查基本語法錯誤（括號、引號、大小寫）。
5. 用 f-string 做簡單輸出格式化。

用途：

- 驗證環境正常
- 最小可執行程式
- 建立 I/O（輸入輸出）基本功
