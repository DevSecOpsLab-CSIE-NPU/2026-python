import sys
import math


def is_square(number):
    """
    判斷 number 是否為完全平方數。

    math.isqrt(number) 會回傳不超過 sqrt(number) 的最大整數。
    如果 root * root 剛好等於 number，
    代表 number 可以被寫成 root 的平方，
    所以它就是完全平方數。
    """

    root = math.isqrt(number)
    return root * root == number


def count_squares(a, b):
    """
    用直觀方式計算 [a, b] 中有幾個完全平方數。

    因為 b 最大是 100000，
    所以我們可以從 1 開始產生平方數：

    1², 2², 3², ...

    只要平方數不超過 b，就檢查它是否大於等於 a。
    如果落在 [a, b] 內，就把答案加 1。
    """

    count = 0
    number = 1

    while number * number <= b:
        square = number * number

        if square >= a:
            count += 1

        number += 1

    return count


def solve(data):
    """
    讀取所有輸入並產生輸出。

    每一組資料有 a 和 b。
    如果遇到 0 0，表示結束。
    """

    parts = data.split()
    output = []

    for i in range(0, len(parts), 2):
        a = int(parts[i])
        b = int(parts[i + 1])

        if a == 0 and b == 0:
            break

        output.append(str(count_squares(a, b)))

    return "\n".join(output)


def main():
    data = sys.stdin.read()
    answer = solve(data)
    print(answer)


if __name__ == "__main__":
    main()