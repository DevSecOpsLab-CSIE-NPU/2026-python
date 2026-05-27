import sys
from math import gcd


# 簡化版：
# 直接把每一組 N 讀進來，然後把所有 i < j 的 gcd 加總起來。
def main() -> None:
    answers = []

    for line in sys.stdin:
        # 題目用 0 當作結束符號。
        n = int(line.strip())
        if n == 0:
            break

        # 暴力枚舉每一對數字，
        # 這題 N 最多只有 500，所以寫成雙迴圈也很容易記。
        total = 0
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                total += gcd(i, j)

        answers.append(str(total))

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    main()
