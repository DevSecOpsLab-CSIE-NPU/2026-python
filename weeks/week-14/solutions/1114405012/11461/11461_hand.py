import sys
from math import isqrt

def main() -> None:
    answers = []

    for line in sys.stdin:
        a, b = map(int, line.split())

        if a == 0 and b == 0:
            break

        count = isqrt(b) - isqrt(a - 1)
        answers.append(str(count))
    sys.stdout.write("\n".join(answers))
if __name__ == "__main__":
    main()