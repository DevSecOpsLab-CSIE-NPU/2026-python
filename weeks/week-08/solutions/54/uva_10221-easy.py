import math
import sys


def solve(data: str) -> str:
    ans: list[str] = []

    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue

        s_text, a_text, unit = line.split()
        r = 6440.0 + float(s_text)
        angle = float(a_text)

        if unit == "min":
            angle /= 60.0
        if angle > 180.0:
            angle = 360.0 - angle

        rad = math.radians(angle)
        arc = r * rad
        chord = 2.0 * r * math.sin(rad / 2.0)
        ans.append(f"{arc:.6f} {chord:.6f}")

    return "\n".join(ans)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
