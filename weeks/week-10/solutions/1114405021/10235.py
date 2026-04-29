# UVA 10235 - Simply Emirp
import sys
import math


def standard_solution():
    """
    Standard: 使用高效素數篩法或平方根判斷。
    """

    def is_prime(n):
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(math.isqrt(n)) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    for line in sys.stdin:
        n_str = line.strip()
        if not n_str:
            continue
        n = int(n_str)
        if not is_prime(n):
            print(f"{n} is not prime.")
        else:
            rev_n = int(n_str[::-1])
            if rev_n != n and is_prime(rev_n):
                print(f"{n} is emirp.")
            else:
                print(f"{n} is prime.")


def easy_solution():
    """
    Easy: 使用直觀的平方根迴圈判斷質數，內建字串反轉。
    """

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    while True:
        try:
            line = input()
            n = int(line)
        except EOFError:
            break

        if not is_prime(n):
            print(f"{n} is not prime.")
        else:
            rev_n = int(str(n)[::-1])
            if rev_n != n and is_prime(rev_n):
                print(f"{n} is emirp.")
            else:
                print(f"{n} is prime.")


def manual_solution():
    """
    Manual: 不使用 math 模組和字串反轉切片，全手寫質數判斷和反轉邏輯，方便考試手刻。
    """

    def is_prime(num):
        if num < 2:
            return False
        i = 2
        while i * i <= num:
            if num % i == 0:
                return False
            i += 1
        return True

    while True:
        try:
            line = input()
        except EOFError:
            break

        if line == "":
            continue

        n = int(line)

        # 判斷 n 是否為質數
        if not is_prime(n):
            print(f"{n} is not prime.")
            continue

        # 手動反轉數字
        rev_n = 0
        temp = n
        while temp > 0:
            rev_n = rev_n * 10 + (temp % 10)
            temp = temp // 10

        # 判斷反轉後是否為質數
        if rev_n != n and is_prime(rev_n):
            print(f"{n} is emirp.")
        else:
            print(f"{n} is prime.")


if __name__ == "__main__":
    standard_solution()
