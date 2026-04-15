"""
UVA 10190 (課程版本敘述)
手打版本
"""

import sys


def bounce_pos(x0: float, v: float, t: float, span: float) -> float:
    if span <= 0:
        return 0.0

    value = x0 + v * t
    cycle = 2.0 * span
    r = value % cycle

    if r <= span:
        return r
    return cycle - r


def merge_len(segs: list[tuple[float, float]], width: float) -> float:
    arr = []
    for a, b in segs:
        left = max(0.0, a)
        right = min(width, b)
        if left < right:
            arr.append((left, right))

    if not arr:
        return 0.0

    arr.sort()
    total = 0.0
    s, e = arr[0]

    for a, b in arr[1:]:
        if a <= e:
            if b > e:
                e = b
        else:
            total += e - s
            s, e = a, b

    total += e - s
    return total


def solve_one_case(n: int, w: float, t_total: float, v_rain: float, items: list[tuple[float, float, float]]) -> float:
    if t_total <= 0 or w <= 0 or v_rain <= 0:
        return 0.0

    parts = max(4000, min(200000, int(t_total * 300)))
    dt = t_total / parts

    area_time = 0.0

    for i in range(parts):
        now = (i + 0.5) * dt
        segs = []

        for x0, length, speed in items:
            if length >= w:
                segs = [(0.0, w)]
                break

            span = w - length
            left = bounce_pos(x0, speed, now, span)
            segs.append((left, left + length))

        covered = merge_len(segs, w)
        free_len = w - covered
        if free_len < 0:
            free_len = 0.0

        area_time += free_len * dt

    return area_time * v_rain


def run(text: str) -> str:
    rows = [r.strip() for r in text.splitlines() if r.strip()]
    if not rows:
        return ""

    p = 0
    outs = []

    while p < len(rows):
        n_f, w, t_total, v_rain = map(float, rows[p].split())
        p += 1
        n = int(n_f)

        items = []
        for _ in range(n):
            x0, length, speed = map(float, rows[p].split())
            p += 1
            items.append((x0, length, speed))

        value = solve_one_case(n, w, t_total, v_rain, items)
        outs.append(f"{value:.2f}")

    return "\n".join(outs)


def main() -> None:
    text = sys.stdin.read()
    print(run(text))


if __name__ == "__main__":
    main()
