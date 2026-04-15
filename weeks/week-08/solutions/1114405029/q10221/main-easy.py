import math
import sys


EARTH_RADIUS = 6440.0


def solve_case(s, a, unit):
    # 先算出衛星到地心的距離
    radius = EARTH_RADIUS + s

    # 如果輸入單位是 min，表示角分
    # 要先除以 60 變成度
    if unit == "min":
        degree = a / 60.0
    else:
        degree = a

    # 圓上兩點之間有長弧和短弧
    # 題目要的是較短距離，所以要取較小中心角
    if degree > 180.0:
        degree = 360.0 - degree

    # 數學公式需要弧度，所以再把 degree 轉成 radian
    rad = math.radians(degree)

    # 弧長公式：r * a
    arc = radius * rad

    # 弦長公式：2 * r * sin(a / 2)
    chord = 2.0 * radius * math.sin(rad / 2.0)

    return arc, chord


def main():
    # 一次讀入所有輸入行
    lines = sys.stdin.read().strip().splitlines()

    if not lines:
        return

    outputs = []

    # 每一行都是一組測資
    for line in lines:
        if not line.strip():
            continue

        s_str, a_str, unit = line.split()

        s = float(s_str)
        a = float(a_str)

        arc, chord = solve_case(s, a, unit)

        # 依題目要求輸出到小數點後六位
        outputs.append(f"{arc:.6f} {chord:.6f}")

    print("\n".join(outputs))


if __name__ == "__main__":
    main()