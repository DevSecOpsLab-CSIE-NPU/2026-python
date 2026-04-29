# 題目 10071

**題名**: UVA 10071 — Back to High School Physics

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a064)
- [Yui Huang 題解](https://yuihuang.com/zj-a064/)

## 題目敘述

給定兩個整數 v 與 t，請計算物體在等加速度運動下，從時間 0 到時間 2t 的位移。

在這題的設定裡，答案就是公式 **2 × v × t**。

## 輸入說明

每一行包含兩個整數 **v** 與 **t**。

輸入會持續到 EOF。

## 輸出說明

對每一行輸入，輸出一個整數，表示 **2 × v × t**。

---

## 解題思路

這題只需要直接套公式。

1. 讀入每一組 v、t。
2. 計算 2 × v × t。
3. 逐行輸出結果。

時間複雜度為 O(1) / 組。

## 解題代碼

```python
import sys


def main() -> None:
	data = sys.stdin.read().split()
	if not data:
		return

	values = []
	for i in range(0, len(data), 2):
		v = int(data[i])
		t = int(data[i + 1])
		values.append(str(2 * v * t))

	sys.stdout.write("\n".join(values))


if __name__ == "__main__":
	main()
```

## 測試用例

輸入：

```text
3 4
```

輸出：

```text
24
```
