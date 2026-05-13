# 題目 10922

**題名**: UVA 10922 — 2 the 9s

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a915)
- [Yui Huang 題解](https://yuihuang.com/zj-a915/)

## 題目敘述

一個整數若能被 **9 整除**，則稱為「9 的倍數」。

有一個判斷一個數是否為 9 的倍數的**遞迴方法**：

1. 計算該數**各位數字的總和**。
2. 若總和仍為多位數，再次計算**各位數字的總和**。
3. 重複此過程，直到只剩**一位數**。
4. 若最終結果為 **9**，則原數為 9 的倍數。

定義「**9 的深度**（9-degree）」為：一個能被 9 整除的數，需要**重複幾次上述加總過程**才能得到 9。

給定一個正整數，請判斷它是否為 9 的倍數，若是則輸出其 9 的深度。

## 輸入說明

- 每行輸入一個**正整數**（位數可能很多）。
- 以 **0** 結束輸入（不需處理）。

## 輸出說明

對每個整數輸出一行：

- 若不是 9 的倍數：`X is not a multiple of 9.`
- 若是 9 的倍數：`9-degree of X is Y.`

其中 X 為輸入整數，Y 為 9 的深度。

---

## 解題思路

### 核心概念
判斷一個數是否為 9 的倍數，可以用「數字根」的方法：
1. 將所有數字相加
2. 如果結果是多位數，重複步驟 1
3. 當結果是一位數時：
   - 若為 9，則原數是 9 的倍數
   - 否則不是 9 的倍數

「9 的深度」就是執行上述過程的次數。

### 解題步驟
**1. 先檢查整除性**
- 直接用 `N % 9 == 0` 判斷是否為 9 的倍數

**2. 計算 9 的深度**
- 不斷計算各位數字之和
- 直到結果為一位數
- 計數執行的次數

**3. 輸出結果**
- 若不是 9 的倍數：輸出「X is not a multiple of 9.」
- 若是 9 的倍數：輸出「9-degree of X is Y.」

### 時間複雜度
O(log N × log log N) - 數字和會快速遞減

## 解題代碼

```python
def calculate_degree(num_str):
	"""計算數字 9 的深度"""
	# 深度計數器
	degree = 0
    
	# 持續計算數字和，直到結果為一位數
	while len(num_str) > 1:
		# 計算所有數字的總和
		digit_sum = sum(int(digit) for digit in num_str)
		# 將和轉換為字符串，便於計算下一輪
		num_str = str(digit_sum)
		# 增加深度計數
		degree += 1
    
	# 返回深度（最後一位數字應該是 9）
	return degree


# 讀取輸入
while True:
	# 讀取一行輸入
	num_str = input().strip()
    
	# 當輸入為 '0' 時停止
	if num_str == '0':
		break
    
	# 轉換為整數檢查是否為 9 的倍數
	num = int(num_str)
    
	# 步驟 1：檢查是否為 9 的倍數
	if num % 9 != 0:
		# 不是 9 的倍數
		print(f"{num_str} is not a multiple of 9.")
	else:
		# 是 9 的倍數，計算深度
		degree = calculate_degree(num_str)
		print(f"9-degree of {num_str} is {degree}.")
```

## 測試用例

*測試輸入與預期輸出*
