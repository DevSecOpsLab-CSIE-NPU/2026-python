# 題目 10190

**題名**: UVA 10190

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a183)
- [Yui Huang 題解](https://yuihuang.com/zj-a183/)

## 題目敘述

M 國是個多雨的國家，尤其是 P 城，頻繁的降雨給人們的出行帶來了很多麻煩。

為了方便行人雨天過馬路，有關部門在每處人行橫道的上空都安裝了一種名為「**自動傘**」的裝置。每把自動傘都可以近似看作一塊**長方形的板**（厚度不計），具有相當出色的吸水能力——落到傘上的雨水會完全被傘頂的小孔吸入，並通過管道排走。

**自動傘的運作方式：**

- 不下雨時，傘閒置。
- 一旦下雨，傘便以**均速直線往返運動**：從馬路一邊移動到另一邊，再返回，如此往復，直到雨停。
- 任何時刻，自動傘都不會越過馬路邊界。

由於單把傘大小有限，主要人行橫道上空安裝了**多把自動傘**。每把傘的寬度等於人行橫道寬度，但長度和移動速率各不相同。

以馬路**左邊界為原點**，向右為 x 軸正方向，建立平面直角坐標系，每把傘可看作平面上的一條**線段**。

請計算從開始下雨到 **T 秒後**，一共有多少**體積**的雨水落到人行橫道上。

## 輸入說明

第一行有四個整數 **N、W、T、V**：
- **N**：自動傘的數目
- **W**：馬路的寬度
- **T**：統計時間長度（秒）
- **V**：單位面積單位時間內的降雨體積

接下來的 N 行，每行用三個整數描述一把自動傘：
- **x**：傘的初始位置（左端點的橫坐標）
- **l**：傘的長度（x 方向的尺寸）
- **v**：傘的速度（v > 0 向右移動；v < 0 向左移動；v = 0 靜止不動）

## 輸出說明

輸出一個實數，表示從開始下雨到 T 秒後，落到人行橫道上的**雨水總體積**，結果**精確到小數點後第二位**。

---

## 解題思路

把每把自動傘看成在 `0 ~ W-l` 之間來回移動的線段。

先把整段時間切成「每把傘速度都固定」的小區間，再在每個小區間內找出任兩個端點相交的時間點，把時間切得更細。

在最小時間區間中，所有線段端點的相對順序都不會變，所以覆蓋長度是線性的。只要算出區間兩端的覆蓋長度，用梯形公式積分，就能得到覆蓋面積。

最後用 `W * T - 覆蓋面積` 得到沒被傘擋住的雨量，再乘上雨量密度 `V` 就是答案。

## 解題代碼

```python
import sys


EPS = 1e-10


def build_segments(x, length, velocity, road_width, total_time):
	"""建立每把傘的直線運動分段。"""
	travel_range = road_width - length

	# 沒有空間移動，或速度為 0，就視為靜止
	if velocity == 0 or travel_range <= EPS or total_time <= EPS:
		return [(0.0, total_time, float(x), 0.0)]

	speed = abs(velocity)
	direction = 1.0 if velocity > 0 else -1.0
	now = 0.0
	position = float(x)
	segments = []

	while now < total_time - EPS:
		boundary = travel_range if direction > 0 else 0.0

		# 距離最近邊界的距離
		if direction > 0:
			distance = boundary - position
		else:
			distance = position - boundary

		# 已經在邊界上，直接反向，避免卡住
		if distance <= EPS:
			position = boundary
			direction = -direction
			continue

		delta = distance / speed
		end_time = now + delta

		# 如果來不及撞到邊界就結束
		if end_time >= total_time - EPS:
			segments.append((now, total_time, position, direction * speed))
			break

		segments.append((now, end_time, position, direction * speed))

		# 到達邊界後反彈
		now = end_time
		position = boundary
		direction = -direction

	return segments


def union_length_at_time(lines, tau):
	"""計算某一時刻所有線段的聯集長度。"""
	intervals = []
	for left_at_start, velocity, length in lines:
		left = left_at_start + velocity * tau
		intervals.append((left, left + length))

	intervals.sort()

	total = 0.0
	current_left, current_right = intervals[0]

	for left, right in intervals[1:]:
		if left > current_right + EPS:
			total += current_right - current_left
			current_left, current_right = left, right
		else:
			if right > current_right:
				current_right = right

	total += current_right - current_left
	return total


def main():
	data = sys.stdin.read().split()
	if not data:
		return

	n = int(data[0])
	road_width = float(data[1])
	total_time = float(data[2])
	rain_volume = float(data[3])

	lengths = []
	umbrella_segments = []

	index = 4
	for _ in range(n):
		x = int(data[index])
		length = int(data[index + 1])
		velocity = int(data[index + 2])
		index += 3

		lengths.append(float(length))
		umbrella_segments.append(build_segments(x, length, velocity, road_width, total_time))

	# 收集所有會改變速度的時間點
	time_points = {0.0, total_time}
	for segments in umbrella_segments:
		for start_time, end_time, _, _ in segments:
			time_points.add(start_time)
			time_points.add(end_time)

	time_points = sorted(time_points)

	# 每個小區間內，每把傘都只有固定速度
	current_index = [0] * n
	covered_area = 0.0

	for left_time, right_time in zip(time_points, time_points[1:]):
		if right_time - left_time <= EPS:
			continue

		# 先抓出這個小區間起點時，每把傘的位置與速度
		lines = []
		for umbrella_id in range(n):
			segs = umbrella_segments[umbrella_id]

			while (
				current_index[umbrella_id] + 1 < len(segs)
				and segs[current_index[umbrella_id]][1] <= left_time + EPS
			):
				current_index[umbrella_id] += 1

			start_time, end_time, left_pos, velocity = segs[current_index[umbrella_id]]
			left_at_left_time = left_pos + velocity * (left_time - start_time)
			lines.append((left_at_left_time, velocity, lengths[umbrella_id]))

		# 找出端點互相交會的時間，把區間切更細
		split_times = [left_time, right_time]
		endpoints = []
		for left_pos, velocity, length in lines:
			endpoints.append((left_pos, velocity))
			endpoints.append((left_pos + length, velocity))

		endpoint_count = len(endpoints)
		for i in range(endpoint_count):
			p1, v1 = endpoints[i]
			for j in range(i + 1, endpoint_count):
				p2, v2 = endpoints[j]
				if abs(v1 - v2) <= EPS:
					continue

				t = left_time + (p2 - p1) / (v1 - v2)
				if left_time + EPS < t < right_time - EPS:
					split_times.append(t)

		split_times.sort()
		unique_times = [split_times[0]]
		for t in split_times[1:]:
			if t - unique_times[-1] > 1e-9:
				unique_times.append(t)

		# 端點順序固定的每個子區間，用梯形公式積分
		for u, v in zip(unique_times, unique_times[1:]):
			if v - u <= EPS:
				continue

			tau_u = u - left_time
			tau_v = v - left_time
			length_u = union_length_at_time(lines, tau_u)
			length_v = union_length_at_time(lines, tau_v)
			covered_area += (length_u + length_v) * (v - u) / 2.0

	# 沒被傘遮住的雨量
	answer = max(0.0, (road_width * total_time - covered_area) * rain_volume)
	print(f'{answer:.2f}')


if __name__ == '__main__':
	main()
```

## 測試用例

*測試輸入與預期輸出*
