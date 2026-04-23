import sys
import math

def main():
    for line in sys.stdin:
        parts = line.split()
        s = int(parts[0])
        a = float(parts[1])
        unit = parts[2]
        r = 6440 + s
        if unit == 'min':
            a_deg = a / 60.0
        else:
            a_deg = a
        a_rad = math.radians(a_deg)
        arc = r * a_rad
        chord = 2 * r * math.sin(a_rad / 2)
        print(f"{arc:.6f} {chord:.6f}")

if __name__ == "__main__":
    main()