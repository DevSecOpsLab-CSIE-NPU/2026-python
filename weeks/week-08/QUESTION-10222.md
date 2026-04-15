# 題目 10222

把鍵盤上每個字元對應到左邊一格的字元。

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a215)
- [Yui Huang 題解](https://yuihuang.com/zj-a215/)

## 題目敘述
	# 依照題目的 QWERTY 鍵盤排列建立對照表
	rows = [
		"`1234567890-=",
		"qwertyuiop[]\\",
		"asdfghjkl;'",
		"zxcvbnm,./",
	]

	decode = {}
	for row in rows:
		# 每個字元都對應到左邊一格
		for index in range(1, len(row)):
			decode[row[index]] = row[index - 1]
第四排：z x c v b n m , . /
```

若加密字元是 `r`，則解碼後是 `e`（將位置向左移 3 位）。

## 輸入說明

輸入只有一行，含有某個學生的編號 **id**（**2 ≤ id ≤ 10000**）。

## 輸出說明

- 如果該名學生為**優質學生**，請輸出 `yes`
- 否則請輸出 `no`

---

## 解題思路

把鍵盤上每個字元對應到左邊一格的字元。

輸入時逐字讀取，遇到換行和空白就原樣輸出；其他字元就查表轉換。

## 解題代碼

```python
import sys


def main():
	# 依照題目的鍵盤排列建立對照表
	rows = [
		"`1234567890-=",
		"qwertyuiop[]\\",
		"asdfghjkl;'",
		"zxcvbnm,./",
	]

	decode = {}
	for row in rows:
		# 每個字元都對應到左邊一格
		for index in range(1, len(row)):
			decode[row[index]] = row[index - 1]

	text = sys.stdin.read()
	result = []

	for ch in text:
		# 空白和換行都要保留
		result.append(decode.get(ch, ch))

	sys.stdout.write(''.join(result))


if __name__ == '__main__':
	main()
```

## 測試用例

*測試輸入與預期輸出*
