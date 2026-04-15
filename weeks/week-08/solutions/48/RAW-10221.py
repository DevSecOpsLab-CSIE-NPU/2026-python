import math
import sys


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        s, angle, unit = line.split()
        s = float(s)
        angle = float(angle)

        if unit == 'min':
            angle = angle / 60.0
        radians = math.radians(angle)

        radius = 6440.0 + s
        arc_length = radius * radians
        chord_length = 2.0 * radius * math.sin(radians / 2.0)

        print(f'{arc_length:.6f} {chord_length:.6f}')


if __name__ == '__main__':
    main()
