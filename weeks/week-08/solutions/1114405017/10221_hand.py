import math, sys
R = 6440
for line in sys.stdin:
    if not line.strip(): continue
    s_val, a_val, unit = line.split()
    s, a = float(s_val), float(a_val)
    deg = a / 60 if unit == 'min' else a
    deg = min(deg, 360 - deg) if deg > 180 else deg
    r = R + s
    rad = deg * math.pi / 180
    print(f"{r * rad:.6f} {2 * r * math.sin(rad / 2):.6f}")