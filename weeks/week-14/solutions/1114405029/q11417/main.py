import sys
import math


def gcd_sum(n):
    """
    計算 1 ≤ i < j ≤ n 的所有 gcd(i, j) 總和。

    本題 N 最大只有 500，所以可以直接使用雙層迴圈列舉所有數對。
    外層 i 從 1 到 n - 1。
    內層 j 從 i + 1 到 n。

    這樣可以保證：
    1. 不會算到 i = j。
    2. 不會重複計算 gcd(i, j) 和 gcd(j, i)。
    """

    total = 0

    for i in range(1, n):
        for j in range(i + 1, n + 1):
            total += math.gcd(i, j)

    return total


def solve(data):
    """
    處理整份輸入資料。

    輸入會有多個 N，每個 N 代表一筆測試資料。
    當讀到 N = 0 時代表結束，不需要處理 0，也不需要輸出。
    """

    numbers = data.split()
    answers = []

    for item in numbers:
        n = int(item)

        if n == 0:
            break

        answers.append(str(gcd_sum(n)))

    return "\n".join(answers)


def main():
    data = sys.stdin.read()
    result = solve(data)
    print(result)


if __name__ == "__main__":
    main()