import sys


EPS = 1e-10


def build_segments(x, length, velocity, road_width, total_time):
    travel_range = road_width - length

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
        boundary = travel_range if direction > 0 else 0.0

        if direction > 0:
            distance = boundary - position
        else:
            distance = position - boundary

        if distance <= EPS:
            position = boundary
            direction = -direction
            continue

        delta = distance / speed
        end_time = now + delta

        if end_time >= total_time - EPS:
            segments.append((now, total_time, position, direction * speed, float(length)))
            break

        segments.append((now, end_time, position, direction * speed, float(length)))
        now = end_time
        position = boundary
        direction = -direction

    return segments


def union_length_at_time(lines, tau):
    intervals = []
    for left_pos, velocity, length in lines:
        left = left_pos + velocity * tau
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

    umbrellas = []
    index = 4
    for _ in range(n):
        x = int(data[index])
        length = int(data[index + 1])
        velocity = int(data[index + 2])
        index += 3
        umbrellas.append(build_segments(x, length, velocity, road_width, total_time))

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

        lines = []
        for umbrella_id in range(n):
            segs = umbrellas[umbrella_id]

            while (
                current_index[umbrella_id] + 1 < len(segs)
                and segs[current_index[umbrella_id]][1] <= left_time + EPS
            ):
                current_index[umbrella_id] += 1

            start_time, end_time, left_pos, velocity, length = segs[current_index[umbrella_id]]
            left_at_left_time = left_pos + velocity * (left_time - start_time)
            lines.append((left_at_left_time, velocity, length))

        split_times = [left_time, right_time]
        endpoints = []
        for left_pos, velocity, length in lines:
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
                    split_times.append(t)

        split_times.sort()
        unique_times = [split_times[0]]
        for t in split_times[1:]:
            if t - unique_times[-1] > 1e-9:
                unique_times.append(t)

        for u, v in zip(unique_times, unique_times[1:]):
            if v - u <= EPS:
                continue

            tau_u = u - left_time
            tau_v = v - left_time
            length_u = union_length_at_time(lines, tau_u)
            length_v = union_length_at_time(lines, tau_v)
            covered_area += (length_u + length_v) * (v - u) / 2.0

    answer = max(0.0, (road_width * total_time - covered_area) * rain_volume)
    print(f'{answer:.2f}')


if __name__ == '__main__':
    main()
