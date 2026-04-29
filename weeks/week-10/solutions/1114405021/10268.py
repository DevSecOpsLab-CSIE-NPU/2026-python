# UVA 10268 - 498-bis
import sys


def solve_standard():
    """
    Standard: 使用 sys.stdin.read 配合 Horner's Method 高效求導。
    """
    input_data = sys.stdin.read().splitlines()
    i = 0
    while i < len(input_data):
        try:
            x = int(input_data[i].strip())
            coeffs = list(map(int, input_data[i + 1].split()))

            n = len(coeffs) - 1
            result = 0

            for j in range(n):
                term = coeffs[j] * (n - j)
                result = result * x + term

            print(result)
            i += 2
        except:
            break


def solve_easy():
    """
    Easy: 直觀計算多項式微商的值，使用 pow()。
    """
    while True:
        try:
            line = input()
            if not line.strip():
                continue
            x = int(line)
            coeffs = list(map(int, input().split()))

            n = len(coeffs) - 1
            res = 0
            for i in range(n):
                power = n - 1 - i
                term_coeff = coeffs[i] * (n - i)
                res += term_coeff * (x**power)

            print(res)
        except EOFError:
            break


def solve_manual():
    """
    Manual: 避免 pow，純手寫迴圈累乘 (Horner's Method 手刻版)，防止大數字超時。
    """
    while True:
        try:
            x_str = input()
            if not x_str.strip():
                continue
            x = int(x_str)

            coeffs_str = input().split()
            coeffs = []
            for c in coeffs_str:
                coeffs.append(int(c))

            n = len(coeffs) - 1
            res = 0

            # 使用 Horner's Rule 求多項式微商值 (較快且避免超大指數)
            for j in range(n):
                coeff = coeffs[j] * (n - j)
                if j == 0:
                    res = coeff
                else:
                    res = res * x + coeff

            if n == 0:
                print(0)
            else:
                print(res)
        except EOFError:
            break


if __name__ == "__main__":
    solve_standard()
