import sys
from math import gcd


# 逐行讀入 N，直到遇到 0 為止。
def main() -> None:
    outputs = []

    for line in sys.stdin:
        n = int(line.strip())
        if n == 0:
            break

        total = 0

        # 直接枚舉所有 1 <= i < j <= N 的組合。
        # 因為 N 最大只有 500，所以這種寫法已經夠快，也很好理解。
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                total += gcd(i, j)

        outputs.append(str(total))

    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    main()
