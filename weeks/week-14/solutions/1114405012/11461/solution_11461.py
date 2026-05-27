import sys
from math import isqrt


# 逐行讀入區間 [a, b]，直到遇到 0 0 結束。
def main() -> None:
    outputs = []

    for line in sys.stdin:
        a, b = map(int, line.split())
        if a == 0 and b == 0:
            break

        # 區間內完全平方數個數 = floor(sqrt(b)) - floor(sqrt(a - 1))
        # 因為平方數是 1, 4, 9, 16, ...，只要知道上下界各有幾個平方數即可。
        count = isqrt(b) - isqrt(a - 1)
        outputs.append(str(count))

    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    main()
