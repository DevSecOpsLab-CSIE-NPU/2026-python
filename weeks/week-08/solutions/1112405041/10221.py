import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return

    idx = 0
    while idx < len(input_data):
        try:
            s = float(input_data[idx])
            a = float(input_data[idx+1])
            unit = input_data[idx+2]
            idx += 3

            r = 6440 + s

            # Convert angle to degrees first, then check > 180
            if unit == 'min':
                angle_deg = a / 60.0
            else:
                angle_deg = a

            # If angle > 180, take the smaller arc
            if angle_deg > 180:
                angle_deg = 360 - angle_deg

            angle_rad = math.radians(angle_deg)

            arc_len = r * angle_rad
            chord_len = 2 * r * math.sin(angle_rad / 2.0)

            print(f"{arc_len:.6f} {chord_len:.6f}")
        except (EOFError, IndexError):
            break

if __name__ == "__main__":
    solve()
