import sys


EPS = 1e-10


def build_segments(x, length, velocity, road_width, total_time):
    """建立每把傘的直線運動分段。"""
    travel_range = road_width - length

    # 沒有空間移動，或速度為 0，就視為靜止
    if total_time <= EPS:
        return []
    if velocity == 0 or travel_range <= EPS:
        return [(0.0, total_time, float(x), 0.0, float(length))]

    speed = abs(velocity)
    direction = 1.0 if velocity > 0 else -1.0
    now = 0.0
    position = float(x)
    segments = []

    while now < total_time - EPS:
        # 根據目前前進方向，決定下一個會碰到的邊界
        boundary = travel_range if direction > 0 else 0.0

        # 距離最近邊界的距離
        if direction > 0:
            distance = boundary - position
        else:
            distance = position - boundary

        # 已經在邊界上，直接反向，避免卡住
        if distance <= EPS:
            # 剛好卡在邊界上就直接反向，避免數值誤差造成死循環
            position = boundary
            direction = -direction
            continue

        delta = distance / speed
        end_time = now + delta

        # 如果來不及撞到邊界就結束
        if end_time >= total_time - EPS:
            # 這一段到時間結束都不會再碰到邊界
            segments.append((now, total_time, position, direction * speed, float(length)))
            break

        segments.append((now, end_time, position, direction * speed, float(length)))

        # 到達邊界後反彈
        now = end_time
        position = boundary
        direction = -direction

    return segments


def union_length_at_time(lines, tau):
    """計算某一時刻所有線段的聯集長度。"""
    intervals = []
    for left_pos, velocity, length in lines:
        # 先把每把傘的左端點推到時間 tau 的位置，再形成區間
        left = left_pos + velocity * tau
        intervals.append((left, left + length))

    intervals.sort()

    total = 0.0
    current_left, current_right = intervals[0]

    for left, right in intervals[1:]:
        if left > current_right + EPS:
            # 遇到不重疊的區間，先把前一段長度累加進去
            total += current_right - current_left
            current_left, current_right = left, right
        else:
            # 重疊時只需要把右端點往右延伸
            if right > current_right:
                current_right = right

    total += current_right - current_left
    return total


def main():
    # 題目是單筆輸入
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    road_width = float(data[1])
    total_time = float(data[2])
    rain_volume = float(data[3])

    # 每把傘先展開成多段「等速度運動」區間
    umbrellas = []
    index = 4
    for _ in range(n):
        # 每一把傘都記錄初始位置、長度與速度
        x = int(data[index])
        length = int(data[index + 1])
        velocity = int(data[index + 2])
        index += 3
        umbrellas.append(build_segments(x, length, velocity, road_width, total_time))

    # 收集所有會改變運動狀態的時間點
    time_points = {0.0, total_time}
    for segments in umbrellas:
        for start_time, end_time, _, _, _ in segments:
            time_points.add(start_time)
            time_points.add(end_time)

    time_points = sorted(time_points)

    current_index = [0] * n
    covered_area = 0.0

    for left_time, right_time in zip(time_points, time_points[1:]):
        if right_time - left_time <= EPS:
            continue

        # 取出這段時間內，每把傘的左端點位置與速度
        lines = []
        for umbrella_id in range(n):
            segs = umbrellas[umbrella_id]

            while (
                current_index[umbrella_id] + 1 < len(segs)
                and segs[current_index[umbrella_id]][1] <= left_time + EPS
            ):
                current_index[umbrella_id] += 1

            start_time, end_time, left_pos, velocity, length = segs[current_index[umbrella_id]]
            # 把目前區間起點的左端點位置算出來，後面就能當成線性函數處理
            left_at_left_time = left_pos + velocity * (left_time - start_time)
            lines.append((left_at_left_time, velocity, length))

        # 再把端點相交的時間切出來
        split_times = [left_time, right_time]
        endpoints = []
        for left_pos, velocity, length in lines:
            # 每把傘有左端點與右端點，兩者都可能和別把傘的端點交會
            endpoints.append((left_pos, velocity))
            endpoints.append((left_pos + length, velocity))

        for i in range(len(endpoints)):
            p1, v1 = endpoints[i]
            for j in range(i + 1, len(endpoints)):
                p2, v2 = endpoints[j]
                if abs(v1 - v2) <= EPS:
                    continue

                t = left_time + (p2 - p1) / (v1 - v2)
                if left_time + EPS < t < right_time - EPS:
                    # 只把真正落在區間內的交會時間拿來切段
                    split_times.append(t)

        split_times.sort()
        unique_times = [split_times[0]]
        for t in split_times[1:]:
            if t - unique_times[-1] > 1e-9:
                unique_times.append(t)

        # 在每個最小子區間內，聯集長度是線性的
        for u, v in zip(unique_times, unique_times[1:]):
            if v - u <= EPS:
                continue

            # 在小區間兩端取聯集長度，用梯形公式積分
            tau_u = u - left_time
            tau_v = v - left_time
            length_u = union_length_at_time(lines, tau_u)
            length_v = union_length_at_time(lines, tau_v)
            covered_area += (length_u + length_v) * (v - u) / 2.0

    # 沒被傘遮住的雨量 = 總雨量 - 被傘遮住的量
    answer = max(0.0, (road_width * total_time - covered_area) * rain_volume)
    print(f'{answer:.2f}')


if __name__ == '__main__':
    main()
