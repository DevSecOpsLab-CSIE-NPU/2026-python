# 題目 10931

**題名**: UVA 10931 — Parity

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a924)
- [UVA Online Judge](https://uva.onlinejudge.org/external/10931.pdf)

## 題目敘述

整數 N 的「**奇偶性（Parity）**」定義為其**二進位表示中，1 的個數**。

給定一個整數 I，請：
1. 將其轉換為**二進位表示**（不含前導零）
2. 計算二進位中 **1 的個數 P**
3. 依照固定格式輸出結果

## 輸入說明

- 每行輸入一個整數 **I**（**1 ≤ I ≤ 2,147,483,647**）。
- 以 **I = 0** 結束輸入（不需處理）。

## 輸出說明

對每個整數 I，輸出一行：

```
The parity of B is P (mod 2).
```

- **B** 為 I 的二進位表示（不含前導零）
- **P** 為二進位中 1 的個數

---

## 解題思路

*請填入你的解題思路*

## 解題代碼

### 核心概念
**奇偶性（Parity）**定義為二進位表示中 1 的個數。

例如：
- 1 的二進位是 1，有 1 個 1，奇偶性 = 1
- 2 的二進位是 10，有 1 個 1，奇偶性 = 1
- 10 的二進位是 1010，有 2 個 1，奇偶性 = 2
- 21 的二進位是 10101，有 3 個 1，奇偶性 = 3

### 解題步驟
**1. 讀取整數 I**

**2. 轉換為二進位**
- 使用 `bin(I)` 函數得到二進位字符串
- 移除前綴 '0b'

**3. 計算 1 的個數**
- 計數二進位中有多少個 '1'
- 或用 `bin(I).count('1')` 直接計數

**4. 輸出結果**
- 格式：「The parity of B is P (mod 2).」
- B 為二進位表示
- P 為 1 的個數

### 時間複雜度
O(log I) - 二進位位數為 log I

### 進階技巧
也可以使用位操作來計算 1 的個數（Brian Kernighan 演算法）：
```python
def count_ones(n):
	count = 0
	while n:
		n &= n - 1  # 移除最低的 1
		count += 1
	return count
```

# 你的代碼這裡
```

# 讀取輸入
while True:
	# 讀取一個整數 I
	i = int(input())
    
	# 當輸入為 0 時停止
	if i == 0:
		break
    
	# 步驟 1：轉換為二進位
	# bin(i) 返回形如 '0b1010' 的字符串
	# [2:] 移除前綴 '0b'
	binary = bin(i)[2:]
    
	# 步驟 2：計算二進位中 1 的個數（奇偶性）
	# count('1') 計數字符串中 '1' 出現的次數
	parity = binary.count('1')
    
	# 步驟 3：輸出結果
	# 格式：「The parity of B is P (mod 2).」
	# B 是二進位表示，P 是 1 的個數
	print(f"The parity of {binary} is {parity} (mod 2).")

```
輸入:
1
2
10
21
0

輸出:
The parity of 1 is 1 (mod 2).
The parity of 10 is 1 (mod 2).
The parity of 1010 is 2 (mod 2).
The parity of 10101 is 3 (mod 2).
```
