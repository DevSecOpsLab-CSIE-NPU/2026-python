import sys


def main() -> None:
    for raw in sys.stdin:
        n = raw.strip()
        if n == "0":
            break
        if not n:
            continue

        # 從右邊開始，數字依序做 + - + - + - ...
        diff = 0
        plus = True
        for ch in reversed(n):
            digit = int(ch)
            if plus:
                diff += digit
            else:
                diff -= digit
            plus = not plus

        if diff % 11 == 0:
            print(f"{n} is a multiple of 11.")
        else:
            print(f"{n} is not a multiple of 11.")


if __name__ == "__main__":
    main()