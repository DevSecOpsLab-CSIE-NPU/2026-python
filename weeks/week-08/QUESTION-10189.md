# 題目 10189

**題名**: UVA 10189 — Minesweeper

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a182)
- [Yui Huang 題解](https://yuihuang.com/zj-a182/)

## 題目敘述

你一定玩過 Windows 上的**踩地雷（Minesweeper）**！

遊戲規則如下：
- 在一個 **n 行 m 列**的網格中，某些格子放有**地雷**（以 `*` 表示），其餘格子為空白（以 `.` 表示）。
- 對於每個**空白格子**，需要計算其**周圍 8 個方向**（上、下、左、右、四斜角）中**地雷的數量**，並以該數字填入。

請根據輸入的地雷位置，輸出填好數字的完整地圖。
## 輸入說明

- 輸入包含多組測試資料。
- 每組測試資料第一行為兩個整數 **n** 和 **m**（表示網格的行數和列數）。
- 接下來 n 行，每行 m 個字元（`*` 表示地雷，`.` 表示空白）。
- 以 **n = 0, m = 0** 結束輸入（不需處理）。
## 輸出說明

- 對每組測試資料，先輸出 `Field #X:`（X 為組號，從 1 開始）。
- 地雷格子保持 `*`，空白格子改為周圍 8 格中地雷的數量（0~8 的數字）。
- 每組測試資料之間**輸出一個空行**。

---

## 解題思路

逐格掃描地圖。

如果目前格子是地雷就直接保留 `*`；如果是空白格子，就檢查周圍 8 個方向，統計地雷數量後填入對應數字。

因為地圖大小不大，直接暴力檢查鄰居就足夠了。

## 解題代碼

```python
import sys


def main():
	data = sys.stdin.read().split()
	index = 0
	field_number = 1
	outputs = []

	# 8 個方向：上、下、左、右、四個斜角
	directions = [
		(-1, -1), (-1, 0), (-1, 1),
		(0, -1),           (0, 1),
		(1, -1),  (1, 0),  (1, 1),
	]

	while index < len(data):
		n = int(data[index])
		m = int(data[index + 1])
		index += 2

		if n == 0 and m == 0:
			break

		grid = data[index:index + n]
		index += n

		outputs.append(f'Field #{field_number}:')

		for row in range(n):
			answer_row = []
			for col in range(m):
				# 地雷直接保留
				if grid[row][col] == '*':
					answer_row.append('*')
					continue

				# 空白格子就數周圍地雷
				mine_count = 0
				for dr, dc in directions:
					nr = row + dr
					nc = col + dc
					if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '*':
						mine_count += 1

				answer_row.append(str(mine_count))

			outputs.append(''.join(answer_row))

		field_number += 1

		# 不是最後一組資料時，補一個空行
		if index < len(data):
			outputs.append('')

	sys.stdout.write('\n'.join(outputs))


if __name__ == '__main__':
	main()
```

## 測試用例

```
輸入:
4 4
*...
....
.*..
....
3 5
**...
.....
.*...
0 0

輸出:
Field #1:
*100
2210
1*10
1110

Field #2:
**100
33200
1*100
```
