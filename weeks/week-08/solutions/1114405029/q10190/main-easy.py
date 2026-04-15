import sys


def reflected_position(x, length, velocity, road_width, t):
    # 這個函式用來求某一把傘在時間 t 時
    # 它的左端點位置在哪裡

    # 左端點最多只能移動到 road_width - length
    # 因為再往右就會超出馬路範圍
    limit = road_width - length

    # 如果 limit <= 0，代表這把傘已經跟整條路一樣長
    # 所以它根本不能移動，左端點永遠都是 0
    if limit <= 0:
        return 0.0

    # 傘會在 [0, limit] 之間來回反彈
    # 這種運動可以用「鏡射 + 取模」的方式處理
    period = 2.0 * limit

    # 如果不考慮反彈，原本左端點會走到 raw
    raw = x + velocity * t

    # 先把位置折回一個週期內
    r = raw % period

    # 如果還在前半段，表示是往右的那一段
    if r <= limit:
        return r

    # 否則在後半段，表示正在往左折返
    return period - r


def covered_length_at_time(umbrellas, road_width, t):
    # 這個函式要算在時間 t 的時候
    # 所有雨傘總共蓋住了多少長度

    intervals = []

    # 先把每把傘的覆蓋區間算出來
    for x, length, velocity in umbrellas:
        left = reflected_position(x, length, velocity, road_width, t)
        right = left + length
        intervals.append((left, right))

    # 如果根本沒有任何傘
    if not intervals:
        return 0.0

    # 把所有區間依左端點排序
    intervals.sort()

    # 接著做區間合併
    total = 0.0
    current_left, current_right = intervals[0]

    for left, right in intervals[1:]:
        # 如果新區間跟目前區間完全分開
        # 就先把目前區間長度加進答案
        if left > current_right:
            total += current_right - current_left
            current_left, current_right = left, right
        else:
            # 如果有重疊，就只需要把右端往更大的地方延伸
            if right > current_right:
                current_right = right

    # 最後一段也要記得加進去
    total += current_right - current_left

    return total


def simpson(f, a, b, fa, fm, fb):
    # 辛普森公式
    return (b - a) * (fa + 4.0 * fm + fb) / 6.0


def adaptive_simpson(f, a, b, fa, fm, fb, whole, eps, depth):
    # 自適應辛普森積分
    # 目的是把積分算得夠精準

    mid = (a + b) / 2.0
    left_mid = (a + mid) / 2.0
    right_mid = (mid + b) / 2.0

    f_left_mid = f(left_mid)
    f_right_mid = f(right_mid)

    left_value = simpson(f, a, mid, fa, f_left_mid, fm)
    right_value = simpson(f, mid, b, fm, f_right_mid, fb)

    # 如果左右兩半的和已經夠接近原本整段的估計值
    # 就可以停止遞迴
    if depth <= 0 or abs(left_value + right_value - whole) <= 15.0 * eps:
        return left_value + right_value + (left_value + right_value - whole) / 15.0

    # 否則就繼續往左右兩邊細分
    return (
        adaptive_simpson(f, a, mid, fa, f_left_mid, fm, left_value, eps / 2.0, depth - 1)
        + adaptive_simpson(f, mid, b, fm, f_right_mid, fb, right_value, eps / 2.0, depth - 1)
    )


def integrate_uncovered_length(umbrellas, road_width, total_time):
    # f(t) 代表時間 t 時
    # 還沒有被雨傘遮住的長度
    def f(t):
        covered = covered_length_at_time(umbrellas, road_width, t)
        return road_width - covered

    # 如果時間是 0，答案自然就是 0
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
    # 先把所有輸入切成 token
    data = sys.stdin.read().strip().split()

    if not data:
        return

    it = iter(data)

    # 讀入 N, W, T, V
    n = int(next(it))
    w = float(next(it))
    t = float(next(it))
    v_rain = float(next(it))

    umbrellas = []

    # 讀入每一把傘
    for _ in range(n):
        x = float(next(it))
        length = float(next(it))
        velocity = float(next(it))
        umbrellas.append((x, length, velocity))

    # 先算在 0~T 之間，未遮蔽長度對時間的積分
    uncovered_integral = integrate_uncovered_length(umbrellas, w, t)

    # 再乘上單位面積單位時間降雨量
    answer = uncovered_integral * v_rain

    # 題目要求輸出到小數點後兩位
    print(f"{answer:.2f}")


if __name__ == "__main__":
    main()