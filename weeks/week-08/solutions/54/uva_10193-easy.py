import math
import sys


def solve(data: str) -> str:
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if not lines:
        return ""

    t = int(lines[0])
    ans: list[str] = []
    p = 1

    for i in range(1, t + 1):
        x = int(lines[p], 2)
        y = int(lines[p + 1], 2)
        p += 2
        if math.gcd(x, y) > 1:
            ans.append(f"Pair #{i}: All you need is love!")
        else:
            ans.append(f"Pair #{i}: Love is not all you need!")

    return "\n".join(ans)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
