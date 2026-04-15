"""
UVA 10190 (課程版本敘述)
AI 教學簡單版本（含中文註解）

說明：
- 依照題目描述，計算 0 到 T 秒內，落在馬路上的雨水體積。
- 由於自動傘會移動，這裡用「時間離散 + 中點積分」做近似。
"""

import sys


def reflected_position(x: float, v: float, t: float, right_bound: float) -> float:
    """計算在 [0, right_bound] 之間來回反射後的位置。"""
    if right_bound <= 0:
        return 0.0

    raw = x + v * t
    period = 2.0 * right_bound
    mod = raw % period

    if mod <= right_bound:
        return mod
    return period - mod


def union_length(intervals: list[tuple[float, float]], width: float) -> float:
    """計算區間聯集長度（會裁切到 [0, width]）。"""
    clipped = []
    for left, right in intervals:
        l = max(0.0, left)
        r = min(width, right)
        if l < r:
            clipped.append((l, r))

    if not clipped:
        return 0.0

    clipped.sort()
    total = 0.0
    cur_l, cur_r = clipped[0]

    for l, r in clipped[1:]:
        if l <= cur_r:
            cur_r = max(cur_r, r)
        else:
            total += cur_r - cur_l
            cur_l, cur_r = l, r

    total += cur_r - cur_l
    return total


def solve_case(n: int, w: float, t_total: float, rain_v: float, umbrellas: list[tuple[float, float, float]]) -> float:
    """用數值積分近似總雨量。"""
    if t_total <= 0 or w <= 0 or rain_v <= 0:
        return 0.0

    # 簡單版本：固定時間切片數，兼顧精度與可讀性
    steps = max(4000, min(200000, int(t_total * 300)))
    dt = t_total / steps

    integral_uncovered = 0.0

    for k in range(steps):
        now = (k + 0.5) * dt
        intervals = []

        for x0, length, speed in umbrellas:
            if length >= w:
                intervals = [(0.0, w)]
                break

            travel_right = w - length
            left = reflected_position(x0, speed, now, travel_right)
            intervals.append((left, left + length))

        covered = union_length(intervals, w)
        uncovered = max(0.0, w - covered)
        integral_uncovered += uncovered * dt

    return integral_uncovered * rain_v


def parse_and_solve(data: str) -> str:
    """支援單組或多組（讀到 EOF）。"""
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if not lines:
        return ""

    idx = 0
    outputs = []

    while idx < len(lines):
        n, w, t_total, rain_v = map(float, lines[idx].split())
        n = int(n)
        idx += 1

        umbrellas = []
        for _ in range(n):
            x, length, speed = map(float, lines[idx].split())
            idx += 1
            umbrellas.append((x, length, speed))

        ans = solve_case(n, w, t_total, rain_v, umbrellas)
        outputs.append(f"{ans:.2f}")

    return "\n".join(outputs)


def main() -> None:
    data = sys.stdin.read()
    print(parse_and_solve(data))


if __name__ == "__main__":
    main()
