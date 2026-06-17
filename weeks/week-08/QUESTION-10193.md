# 題目 10193

**題名**: UVA 10193

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a186)
- [Yui Huang 題解](https://yuihuang.com/zj-a186/)

## 題目敘述

**反正切函數**可展開成無窮級數，有如下公式（其中 0 ≤ x ≤ 1）：

$$\arctan(x) = x - \frac{x^3}{3} + \frac{x^5}{5} - \cdots$$

使用反正切函數來計算 **π** 是一種常用方法。

例如，最簡單的計算 π 的方式：

$$\pi = 4\arctan(1) = 4\left(1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \cdots\right)$$

然而這種方法效率很低。利用角度和的正切函數公式：

$$\tan(a+b) = \frac{\tan(a)+\tan(b)}{1-\tan(a)\cdot\tan(b)}$$

可以推導出：

$$\arctan(p) + \arctan(q) = \arctan\!\left(\frac{p+q}{1-pq}\right)$$

例如令 p = 1/2，q = 1/3，則：

$$\arctan\!\left(\frac{1}{2}\right) + \arctan\!\left(\frac{1}{3}\right) = \arctan(1)$$

使用 1/2 和 1/3 的反正切來計算 arctan(1)，速度快得多。

我們將上式寫成如下形式：

$$\arctan\!\left(\frac{1}{a}\right) = \arctan\!\left(\frac{1}{b}\right) + \arctan\!\left(\frac{1}{c}\right)$$

其中 **a、b、c 均為正整數**。

**問題**：對於每一個給定的 a（1 ≤ a ≤ 60000），求 **b + c** 的值。

保證對任意的 a 都存在整數解。若有多個解，要求給出 **b + c 最小**的解。

## 輸入說明

輸入檔案中只有一個正整數 **a**，其中 **1 ≤ a ≤ 60000**。

## 輸出說明

輸出一個整數，為 **b + c** 的值。

---

## 解題思路

*請填入你的解題思路*

## 解題代碼

```python
# 你的代碼這裡
```

## 測試用例

*測試輸入與預期輸出*
