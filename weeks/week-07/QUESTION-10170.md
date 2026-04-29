# 題目 10170

**題名**: UVA 10170 — The Hotel with Infinite Rooms

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a163)
- [UVA Online Judge](https://uva.onlinejudge.org/external/10170.pdf)

## 題目敘述

HaluaRuti 城裡有一家奇特的旅館，擁有**無限多間房間**。

旅館的住宿規則如下：

- 同一時間只能有**一個旅行團**住宿。
- 每個旅行團**早上入住，傍晚退房**。
- 前一個旅行團退房的**隔天早上**，下一個旅行團入住。
- **每個旅行團的人數比前一個多 1 人**（起始旅行團除外，其人數為 S）。
- 一個有 **n 人**的旅行團，會住 **n 天**。

例如：若起始旅行團有 4 人，則第 1~4 天住 4 人團，第 5~9 天住 5 人團，以此類推。

給定起始旅行團的人數 **S** 和查詢天數 **D**，請找出**第 D 天住宿的旅行團有幾人**。

## 輸入說明

- 每行包含兩個整數 **S**（1 ≤ S ≤ 10000）和 **D**（1 ≤ D < 10¹⁵）。
- 所有輸入和輸出整數均小於 10¹⁵。
- 輸入直到 **EOF** 結束。

## 輸出說明

每行輸入對應一行輸出，為**第 D 天住宿的旅行團人數**。

---

## 解題思路

這題的關鍵是把「第 D 天屬於哪一團」轉成累積天數問題。

第 1 團的人數是 S，住 S 天；第 2 團人數是 S+1，住 S+1 天；依此類推。

若前 k 團總共住了 `S + (S+1) + ... + (S+k-1)` 天，則可以用等差級數公式表示為：

`k * (2S + k - 1) / 2`

所以只要找出最小的 k，使得累積天數大於等於 D，就能知道第 D 天屬於第 k 團，答案就是 `S + k - 1`。

因為 D 很大，直接模擬不適合，使用二分搜尋找 k 最穩定。

## 解題代碼

```python
import sys


def find_group_size(s: int, d: int) -> int:
	left = 1
	right = 2 * 10**9

	while left < right:
		mid = (left + right) // 2
		total_days = mid * (2 * s + mid - 1) // 2
		if total_days >= d:
			right = mid
		else:
			left = mid + 1

	return s + left - 1


def main() -> None:
	data = sys.stdin.read().split()
	if not data:
		return

	results = []
	for i in range(0, len(data), 2):
		s = int(data[i])
		d = int(data[i + 1])
		results.append(str(find_group_size(s, d)))

	sys.stdout.write("\n".join(results))


if __name__ == "__main__":
	main()
```

## 測試用例

輸入：

```text
4 10
```

輸出：

```text
6
```
