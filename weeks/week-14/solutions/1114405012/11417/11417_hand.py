import sys
from math import gcd

def main() -> None:
    answers = []

    for line in sys.stdin:
        n = int(line.strip())
        if n == 0:
            break

        total = 0
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                total += gcd(i, j)

        answers.append(str(total)) 
if __name__ == "__main__":
    main()