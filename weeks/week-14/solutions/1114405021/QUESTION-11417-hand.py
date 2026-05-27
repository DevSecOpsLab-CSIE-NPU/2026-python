import sys
from math import gcd


MAX_N = 500
answers = [0] * (MAX_N + 1)

for n in range(1, MAX_N + 1):
    total = 0
    for i in range(1, n):
        total += gcd(i, n)
    answers[n] = answers[n - 1] + total


def solve(data):
    output = []
    for token in data.split():
        n = int(token)
        if n == 0:
            break
        output.append(str(answers[n]))
    return "\n".join(output)


if __name__ == "__main__":
    sys.stdout.write(solve(sys.stdin.read()))