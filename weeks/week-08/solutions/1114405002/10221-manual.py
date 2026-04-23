# 手打版衛星距離計算程式
# 手動處理輸入

import sys
import math

def main():
    lines = sys.stdin.readlines()
    for line in lines:
        parts = line.split()
        if not parts:
            continue
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