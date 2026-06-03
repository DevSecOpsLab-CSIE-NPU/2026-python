# TEST_LOG.md

# UVA 11417 - GCD

學號：1114405029

---

## 題目說明

實作函式：

```python
sum_of_gcd(n: int) -> int
```

計算：

```text
G = Σ Σ gcd(i, j)
    1 ≤ i < j ≤ n
```

也就是將所有符合條件的 `(i,j)` 配對之最大公因數（GCD）加總後回傳。

---

# 測試案例設計

依照課堂要求，先設計測試案例，再進行實作。

## Test Case 1：Edge Case

輸入：

```python
sum_of_gcd(1)
```

預期結果：

```python
0
```

原因：

當 n=1 時不存在任何滿足：

```text
1 ≤ i < j ≤ n
```

的配對，因此總和應為 0。

---

## Test Case 2：最小有效輸入

輸入：

```python
sum_of_gcd(2)
```

計算：

```text
gcd(1,2)=1
```

預期結果：

```python
1
```

---

## Test Case 3：小型驗證

輸入：

```python
sum_of_gcd(3)
```

計算：

```text
gcd(1,2)=1
gcd(1,3)=1
gcd(2,3)=1
```

總和：

```text
1+1+1=3
```

預期結果：

```python
3
```

---

## Test Case 4：人工驗證案例

輸入：

```python
sum_of_gcd(4)
```

計算：

```text
gcd(1,2)=1
gcd(1,3)=1
gcd(1,4)=1
gcd(2,3)=1
gcd(2,4)=2
gcd(3,4)=1
```

總和：

```text
1+1+1+1+2+1=7
```

預期結果：

```python
7
```

---

## Test Case 5：題目範例

輸入：

```python
sum_of_gcd(10)
```

預期結果：

```python
67
```

此案例用來驗證是否與題目官方範例一致。

---

# Red（紅燈）階段

建立：

```text
test_gcd.py
```

但尚未建立：

```text
gcd.py
```

執行：

```bash
python -m unittest test_gcd.py
```

測試結果：

```text
ModuleNotFoundError: No module named 'gcd'
```

結果：

```text
Red
```

代表測試成功偵測到尚未完成實作。

---

# Test Commit

完成紅燈驗證後進行 Commit：

```bash
git commit -m "test: add failing tests for UVA 11417 GCD"
```

Commit：

```text
d44936d
```

---

# Green（綠燈）階段

建立：

```text
gcd.py
```

實作：

```python
sum_of_gcd()
```

利用：

```python
math.gcd()
```

計算所有合法配對的最大公因數總和。

執行：

```bash
python -m unittest test_gcd.py
```

結果：

```text
.....
----------------------------------------------------------------------
Ran 5 tests

OK
```

結果：

```text
Green
```

代表所有測試皆通過。

---

# Feature Commit

完成實作後進行 Commit：

```bash
git commit -m "feat: implement UVA 11417 GCD"
```

Commit：

```text
36f0956
```

---

# Git Log 驗證

執行：

```bash
git log --oneline -5
```

結果：

```text
36f0956 feat: implement UVA 11417 GCD
d44936d test: add failing tests for UVA 11417 GCD
```

確認：

```text
Red
↓
test commit
↓
Green
↓
feat commit
```

符合課堂要求之 TDD 開發流程。

---

# 結論

本次作業依照課堂 SOP 完成：

1. 建立 Feature Branch
2. 設計測試案例
3. 驗證 Red（紅燈）
4. 完成 Test Commit
5. 撰寫實作
6. 驗證 Green（綠燈）
7. 完成 Feature Commit

並成功通過所有測試案例，符合 UVA 11417 題目要求與 TDD 開發流程。
