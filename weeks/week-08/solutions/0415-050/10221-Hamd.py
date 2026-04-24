import sys
import math

EARTH_RADIUS = 6440

def solve(s, a, unit):
    r = EARTH_RADIUS + s
    if unit == 'min':
        a /= 60.0
    if a > 180:
        a = 360 - a
    angle_rad = math.radians(a)
    arc_length = r * angle_rad
    chord_length = 2 * r * math.sin(angle_rad / 2)
    return arc_length, chord_length

if __name__ == '__main__':
    for line in sys.stdin:
        s, a, unit = line.strip().split()
        arc, chord = solve(float(s), float(a), unit)
        print(f"{arc:.6f} {chord:.6f}")