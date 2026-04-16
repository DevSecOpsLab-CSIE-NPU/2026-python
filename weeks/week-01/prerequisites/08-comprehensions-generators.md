# 8 容器操作與推導式

你必須已經「不需要解釋」就能看懂：

```python
[x for x in data if x > 0]
{k: v for k, v in d.items()}
```

```python
(x * x for x in nums)
```

用途（對應第一章範例）：

- 過濾序列（1.16）
- 字典子集（1.17）
- `sum(...)` / `min(...)` / `join(...)`

---

## 推導式的基本讀法

推導式可以把「建立新容器」和「篩選資料」寫在同一行。

```python
[x for x in data if x > 0]
```

這行可以拆成三個部分來看：

- `x`：要放進新列表的值
- `for x in data`：逐一取出 `data` 裡的元素
- `if x > 0`：只保留大於 0 的元素

等同於下面這段寫法：

```python
result = []
for x in data:
    if x > 0:
        result.append(x)
```

推導式適合用在邏輯簡單的情況。如果條件太多或需要多步處理，改用一般 `for` 迴圈會比較好讀。

---

## 字典推導式

```python
{k: v for k, v in d.items()}
```

這種寫法會逐一取出字典中的 key 和 value，並建立一個新的字典。

常見用途是過濾字典內容：

```python
prices = {"apple": 30, "banana": 15, "cake": 120}
cheap = {name: price for name, price in prices.items() if price < 50}
```

結果：

```python
{"apple": 30, "banana": 15}
```

重點是：原本的 `prices` 不會被修改，`cheap` 是新建出來的字典。

---

## 生成器表示式

```python
(x * x for x in nums)
```

這不是 tuple，而是生成器。

生成器的特點是「需要時才產生下一個值」，不會一次把所有結果放進記憶體。

常見用法：

```python
total = sum(x * x for x in nums)
```

這段會逐一計算平方後交給 `sum()`，不需要先建立完整列表。

如果資料量很小，列表推導式和生成器表示式差異不大；如果資料量很大，生成器通常比較省記憶體。

---

## 什麼時候不要用推導式

推導式不是越短越好。

以下情況建議改用一般迴圈：

- 條件判斷很多層
- 需要在迴圈中印出除錯資訊
- 每個元素要做多步處理
- 推導式一行太長，閱讀成本變高

目標是讓程式容易看懂，而不是把所有邏輯都壓在同一行。
