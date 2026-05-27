import sys
import math


def calculate_answer(n):
    answer = 0

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            answer += math.gcd(i, j)

    return answer


def solve(data):
    lines = data.split()
    output = []

    for line in lines:
        n = int(line)

        if n == 0:
            break

        result = calculate_answer(n)
        output.append(str(result))

    return "\n".join(output)


def main():
    data = sys.stdin.read()
    answer = solve(data)
    print(answer)


if __name__ == "__main__":
    main()