# 題目 10093

**題名**: UVA 10093

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a086)
- [Yui Huang 題解](https://yuihuang.com/zj-a086/)

## 題目敘述

司令部的將軍們打算在 **N×M 的網格地圖**上部署炮兵部隊。

地圖的每一格可能是：
- **山地**（用 `H` 表示）：不能部署炮兵
- **平原**（用 `P` 表示）：每格最多可部署一支炮兵部隊

一支炮兵部隊的**攻擊範圍**為：沿橫向左右各兩格，沿縱向上下各兩格（攻擊範圍不受地形影響）。

為了**防止誤傷**，任何兩支炮兵部隊之間不能互相攻擊（即任何一支炮兵部隊都不在其他支炮兵部隊的攻擊範圍內）。

請問在整個地圖區域內，**最多能部署多少支炮兵部隊**？

## 輸入說明

- 第一行包含兩個正整數 **N** 和 **M**，以空格分隔（**N ≤ 100，M ≤ 10**）。
- 接下來的 N 行，每行含有連續的 M 個字元（`P` 或 `H`），表示地圖各列的地形。

## 輸出說明

輸出一個整數 **K**，表示最多能部署的炮兵部隊數量。

---

## 解題思路

這題是經典的狀態壓縮動態規劃。

因為地圖寬度 M 最多只有 10，所以可以用 bitmask 表示每一列是否放炮兵。

核心限制有三個：

1. 同一列的兩個炮兵不能距離 1 或 2 格，所以同一列的 bitmask 必須滿足 `mask & (mask << 1) == 0` 且 `mask & (mask << 2) == 0`。
2. 與前一列不能有相同欄位的炮兵，避免垂直距離 1 互相攻擊。
3. 與前兩列也不能有相同欄位的炮兵，避免垂直距離 2 互相攻擊。

做法：

1. 先把每一列哪些位置可放炮兵轉成 bitmask。
2. 列舉所有符合同列限制的 mask。
3. 用 `dp[(prev2, prev1)]` 表示處理到目前列時，前兩列狀態為 `prev2`、`prev1` 的最大炮兵數量。
4. 轉移到當前列 `cur` 時，只要 `cur` 與 `prev1`、`prev2` 都沒有重疊，就可以更新答案。

因為 M 很小，這個做法可以在可接受時間內完成。

## 解題代碼

```python
import sys


def build_valid_masks(width: int):
	masks = []
	for mask in range(1 << width):
		if mask & (mask << 1):
			continue
		if mask & (mask << 2):
			continue
		masks.append(mask)
	return masks


def main() -> None:
	data = sys.stdin.read().splitlines()
	if not data:
		return

	n, m = map(int, data[0].split())
	rows = data[1:1 + n]

	usable = []
	for row in rows:
		mask = 0
		for idx, ch in enumerate(row):
			if ch == "P":
				mask |= 1 << idx
		usable.append(mask)

	all_valid_masks = build_valid_masks(m)

	dp = {(0, 0): 0}
	for row_index in range(n):
		next_dp = {}
		allowed = usable[row_index]
		current_masks = [mask for mask in all_valid_masks if mask & allowed == mask]

		for (prev2, prev1), value in dp.items():
			for cur in current_masks:
				if cur & prev1:
					continue
				if cur & prev2:
					continue

				state = (prev1, cur)
				candidate = value + cur.bit_count()
				if candidate > next_dp.get(state, -1):
					next_dp[state] = candidate

		dp = next_dp

	print(max(dp.values(), default=0))


if __name__ == "__main__":
	main()
```

## 測試用例

輸入：

```text
1 5
PPPPP
```

輸出：

```text
2
```
