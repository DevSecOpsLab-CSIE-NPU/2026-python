import math

# 雨傘遮雨：計算在時間 T 內，未被遮住的雨水總量

def umbrella_left(x0, l, v, W, t):
    """計算雨傘左端在時間 t 的位置（來回反彈）"""
    max_x = W - l  # 雨傘最多能移到的最右位置
    if max_x <= 0 or v == 0:
        return max(0.0, min(float(max_x), float(x0)))
    # 計算移動距離，並折疊成來回振盪
    pos = x0 + v * t
    period = 2.0 * max_x
    pos = pos % period
    if pos < 0:
        pos += period
    # 超過 max_x 就反彈回來
    if pos > max_x:
        pos = period - pos
    return pos


def covered_length(intervals, W):
    """計算所有雨傘區間聯集的總長度"""
    if not intervals:
        return 0.0
    intervals.sort()
    total = 0.0
    cur_l, cur_r = intervals[0]
    for l, r in intervals[1:]:
        if l <= cur_r:
            cur_r = max(cur_r, r)  # 區間重疊，合併
        else:
            total += cur_r - cur_l
            cur_l, cur_r = l, r
    total += cur_r - cur_l
    return total


# 讀入參數：雨傘數量、場地寬度、時間長度、降雨速率
N, W, T, V = map(int, input().split())
umbrellas = []
for _ in range(N):
    x, l, v = map(int, input().split())
    umbrellas.append((x, l, v))

# 用數值積分（切成很多小段）估算未遮到的雨水
STEPS = 100000
dt = T / STEPS
rain = 0.0

for i in range(STEPS):
    t = (i + 0.5) * dt  # 取每小段的中間時間點
    intervals = []
    for x0, l, v in umbrellas:
        pos = umbrella_left(x0, l, v, W, t)
        intervals.append((pos, pos + l))
    covered = covered_length(intervals, W)
    # 未遮住的寬度 × 降雨速率 × 時間 = 這段時間的雨水量
    rain += max(0.0, W - covered) * V * dt

print(f"{rain:.2f}")


solve()
