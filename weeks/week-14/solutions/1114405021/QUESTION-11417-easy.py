import sys
from math import gcd


# 先把 1~500 的答案全部算好。
# 想法很簡單：把每個 N 當作「新增一個數字 N」來看，
# 只要把 gcd(1, N)、gcd(2, N)...、gcd(N-1, N) 全部加起來，
# 再累加到前一題的答案上就好。
MAX_N = 500
prefix_answers = [0] * (MAX_N + 1)

for current in range(1, MAX_N + 1):
    pair_total = 0
    for other in range(1, current):
        pair_total += gcd(other, current)
    prefix_answers[current] = prefix_answers[current - 1] + pair_total


def solve(data):
    outputs = []
    for token in data.split():
        n = int(token)
        if n == 0:
            break
        outputs.append(str(prefix_answers[n]))
    return "\n".join(outputs)


def main():
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()