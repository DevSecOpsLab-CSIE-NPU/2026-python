import sys
import math


def calculate_answer(n):
    """
    用最直觀的方式計算答案。

    題目要我們找出所有 i < j 的組合，
    所以可以直接用兩層 for 迴圈：

    第一層控制 i。
    第二層控制 j。

    j 從 i + 1 開始，是因為題目要求 i 必須小於 j。
    """

    answer = 0

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # math.gcd(i, j) 會回傳 i 和 j 的最大公因數
            answer += math.gcd(i, j)

    return answer


def solve(data):
    """
    讀取所有輸入並產生輸出。

    每一行是一個 N。
    如果 N 是 0，就結束。
    否則就計算該 N 的 gcd 總和。
    """

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