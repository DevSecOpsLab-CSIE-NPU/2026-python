import sys


def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    test_count = int(data[0])
    index = 1
    answers = []

    for _ in range(test_count):
        total = int(data[index])
        diff = int(data[index + 1])
        index += 2

        if total < diff or (total + diff) % 2 != 0:
            answers.append("impossible")
            continue

        bigger = (total + diff) // 2
        smaller = (total - diff) // 2

        if smaller < 0:
            answers.append("impossible")
        else:
            answers.append(f"{bigger} {smaller}")

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    solve()