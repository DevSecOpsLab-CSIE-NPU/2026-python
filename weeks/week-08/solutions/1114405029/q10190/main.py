import sys


def reflected_position(x, length, velocity, road_width, t):
    # 計算某把傘在時間 t 時，左端點的位置
    limit = road_width - length

    # 如果傘長等於整條路，左端點永遠只能在 0
    if limit <= 0:
        return 0.0

    period = 2.0 * limit
    raw = x + velocity * t
    r = raw % period

    if r <= limit:
        return r
    return period - r


def covered_length_at_time(umbrellas, road_width, t):
    # 先求出所有傘在時間 t 的覆蓋區間
    intervals = []

    for x, length, velocity in umbrellas:
        left = reflected_position(x, length, velocity, road_width, t)
        right = left + length
        intervals.append((left, right))

    if not intervals:
        return 0.0

    # 依左端點排序後合併區間
    intervals.sort()

    total = 0.0
    current_left, current_right = intervals[0]

    for left, right in intervals[1:]:
        if left > current_right:
            total += current_right - current_left
            current_left, current_right = left, right
        else:
            if right > current_right:
                current_right = right

    total += current_right - current_left
    return total


def simpson(f, a, b, fa, fm, fb):
    return (b - a) * (fa + 4.0 * fm + fb) / 6.0


def adaptive_simpson(f, a, b, fa, fm, fb, whole, eps, depth):
    mid = (a + b) / 2.0
    left_mid = (a + mid) / 2.0
    right_mid = (mid + b) / 2.0

    f_left_mid = f(left_mid)
    f_right_mid = f(right_mid)

    left_value = simpson(f, a, mid, fa, f_left_mid, fm)
    right_value = simpson(f, mid, b, fm, f_right_mid, fb)

    if depth <= 0 or abs(left_value + right_value - whole) <= 15.0 * eps:
        return left_value + right_value + (left_value + right_value - whole) / 15.0

    return (
        adaptive_simpson(f, a, mid, fa, f_left_mid, fm, left_value, eps / 2.0, depth - 1)
        + adaptive_simpson(f, mid, b, fm, f_right_mid, fb, right_value, eps / 2.0, depth - 1)
    )


def integrate_uncovered_length(umbrellas, road_width, total_time):
    # f(t) = 當下未被遮住的長度
    def f(t):
        return road_width - covered_length_at_time(umbrellas, road_width, t)

    if total_time == 0:
        return 0.0

    a = 0.0
    b = float(total_time)
    mid = (a + b) / 2.0

    fa = f(a)
    fm = f(mid)
    fb = f(b)

    whole = simpson(f, a, b, fa, fm, fb)

    return adaptive_simpson(f, a, b, fa, fm, fb, whole, 1e-7, 25)


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    it = iter(data)

    n = int(next(it))
    w = float(next(it))
    t = float(next(it))
    v_rain = float(next(it))

    umbrellas = []
    for _ in range(n):
        x = float(next(it))
        length = float(next(it))
        velocity = float(next(it))
        umbrellas.append((x, length, velocity))

    uncovered_integral = integrate_uncovered_length(umbrellas, w, t)
    answer = uncovered_integral * v_rain

    print(f"{answer:.2f}")


if __name__ == "__main__":
    main()