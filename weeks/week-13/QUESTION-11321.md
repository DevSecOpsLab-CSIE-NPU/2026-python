# 題目 11321

**題名**: UVA 11321

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=b314)
- [Yui Huang 題解](https://yuihuang.com/zj-b314/)

## 題目敘述


相信大家都知道紅圓茵可是誰，就不多介紹了。
最近他有一個煩惱，身為一位大魔法師，每天都有成千上萬的人來膜拜他<(_ _)>。
因為人數實在太多了，這麼多人跑到他家膜拜他，害他都無法好好練習魔法了。
茵可家門前有一條柏油路，要到他家一定得經過這條柏油路，他決定把這條柏油路(長方形)切成N*M個格子，並且在其中某些格子設下陷阱，踩到陷阱的人會被傳送回柏油路的起點。
「恩~這樣子就可以減少膜拜我的人了~」紅圓茵可心想。
但是，為了讓jackyXX等人可以到達他家，也不能把柏油路封死，必須確保一定有條路徑可以走到茵可家。
而你的任務是要提醒茵可大大<(_ _)>，哪些點能放陷阱，而哪些點不能放陷阱(導致道路封死)。
柏油路的起點在左邊，而茵可家在柏油路的右邊。
一個人在柏油路上只能往上下左右四個方向走，不能走斜對角。
一條3*10的柏油路oooooooooooooooooooooooooooooo一條被封死的柏油路ooooxooooooooxooooooooxooooooo一條沒被封死的柏油路xxxxxxoooooooooxoxxxooxxoooxoo

## 輸入說明


第一行有3個正整數N、M、T，T為茵可接下來要放的陷阱數量(0<T<=N*M)。
接下來T行每行有2個非負整數x,y表示這個陷阱要放的位址。
縱軸為x軸，橫軸為y軸，左下角那格為(0,0)。
保證一個點只會被放最多一次。
測資1. N,M<=102. N,M<=503. N,M<=1004. N,M<=10005. N,M<=1000

## 輸出說明


對每一個要放的陷阱，若該點可放，請輸出一行"<(_ _)>"(不含雙引號)，並且把陷阱放上去。
若該點不可放(會導致道路封死)，請輸出">_<"(不含雙引號)，並且不放該陷阱。

---

## 解題思路

*請填入你的解題思路*

## 解題代碼

本題欲逐一嘗試放置陷阱，且每次放置後必須保證從左邊任一可通行格子仍可到達右邊任一可通行格子。

直觀且容易理解的做法（本檔採用）：

- 以二維格子表示道路，0 表示可通行，1 表示已放陷阱。
- 依序對每個提案位置 (x,y) 進行：
  1. 暫時把該點標為陷阱（grid[x][y] = 1）。
  2. 使用 BFS（四方向）從左邊邊界所有可通行格子出發，檢查是否能抵達右邊邊界任一可通行格子。
  3. 若存在任一路徑則接受該陷阱（保留 1），否則還原為 0 並回報不可放。

此法直觀且易於實作，適用於小到中等尺寸輸入。若要處理非常大的 N, M，可考慮更高級的技巧，例如：
- 逆向處理（將所有陷阱先放上再逆序移除並用聯通性 DSU 維護連通塊）。
- 使用動態聯通性/橋樑結構或壓縮座標以降低狀態數量。

時間與空間複雜度：
- 每次放置提案都需做一次 BFS，最壞情況下為 O(N*M)；若有 T 個提案，總複雜度約 O(T * N * M)。

# 你的代碼這裡

```python
# 以下為本題的教學版實作，包含 stdin 解析與模組化函式，可直接用於單元測試。
from typing import List, Tuple
from collections import deque


def path_exists(grid: List[List[int]]) -> bool:
	"""檢查在目前 grid 布局下，是否有從左邊任一可通行格子到右邊任一可通行格子的路徑（四方向）。"""
	if not grid or not grid[0]:
		return False
	N = len(grid)
	M = len(grid[0])
	visited = [[False] * M for _ in range(N)]
	dq = deque()

	for x in range(N):
		if grid[x][0] == 0:
			visited[x][0] = True
			dq.append((x, 0))

	while dq:
		x, y = dq.popleft()
		if y == M - 1:
			return True
		for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
			nx, ny = x + dx, y + dy
			if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and grid[nx][ny] == 0:
				visited[nx][ny] = True
				dq.append((nx, ny))

	return False


def simulate_trap_sequence(N: int, M: int, proposals: List[Tuple[int, int]]) -> List[str]:
	"""依序模擬放陷阱，回傳每一步的接受/拒絕結果。"""
	grid = [[0] * M for _ in range(N)]
	outputs: List[str] = []

	for x, y in proposals:
		if grid[x][y] == 1:
			outputs.append('>_<')
			continue
		grid[x][y] = 1
		if path_exists(grid):
			outputs.append('<(_ _)>')
		else:
			outputs.append('>_<')
			grid[x][y] = 0

	return outputs


def parse_and_run_stdin() -> None:
	import sys
	data = sys.stdin.read().strip().split()
	if not data:
		return
	it = iter(data)
	try:
		N = int(next(it)); M = int(next(it)); T = int(next(it))
	except StopIteration:
		return
	proposals = []
	for _ in range(T):
		try:
			x = int(next(it)); y = int(next(it))
		except StopIteration:
			break
		proposals.append((x, y))
	results = simulate_trap_sequence(N, M, proposals)
	if results:
		print('\n'.join(results))


if __name__ == '__main__':
	import sys
	if sys.stdin.isatty():
		# 互動時示範範例
		print(simulate_trap_sequence(3, 3, [(0, 1), (1, 1), (2, 1)]))
	else:
		parse_and_run_stdin()
```

## 測試

單元測試檔：`weeks/week-13/1114405006/test_question_11321.py` 已加入多個情境測試。

測試紀錄（簡要可讀版）：`weeks/week-13/1114405006/test_results_11321_saved.txt`

*測試輸入與預期輸出*
