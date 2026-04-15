import math
import sys


def solve(data: str) -> str:
    out: list[str] = []
    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue

        s_text, a_text, unit = line.split()
        r = 6440.0 + float(s_text)
        a = float(a_text)
        if unit == "min":
            a /= 60.0
        if a > 180.0:
            a = 360.0 - a

        rad = math.radians(a)
        arc = r * rad
        chord = 2.0 * r * math.sin(rad / 2.0)
        out.append(f"{arc:.6f} {chord:.6f}")

    return "\n".join(out)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
