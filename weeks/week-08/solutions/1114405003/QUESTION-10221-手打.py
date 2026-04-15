import math
import sys


EARTH_RADIUS = 6440.0


def solve_one(s, a, unit):
    # 先把角度統一成 degree
    angle_deg = a / 60.0 if unit == "min" else a

    # 題目要取兩點之間較短的弧
    if angle_deg > 180.0:
        angle_deg = 360.0 - angle_deg

    r = EARTH_RADIUS + s
    rad = math.radians(angle_deg)

    arc = r * rad
    chord = 2.0 * r * math.sin(rad / 2.0)
    return arc, chord


def main():
    out = []
    for line in sys.stdin.read().splitlines():
        line = line.strip()
        if not line:
            continue
        s_str, a_str, unit = line.split()
        s = float(s_str)
        a = float(a_str)
        arc, chord = solve_one(s, a, unit)
        out.append(f"{arc:.6f} {chord:.6f}")

    sys.stdout.write("\n".join(out))
    if out:
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
