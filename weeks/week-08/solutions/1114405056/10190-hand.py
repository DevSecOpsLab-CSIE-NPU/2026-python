import math

def umbrella_left(x0, l, v, W, t):
    max_x = W - l
    if max_x <= 0 or v == 0:
        return max(0.0, min(float(max_x), float(x0)))
    pos = x0 + v * t
    period = 2.0 * max_x
    pos = pos % period
    if pos < 0:
        pos += period
    if pos > max_x:
        pos = period - pos
    return pos

def covered_length(intervals):
    if not intervals:
        return 0.0
    intervals.sort()
    total = 0.0
    cur_l, cur_r = intervals[0]
    for l, r in intervals[1:]:
        if l <= cur_r:
            cur_r = max(cur_r, r)
        else:
            total += cur_r - cur_l
            cur_l, cur_r = l, r
    total += cur_r - cur_l
    return total

N, W, T, V = map(int, input().split())
umbrellas = []
for _ in range(N):
    x, l, v = map(int, input().split())
    umbrellas.append((x, l, v))

STEPS = 100000
dt = T / STEPS
rain = 0.0

for i in range(STEPS):
    t = (i + 0.5) * dt
    intervals = []
    for x0, l, v in umbrellas:
        pos = umbrella_left(x0, l, v, W, t)
        intervals.append((pos, pos + l))
    covered = covered_length(intervals)
    rain += max(0.0, W - covered) * V * dt

print(f"{rain:.2f}")
