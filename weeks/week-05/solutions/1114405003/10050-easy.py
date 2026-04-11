import sys


def solve():
    # 這題只要記住兩件事：
    # 1. 罷工是固定週期出現。
    # 2. 星期五、星期六不算工作天。
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    index = 0
    test_cases = data[index]
    index += 1
    answers = []

    for _ in range(test_cases):
        days = data[index]
        index += 1

        parties = data[index]
        index += 1

        lost = set()

        for _ in range(parties):
            period = data[index]
            index += 1

            # 從 period 開始，每隔 period 天就會罷工一次。
            for day in range(period, days + 1, period):
                # day % 7 = 6 代表星期五，day % 7 = 0 代表星期六。
                if day % 7 != 6 and day % 7 != 0:
                    lost.add(day)

        answers.append(str(len(lost)))

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    solve()