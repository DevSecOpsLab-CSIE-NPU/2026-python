import math
import sys

def solve(text):

    out = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue

        s, angle, unit = line.split()
        s = int(s)
        angle = float(angle)

        radius = 6440 + s

        if unit == "deg":
            theta = math.radians(angle)
        else:
            theta = math.radians(angle / 60.0)

        arc = radius * theta
        chord = 2 * radius * math.sin(theta / 2.0)

        out.append(f"{arc:.6f} {chord:.6f}")

    return "\n".join(out)

def main():
    sys.stdout.write(solve(sys.stdin.read()))

if __name__ == "__main__":
    main()
    