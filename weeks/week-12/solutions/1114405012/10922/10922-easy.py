import sys


def sum_digits(value: int) -> int:
    # 直接把數字轉成字串，逐位相加。
    return sum(int(ch) for ch in str(value))


def main() -> None:
    for raw in sys.stdin:
        n = raw.strip()
        if n == "0":
            break
        if not n:
            continue

        total = sum_digits(int(n))
        if total % 9 != 0:
            print(f"{n} is not a multiple of 9.")
            continue

        degree = 1
        while total > 9:
            total = sum_digits(total)
            degree += 1

        print(f"9-degree of {n} is {degree}.")


if __name__ == "__main__":
    main()