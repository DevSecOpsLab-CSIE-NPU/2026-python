import sys
import math


def ceil_sqrt(number):
    """
    計算 ceil(sqrt(number))。

    math.isqrt(number) 會得到 floor(sqrt(number))。
    如果 root * root 剛好等於 number，代表 number 是完全平方數，
    那 ceil(sqrt(number)) 就是 root。

    如果 root * root 小於 number，
    代表真正的 sqrt(number) 介於 root 和 root + 1 之間，
    所以 ceil(sqrt(number)) 要回傳 root + 1。
    """

    root = math.isqrt(number)

    if root * root == number:
        return root

    return root + 1


def count_square_numbers(a, b):
    """
    計算閉區間 [a, b] 中有多少個完全平方數。

    若 k² 落在 [a, b] 內，代表：
    a <= k² <= b

    對 k 來說，也就是：
    ceil(sqrt(a)) <= k <= floor(sqrt(b))

    因此答案為：
    floor(sqrt(b)) - ceil(sqrt(a)) + 1
    """

    left = ceil_sqrt(a)
    right = math.isqrt(b)

    if left > right:
        return 0

    return right - left + 1


def solve(data):
    """
    處理整份輸入資料。

    每筆資料有兩個整數 a 和 b。
    當讀到 0 0 時代表結束，不需要輸出。
    """

    tokens = data.split()
    answers = []

    for i in range(0, len(tokens), 2):
        a = int(tokens[i])
        b = int(tokens[i + 1])

        if a == 0 and b == 0:
            break

        answers.append(str(count_square_numbers(a, b)))

    return "\n".join(answers)


def main():
    data = sys.stdin.read()
    result = solve(data)
    print(result)


if __name__ == "__main__":
    main()