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

這道題目要求判斷一個大整數是否為 9 的倍數，並計算其「9 的深度」（9-degree）。

1. **判斷 9 的倍數**：
   - 一個數是 9 的倍數，若且唯若其各位數字之和也是 9 的倍數。
   - 由於輸入的數字位數可能很多，我們必須以字串形式讀入。

2. **遞迴計算 9 的深度**：
   - 步聚 1：計算該數各位數字的總和 $S_1$。
   - 步聚 2：如果 $S_1$ 是 9 的倍數，深度加 1。
   - 步聚 3：如果 $S_1 > 9$，則對 $S_1$ 重複上述過程（計算其各位數字之和 $S_2$），直到結果為一位數。
   - 如果最終一位數是 9，則原數是 9 的倍數；否則不是。

3. **實作細節**：
   - 使用 `sum(int(d) for d in n_str)` 來快速計算位數和。
   - 使用迴圈或遞迴來處理深度的計算。
   - 注意輸入為 "0" 時停止。

## 解題代碼

```python
import sys

def solve():
    for line in sys.stdin:
        n_str = line.strip()
        if n_str == '0':
            break
        
        # 計算初步位數和
        current_sum = sum(int(d) for d in n_str)
        
        if current_sum % 9 != 0:
            print(f"{n_str} is not a multiple of 9.")
        else:
            degree = 1
            # 如果位數和仍大於 9，則繼續遞迴
            temp_sum = current_sum
            while temp_sum > 9:
                temp_sum = sum(int(d) for d in str(temp_sum))
                degree += 1
            
            print(f"{n_str} is a multiple of 9 and has 9-degree {degree}.")

if __name__ == "__main__":
    solve()
```

## 測試用例

```
輸入:
999
9
181
0

輸出:
999 is a multiple of 9 and has 9-degree 2.
9 is a multiple of 9 and has 9-degree 1.
181 is not a multiple of 9.
```
