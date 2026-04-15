import math
import sys


YES = "All you need is love!"
NO = "Love is not all you need!"


def is_love(a: str, b: str) -> bool:
    return math.gcd(int(a, 2), int(b, 2)) > 1


def solve(data: str) -> str:
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if not lines:
        return ""

    t = int(lines[0])
    out: list[str] = []
    idx = 1

    for case_no in range(1, t + 1):
        a = lines[idx]
        b = lines[idx + 1]
        idx += 2
        out.append(f"Pair #{case_no}: {YES if is_love(a, b) else NO}")

    return "\n".join(out)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
