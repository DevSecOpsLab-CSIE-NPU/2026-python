import math
import sys


LIMIT = 500


def precompute():
    # 用「累加新加入的 n」來建表，比起每次查詢都重算快很多。
    table = [0] * (LIMIT + 1)
    running = 0

    for n in range(1, LIMIT + 1):
        for i in range(1, n):
            running += math.gcd(i, n)
        table[n] = running

    return table


ANS = precompute()


def solve(data):
    # 輸入直到遇到 0 為止。
    result = []
    for text in data.split():
        n = int(text)
        if n == 0:
            break
        result.append(str(ANS[n]))
    return "\n".join(result)


if __name__ == "__main__":
    sys.stdout.write(solve(sys.stdin.read()))