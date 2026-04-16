import math

while True:
    try:
        line = input().split()
    except EOFError:
        break

    s = int(line[0])
    a_val = int(line[1])
    unit = line[2]

    if unit == 'deg':
        angle = math.radians(a_val)
    else:
        angle = math.radians(a_val / 60.0)

    r = 6440 + s
    arc = r * angle
    chord = 2 * r * math.sin(angle / 2)
    print(f"{arc:.6f} {chord:.6f}")
