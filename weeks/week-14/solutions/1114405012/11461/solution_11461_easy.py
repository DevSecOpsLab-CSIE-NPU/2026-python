import sys
from math import isqrt


# 簡化版：
# 這題只要算區間 [a, b] 裡面有幾個完全平方數。
def main() -> None:
    answers = []

    for line in sys.stdin:
        a, b = map(int, line.split())

        # 0 0 是結束符號，不需要輸出。
        if a == 0 and b == 0:
            break

        # 小於等於 b 的平方數個數是 isqrt(b)，
        # 小於 a 的平方數個數是 isqrt(a - 1)，
        # 兩者相減就是區間內的答案。
        count = isqrt(b) - isqrt(a - 1)
        answers.append(str(count))

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    main()
