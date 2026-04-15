import sys


def reflect_position(x0, length, v, width, t):
    """計算時間 t 時雨傘左端點位置（含碰邊反彈）。"""
    # 可移動區間長度：左端點只能在 [0, width-length]
    travel = max(0.0, width - length)
    if travel == 0.0:
        return 0.0
    if v == 0.0:
        # 靜止雨傘仍需保證在合法範圍
        return min(max(x0, 0.0), travel)

    start = min(max(x0, 0.0), travel)
    p = start + v * t

    # 反射展開法：週期為 2*travel
    period = 2.0 * travel
    q = p % period
    if q < 0:
        q += period

    if q <= travel:
        return q
    return period - q


def merged_covered_length(intervals):
    """合併多段區間，回傳總覆蓋長度。"""
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


def estimate_uncovered_integral(n, w, t_total, umbrellas):
    """數值近似積分：估計 0~T 的未遮蔽寬度積分。"""
    if t_total <= 0:
        return 0.0
    if n == 0:
        # 沒有雨傘時可直接精確值
        return w * t_total

    # 取固定步數，題目作業用途足夠直觀；時間越長，步距越大。
    steps = 4000
    dt = t_total / steps
    acc = 0.0

    # 中點法：每段 [k*dt, (k+1)*dt] 使用中點取樣
    for k in range(steps):
        time_mid = (k + 0.5) * dt
        intervals = []

        for x, length, speed in umbrellas:
            left = reflect_position(x, length, speed, w, time_mid)
            right = left + length
            left = max(0.0, left)
            right = min(w, right)
            if right > left:
                intervals.append((left, right))

        covered = merged_covered_length(intervals)
        uncovered = max(0.0, w - covered)
        acc += uncovered * dt

    return acc


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    it = iter(data)
    n = int(next(it))
    w = float(next(it))
    t_total = float(next(it))
    v_rain = float(next(it))

    umbrellas = []
    for _ in range(n):
        x = float(next(it))
        length = float(next(it))
        speed = float(next(it))
        umbrellas.append((x, length, speed))

    # 邊界條件：沒時間或沒雨，答案必為 0
    if t_total == 0 or v_rain == 0:
        print("0.00")
        return

    uncovered_integral = estimate_uncovered_integral(n, w, t_total, umbrellas)
    volume = uncovered_integral * v_rain
    print(f"{volume:.2f}")


if __name__ == "__main__":
    main()
