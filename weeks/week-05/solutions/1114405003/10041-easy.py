import sys


def solve():
    # 這題的核心觀念很簡單：
    # 把所有門牌號碼排序後，選中位數，總距離一定最小。
    # 因為中位數左右兩邊的距離會盡量互相抵銷。
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    count = data[0]
    index = 1
    answers = []

    for _ in range(count):
        n = data[index]
        index += 1

        houses = data[index:index + n]
        index += n

        # 排序後直接抓正中間的位置。
        houses.sort()
        median = houses[n // 2]

        # 把每一戶到中位數的距離加總起來。
        total = 0
        for value in houses:
            if value > median:
                total += value - median
            else:
                total += median - value

        answers.append(str(total))

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    solve()