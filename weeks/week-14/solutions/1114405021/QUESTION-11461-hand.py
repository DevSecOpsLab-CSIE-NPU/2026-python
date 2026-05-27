import sys


def count_squares(a, b):
    count = 0
    root = 1
    square = 1

    # 一個一個往上找平方數，直到超過上界 b。
    while square <= b:
        if square >= a:
            count += 1
        root += 1
        square = root * root

    return count


def solve(data):
    outputs = []
    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue

        a, b = map(int, line.split())
        if a == 0 and b == 0:
            break

        outputs.append(str(count_squares(a, b)))

    return "\n".join(outputs)


if __name__ == "__main__":
    sys.stdout.write(solve(sys.stdin.read()))