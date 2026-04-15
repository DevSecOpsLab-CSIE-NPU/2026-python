import math
import sys


EARTH_RADIUS = 6440.0


def solve_case(s, a, unit):
    # 衛星到地心的半徑
    radius = EARTH_RADIUS + s

    # 先把角度統一成 degree
    if unit == "min":
        degree = a / 60.0
    else:
        degree = a

    # 取較小的中心角
    if degree > 180.0:
        degree = 360.0 - degree

    # 轉成弧度
    rad = math.radians(degree)

    # 計算弧長與弦長
    arc = radius * rad
    chord = 2.0 * radius * math.sin(rad / 2.0)

    return arc, chord


def main():
    lines = sys.stdin.read().strip().splitlines()
    if not lines:
        return

    outputs = []

    for line in lines:
        if not line.strip():
            continue

        s_str, a_str, unit = line.split()
        s = float(s_str)
        a = float(a_str)

        arc, chord = solve_case(s, a, unit)
        outputs.append(f"{arc:.6f} {chord:.6f}")

    print("\n".join(outputs))


if __name__ == "__main__":
    main()